let ConcatenatedModule;
try {
  // eslint-disable-next-line global-require,import/no-unresolved,import/no-extraneous-dependencies
  ConcatenatedModule = require('webpack/lib/optimize/ConcatenatedModule');
  // eslint-disable-next-line no-empty
} catch (e) {}

/**
 * Get all modules from main & child compilations.
 * Merge modules from ConcatenatedModule (when webpack.optimize.ModuleConcatenationPlugin is used)
 * @param {Compilation} compilation
 * @return {NormalModule[]}
 */
function getAllModules(compilation) {
  let modules = compilation.modules;

  // Look up in child compilations
  if (compilation.children.length > 0) {
    const childModules = compilation.children.map(getAllModules)
      .reduce((acc, compilationModules) => acc.concat(compilationModules), []);

    modules = modules.concat(childModules);
  }

  // Merge modules from ConcatenatedModule
  if (ConcatenatedModule) {
    const concatenatedModules = modules
      .filter(m => m instanceof ConcatenatedModule)
      .reduce((acc, m) => {
        /**
         * @see https://git.io/v7XDu
         * In webpack@3.5.1 `modules` public property was removed
         * To workaround this private `_orderedConcatenationList` property is used to collect modules
         */
        const subModules = 'modules' in m
          ? m.modules
          : m._orderedConcatenationList.map(entry => entry.module);

        return acc.concat(subModules);
      }, []);

    if (concatenatedModules.length > 0) {
      modules = modules.concat(concatenatedModules);
    }
  }

  return modules;
}

module.exports = getAllModules;
