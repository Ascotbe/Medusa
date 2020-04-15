'use strict';

const CONSTANTS = require('./constants.js');

const common = require('./common.js');
const debug = common.debug;
const getScriptName = common.getScriptName;
const isResourceLink = common.isResourceLink;
const isScript = common.isScript;
const matches = common.matches;

const shouldAdd = options => {
  return options.custom.length > 0;
};

const add = (options, tags) => {
  const update = updateElement.bind(null, options);
  return tags.map(update);
};

const updateElement = (options, tag) => {
  return (isScript(tag) || isResourceLink(tag))
    ? updateScriptElement(options, tag)
    : tag;
};

const updateScriptElement = (options, tag) => {
  const scriptName = getScriptName(options, tag);
  let updated = false;
  options.custom.forEach(customOption => {
    if (matches(scriptName, customOption.test)) {
      tag.attributes = tag.attributes || {};
      tag.attributes[customOption.attribute] = customOption.value;
      updated = true;
    }
  });
  if (updated) {
    debug(`${CONSTANTS.PLUGIN}: updated to: ${JSON.stringify(tag)}`);
  }
  return tag;
};

module.exports = {
  shouldAdd,
  add
};
