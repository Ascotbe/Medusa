/* eslint-disable no-cond-assign, default-case */
const escapeForRegexp = require('escape-string-regexp');

const URL_PATTERN = /url\(#([^ ]+?)\s*\)/g;
const defaultPattern = '[id]';

/**
 * @param {string} id
 * @param {string|Function} pattern
 */
function renameId(id, pattern) {
  const result = (typeof pattern === 'function' ? pattern(id) : pattern).toString();
  const re = new RegExp(escapeForRegexp('[id]'), 'g');
  return result.replace(re, id);
}

/**
 * @param {string|Function} [pattern]
 * @returns {Function}
 */
function plugin(pattern) {
  const p = pattern || defaultPattern;

  return (tree) => {
    const mappedIds = {};

    tree.match({ attrs: { id: /.*/ } }, (node) => {
      const { attrs } = node;
      const currentId = attrs.id;
      const newId = renameId(currentId, p);
      attrs.id = newId;

      mappedIds[currentId] = {
        id: newId,
        referenced: false,
        node
      };

      return node;
    });

    tree.match({ tag: /.*/ }, (node) => {
      const { attrs } = node;

      if (node.tag === 'style') {
        while (true) {
          const content = Array.isArray(node.content) ? node.content.join('') : node.content.toString();
          const match = URL_PATTERN.exec(content);
          if (match === null) {
            break;
          }

          const id = match[1];
          if (mappedIds[id]) {
            mappedIds[id].referenced = true;
            const re = new RegExp(escapeForRegexp(match[0]), 'g');
            node.content = content.replace(re, `url(#${mappedIds[id].id})`);
          }
        }
      }

      if ('attrs' in node === false) {
        return node;
      }

      Object.keys(attrs).forEach((attrName) => {
        const value = attrs[attrName];
        let id;
        let match;

        while ((match = URL_PATTERN.exec(value)) !== null) {
          id = match[1];
          if (mappedIds[id]) {
            mappedIds[id].referenced = true;
            const re = new RegExp(escapeForRegexp(match[0]), 'g');
            attrs[attrName] = value.replace(re, `url(#${mappedIds[id].id})`);
          }
        }

        let idObj;

        switch (attrName) {
          case 'href':
          case 'xlink:href':
            if (value.substring(0, 1) !== '#') {
              break;
            }

            id = value.substring(1);
            idObj = mappedIds[id];
            if (idObj) {
              idObj.referenced = false;
              attrs[attrName] = `#${idObj.id}`;
            }
            break;

          case 'for':
            if (node.tag !== 'label') {
              break;
            }

            id = value;
            idObj = mappedIds[id];
            if (idObj) {
              idObj.referenced = false;
              attrs[attrName] = idObj.id;
            }
            break;
        }
      });

      return node;
    });

    return tree;
  };
}

module.exports = plugin;
