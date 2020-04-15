"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
const lodash_1 = require("lodash");
const microargs_1 = __importDefault(require("microargs"));
const path_1 = __importDefault(require("path"));
class CLIError extends Error {
}
function optionToString(optionName) {
    return optionName.length === 1 ? `-${optionName}` : `--${optionName}`;
}
function optionsToString(optionsKeys) {
    return optionsKeys.map(optionToString).join(" ");
}
function printHelp(scriptName, annotations, logger) {
    if (lodash_1.isEmpty(annotations)) {
        logger.log("Documentation not found");
        return null;
    }
    const { description, params, options } = annotations;
    const extra = lodash_1.omit(annotations, ["description", "params", "options"]);
    const usageOptions = lodash_1.isEmpty(options) ? "" : "[options]";
    const usageParams = !Array.isArray(params) || lodash_1.isEmpty(params) ? "" : `[${params.join(" ")}]`;
    logger.log(`Usage: ${path_1.default.basename(scriptName)} ${usageOptions} ${usageParams}\n`);
    if (description) {
        logger.log(`${description}\n`);
    }
    if (!lodash_1.isEmpty(options)) {
        logger.log("Options:\n");
        lodash_1.forEach(options, (value, key) => {
            logger.log(`  ${lodash_1.padEnd(optionToString(key), 12)}${value}`);
        });
    }
    lodash_1.forEach(extra, (value, key) => {
        logger.log(`\n${lodash_1.capitalize(key)}:\n`);
        logger.log(`${value}\n`);
    });
}
const Cli = (argv, annotations = {}, help = printHelp, logger = console) => {
    return (callback) => {
        const { params, options } = microargs_1.default(argv.slice(2));
        const scriptName = path_1.default.basename(argv[1]);
        if (lodash_1.isString(annotations)) {
            annotations = {
                description: annotations
            };
        }
        if (options.help) {
            return help(scriptName, annotations, logger);
        }
        const annotatedOptionsKeys = (annotations &&
            annotations.options &&
            Object.keys(annotations.options)) ||
            [];
        const optionsKeys = Object.keys(options);
        const illegalOptionsKeys = lodash_1.difference(optionsKeys, annotatedOptionsKeys);
        if (annotatedOptionsKeys.length && illegalOptionsKeys.length) {
            const msg = `Illegal option: ${optionsToString(illegalOptionsKeys)}\n` +
                `Available options: ${optionsToString(annotatedOptionsKeys)}\n` +
                `Type "${scriptName} --help" for more information`;
            throw new CLIError(msg);
        }
        return callback(options, ...params);
    };
};
Cli.CliError = CLIError;
module.exports = Cli;
//# sourceMappingURL=index.js.map