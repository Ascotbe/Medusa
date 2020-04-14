import arrayFrom from './array-from';

/**
 * @param {NodeList|Node} nodes
 * @param {boolean} [clone=true]
 * @return {string}
 */
export default function (nodes, clone = true) {
  const wrapper = document.createElement('div');

  if (nodes instanceof NodeList) {
    arrayFrom(nodes).forEach((node) => {
      wrapper.appendChild(clone === true ? node.cloneNode(true) : node);
    });
  } else if (nodes instanceof Node) {
    wrapper.appendChild(clone === true ? nodes.cloneNode(true) : nodes);
  }

  return wrapper.innerHTML;
}
