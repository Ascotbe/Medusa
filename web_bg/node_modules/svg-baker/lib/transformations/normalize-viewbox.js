const merge = require('merge-options');
const { getRoot } = require('../utils');

const defaultConfig = {
  removeDimensions: false
};

/**
 * @param {Object} [config] {@see defaultConfig}
 * @return {Function} PostHTML plugin
 */
function normalizeViewBox(config = {}) {
  const cfg = merge(defaultConfig, config);

  return (tree) => {
    const root = getRoot(tree);
    root.attrs = root.attrs || {};
    const attrs = root.attrs;
    const { width, height, viewBox } = attrs;

    if (!viewBox && width && height) {
      attrs.viewBox = `0 0 ${parseFloat(width).toString()} ${parseFloat(height).toString()}`;

      if (cfg.removeDimensions) {
        delete attrs.width;
        delete attrs.height;
      }
    }

    return tree;
  };
}

module.exports = normalizeViewBox;
