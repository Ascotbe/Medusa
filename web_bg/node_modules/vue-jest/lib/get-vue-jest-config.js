/**
 * This module extracts vue-jest relevant parts of a jest config
 *
 * @param {Object} jestConfig - a complete jest config object
 * @returns {Object} vueJestConfig - an object holding vue-jest specific configuration
 */
module.exports = function getVueJestConfig (jestConfig) {
  return (jestConfig && jestConfig.globals && jestConfig.globals['vue-jest']) || {}
}
