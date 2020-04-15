/**
 * @param {string} [url] If not provided - current URL will be used
 * @return {string}
 */
export default function (url) {
  return (url || window.location.href).split('#')[0];
}
