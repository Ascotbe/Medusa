const webpackVersion = require('./get-webpack-version');

/**
 * Find nearest module chunk (not sure that is reliable method, but who cares).
 * @see http://stackoverflow.com/questions/43202761/how-to-determine-all-module-chunks-in-webpack
 * @param {NormalModule} module
 * @param {NormalModule[]} modules - webpack 1 compat
 * @return {Chunk|null}
 */
function getModuleChunk(module, modules) {
  let chunks;

  if (webpackVersion.IS_4) {
    chunks = Array.from(module.chunksIterable);
  } else if (parseInt(webpackVersion(), 10) >= 3) {
    chunks = module.mapChunks();
  } else {
    chunks = module.chunks;
  }

  // webpack 1 compat
  const issuer = typeof module.issuer === 'string'
    ? modules.find(m => m.request === module.issuer)
    : module.issuer;

  if (Array.isArray(chunks) && chunks.length > 0) {
    return chunks[chunks.length - 1];
  } else if (issuer) {
    return getModuleChunk(issuer, modules);
  }

  return null;
}

module.exports = getModuleChunk;
