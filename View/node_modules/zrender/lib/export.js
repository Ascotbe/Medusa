var zrUtil = require("./core/util");

exports.util = zrUtil;

var matrix = require("./core/matrix");

exports.matrix = matrix;

var vector = require("./core/vector");

exports.vector = vector;

var colorTool = require("./tool/color");

exports.color = colorTool;

var pathTool = require("./tool/path");

exports.path = pathTool;

var _parseSVG = require("./tool/parseSVG");

var parseSVG = _parseSVG.parseSVG;
exports.parseSVG = _parseSVG.parseSVG;

var _Group = require("./container/Group");

exports.Group = _Group;

var _Path = require("./graphic/Path");

exports.Path = _Path;

var _Image = require("./graphic/Image");

exports.Image = _Image;

var _CompoundPath = require("./graphic/CompoundPath");

exports.CompoundPath = _CompoundPath;

var _Text = require("./graphic/Text");

exports.Text = _Text;

var _IncrementalDisplayable = require("./graphic/IncrementalDisplayable");

exports.IncrementalDisplayable = _IncrementalDisplayable;

var _Arc = require("./graphic/shape/Arc");

exports.Arc = _Arc;

var _BezierCurve = require("./graphic/shape/BezierCurve");

exports.BezierCurve = _BezierCurve;

var _Circle = require("./graphic/shape/Circle");

exports.Circle = _Circle;

var _Droplet = require("./graphic/shape/Droplet");

exports.Droplet = _Droplet;

var _Ellipse = require("./graphic/shape/Ellipse");

exports.Ellipse = _Ellipse;

var _Heart = require("./graphic/shape/Heart");

exports.Heart = _Heart;

var _Isogon = require("./graphic/shape/Isogon");

exports.Isogon = _Isogon;

var _Line = require("./graphic/shape/Line");

exports.Line = _Line;

var _Polygon = require("./graphic/shape/Polygon");

exports.Polygon = _Polygon;

var _Polyline = require("./graphic/shape/Polyline");

exports.Polyline = _Polyline;

var _Rect = require("./graphic/shape/Rect");

exports.Rect = _Rect;

var _Ring = require("./graphic/shape/Ring");

exports.Ring = _Ring;

var _Rose = require("./graphic/shape/Rose");

exports.Rose = _Rose;

var _Sector = require("./graphic/shape/Sector");

exports.Sector = _Sector;

var _Star = require("./graphic/shape/Star");

exports.Star = _Star;

var _Trochoid = require("./graphic/shape/Trochoid");

exports.Trochoid = _Trochoid;

var _LinearGradient = require("./graphic/LinearGradient");

exports.LinearGradient = _LinearGradient;

var _RadialGradient = require("./graphic/RadialGradient");

exports.RadialGradient = _RadialGradient;

var _Pattern = require("./graphic/Pattern");

exports.Pattern = _Pattern;

var _BoundingRect = require("./core/BoundingRect");

exports.BoundingRect = _BoundingRect;