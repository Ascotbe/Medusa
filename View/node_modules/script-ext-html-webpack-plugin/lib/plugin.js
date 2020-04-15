'use strict';

const htmlWebpackPlugin = require('html-webpack-plugin');

const { EVENT, PLUGIN } = require('./constants.js');

const debug = require('./common.js').debug;
const matches = require('./common.js').matches;
const normaliseOptions = require('./config.js');
const shouldAddResourceHints = require('./resource-hints.js').shouldAddResourceHints;
const addInitialChunkResourceHints = require('./initial-chunk-resource-hints.js');
const addAsyncChunkResourceHints = require('./async-chunk-resource-hints.js');
const elements = require('./elements.js');
const customAttributes = require('./custom-attributes.js');

const debugEvent = msg => debug(`${EVENT}: ${msg}`);

const falsySafeConcat = arrays =>
  arrays.reduce(
    (combined, array) => array ? combined.concat(array) : combined,
    []
  );

const getHtmlWebpackOptions = pluginArgs =>
  (pluginArgs && pluginArgs.plugin && pluginArgs.plugin.options)
    ? pluginArgs.plugin.options
    : {};

const getCompilationOptions = compilation =>
  (compilation && compilation.options) ? compilation.options : {};

class ScriptExtHtmlWebpackPlugin {
  constructor (options) {
    this.options = normaliseOptions(options);
  }

  apply (compiler) {
    const compile = this.compilationCallback.bind(this);
    const emit = this.emitCallback.bind(this);
    if (compiler.hooks) {
      compiler.hooks.compilation.tap(PLUGIN, compile);
      compiler.hooks.emit.tap(PLUGIN, emit);
    } else {
      compiler.plugin('compilation', compile);
      compiler.plugin('emit', emit);
    }
  }

  compilationCallback (compilation) {
    const alterAssetTags = this.alterAssetTagsCallback.bind(this, compilation);
    if (compilation.hooks) {
      const alterAssetTagGroups = compilation.hooks.htmlWebpackPluginAlterAssetTags || htmlWebpackPlugin.getHooks(compilation).alterAssetTagGroups;
      alterAssetTagGroups.tap(PLUGIN, alterAssetTags);
    } else {
      compilation.plugin(EVENT, alterAssetTags);
    }
  }

  alterAssetTagsCallback (compilation, pluginArgs, callback) {
    const options = this.options;
    const headTagName = pluginArgs.hasOwnProperty('headTags') ? 'headTags' : 'head';
    const bodyTagName = pluginArgs.hasOwnProperty('bodyTags') ? 'bodyTags' : 'body';
    try {
      options.htmlWebpackOptions = getHtmlWebpackOptions(pluginArgs);
      options.compilationOptions = getCompilationOptions(compilation);
      debugEvent('starting');
      if (elements.shouldUpdate(options)) {
        debugEvent('replacing <head> <script> elements');
        pluginArgs[headTagName] = elements.update(compilation.assets, options, pluginArgs[headTagName]);
        debugEvent('replacing <body> <script> elements');
        pluginArgs[bodyTagName] = elements.update(compilation.assets, options, pluginArgs[bodyTagName]);
      }
      if (shouldAddResourceHints(options)) {
        debugEvent('adding resource hints');
        pluginArgs[headTagName] = falsySafeConcat([
          pluginArgs[headTagName],
          addInitialChunkResourceHints(options, pluginArgs[headTagName]),
          addInitialChunkResourceHints(options, pluginArgs[bodyTagName]),
          addAsyncChunkResourceHints(compilation.chunks, options)
        ]);
      }
      if (customAttributes.shouldAdd(options)) {
        debugEvent('adding custom attribues to <head> <script> elements');
        pluginArgs[headTagName] = customAttributes.add(options, pluginArgs[headTagName]);
        debugEvent('adding custom attributes to <body> <script> elements');
        pluginArgs[bodyTagName] = customAttributes.add(options, pluginArgs[bodyTagName]);
      }
      debugEvent('completed');
      if (callback) {
        callback(null, pluginArgs);
      }
    } catch (err) {
      if (callback) {
        callback(err);
      } else {
        compilation.errors.push(err);
      }
    }
  }

  emitCallback (compilation, callback) {
    const options = this.options;
    if (options.inline.test.length > 0 && options.removeInlinedAssets) {
      debug('emit: deleting assets');
      Object.keys(compilation.assets).forEach((assetName) => {
        if (matches(assetName, options.inline.test)) {
          debug(`emit: deleting asset '${assetName}'`);
          delete compilation.assets[assetName];
        }
      });
    }
    if (callback) {
      callback();
    }
  }
}

module.exports = ScriptExtHtmlWebpackPlugin;
