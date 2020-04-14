"use strict";
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
var chalk_1 = __importStar(require("chalk"));
// Always enable at least basic color support, even if not auto-detected
var chalk = new chalk_1.default.Instance({ level: Math.min(chalk_1.default.level, 1 /* Basic */) });
/**
 * Identity function for tokens that should not be styled (returns the input string as-is).
 * See [[Theme]] for an example.
 */
exports.plain = function (codePart) { return codePart; };
/**
 * The default theme. It is possible to override just individual keys.
 */
exports.DEFAULT_THEME = {
    /**
     * keyword in a regular Algol-style language
     */
    keyword: chalk.blue,
    /**
     * built-in or library object (constant, class, function)
     */
    built_in: chalk.cyan,
    /**
     * user-defined type in a language with first-class syntactically significant types, like
     * Haskell
     */
    type: chalk.cyan.dim,
    /**
     * special identifier for a built-in value ("true", "false", "null")
     */
    literal: chalk.blue,
    /**
     * number, including units and modifiers, if any.
     */
    number: chalk.green,
    /**
     * literal regular expression
     */
    regexp: chalk.red,
    /**
     * literal string, character
     */
    string: chalk.red,
    /**
     * parsed section inside a literal string
     */
    subst: exports.plain,
    /**
     * symbolic constant, interned string, goto label
     */
    symbol: exports.plain,
    /**
     * class or class-level declaration (interfaces, traits, modules, etc)
     */
    class: chalk.blue,
    /**
     * function or method declaration
     */
    function: chalk.yellow,
    /**
     * name of a class or a function at the place of declaration
     */
    title: exports.plain,
    /**
     * block of function arguments (parameters) at the place of declaration
     */
    params: exports.plain,
    /**
     * comment
     */
    comment: chalk.green,
    /**
     * documentation markup within comments
     */
    doctag: chalk.green,
    /**
     * flags, modifiers, annotations, processing instructions, preprocessor directive, etc
     */
    meta: chalk.grey,
    /**
     * keyword or built-in within meta construct
     */
    'meta-keyword': exports.plain,
    /**
     * string within meta construct
     */
    'meta-string': exports.plain,
    /**
     * heading of a section in a config file, heading in text markup
     */
    section: exports.plain,
    /**
     * XML/HTML tag
     */
    tag: chalk.grey,
    /**
     * name of an XML tag, the first word in an s-expression
     */
    name: chalk.blue,
    /**
     * s-expression name from the language standard library
     */
    'builtin-name': exports.plain,
    /**
     * name of an attribute with no language defined semantics (keys in JSON, setting names in
     * .ini), also sub-attribute within another highlighted object, like XML tag
     */
    attr: chalk.cyan,
    /**
     * name of an attribute followed by a structured value part, like CSS properties
     */
    attribute: exports.plain,
    /**
     * variable in a config or a template file, environment var expansion in a script
     */
    variable: exports.plain,
    /**
     * list item bullet in text markup
     */
    bullet: exports.plain,
    /**
     * code block in text markup
     */
    code: exports.plain,
    /**
     * emphasis in text markup
     */
    emphasis: chalk.italic,
    /**
     * strong emphasis in text markup
     */
    strong: chalk.bold,
    /**
     * mathematical formula in text markup
     */
    formula: exports.plain,
    /**
     * hyperlink in text markup
     */
    link: chalk.underline,
    /**
     * quotation in text markup
     */
    quote: exports.plain,
    /**
     * tag selector in CSS
     */
    'selector-tag': exports.plain,
    /**
     * #id selector in CSS
     */
    'selector-id': exports.plain,
    /**
     * .class selector in CSS
     */
    'selector-class': exports.plain,
    /**
     * [attr] selector in CSS
     */
    'selector-attr': exports.plain,
    /**
     * :pseudo selector in CSS
     */
    'selector-pseudo': exports.plain,
    /**
     * tag of a template language
     */
    'template-tag': exports.plain,
    /**
     * variable in a template language
     */
    'template-variable': exports.plain,
    /**
     * added or changed line in a diff
     */
    addition: chalk.green,
    /**
     * deleted line in a diff
     */
    deletion: chalk.red,
    /**
     * things not matched by any token
     */
    default: exports.plain,
};
/**
 * Converts a [[JsonTheme]] with string values to a [[Theme]] with formatter functions. Used by [[parse]].
 */
function fromJson(json) {
    var theme = {};
    for (var _i = 0, _a = Object.keys(json); _i < _a.length; _i++) {
        var key = _a[_i];
        var style = json[key];
        if (Array.isArray(style)) {
            ;
            theme[key] = style.reduce(function (prev, curr) { return (curr === 'plain' ? exports.plain : prev[curr]); }, chalk);
        }
        else {
            ;
            theme[key] = chalk[style];
        }
    }
    return theme;
}
exports.fromJson = fromJson;
/**
 * Converts a [[Theme]] with formatter functions to a [[JsonTheme]] with string values. Used by [[stringify]].
 */
function toJson(theme) {
    var jsonTheme = {};
    for (var _i = 0, _a = Object.keys(jsonTheme); _i < _a.length; _i++) {
        var key = _a[_i];
        var style = jsonTheme[key];
        jsonTheme[key] = style._styles;
    }
    return jsonTheme;
}
exports.toJson = toJson;
/**
 * Stringifies a [[Theme]] with formatter functions to a JSON string.
 *
 * ```ts
 * import chalk = require('chalk');
 * import {stringify} from 'cli-highlight';
 * import * as fs from 'fs';
 *
 * const myTheme: Theme = {
 *     keyword: chalk.red.bold,
 *     addition: chalk.green,
 *     deletion: chalk.red.strikethrough,
 *     number: plain
 * }
 * const json = stringify(myTheme);
 * fs.writeFile('mytheme.json', json, (err: any) => {
 *     if (err) throw err;
 *     console.log('Theme saved');
 * });
 * ```
 */
function stringify(theme) {
    return JSON.stringify(toJson(theme));
}
exports.stringify = stringify;
/**
 * Parses a JSON string into a [[Theme]] with formatter functions.
 *
 * ```ts
 * import * as fs from 'fs';
 * import {parse, highlight} from 'cli-highlight';
 *
 * fs.readFile('mytheme.json', 'utf8', (err: any, json: string)  => {
 *     if (err) throw err;
 *     const code = highlight('SELECT * FROM table', {theme: parse(json)});
 *     console.log(code);
 * });
 * ```
 */
function parse(json) {
    return fromJson(JSON.parse(json));
}
exports.parse = parse;
//# sourceMappingURL=theme.js.map