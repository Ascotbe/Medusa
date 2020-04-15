"use strict";
module.exports = (args) => {
    const options = {};
    const params = args.filter(arg => {
        const doubleDashMatch = arg.match(/^--(\w[\w-.]*)(=(\S+))?$/);
        if (doubleDashMatch) {
            options[doubleDashMatch[1]] =
                Number(doubleDashMatch[3]) || doubleDashMatch[3] || true;
            return false;
        }
        const singleDashMatch = arg.match(/^-(\w)(=(\S+))?$/);
        if (singleDashMatch) {
            options[singleDashMatch[1]] =
                Number(singleDashMatch[3]) || singleDashMatch[3] || true;
            return false;
        }
        return true;
    });
    return {
        options,
        params
    };
};
//# sourceMappingURL=index.js.map