import forEachArray from '../collection/forEachArray';
import forEachOwnProperties from '../collection/forEachOwnProperties';
import extend from '../object/extend';
import isArray from '../type/isArray';
import isEmpty from '../type/isEmpty';
import isFunction from '../type/isFunction';
import isNull from '../type/isNull';
import isObject from '../type/isObject';
import isUndefined from '../type/isUndefined';

function encodePairs(key, value) {
  return `${encodeURIComponent(key)}=${encodeURIComponent(
    isNull(value) || isUndefined(value) ? '' : value
  )}`;
}

function serializeParams(key, value, serializedList) {
  if (isArray(value)) {
    forEachArray(value, (arrVal, index) => {
      serializeParams(`${key}[${isObject(arrVal) ? index : ''}]`, arrVal, serializedList);
    });
  } else if (isObject(value)) {
    forEachOwnProperties(value, (objValue, objKey) => {
      serializeParams(`${key}[${objKey}]`, objValue, serializedList);
    });
  } else {
    serializedList.push(encodePairs(key, value));
  }
}

/**
 * Serializer to serialize parameters
 * @callback ajax/serializer
 * @param {*} params - parameter to serialize
 * @returns {string} - serialized strings
 */

/**
 * Serializer
 *
 * 1. Array format
 *
 * The default array format to serialize is 'bracket'.
 * However in case of nested array, only the deepest format follows the 'bracket', the rest follow 'indice' format.
 *
 * - basic
 *   { a: [1, 2, 3] } => a[]=1&a[]=2&a[]=3
 * - nested
 *   { a: [1, 2, [3]] } => a[]=1&a[]=2&a[2][]=3
 *
 * 2. Object format
 *
 * The default object format to serialize is 'bracket' notation and doesn't allow the 'dot' notation.
 *
 * - basic
 *   { a: { b: 1, c: 2 } } => a[b]=1&a[c]=2
 *
 * @param {*} params - parameters to serialize
 * @returns {string}
 * @private
 */
function serialize(params) {
  if (!params || isEmpty(params)) {
    return '';
  }
  const serializedList = [];
  forEachOwnProperties(params, (value, key) => {
    serializeParams(key, value, serializedList);
  });

  return serializedList.join('&');
}

const getDefaultOptions = () => ({
  baseURL: '',
  headers: {
    common: {},
    get: {},
    post: {},
    put: {},
    delete: {},
    patch: {},
    options: {},
    head: {}
  },
  serializer: serialize
});

const HTTP_PROTOCOL_REGEXP = /^(http|https):\/\//i;

/**
 * Combine an absolute URL string (baseURL) and a relative URL string (url).
 * @param {string} baseURL - An absolute URL string
 * @param {string} url - An relative URL string
 * @returns {string}
 * @private
 */
function combineURL(baseURL, url) {
  if (HTTP_PROTOCOL_REGEXP.test(url)) {
    return url;
  }

  if (baseURL.slice(-1) === '/' && url.slice(0, 1) === '/') {
    url = url.slice(1);
  }

  return baseURL + url;
}

/**
 * Get merged options by its priorities.
 * defaults.common < defaults[method] < custom options
 * @param {Object} defaultOptions - The default options
 * @param {Object} customOptions - The custom options
 * @returns {Object}
 * @private
 */
function getComputedOptions(defaultOptions, customOptions) {
  const {
    baseURL,
    headers: defaultHeaders,
    serializer: defaultSerializer,
    beforeRequest: defaultBeforeRequest,
    success: defaultSuccess,
    error: defaultError,
    complete: defaultComplete
  } = defaultOptions;
  const {
    url,
    contentType,
    method,
    params,
    headers,
    serializer,
    beforeRequest,
    success,
    error,
    complete,
    withCredentials,
    mimeType
  } = customOptions;

  const options = {
    url: combineURL(baseURL, url),
    method,
    params,
    headers: extend(defaultHeaders.common, defaultHeaders[method.toLowerCase()], headers),
    serializer: serializer || defaultSerializer || serialize,
    beforeRequest: [defaultBeforeRequest, beforeRequest],
    success: [defaultSuccess, success],
    error: [defaultError, error],
    complete: [defaultComplete, complete],
    withCredentials,
    mimeType
  };

  options.contentType = contentType || options.headers['Content-Type'];
  delete options.headers['Content-Type'];

  return options;
}

function validateStatus(status) {
  return status >= 200 && status < 300;
}

function hasRequestBody(method) {
  return /^(?:POST|PUT|PATCH)$/.test(method.toUpperCase());
}

function executeCallback(callback, param) {
  if (isArray(callback)) {
    forEachArray(callback, fn => executeCallback(fn, param));
  } else if (isFunction(callback)) {
    callback(param);
  }
}

