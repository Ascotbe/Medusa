const stringify = require('./stringify');

/**
 * @param {SpriteSymbol} symbol
 * @return {string}
 */
function stringifySymbol(symbol) {
  return stringify({
    id: symbol.id,
    use: symbol.useId,
    viewBox: symbol.viewBox,
    content: symbol.render()
  });
}

module.exports = stringifySymbol;
