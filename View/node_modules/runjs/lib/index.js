"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
const path_1 = __importDefault(require("path"));
const common_1 = require("./common");
const loggerAlias = common_1.logger;
function runSync(command, options) {
    try {
        const nextOptions = {
            cwd: options.cwd,
            env: options.env,
            stdio: options.stdio,
            timeout: options.timeout
        };
        const buffer = child_process_1.execSync(command, nextOptions);
        if (buffer) {
            return buffer.toString();
        }
        return null;
    }
    catch (error) {
        throw new common_1.RunJSError(error.message);
    }
}
function runAsync(command, options) {
    return new Promise((resolve, reject) => {
        const nextOptions = {
            cwd: options.cwd,
            env: options.env,
            shell: true,
            stdio: options.stdio
        };
        const asyncProcess = child_process_1.spawn(command, nextOptions);
        let output = null;
        asyncProcess.on("error", (error) => {
            reject(new Error(`Failed to start command: ${command}; ${error.toString()}`));
        });
        asyncProcess.on("close", (exitCode) => {
            if (exitCode === 0) {
                resolve(output);
            }
            else {
                reject(new Error(`Command failed: ${command} with exit code ${exitCode}`));
            }
        });
        if (options.stdio === "pipe") {
            asyncProcess.stdout.on("data", (buffer) => {
                output = buffer.toString();
            });
        }
        if (options.timeout) {
            setTimeout(() => {
                asyncProcess.kill();
                reject(new Error(`Command timeout: ${command}`));
            }, options.timeout);
        }
    });
}
function run(command, options = {}, logger = loggerAlias) {
    const binPath = path_1.default.resolve("./node_modules/.bin");
    // Pick relevant option keys and set default values
    const nextOptions = {
        async: !!options.async,
        cwd: options.cwd,
        env: options.env || process.env,
        stdio: options.stdio || "inherit",
        timeout: options.timeout
    };
    const env = nextOptions.env;
    // Include in PATH node_modules bin path
    if (env) {
        env.PATH = [binPath, env.PATH || process.env.PATH].join(path_1.default.delimiter);
    }
    logger.title(command);
    // Handle async call
    if (options.async) {
        return runAsync(command, nextOptions);
    }
    // Handle sync call by default
    return runSync(command, nextOptions);
}
exports.run = run;
/**
 * @deprecated
 */
function option(thisObj, name = "") {
    return (thisObj && thisObj.options && thisObj.options[name]) || null;
}
exports.option = option;
function options(thisObj) {
    return (thisObj && thisObj.options) || {};
}
exports.options = options;
function help(func, annotation) {
    // Because the validation above currently gets compiled out,
    // Explictly  validate the function input
    if (typeof func === "function") {
        func.help = annotation;
    }
    else {
        throw new Error("first help() argument must be a function");
    }
}
exports.help = help;
//# sourceMappingURL=index.js.map