const { parseQuery } = require('loader-utils');
const isWebpack1 = require('./is-webpack-1');

/**
 * webpack 1 compat rule normalizer
 * @param {string|Rule} rule (string - webpack 1, Object - webpack 2)
 * @return {Object<loader: string, options: Object|null>}
 */
function normalizeRule(rule) {
  if (!rule) {
    throw new Error('Rule should be string or object');
  }

  let data;

  if (typeof rule === 'string') {
    const parts = rule.split('?');
    data = {
      loader: parts[0],
      options: parts[1] ? parseQuery(`?${parts[1]}`) : null
    };
  } else {
    const options = isWebpack1 ? rule.query : rule.options;
    data = {
      loader: rule.loader,
      options: options || null
    };
  }

  return data;
}

module.exports = normalizeRule;
