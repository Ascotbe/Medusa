const normalizeRule = require('./normalize-rule');
const isWebpack1 = require('./is-webpack-1');

/**
 * webpack 1 compat loader options finder. Returns normalized options.
 * @param {string} loaderPath
 * @param {Object|Rule} rule
 * @return {Object|null}
 */
function getLoaderOptions(loaderPath, rule) {
  let multiRuleProp;

  if (isWebpack1) {
    multiRuleProp = 'loaders';
  } else if (rule.oneOf) {
    multiRuleProp = 'oneOf';
  } else {
    multiRuleProp = 'use';
  }

  const multiRule = typeof rule === 'object' && Array.isArray(rule[multiRuleProp]) ? rule[multiRuleProp] : null;
  let options;

  if (multiRule) {
    const rules = [].concat(...multiRule.map(r => (r.use || r)));
    options = rules.map(normalizeRule).find(r => loaderPath.includes(r.loader)).options;
  } else {
    options = normalizeRule(rule).options;
  }

  return options;
}

module.exports = getLoaderOptions;
