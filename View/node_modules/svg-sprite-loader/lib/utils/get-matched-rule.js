// eslint-disable-next-line import/no-extraneous-dependencies
const RuleSet = require('webpack/lib/RuleSet');

module.exports = (compiler) => {
  const rawRules = compiler.options.module.rules;
  const { rules } = new RuleSet(rawRules);
  const rule = rules
    .reduce((pre, cur) => pre.concat(cur.use || []), [])
    .find((item) => {
      return /svg-sprite-loader/.test(item.loader);
    });

  return rule.options || {};
};
