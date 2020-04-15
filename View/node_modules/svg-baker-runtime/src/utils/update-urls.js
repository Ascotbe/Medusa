import namespaces from 'svg-baker/namespaces';
import selectAttributes from './select-attributes';
import arrayFrom from './array-from';

const xLinkNS = namespaces.xlink.uri;
const xLinkAttrName = 'xlink:href';

// eslint-disable-next-line no-useless-escape
const specialUrlCharsPattern = /[{}|\\\^\[\]`"<>]/g;

function encoder(url) {
  return url.replace(specialUrlCharsPattern, (match) => {
    return `%${match[0].charCodeAt(0).toString(16).toUpperCase()}`;
  });
}

function escapeRegExp(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); // $& means the whole matched string
}

/**
 * @param {NodeList} nodes
 * @param {string} startsWith
 * @param {string} replaceWith
 * @return {NodeList}
 */
function updateReferences(nodes, startsWith, replaceWith) {
  arrayFrom(nodes).forEach((node) => {
    const href = node.getAttribute(xLinkAttrName);
    if (href && href.indexOf(startsWith) === 0) {
      const newUrl = href.replace(startsWith, replaceWith);
      node.setAttributeNS(xLinkNS, xLinkAttrName, newUrl);
    }
  });

  return nodes;
}

/**
 * List of SVG attributes to update url() target in them
 */
const attList = [
  'clipPath',
  'colorProfile',
  'src',
  'cursor',
  'fill',
  'filter',
  'marker',
  'markerStart',
  'markerMid',
  'markerEnd',
  'mask',
  'stroke',
  'style'
];

const attSelector = attList.map(attr => `[${attr}]`).join(',');

/**
 * Update URLs in svg image (like `fill="url(...)"`) and update referencing elements
 * @param {Element} svg
 * @param {NodeList} references
 * @param {string|RegExp} startsWith
 * @param {string} replaceWith
 * @return {void}
 *
 * @example
 * const sprite = document.querySelector('svg.sprite');
 * const usages = document.querySelectorAll('use');
 * updateUrls(sprite, usages, '#', 'prefix#');
 */
export default function (svg, references, startsWith, replaceWith) {
  const startsWithEncoded = encoder(startsWith);
  const replaceWithEncoded = encoder(replaceWith);

  const nodes = svg.querySelectorAll(attSelector);
  const attrs = selectAttributes(nodes, ({ localName, value }) => {
    return attList.indexOf(localName) !== -1 && value.indexOf(`url(${startsWithEncoded}`) !== -1;
  });

  attrs.forEach(attr => attr.value = attr.value.replace(new RegExp(escapeRegExp(startsWithEncoded), 'g'), replaceWithEncoded));
  updateReferences(references, startsWithEncoded, replaceWithEncoded);
}
