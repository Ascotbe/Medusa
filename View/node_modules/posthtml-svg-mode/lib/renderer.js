const merge = require('merge-options');
const renderer = require('posthtml-render');
const api = require('posthtml/lib/api');

const defaultOptions = {
  closingSingleTag: 'slash',
  singleTags: [
    'circle',
    'path',
    'ellipse',
    'line',
    'path',
    'polygon',
    'polyline',
    'rect',
    'use',
    'animateTransform',
    'stop'
  ]
};

/**
 * @param {PostHTMLTree} tree
 * @param {Object|null} [options] {@see https://github.com/posthtml/posthtml-render#options}
 */
module.exports = function xmlRenderer(tree, options) {
  const opts = merge(defaultOptions, options || {});

  /**
   * Workaround for https://github.com/fb55/htmlparser2/issues/187
   * Also see https://github.com/fb55/htmlparser2/pull/129
   */
  opts.singleTags = opts.singleTags.filter((tag) => {
    let hasContent = false;

    api.match.call(tree, { tag }, (node) => {
      if (typeof node.content !== 'undefined' && !hasContent) {
        hasContent = true;
      }
      return node;
    });

    return !hasContent;
  });

  return renderer(tree, opts);
};

module.exports.defaultOptions = defaultOptions;
