/// <reference types="node" />
import { StdioOptions } from 'child_process';
export declare class ShellError extends Error {
    constructor(message: string);
}
interface ICommonShellOptions {
    cwd?: string;
    env?: NodeJS.ProcessEnv;
    stdio?: StdioOptions;
    timeout?: number;
}
export interface IShellOptions extends ICommonShellOptions {
    async?: boolean;
}
declare function shell(command: string, options: IShellOptions & {
    async: true;
}): Promise<string | null>;
declare function shell(command: string, options?: IShellOptions & {
    async?: false | null;
}): string | null;
declare function shell(command: string, options?: IShellOptions): Promise<string | null> | string | null;
export default shell;
