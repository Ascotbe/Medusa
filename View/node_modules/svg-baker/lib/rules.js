class Rule {
  constructor({ test, value }) {
    if (!(test instanceof RegExp)) {
      throw new TypeError('`test` should be a regexp');
    }

    this.test = test;
    this.value = value;
  }

  /**
   * @param {string} value
   * @return {boolean}
   */
  match(value) {
    return this.test.test(value);
  }
}

class RuleSet {
  /**
   * @param {Array<{test: RegExp, uri: string}>} rules
   */
  constructor(rules) {
    if (!Array.isArray(rules)) {
      throw new TypeError('`data` should be an array');
    }

    this.rules = rules.map(params => new Rule(params));
  }

  /**
   * @param {string} value
   * @return {Rule|null}
   */
  getMatchedRule(value) {
    return this.rules.find(rule => rule.match(value)) || null;
  }
}

module.exports = RuleSet;
module.exports.Rule = Rule;
