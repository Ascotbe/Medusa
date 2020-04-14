"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
class ShellError extends Error {
    constructor(message) {
        message = message && message.split('\n')[0]; // assign only first line
        super(message);
    }
}
exports.ShellError = ShellError;
function shellAsync(command, options = {}) {
    return new Promise((resolve, reject) => {
        const nextOptions = Object.assign({}, options, { shell: true, stdio: options.stdio || 'inherit' });
        const asyncProcess = child_process_1.spawn(command, nextOptions);
        let output = null;
        asyncProcess.on('error', (error) => {
            reject(new ShellError(`Failed to start command: ${command}; ${error.toString()}`));
        });
        asyncProcess.on('close', (exitCode) => {
            if (exitCode === 0) {
                resolve(output);
            }
            else {
                reject(new ShellError(`Command failed: ${command} with exit code ${exitCode}`));
            }
        });
        if (nextOptions.stdio === 'pipe') {
            asyncProcess.stdout.on('data', (buffer) => {
                output = buffer.toString();
            });
        }
        if (nextOptions.timeout) {
            setTimeout(() => {
                asyncProcess.kill();
                reject(new ShellError(`Command timeout: ${command}`));
            }, nextOptions.timeout);
        }
    });
}
function shellSync(command, options = {}) {
    try {
        const nextOptions = Object.assign({}, options, { stdio: options.stdio || 'inherit' });
        const buffer = child_process_1.execSync(command, nextOptions);
        if (buffer) {
            return buffer.toString();
        }
        return null;
    }
    catch (error) {
        throw new ShellError(error.message);
    }
}
function shell(command, options) {
    return options && options.async
        ? shellAsync(command, options)
        : shellSync(command, options);
}
exports.default = shell;
//# sourceMappingURL=shell.js.map