function parseHeaders(text) {
  const headers = {};

  forEachArray(text.split('\r\n'), header => {
    const [key, value] = header.split(': ');

    if (key !== '' && !isUndefined(value)) {
      headers[key] = value;
    }
  });

  return headers;
}

function parseJSONData(data) {
  let result = '';
  try {
    result = JSON.parse(data);
  } catch (_) {
    result = data;
  }

  return result;
}

const REQUEST_DONE = 4;

function handleReadyStateChange(xhr, options) {
  const { readyState } = xhr;

  // eslint-disable-next-line eqeqeq
  if (readyState != REQUEST_DONE) {
    return;
  }

  const { status, statusText, responseText } = xhr;
  const { success, resolve, error, reject, complete } = options;

  if (validateStatus(status)) {
    const contentType = xhr.getResponseHeader('Content-Type');
    let data = responseText;

    if (contentType && contentType.indexOf('application/json') > -1) {
      data = parseJSONData(data);
    }

    /**
     * successCallback is executed when the response is received successfully
     * @callback ajax/successCallback
     * @param {Object} response - success response wrapper
     * @param {number} response.status - response status code
     * @param {string} response.statusText - response status text
     * @param {*} response.data - response data. If its Content-Type is 'application/json', the parsed object will be passed.
     * @param {Object.<string,string>} response.headers - response headers
     */
    executeCallback([success, resolve], {
      status,
      statusText,
      data,
      headers: parseHeaders(xhr.getAllResponseHeaders())
    });
  } else {
    /**
     * errorCallback executed when the request failed
     * @callback ajax/errorCallback
     * @param {Object} response - error response wrapper
     * @param {number} response.status - response status code
     * @param {string} response.statusText - response status text
     */
    executeCallback([error, reject], { status, statusText });
  }

  /**
   * completeCallback executed when the request is completed after success or error callbacks are executed
   * @callback ajax/completeCallback
   * @param {Object} response - error response wrapper
   * @param {number} response.status - response status code
   * @param {string} response.statusText - response status text
   */
  executeCallback(complete, { status, statusText });
}

const QS_DELIM_REGEXP = /\?/;

function open(xhr, options) {
  const { url, method, serializer, params } = options;

  let requestUrl = url;

  if (!hasRequestBody(method) && params) {
    // serialize query string
    const qs = (QS_DELIM_REGEXP.test(url) ? '&' : '?') + serializer(params);
    requestUrl = `${url}${qs}`;
  }

  xhr.open(method, requestUrl);
}

function applyConfig(xhr, options) {
  const { method, contentType, mimeType, headers, withCredentials = false } = options;

  // set withCredentials (IE10+)
  if (withCredentials) {
    xhr.withCredentials = withCredentials;
  }

  // override MIME type (IE11+)
  if (mimeType) {
    xhr.overrideMimeType(mimeType);
  }

  forEachOwnProperties(headers, (value, header) => {
    if (!isObject(value)) {
      xhr.setRequestHeader(header, value);
    }
  });

  if (hasRequestBody(method)) {
    xhr.setRequestHeader('Content-Type', `${contentType}; charset=UTF-8`);
  }

  // set 'x-requested-with' header to prevent CSRF in old browser
  xhr.setRequestHeader('x-requested-with', 'XMLHttpRequest');
}

const ENCODED_SPACE_REGEXP = /%20/g;

function send(xhr, options) {
  const {
    method,
    serializer,
    beforeRequest,
    params = {},
    contentType = 'application/x-www-form-urlencoded'
  } = options;

  let body = null;

  if (hasRequestBody(method)) {
    // The space character '%20' is replaced to '+', because application/x-www-form-urlencoded follows rfc-1866
    body =
      contentType.indexOf('application/x-www-form-urlencoded') > -1
        ? serializer(params).replace(ENCODED_SPACE_REGEXP, '+')
        : JSON.stringify(params);
  }

  xhr.onreadystatechange = () => handleReadyStateChange(xhr, options);

  /**
   * beforeRequestCallback is executed before the Ajax request is sent
   * @callback ajax/beforeRequestCallback
   * @param {XMLHttpRequest} xhr - XMLHttpRequest object
   */
  executeCallback(beforeRequest, xhr);
  xhr.send(body);
}

