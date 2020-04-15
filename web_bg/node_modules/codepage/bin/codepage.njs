#!/usr/bin/env node
/* js-codepage (C) 2014-present SheetJS -- http://sheetjs.com */
/* vim: set ts=2 ft=javascript: */
/* eslint-env node */
var codepage = require('../');
require('exit-on-epipe');
var fs = require('fs'), program/*:any*/ = (require('commander')/*:any*/);
program
	.version(codepage.version)
	.usage('[options] <file>')
	.option('-f, --from-code <code>', 'codepage of input (default 65001 utf8)')
	.option('-t, --to-code <code>', 'codepage of output (default 65001 utf8)')
	.option('-o, --output <file>', 'output file (<file>.<to> if specified)')
	.option('-B, --bom', 'write BOM (for unicode codepages)')
	.option('-F, --force', 'force writing to stdout for non-utf8 codepages')
	.option('-l, --list', 'List supported codepages');

program.on('--help', function() {
	console.log('  Codepage descriptions can be found in the README');
	console.log('      http://oss.sheetjs.com/js-codepage/README.md');
	console.log('  Support email: dev.codepage@sheetjs.com');
});

program.parse(process.argv);

if(program.list) {
	var l/*:Array<number>*/ = [];
	Object.keys(codepage).forEach(function(x) { if(parseInt(x, 10) == +x) l.push(+x); });
	Object.keys(codepage.utils.magic).forEach(function(x) { if(parseInt(x, 10) == +x && +x != 16969) l.push(+x); });
	l.sort(function(a,b) { return a-b; }).forEach(function(x) { console.log(x); });
	process.exit();
}

var fr = +program.fromCode || 65001;
var to = +program.toCode || 65001;
var f = program.args[0];
var o = program.output;

if(!process.stdin.isTTY) f = f || "-";

if(f !== "-" && !fs.existsSync(f)) {
	console.error('codepage: must specify a filename');
	process.exit(13);
}

function concat(func) {
	// $FlowIgnore
	var writable = require('stream').Writable();
	var buf = [];
	writable._write = function(chunk, e, cb) { buf.push(chunk); cb(); };
	writable._writev = function(chunks, cb) { chunks.forEach(function(c) { buf.push(c.chunk); cb(); }); };
	writable.on('finish', function() { func(Buffer.concat(buf)); });
	return writable;
}

if(f === "-") process.stdin.pipe(concat(process_text));
else process_text(fs.readFileSync(f));

function process_text(text/*:Buffer*/) {
	var dec/*:Buffer*/ = (codepage.utils.decode(fr, text)/*:any*/);

	var bom/*:Array<Buffer>*/ = [];
	bom[1200] = new Buffer([0xFF, 0xFE]);
	bom[1201] = new Buffer([0xFE, 0xFF]);
	bom[12000] = new Buffer([0xFF, 0xFE, 0x00, 0x00]);
	bom[12001] = new Buffer([0x00, 0x00, 0xFE, 0xFF]);
	bom[16969] = new Buffer([0x69, 0x69]);
	bom[65000] = new Buffer([0x2B, 0x2F, 0x76, 0x2B]);
	bom[65001] = new Buffer([0xEF, 0xBB, 0xBF]);

	var mybom = (program.bom && bom[to] ? bom[to] : "");
	var out/*:any*/ = to === 65001 ? dec.toString('utf8') : codepage.utils.encode(to, dec);

	/* if output file is specified */
	if(o) writefile(o, out, mybom);
	/* utf8 -> print to stdout */
	else if(to === 65001) logit(out, mybom);
	/* stdout piped to process -> print */
	else if(!process.stdout.isTTY) logit(out, mybom);
	/* forced */
	else if(program.force) logit(out, mybom);
	/* input file specified -> write to file */
	else if(f !== "-") writefile(f + "." + to, out, mybom);
	else {
		console.error('codepage: use force (-F, --force) to print ' + to + ' codes');
		process.exit(14);
	}
}

function logit(out/*:Buffer*/, bom) {
	process.stdout.write(bom);
	process.stdout.write(out);
}

function writefile(o, out/*:Buffer*/, bom) {
	fs.writeFileSync(o, bom);
	fs.appendFileSync(o, out);
}
