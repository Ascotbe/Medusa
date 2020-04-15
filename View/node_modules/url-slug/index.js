const unidecode = require('unidecode');

const INVALID_SEPARATOR_REGEXP = /[^-._~]/;
const TITLE_CASE_REGEXP = /(?:^| )[a-z]/g;
const CONVERT_REGEXP = /[^A-Za-z0-9]+|([a-z])([A-Z])/g;
const CONVERT_SEPARATOR_REGEXP = / /g;
const REVERT_REGEXP = {}; /* RegExp intances are based on the separator and then cached */
const REVERT_AUTO_REGEXP = /[-._~]+|([a-z])([A-Z])/g;
const REVERT_CAMEL_CASE_REGEXP = /([a-z])([A-Z])/g;

/**
 * Creates a new instance of url-slug
 */
function UrlSlug(separator, transform) {

    /* Set defaults */

    separator = null == separator ? '-' : separator;
    transform = null == transform ? 'lowercase' : transform;

    /* Validate through prepare method */

    var options = this.prepare(separator, transform);

    this.separator = options.separator;
    this.transform = options.transform;

}

/**
 * Builtin transformers
 */
UrlSlug.prototype.transformers = {

    lowercase: function (string) {
        return string.toLowerCase();
    },

    uppercase: function (string) {
        return string.toUpperCase();
    },

    titlecase: function (string) {
        return string.toLowerCase().replace(TITLE_CASE_REGEXP, function (character) {
            return character.toUpperCase();
        });
    },

};

/**
 * Check and return validated options
 */
UrlSlug.prototype.prepare = function (separator, transform) {

    if (null == separator) {
        separator = this.separator;
    } else if ('string' !== typeof separator) {
        throw new Error('Invalid separator, must be a string: "' + separator + '".');
    } else if (INVALID_SEPARATOR_REGEXP.test(separator)) {
        throw new Error('Invalid separator, has invalid characters: "' + separator + '".');
    }

    if (null == transform) {
        transform = this.transform;
    } else if (false === transform) {
        transform = false;
    } else if (this.transformers[transform]) {
        transform = this.transformers[transform];
    } else if ('function' !== typeof transform) {
        throw new Error('Invalid transform, must be a builtin transform or a function: "' + transform + '".');
    }

    return {
        separator: separator,
        transform: transform,
    }

}

/**
 * Converts a string into a slug
 */
UrlSlug.prototype.convert = function (string, separator, transform) {

    if ('string' !== typeof string) {
        throw new Error('Invalid value, must be a string: "' + string + '".');
    }

    options = this.prepare(separator, transform);

    /* Transliterate and replace invalid characters, then replace non alphanumeric characters with spaces */

    string = unidecode(string).replace('[?]', '').replace(CONVERT_REGEXP, '$1 $2').trim();

    /* Pass string through transform function */

    if (options.transform) {
        string = options.transform(string);
    }

    /* Replace spaces with separator and return */

    return string.replace(CONVERT_SEPARATOR_REGEXP, options.separator);

};

/**
 * Reverts a slug back to a string
 */
UrlSlug.prototype.revert = function (slug, separator, transform) {

    if ('string' !== typeof slug) {
        throw new Error('Invalid value, must be a string: "' + slug + '".');
    }

    options = this.prepare(separator, transform);

    /* Determine which regular expression will be used to—and—remove separators */

    if ('' === options.separator) {
        slug = slug.replace(REVERT_CAMEL_CASE_REGEXP, '$1 $2');
    } else if ('string' === typeof separator) {
        /* If separator argument was set as string, don't check options.separator,
        it can return the default separator (this.separator) */
        REVERT_REGEXP[separator] = REVERT_REGEXP[separator] || new RegExp('\\' + separator.split('').join('\\'), 'g');
        slug = slug.replace(REVERT_REGEXP[separator], ' ');
    } else {
        slug = slug.replace(REVERT_AUTO_REGEXP, '$1 $2');
    }

    /* Pass slug through transform function and return. Check if transform
    was set in arguments, to avoid using the default transform. */

    return transform && options.transform ? options.transform(slug) : slug;

};

/* Prepare the global instance and export it */

var urlSlug = new UrlSlug;
var globalInstance = urlSlug.convert.bind(urlSlug);

globalInstance.UrlSlug = UrlSlug;
globalInstance.convert = globalInstance;
globalInstance.revert = urlSlug.revert.bind(urlSlug);

module.exports = globalInstance;
