const traverse = require('traverse');
const clone = require('clone');

// Fixes Firefox bug https://bugzilla.mozilla.org/show_bug.cgi?id=353575
const defaultConfig = {
  tags: ['linearGradient', 'radialGradient', 'pattern', 'clipPath', 'mask']
};

function moveFromSymbolToRoot(config = null) {
  const cfg = Object.assign({}, defaultConfig, config);

  return (tree) => {
    traverse(tree).forEach(function (node) {
      if (!this.isLeaf && node.tag && node.tag === 'symbol') {
        const symbol = this.parent.node;
        const nodesToRemove = [];

        traverse(node.content).forEach(function (n) {
          if (!this.isLeaf && n.tag && cfg.tags.indexOf(n.tag) !== -1) {
            const parent = this.parent.node;
            const cloned = clone(this.node);
            symbol.push(cloned);
            nodesToRemove.push({ parent, node: n });
          }
        });

        nodesToRemove.forEach((item) => {
          const nodeIndex = item.parent.indexOf(item.node);
          item.parent.splice(nodeIndex, 1);
        });
      }
    });

    return tree;
  };
}

module.exports = moveFromSymbolToRoot;
