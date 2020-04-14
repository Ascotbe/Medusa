/**
 * @param {Object} attrs
 * @return {string}
 */
export default function (attrs) {
  return Object.keys(attrs).map((attr) => {
    const value = attrs[attr].toString().replace(/"/g, '&quot;');
    return `${attr}="${value}"`;
  }).join(' ');
}
