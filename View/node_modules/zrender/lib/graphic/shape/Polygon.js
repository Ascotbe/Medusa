var Path = require("../Path");

var polyHelper = require("../helper/poly");

/**
 * 多边形
 * @module zrender/shape/Polygon
 */
var _default = Path.extend({
  type: 'polygon',
  shape: {
    points: null,
    smooth: false,
    smoothConstraint: null
  },
  buildPath: function (ctx, shape) {
    polyHelper.buildPath(ctx, shape, true);
  }
});

module.exports = _default;