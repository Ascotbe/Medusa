const escapeRegExpSpecialChars = require('escape-string-regexp');

const isWindows = /^win/i.test(process.platform);

/**
 * @param {string} content
 * @param {Object<string, string>} replacements
 * @return {string}
 */
function replaceSpritePlaceholder(content, replacements) {
  let result = content;
  Object.keys(replacements)
    .forEach((subj) => {
      let re = new RegExp(escapeRegExpSpecialChars(subj), 'g');
      result = result.replace(re, replacements[subj]);

      if (isWindows) {
        re = new RegExp(escapeRegExpSpecialChars(subj), 'g');
        result = result.replace(/\\\\/g, '\\').replace(re, replacements[subj]);
      }
    });

  return result;
}

module.exports = replaceSpritePlaceholder;
