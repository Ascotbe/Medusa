/**
 * @param {string} name
 * @param {*} data
 */
export default function (name, data) {
  const event = document.createEvent('CustomEvent');
  event.initCustomEvent(name, false, false, data);
  window.dispatchEvent(event);
}
