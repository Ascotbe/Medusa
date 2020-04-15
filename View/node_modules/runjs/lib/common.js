"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const chalk_1 = __importDefault(require("chalk"));
// Needed to use ES5 inheritance, because of issues with Error subclassing for Babel
class RunJSError extends Error {
    constructor(message) {
        message = message && message.split("\n")[0]; // assign only first line
        super(message);
    }
}
exports.RunJSError = RunJSError;
class Logger {
    title(...args) {
        console.log(chalk_1.default.bold(...args));
    }
    log(...args) {
        console.log(...args);
    }
    warning(...args) {
        console.warn(chalk_1.default.yellow(...args));
    }
    error(...args) {
        console.error(chalk_1.default.red(...args));
    }
}
exports.Logger = Logger;
class SilentLogger {
    title() { }
    log() { }
    warning() { }
    error() { }
}
exports.SilentLogger = SilentLogger;
exports.logger = new Logger();
//# sourceMappingURL=common.js.map