export declare class RunJSError extends Error {
    constructor(message: string);
}
export interface ILogger {
    title(...args: any[]): void;
    log(...args: any[]): void;
    warning(...args: any[]): void;
    error(...args: any[]): void;
}
export declare class Logger implements ILogger {
    title(...args: any[]): void;
    log(...args: any[]): void;
    warning(...args: any[]): void;
    error(...args: any[]): void;
}
export declare class SilentLogger implements ILogger {
    title(): void;
    log(): void;
    warning(): void;
    error(): void;
}
export declare const logger: Logger;
