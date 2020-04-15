/**
 * @param {*} arrayLike
 * @return {Array}
 */
export default function (arrayLike) {
  return Array.prototype.slice.call(arrayLike, 0);
}
