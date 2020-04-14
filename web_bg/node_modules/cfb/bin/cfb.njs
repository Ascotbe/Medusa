#!/usr/bin/env node
/* cfb.js (C) 2013-present  SheetJS -- http://sheetjs.com */
/* eslint-env node */
/* vim: set ts=2 ft=javascript: */
var n = "cfb";
var X = require('../');
var fs = require('fs');
var program = require('commander');
var PRINTJ = require("printj");
var sprintf = PRINTJ.sprintf;
program
	.version(X.version)
	.usage('[options] <file> [subfiles...]')
	.option('-l, --list-files', 'list files')
	.option('-r, --repair', 'attempt to repair and garbage-collect archive')
	.option('-c, --create', 'create file')
	.option('-a, --append', 'add files to CFB (overwrite existing data)')
	.option('-d, --delete', 'delete files from CFB')
	.option('-O, --to-stdout', 'extract raw contents to stdout')
	.option('-z, --dump', 'dump internal representation but do not extract')
	.option('-q, --quiet', 'process but do not report')
	.option('--here', 'skip the CFB root name when extracting')
	.option('--osx', 'use OSX-style unzip listing')
	.option('--zlib', 'use native zlib')
	.option('--local', 'print times in local timezone')
	.option('--dev', 'development mode')
	.option('--read', 'read but do not print out contents');
program.parse(process.argv);

if(program.zlib) X.utils.use_zlib(require('zlib'));

var exit = process.exit;
var die = function(errno/*:number*/, msg/*:string*/) { console.error(n + ": " + msg); exit(errno); };
var logit = function(cmd/*:string*/, f/*:string*/) { console.error(sprintf("%-6s %s", cmd, f)); };

if(program.args.length === 0) die(1, "must specify a filename");

if(program.create) {
	logit("create", program.args[0]);
	var newcfb = X.utils.cfb_new();
	X.writeFile(newcfb, program.args[0]);
}

if(!fs.existsSync(program.args[0])) die(1, "must specify a filename");

var opts = ({type:'file'}/*:any*/);
if(program.dev) opts.WTF = true;

var cfb = X.read(program.args[0], opts);
if(program.quiet) exit(0);

if(program.dump) {
	console.log("Full Paths:");
	console.log(cfb.FullPaths.map(function(x/*:string*/) { return "  " + x; }).join("\n"));
	console.log("File Index:");
	console.log(cfb.FileIndex);
	exit(0);
}
if(program.repair) { X.writeFile(cfb, program.args[0]); exit(0); }

var rlen = cfb.FullPaths[0].length;

function fix_string(x/*:string*/)/*:string*/ { return x.replace(/[\u0000-\u001f]/g, function($$) { return sprintf("\\u%04X", $$.charCodeAt(0)); }); }
var format_date = function(date/*:Date*/, osx/*:?any*/)/*:string*/ {
	var datefmt = osx ? "%02u-%02u-%04u %02u:%02u": "%02u-%02u-%02u %02u:%02u";
	var MM = program.local ? date.getMonth() + 1 : date.getUTCMonth() + 1;
	var DD = program.local ? date.getDate() : date.getUTCDate();
	var YY = (program.local ? date.getFullYear() : date.getUTCFullYear())%(osx ? 10000 : 100);
	var hh = program.local ? date.getHours() : date.getUTCHours();
	var mm = program.local ? date.getMinutes() : date.getUTCMinutes();
	return sprintf(datefmt, MM, DD, YY, hh, mm);
};

if(program.listFiles) {
	var basetime = new Date(Date.UTC(1980,0,1));
	var cnt = 0, rootsize = 0, filesize = 0;
	var fmtstr = "%9lu  %s   %s";
	if(program.osx) {
		console.log("Archive:  " + program.args[0]);
		console.log("  Length      Date    Time    Name");
		console.log("---------  ---------- -----   ----");
		fmtstr = "%9lu  %s   %s";
	} else {
		console.log("  Length     Date   Time    Name");
		console.log(" --------    ----   ----    ----");
	}
	cfb.FileIndex.forEach(function(file/*:CFBEntry*/, i/*:number*/) {
		switch(file.type) {
			case 5:
				basetime = file.ct || file.mt || basetime;
				rootsize = file.size;
				break;
			case 2:
				var fixname = fix_string(cfb.FullPaths[i]);
				if(program.osx && fixname.match(/\\u0001Sh33tJ5/)) return;
				if(program.here) fixname = fixname.slice(rlen);
				console.log(sprintf(fmtstr, file.size, format_date(file.mt || basetime, program.osx), fixname));
				filesize += file.size;
				++cnt;
		}
	});
	var outfmt = "%9lu                   %lu file%s";
	if(program.osx) {
		console.log("---------                     -------");
		outfmt = "%9lu                     %lu file%s";
	} else {
		console.log(" --------                   -------");
	}
	console.log(sprintf(outfmt, rootsize || filesize, cnt, (cnt !== 1 ? "s" : "")));

	exit(0);
}

function mkdirp(path/*:string*/) { path.split("/").reduce(function(acc/*:string*/, p/*:string*/) {
	acc += p + "/";
	if(!fs.existsSync(acc)) { logit("mkdir", acc); fs.mkdirSync(acc); }
	return acc;
}, ""); }

function write(path/*:string*/, data/*:CFBEntry*/) {
	logit("write", fix_string(path));
	fs.writeFileSync(path, /*::new Buffer((*/data.content/*:: :any))*/ || new Buffer(0));
}

if(program.create || program.append) {
	program.args.slice(1).forEach(function(x/*:string*/) {
		logit("append", x);
		X.utils.cfb_add(cfb, "/" + x, fs.readFileSync(x));
	});
	X.writeFile(cfb, program.args[0]);
	exit(0);
}

if(program.delete) {
	program.args.slice(1).forEach(function(x/*:string*/) {
		logit("delete", x);
		X.utils.cfb_del(cfb, "/" + x);
	});
	X.writeFile(cfb, program.args[0]);
	exit(0);
}

if(program.args.length > 1) {
	program.args.slice(1).forEach(function(x/*:string*/) {
		var data/*:?CFBEntry*/ = X.find(cfb, x.replace(/\\u000\d/g,"!"));
		if(!data) { console.error(x + ": file not found"); return; }
		if(data.type !== 2) { console.error(x + ": not a file"); return; }
		var idx = cfb.FileIndex.indexOf(data), path = cfb.FullPaths[idx];
		if(program.toStdout) return process.stdout.write(/*::new Buffer((*/data.content/*:: :any))*/);
		mkdirp(path.slice(0, path.lastIndexOf("/")));
		write(path, data);
	});
	exit(0);
}

if(program.toStdout) exit(0);
for(var i=program.here ? 1 : 0; i!==cfb.FullPaths.length; ++i) {
	if(!cfb.FileIndex[i].name) continue;
	var fp = cfb.FullPaths[i];
	if(program.here) fp = fp.slice(rlen);
	if(fp.slice(-1) === "/") mkdirp(fp);
	else {
		if(fp.indexOf("/") > -1) mkdirp(fp.slice(0, fp.lastIndexOf("/")));
		write(fp, cfb.FileIndex[i]);
	}
}
