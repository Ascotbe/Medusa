require("./graphic");

var _zrender = require("../zrender");

var registerPainter = _zrender.registerPainter;

var Painter = require("./Painter");

registerPainter('vml', Painter);