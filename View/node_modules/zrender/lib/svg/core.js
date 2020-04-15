var svgURI = 'http://www.w3.org/2000/svg';

function createElement(name) {
  return document.createElementNS(svgURI, name);
}

exports.createElement = createElement;