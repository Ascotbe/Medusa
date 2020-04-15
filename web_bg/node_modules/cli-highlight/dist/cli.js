"use strict";
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
var fs = __importStar(require("mz/fs"));
var path = __importStar(require("path"));
var yargs = require("yargs");
var index_1 = require("./index");
var theme_1 = require("./theme");
yargs
    .option('theme', {
    alias: 't',
    nargs: 1,
    description: 'Use a theme defined in a JSON file',
})
    .usage(['', 'Usage: highlight [options] [file]', '', 'Outputs a file or STDIN input with syntax highlighting'].join('\n'))
    .option('language', {
    alias: 'l',
    nargs: 1,
    description: 'Set the langugage explicitely\nIf omitted will try to auto-detect',
})
    .version()
    .help('help')
    .alias('help', 'h')
    .alias('version', 'v');
var argv = yargs.argv;
var file = argv._[0];
var codePromise;
if (!file && !process.stdin.isTTY) {
    // Input from STDIN
    process.stdin.setEncoding('utf8');
    var code_1 = '';
    process.stdin.on('readable', function () {
        var chunk = process.stdin.read();
        if (chunk !== null) {
            code_1 += chunk;
        }
    });
    codePromise = new Promise(function (resolve) {
        process.stdin.on('end', function () {
            var chunk = process.stdin.read();
            if (chunk !== null) {
                code_1 += chunk;
            }
            resolve(code_1);
        });
    });
}
else if (file) {
    // Read file
    codePromise = fs.readFile(file, 'utf-8');
}
else {
    yargs.showHelp();
    process.exit(1);
    throw new Error();
}
Promise.all([codePromise, argv.theme ? fs.readFile(argv.theme, 'utf8') : undefined])
    .then(function (_a) {
    var code = _a[0], theme = _a[1];
    var options = {
        ignoreIllegals: true,
        theme: (theme && theme_1.parse(theme)) || undefined,
    };
    if (file) {
        var ext = path.extname(file).substr(1);
        if (ext && index_1.supportsLanguage(ext)) {
            options.language = ext;
        }
    }
    options.language = argv.language;
    return new Promise(function (resolve, reject) {
        return process.stdout.write(index_1.highlight(code, options), function (err) { return (err ? reject(err) : resolve()); });
    });
})
    .then(function () {
    process.exit(0);
})
    .catch(function (err) {
    console.error(err);
    process.exit(1);
});
//# sourceMappingURL=cli.js.map