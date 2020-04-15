interface IOptions {
    [key: string]: number | string | boolean;
}
declare type Params = string[];
interface IParsedArgs {
    params: Params;
    options: IOptions;
}
declare const _default: (args: string[]) => IParsedArgs;
export = _default;
