'use strict';

const CONSTANTS = require('./constants.js');
const SYNC = 'sync';
const ATTRIBUTE_PRIORITIES = [SYNC, 'async', 'defer'];

const common = require('./common.js');
const debug = common.debug;
const isScript = common.isScript;
const matches = common.matches;
const getScriptName = common.getScriptName;

const shouldUpdate = (options) => {
  if (ATTRIBUTE_PRIORITIES.indexOf(options.defaultAttribute) < 0) {
    throw new Error(`${CONSTANTS.PLUGIN}: invalid default attribute`);
  }
  return !(options.defaultAttribute === SYNC &&
           options.inline.test.length === 0 &&
           options.async.test.length === 0 &&
           options.defer.test.length === 0 &&
           options.module.test.length === 0);
};

const update = (assets, options, tags) => {
  const update = updateElement.bind(null, assets, options);
  return tags.map(update);
};

const updateElement = (assets, options, tag) => {
  return (isScript(tag))
    ? updateScriptElement(assets, options, tag)
    : tag;
};

const updateScriptElement = (assets, options, tag) => {
  debug(`${CONSTANTS.EVENT}: processing <script> element: ${JSON.stringify(tag)}`);
  return (isInline(options, tag))
    ? replaceWithInlineElement(assets, options, tag)
    : updateSrcElement(options, tag);
};

const isInline = (options, tag) =>
  matches(getScriptName(options, tag), options.inline.test);

const replaceWithInlineElement = (assets, options, tag) => {
  const scriptName = getScriptName(options, tag);
  const asset = assets[scriptName];
  if (!asset) throw new Error(`${CONSTANTS.PLUGIN}: no asset with href '${scriptName}'`);
  const newTag = {
    tagName: 'script',
    closeTag: true,
    innerHTML: asset.source()
  };
  debug(`${CONSTANTS.PLUGIN}: replaced by: ${JSON.stringify(newTag)}`);
  return newTag;
};

const updateSrcElement = (options, tag) => {
  const scriptName = getScriptName(options, tag);
  // select new attribute, if any, by priority
  let newAttribute;
  ATTRIBUTE_PRIORITIES.some(attribute => {
    if (matches(scriptName, options[attribute].test)) {
      newAttribute = attribute;
      return true;
    }
  });
  if (!newAttribute) newAttribute = options.defaultAttribute;
  if (newAttribute !== SYNC) {
    tag.attributes[newAttribute] = true;
  }
  // possibly overwrite existing type attribute
  if (matches(scriptName, options.module.test)) {
    tag.attributes.type = 'module';
  }
  debug(`${CONSTANTS.PLUGIN}: updated to: ${JSON.stringify(tag)}`);
  return tag;
};

module.exports = {
  shouldUpdate,
  update
};
