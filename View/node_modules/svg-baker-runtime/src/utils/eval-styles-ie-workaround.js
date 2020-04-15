import arrayFrom from './array-from';

/**
 * IE doesn't evaluate <style> tags in SVGs that are dynamically added to the page.
 * This trick will trigger IE to read and use any existing SVG <style> tags.
 * @see https://github.com/iconic/SVGInjector/issues/23
 * @see https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/10898469/
 *
 * @param {Element} node DOM Element to search <style> tags in
 * @return {Array<HTMLStyleElement>}
 */
export default function (node) {
  const updatedNodes = [];

  arrayFrom(node.querySelectorAll('style'))
    .forEach((style) => {
      style.textContent += '';
      updatedNodes.push(style);
    });

  return updatedNodes;
}