/**
 * @module ajax
 * @description
 * A module for the Ajax request.
 * If the browser supports Promise, return the Promise object. If not, return null.
 * @param {Object} options - Options for the Ajax request
 * @param {string} options.url - URL string
 * @param {('GET'|'POST'|'PUT'|'DELETE'|'PATCH'|'OPTIONS'|'HEAD')} options.method - Method of the Ajax request
 * @param {string} [options.contentType] - Content-Type for the Ajax request. It is applied to POST, PUT, and PATCH requests only. Its encoding automatically sets to UTF-8.
 * @param {*} [options.params] - Parameters to send by the Ajax request
 * @param {serializer} [options.serializer] - {@link ajax_serializer Serializer} that determine how to serialize the parameters. Default serializer is {@link https://github.com/nhn/tui.code-snippet/tree/v2.3.0/ajax/index.mjs#L38 serialize()}.
 * @param {beforeRequestCallback} [options.beforeRequest] - {@link ajax_beforeRequestCallback beforeRequest callback} executed before the Ajax request is sent.
 * @param {successCallback} [options.success] - {@link ajax_successCallback success callback} executed when the response is received successfully.
 * @param {errorCallback} [options.error] - {@link ajax_errorCallback error callback} executed when the request failed.
 * @param {completeCallback} [options.complete] - {@link ajax_completeCallback complete callback} executed when the request is completed after success or error callbacks are executed.
 * @param {boolean} [options.withCredentials] - Determine whether cross-site Access-Control requests should be made using credentials or not. This option can be used on IE10+
 * @param {string} [options.mimeType] - Override the MIME type returned by the server. This options can be used on IE11+
 * @returns {?Promise} - If the browser supports Promise, return the Promise object. If not, return null.
 * @example
 * import ajax from 'tui-code-snippet/ajax'; // import ES6 module (written in ES6)
 * // import ajax from 'tui-code-snippet/ajax/index.js'; // import transfiled file (IE8+)
 * // var ajax = require('tui-code-snippet/ajax/index.js'); // commonjs
 *
 * // If the browser supports Promise, return the Promise object
 * ajax({
 *   url: 'https://nhn.github.io/tui-code-snippet/',
 *   method: 'POST',
 *   contentType: 'application/json',
 *   params: {
 *     version: 'v2.3.0',
 *     author: 'NHN. FE Development Lab <dl_javascript@nhn.com>'
 *   },
 *   success: res => console.log(`success: ${res.status} ${res.statusText}`),
 *   error: res => console.log(`error: ${res.status} ${res.statusText}`)
 * }).then(res => console.log(`resolve: ${res.status} ${res.statusText}`))
 *   .catch(res => console.log(`reject: ${res.status} ${res.statusText}`));
 *
 * // If the request succeeds (200, OK)
 * // success: 200 OK
 * // resolve: 200 OK
 *
 * // If the request failed (503, Service Unavailable)
 * // error: 503 Service Unavailable
 * // reject: 503 Service Unavailable
 *
 * // If the browser does not support Promise, return null
 * ajax({
 *   url: 'https://ui.toast.com/fe-guide/',
 *   method: 'GET',
 *   contentType: 'application/json',
 *   params: {
 *     lang: 'en'
 *     title: 'PERFORMANCE',
 *   },
 *   success: res => console.log(`success: ${res.status} ${res.statusText}`),
 *   error: res => console.log(`error: ${res.status} ${res.statusText}`)
 * });
 *
 * // If the request succeeds (200, OK)
 * // success: 200 OK
 *
 * // If the request failed (503, Service Unavailable)
 * // error: 503 Service Unavailable
 */
function ajax(options) {
  const xhr = new XMLHttpRequest();
  const request = opts => forEachArray([open, applyConfig, send], fn => fn(xhr, opts));

  options = getComputedOptions(ajax.defaults, options);

  if (typeof Promise !== 'undefined') {
    return new Promise((resolve, reject) => {
      request(extend(options, { resolve, reject }));
    });
  }

  request(options);

  return null;
}

