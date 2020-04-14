/// <reference types="node" />
import { StdioOptions } from "child_process";
import { Logger } from "./common";
interface IOptions {
    cwd?: string;
    async?: boolean;
    stdio?: StdioOptions;
    env?: NodeJS.ProcessEnv;
    timeout?: number;
}
interface ICliOptions {
    [key: string]: string;
}
interface ITaskContext {
    options?: ICliOptions;
}
interface ITaskFunction {
    (...args: any[]): any;
    help?: any;
}
export declare function run(command: string, options: IOptions & {
    async: true;
}, logger?: Logger): Promise<string | null>;
export declare function run(command: string, options?: IOptions & {
    async?: false | null;
}, logger?: Logger): string | null;
/**
 * @deprecated
 */
export declare function option(thisObj: ITaskContext | null, name?: string): any;
export declare function options(thisObj: ITaskContext | null): object;
export declare function help(func: ITaskFunction, annotation?: string | any): void;
export {};
