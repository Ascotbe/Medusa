"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// @flow
const chalk_1 = __importDefault(require("chalk"));
const fs_1 = __importDefault(require("fs"));
const lodash_padend_1 = __importDefault(require("lodash.padend"));
const microcli_1 = __importDefault(require("microcli"));
// @ts-ignore
const omelette_1 = __importDefault(require("omelette"));
const path_1 = __importDefault(require("path"));
const CLIError = microcli_1.default.CliError;
const common_1 = require("./common");
const DEFAULT_RUNFILE_PATH = "./runfile.js";
function requirer(filePath) {
    return require(path_1.default.resolve(filePath));
}
exports.requirer = requirer;
function hasAccess(filePath) {
    return fs_1.default.accessSync(path_1.default.resolve(filePath));
}
exports.hasAccess = hasAccess;
function getConfig(filePath) {
    let config;
    try {
        config = requirer(filePath).runjs || {};
    }
    catch (error) {
        config = {};
    }
    return config;
}
exports.getConfig = getConfig;
function load(config, logger, requirer, access) {
    const runfilePath = config.runfile || DEFAULT_RUNFILE_PATH;
    // Load requires if given in config
    if (Array.isArray(config.requires)) {
        config.requires.forEach(modulePath => {
            logger.log(chalk_1.default.gray(`Requiring ${modulePath}...`));
            requirer(modulePath);
        });
    }
    // Process runfile
    logger.log(chalk_1.default.gray(`Processing ${runfilePath}...`));
    try {
        access(runfilePath);
    }
    catch (error) {
        throw new common_1.RunJSError(`No ${runfilePath} defined in ${process.cwd()}`);
    }
    const runfile = requirer(runfilePath);
    if (runfile.default) {
        return runfile.default;
    }
    return runfile;
}
exports.load = load;
function describe(obj, logger, namespace) {
    if (!namespace) {
        logger.log(chalk_1.default.yellow("Available tasks:"));
    }
    Object.keys(obj).forEach(key => {
        const value = obj[key];
        const nextNamespace = namespace ? `${namespace}:${key}` : key;
        const help = value.help;
        if (typeof value === "function") {
            // Add task name
            const funcParams = help && help.params;
            const logArgs = [chalk_1.default.bold(nextNamespace)];
            // Add task params
            if (Array.isArray(funcParams) && funcParams.length) {
                logArgs[0] += ` [${funcParams.join(" ")}]`;
            }
            // Add description
            if (help && (help.description || typeof help === "string")) {
                const description = help.description || help;
                logArgs[0] = lodash_padend_1.default(logArgs[0], 40); // format
                logArgs.push("-", description.split("\n")[0]);
            }
            // Log
            logger.log(...logArgs);
        }
        else if (typeof value === "object") {
            describe(value, logger, nextNamespace);
        }
    });
    if (!namespace) {
        logger.log("\n" +
            chalk_1.default.blue('Type "run [taskname] --help" to get more info if available.'));
    }
}
exports.describe = describe;
function tasks(obj, namespace) {
    let list = [];
    Object.keys(obj).forEach(key => {
        const value = obj[key];
        const nextNamespace = namespace ? `${namespace}:${key}` : key;
        if (typeof value === "function") {
            list.push(nextNamespace);
        }
        else if (typeof value === "object") {
            list = list.concat(tasks(value, nextNamespace));
        }
    });
    return list;
}
function call(obj, args, logger, subtaskName) {
    const taskName = subtaskName || args[2];
    if (typeof obj[taskName] === "function") {
        const cli = microcli_1.default(args.slice(1), obj[taskName].help, undefined, logger);
        cli((options, ...params) => {
            obj[taskName].apply({ options }, params);
        });
        return obj[taskName];
    }
    const namespaces = taskName.split(":");
    const rootNamespace = namespaces.shift() || "";
    const nextSubtaskName = namespaces.join(":");
    if (obj[rootNamespace]) {
        const calledTask = call(obj[rootNamespace], args, logger, nextSubtaskName);
        if (calledTask) {
            return calledTask;
        }
    }
    if (!subtaskName) {
        throw new common_1.RunJSError(`Task ${taskName} not found`);
    }
}
exports.call = call;
function autocomplete(config) {
    const logger = new common_1.SilentLogger();
    const completion = omelette_1.default("run <task>");
    completion.on("task", ({ reply }) => {
        const runfile = load(config, logger, requirer, hasAccess);
        reply(tasks(runfile));
    });
    completion.init();
}
function main() {
    try {
        const config = getConfig("./package.json");
        autocomplete(config);
        const runfile = load(config, common_1.logger, requirer, hasAccess);
        const ARGV = process.argv.slice();
        if (ARGV.length > 2) {
            call(runfile, ARGV, common_1.logger);
        }
        else {
            describe(runfile, common_1.logger);
        }
    }
    catch (error) {
        if (error instanceof common_1.RunJSError || error instanceof CLIError) {
            common_1.logger.error(error.message);
            process.exit(1);
        }
        else {
            common_1.logger.log(error);
            process.exit(1);
        }
    }
}
exports.main = main;
//# sourceMappingURL=script.js.map