/**
 * Default configuration for the Ajax request.
 * @property {string} baseURL - baseURL appended with url of ajax options. If url is absolute, baseURL is ignored.
 * ex) baseURL = 'https://nhn.github.io', url = '/tui.code-snippet' => request is sent to 'https://nhn.github.io/tui.code-snippet'
 * ex) baseURL = 'https://nhn.github.io', url = 'https://ui.toast.com' => request is sent to 'https://ui.toast.com'
 * @property {Object} headers - request headers. It extends the header object in the following order: headers.common -> headers\[method\] -> headers in ajax options.
 * @property {Object.<string,string>} headers.common - Common headers regardless of the type of request
 * @property {Object.<string,string>} headers.get - Headers for the GET method
 * @property {Object.<string,string>} headers.post - Headers for the POST method
 * @property {Object.<string,string>} headers.put - Headers for the PUT method
 * @property {Object.<string,string>} headers.delete - Headers for the DELETE method
 * @property {Object.<string,string>} headers.patch - Headers for the PATCH method
 * @property {Object.<string,string>} headers.options - Headers for the OPTIONS method
 * @property {Object.<string,string>} headers.head - Headers for the HEAD method
 * @property {serializer} serializer - {@link ajax_serializer Serializer} that determine how to serialize the parameters. If serializer is specified in both default options and ajax options, use serializer in ajax options.
 * @property {beforeRequestCallback} beforeRequest - {@link ajax_beforeRequestCallback beforeRequest callback} executed before the Ajax request is sent. Callbacks in both default options and ajax options are executed, but default callbacks are called first.
 * @property {successCallback} success - {@link ajax_successCallback success callback} executed when the response is received successfully. Callbacks in both default options and ajax options are executed, but default callbacks are called first.
 * @property {errorCallback} error - {@link ajax_errorCallback error callback} executed when the request failed. Callbacks in both default options and ajax options are executed, but default callbacks are called first.
 * @property {completeCallback} complete - {@link ajax_completeCallback complete callback} executed when the request is completed after success or error callbacks are executed. Callbacks in both default options and ajax options are executed, but default callbacks are called first.
 * @example
 * ajax.defaults.baseURL = 'https://nhn.github.io/tui.code-snippet';
 * ajax.defaults.headers.common = {
 *   'Content-Type': 'application/json'
 * };
 * ajax.defaults.beforeRequest = () => showProgressBar();
 * ajax.defaults.complete = () => hideProgressBar();
 */
ajax.defaults = getDefaultOptions();

/**
 * Reset the default options
 * @private
 */
ajax._reset = function() {
  ajax.defaults = getDefaultOptions();
};

/**
 * Ajax request
 * @private
 */
ajax._request = function(url, method, options = {}) {
  return ajax(extend(options, { url, method }));
};

/**
 * Send the Ajax request by GET
 * @memberof module:ajax
 * @function get
 * @param {string} url - URL string
 * @param {object} options - Options for the Ajax request. Refer to {@link ajax options of ajax()}.
 * @example
 * ajax.get('https://nhn.github.io/tui.code-snippet/', {
 *   params: {
 *     version: 'v2.3.0'
 *   }
 * });
 */

/**
 * Send the Ajax request by POST
 * @memberof module:ajax
 * @function post
 * @param {string} url - URL string
 * @param {object} options - Options for the Ajax request. Refer to {@link ajax options of ajax()}.
 * @example
 * ajax.post('https://nhn.github.io/tui.code-snippet/', {
 *   contentType: 'application/json',
 *   params: {
 *     version: 'v2.3.0'
 *   }
 * });
 */

/**
 * Send the Ajax request by PUT
 * @memberof module:ajax
 * @function put
 * @param {string} url - URL string
 * @param {object} options - Options for the Ajax request. Refer to {@link ajax options of ajax()}.
 * @example
 * ajax.put('https://nhn.github.io/tui.code-snippet/v2.3.0', {
 *   success: ({status, statusText}) => alert(`success: ${status} ${statusText}`),
 *   error: ({status, statusText}) => alert(`error: ${status} ${statusText}`)
 * });
 */

/**
 * Send the Ajax request by DELETE
 * @memberof module:ajax
 * @function delete
 * @param {string} url - URL string
 * @param {object} options - Options for the Ajax request. Refer to {@link ajax options of ajax()}.
 * @example
 * ajax.delete('https://nhn.github.io/tui.code-snippet/v2.3.0');
 */

/**
 * Send the Ajax request by PATCH
 * @memberof module:ajax
 * @function patch
 * @param {string} url - URL string
 * @param {object} options - Options for the Ajax request. Refer to {@link ajax options of ajax()}.
 * @example
 * ajax.patch('https://nhn.github.io/tui.code-snippet/v2.3.0', {
 *   beforeRequest: () => showProgressBar(),
 *   complete: () => hideProgressBar()
 * });
 */

/**
 * Send the Ajax request by OPTIONS
 * @memberof module:ajax
 * @function options
 * @param {string} url - URL string
 * @param {object} options - Options for the Ajax request. Refer to {@link ajax options of ajax()}.
 * @example
 * ajax.head('https://nhn.github.io/tui.code-snippet/v2.3.0');
 */

/**
 * Send the Ajax request by HEAD
 * @memberof module:ajax
 * @function head
 * @param {string} url - URL string
 * @param {object} options - Options for the Ajax request. Refer to {@link ajax options of ajax()}.
 * @example
 * ajax.options('https://nhn.github.io/tui.code-snippet/v2.3.0');
 */
forEachArray(['get', 'post', 'put', 'delete', 'patch', 'options', 'head'], type => {
  ajax[type] = (url, options) => ajax._request(url, type.toUpperCase(), options);
});

export default ajax;
