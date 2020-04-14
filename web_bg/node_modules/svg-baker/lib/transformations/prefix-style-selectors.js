const Promise = require('bluebird');
const decodeEntities = require('he').decode;
const postcss = require('postcss');
const prefixSelectors = require('postcss-prefix-selector');

/**
 * @return {Function} PostHTML plugin
 */
function prefixStyleSelectors(prefix) {
  return (tree) => {
    const styleNodes = [];

    tree.match({ tag: 'style' }, (node) => {
      styleNodes.push(node);
      return node;
    });

    return Promise.map(styleNodes, (node) => {
      const content = node.content ? decodeEntities(node.content.join('')) : '';

      return postcss()
        .use(prefixSelectors({ prefix }))
        .process(content)
        .then(prefixedStyles => node.content = prefixedStyles.css);
    }).then(() => tree);
  };
}

module.exports = prefixStyleSelectors;

