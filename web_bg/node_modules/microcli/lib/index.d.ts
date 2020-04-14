/// <reference types="node" />
declare class CLIError extends Error {
}
declare type Logger = typeof console;
interface IOptions {
    [key: string]: number | string | boolean;
}
interface IAnnoations {
    description?: string;
    params?: string[];
    options?: IOptions;
    [key: string]: any;
}
declare type PrintHelp = (scriptName: string, annotations: IAnnoations, logger: Logger) => void | null;
declare type CliCallback = (options: IOptions, ...params: string[]) => any;
declare const Cli: {
    (argv: string[], annotations?: string | IAnnoations, help?: PrintHelp, logger?: Console): (callback: CliCallback) => any;
    CliError: typeof CLIError;
};
export = Cli;
