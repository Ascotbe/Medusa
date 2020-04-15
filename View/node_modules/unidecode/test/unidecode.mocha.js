/**
 * Tests are taken from Text-Unidecode-0.04/test.pl
 * 
 * @see <http://search.cpan.org/~sburke/Text-Unidecode-0.04/lib/Text/Unidecode.pm>
 */

'use strict';

/* global describe, it */

var assert = require('assert');
var unidecode = require('../unidecode');

describe('# Purity tests', function(){
	var code;
	var tests = [];
	
	for(code=0; code<=127; code++) {
		tests.push(String.fromCharCode(code));
	}
	tests.forEach(function(test) {
		it(test.charCodeAt(0).toString(16) + ' ' + test, function(){
			var exp = test;
			var res = unidecode(exp);
			assert.equal(res, exp);
		});
	});
});

describe('# Basic string tests', function(){

	var tests = [
		"",
		1/10,
		"I like pie.",
		"\n",
		"\r\n", // "\cm\cj" - perl control chars Ctrl+M, CTRL+J === \r\n
		"I like pie.\n",
	];
	
	tests.forEach(function(test) {
		it(test, function(){
			var exp = test;
			var res = unidecode(test.toString());
			assert.equal(res, exp);
		});
	});
});

describe('# Complex tests', function(){

	var tests = [
		["\u00C6neid", "AEneid"],
		["\u00E9tude", "etude"],
		["\u5317\u4EB0", "Bei Jing "],
		//  Chinese
		["\u1515\u14c7\u14c7", "shanana"],
		//  Canadian syllabics
		["\u13d4\u13b5\u13c6", "taliqua"],
		//  Cherokee
		["\u0726\u071b\u073d\u0710\u073a", "ptu'i"],
		//  Syriac
		["\u0905\u092d\u093f\u091c\u0940\u0924", "abhijiit"],
		//  Devanagari
		["\u0985\u09ad\u09bf\u099c\u09c0\u09a4", "abhijiit"],
		//  Bengali
		["\u0d05\u0d2d\u0d3f\u0d1c\u0d40\u0d24", "abhijiit"],
		//  Malayalaam
		["\u0d2e\u0d32\u0d2f\u0d3e\u0d32\u0d2e\u0d4d", "mlyaalm"],
		//  the Malayaalam word for "Malayaalam"
		//  Yes, if we were doing it right, that'd be "malayaalam", not "mlyaalm"
		["\u3052\u3093\u307e\u3044\u8336", "genmaiCha "],
		//  Japanese, astonishingly unmangled.
	];
	
	tests.forEach(function(test) {
		it(test[0] + '-->' + test[1], function(){
			var exp = test[1];
			var res = unidecode(test[0]);
			assert.equal(res, exp);
		});
	});
});