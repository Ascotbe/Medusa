import { ILogger, Logger } from "./common";
interface IConfig {
    runfile?: string;
    requires?: string[];
}
export declare function requirer(filePath: string): any;
export declare function hasAccess(filePath: string): void;
export declare function getConfig(filePath: string): IConfig;
export declare function load(config: IConfig, logger: ILogger, requirer: (arg: string) => any, access: (arg: string) => void): any;
export declare function describe(obj: any, logger: Logger, namespace?: string): void;
export declare function call(obj: any, args: string[], logger?: ILogger, subtaskName?: string): any;
export declare function main(): void;
export {};
