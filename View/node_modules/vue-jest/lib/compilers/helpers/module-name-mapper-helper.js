const localResolve = require('./local-resolve-helper')

/**
 * Applies the moduleNameMapper substitution from the jest config
 *
 * @param {String} source - the original string
 * @param {String} filePath - the path of the current file (where the source originates)
 * @param {Object} jestConfig - the jestConfig holding the moduleNameMapper settings
 * @returns {String} path - the final path to import (including replacements via moduleNameMapper)
 */
module.exports = function applyModuleNameMapper (source, filePath, jestConfig = {}) {
  if (!jestConfig.moduleNameMapper) return source

  // Extract the moduleNameMapper settings from the jest config. TODO: In case of development via babel@7, somehow the jestConfig.moduleNameMapper might end up being an Array. After a proper upgrade to babel@7 we should probably fix this.
  const module = Array.isArray(jestConfig.moduleNameMapper) ? jestConfig.moduleNameMapper : Object.entries(jestConfig.moduleNameMapper)

  const importPath = module
    .reduce((acc, [regex, replacement]) => {
      const matches = acc.match(regex)

      if (matches === null) {
        return acc
      }

      return replacement.replace(
        /\$([0-9]+)/g,
        (_, index) => matches[parseInt(index, 10)]
      )
    }, source)

  return localResolve(
    filePath,
    importPath
  )
}

