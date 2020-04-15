'use strict';

const PLUGIN = require('./constants.js').PLUGIN;

const DEFAULT_HASH = {
  test: []
};
const DEFAULT_RESOURCE_HINT_HASH = {
  test: [],
  chunks: 'initial'
};
const DEFAULT_CUSTOM_HASH = {
  test: [],
  attribute: '',
  value: true
};
const DEFAULT_OPTIONS = {
  inline: DEFAULT_HASH,
  sync: DEFAULT_HASH,
  async: DEFAULT_HASH,
  defer: DEFAULT_HASH,
  module: DEFAULT_HASH,
  prefetch: DEFAULT_RESOURCE_HINT_HASH,
  preload: DEFAULT_RESOURCE_HINT_HASH,
  defaultAttribute: 'sync',
  removeInlinedAssets: true,
  custom: []
};
const POSSIBLE_VALUES = ['chunks', 'attribute', 'value'];

const normaliseOptions = options => {
  if (!options) return DEFAULT_OPTIONS;
  validate(options);
  const normalised = Object.assign({}, DEFAULT_OPTIONS, options);
  // now overwrite values which are not of DEFAULT_HASH form
  Object.keys(options).forEach(key => {
    const value = options[key];
    switch (key) {
      case 'inline':
      case 'sync':
      case 'async':
      case 'defer':
      case 'module':
        normalised[key] = normaliseAttribute(value);
        break;
      case 'prefetch':
      case 'preload':
        normalised[key] = normaliseResourceHint(value);
        break;
      case 'custom':
        normalised[key] = normaliseCustomArray(value);
        break;
      default:
        break;
    }
  });
  return normalised;
};

const validate = options => {
  const failureTests = []; // TODO!
  if (failureTests.some(test => test(options))) error();
};

const error = () => {
  throw new Error(`${PLUGIN}: invalid configuration - please see https://github.com/numical/script-ext-html-webpack-plugin#configuration`);
};

const normaliseValue = (defaultProps, value) => {
  let normalised = Object.assign({}, defaultProps);
  if (value) {
    normalised.test = convertToArray(value, () => {
      if (typeof value === 'object') {
        POSSIBLE_VALUES.forEach(key => copyValue(key, normalised, value));
        if (value.test) {
          return convertToArray(value.test, error);
        } else {
          error();
        }
      }
    });
  }
  return normalised;
};

const normaliseAttribute = normaliseValue.bind(null, DEFAULT_HASH);

const normaliseResourceHint = normaliseValue.bind(null, DEFAULT_RESOURCE_HINT_HASH);

const normaliseCustomAttribute = normaliseValue.bind(null, DEFAULT_CUSTOM_HASH);

const normaliseCustomArray = value => {
  const array = Array.isArray(value) ? value : [value];
  return array.map(normaliseCustomAttribute);
};

const convertToArray = (value, elseFn) => {
  if (typeof value === 'string') {
    return [value];
  } else if (value instanceof RegExp) {
    return [value];
  } else if (Array.isArray(value)) {
    return value;
  } else {
    return elseFn();
  }
};

const copyValue = (key, to, from) => {
  if (from.hasOwnProperty(key)) {
    to[key] = from[key];
  }
};

module.exports = normaliseOptions;
module.exports.DEFAULT_OPTIONS = DEFAULT_OPTIONS;
