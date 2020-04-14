'use strict';

const CHUNK_OPTIONS = ['all', 'initial'];

const createResourceHint = require('./resource-hints.js').createResourceHint;
const common = require('./common.js');
const matches = common.matches;
const getScriptName = common.getScriptName;
const getRawScriptName = common.getRawScriptName;
const hasScriptName = common.hasScriptName;

const optionsMatch = (option, scriptName) => {
  return matches(option.chunks, CHUNK_OPTIONS) && matches(scriptName, option.test);
};

const addInitialChunkResourceHints = (options, tags) => {
  return tags
    .filter(hasScriptName)
    .reduce((hints, tag) => {
      const scriptName = getScriptName(options, tag);
      if (optionsMatch(options.preload, scriptName)) {
        hints.push(createResourceHint('preload', getRawScriptName(tag)));
      } else if (optionsMatch(options.prefetch, scriptName)) {
        hints.push(createResourceHint('prefetch', getRawScriptName(tag)));
      }
      return hints;
    },
    []
    );
};

module.exports = addInitialChunkResourceHints;
