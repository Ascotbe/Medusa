'use strict';

const shouldAddResourceHints = options => {
  return !(options.prefetch.test.length === 0 &&
           options.preload.test.length === 0);
};

const createResourceHint = (rel, href) => {
  return {
    tagName: 'link',
    selfClosingTag: true,
    attributes: {
      rel: rel,
      href: href,
      as: 'script'
    }
  };
};

module.exports = {
  shouldAddResourceHints,
  createResourceHint
};
