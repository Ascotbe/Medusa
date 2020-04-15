"use strict";

exports.__esModule = true;
exports["default"] = void 0;

var _forEachArray = _interopRequireDefault(require("../collection/forEachArray"));

var _forEachOwnProperties = _interopRequireDefault(require("../collection/forEachOwnProperties"));

var _extend = _interopRequireDefault(require("../object/extend"));

var _isArray = _interopRequireDefault(require("../type/isArray"));

var _isEmpty = _interopRequireDefault(require("../type/isEmpty"));

var _isFunction = _interopRequireDefault(require("../type/isFunction"));

var _isNull = _interopRequireDefault(require("../type/isNull"));

var _isObject = _interopRequireDefault(require("../type/isObject"));

var _isUndefined = _interopRequireDefault(require("../type/isUndefined"));

function _interopRequireDefault(obj) {
  return obj && obj.__esModule ? obj : {
    "default": obj
  };
}

function encodePairs(key, value) {
  return encodeURIComponent(key) + "=" + encodeURIComponent((0, _isNull["default"])(value) || (0, _isUndefined["default"])(value) ? '' : value);
}

function serializeParams(key, value, serializedList) {
  if ((0, _isArray["default"])(value)) {
    (0, _forEachArray["default"])(value, function (arrVal, index) {
      serializeParams(key + "[" + ((0, _isObject["default"])(arrVal) ? index : '') + "]", arrVal, serializedList);
    });
  } else if ((0, _isObject["default"])(value)) {
    (0, _forEachOwnProperties["default"])(value, function (objValue, objKey) {
      serializeParams(key + "[" + objKey + "]", objValue, serializedList);
    });
  } else {
    serializedList.push(encodePairs(key, value));
  }
}

function serialize(params) {
  if (!params || (0, _isEmpty["default"])(params)) {
    return '';
  }

  var serializedList = [];
  (0, _forEachOwnProperties["default"])(params, function (value, key) {
    serializeParams(key, value, serializedList);
  });
  return serializedList.join('&');
}

var getDefaultOptions = function getDefaultOptions() {
  return {
    baseURL: '',
    headers: {
      common: {},
      get: {},
      post: {},
      put: {},
      "delete": {},
      patch: {},
      options: {},
      head: {}
    },
    serializer: serialize
  };
};

var HTTP_PROTOCOL_REGEXP = /^(http|https):\/\//i;

function combineURL(baseURL, url) {
  if (HTTP_PROTOCOL_REGEXP.test(url)) {
    return url;
  }

  if (baseURL.slice(-1) === '/' && url.slice(0, 1) === '/') {
    url = url.slice(1);
  }

  return baseURL + url;
}

function getComputedOptions(defaultOptions, customOptions) {
  var baseURL = defaultOptions.baseURL,
      defaultHeaders = defaultOptions.headers,
      defaultSerializer = defaultOptions.serializer,
      defaultBeforeRequest = defaultOptions.beforeRequest,
      defaultSuccess = defaultOptions.success,
      defaultError = defaultOptions.error,
      defaultComplete = defaultOptions.complete;
  var url = customOptions.url,
      contentType = customOptions.contentType,
      method = customOptions.method,
      params = customOptions.params,
      headers = customOptions.headers,
      serializer = customOptions.serializer,
      beforeRequest = customOptions.beforeRequest,
      success = customOptions.success,
      error = customOptions.error,
      complete = customOptions.complete,
      withCredentials = customOptions.withCredentials,
      mimeType = customOptions.mimeType;
  var options = {
    url: combineURL(baseURL, url),
    method: method,
    params: params,
    headers: (0, _extend["default"])(defaultHeaders.common, defaultHeaders[method.toLowerCase()], headers),
    serializer: serializer || defaultSerializer || serialize,
    beforeRequest: [defaultBeforeRequest, beforeRequest],
    success: [defaultSuccess, success],
    error: [defaultError, error],
    complete: [defaultComplete, complete],
    withCredentials: withCredentials,
    mimeType: mimeType
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
  if ((0, _isArray["default"])(callback)) {
    (0, _forEachArray["default"])(callback, function (fn) {
      return executeCallback(fn, param);
    });
  } else if ((0, _isFunction["default"])(callback)) {
    callback(param);
  }
}

function parseHeaders(text) {
  var headers = {};
  (0, _forEachArray["default"])(text.split('\r\n'), function (header) {
    var _header$split = header.split(': '),
        key = _header$split[0],
        value = _header$split[1];

    if (key !== '' && !(0, _isUndefined["default"])(value)) {
      headers[key] = value;
    }
  });
  return headers;
}

function parseJSONData(data) {
  var result = '';

  try {
    result = JSON.parse(data);
  } catch (_) {
    result = data;
  }

  return result;
}

var REQUEST_DONE = 4;

function handleReadyStateChange(xhr, options) {
  var readyState = xhr.readyState;

  if (readyState != REQUEST_DONE) {
    return;
  }

  var status = xhr.status,
      statusText = xhr.statusText,
      responseText = xhr.responseText;
  var success = options.success,
      resolve = options.resolve,
      error = options.error,
      reject = options.reject,
      complete = options.complete;

  if (validateStatus(status)) {
    var contentType = xhr.getResponseHeader('Content-Type');
    var data = responseText;

    if (contentType && contentType.indexOf('application/json') > -1) {
      data = parseJSONData(data);
    }

    executeCallback([success, resolve], {
      status: status,
      statusText: statusText,
      data: data,
      headers: parseHeaders(xhr.getAllResponseHeaders())
    });
  } else {
    executeCallback([error, reject], {
      status: status,
      statusText: statusText
    });
  }

  executeCallback(complete, {
    status: status,
    statusText: statusText
  });
}

var QS_DELIM_REGEXP = /\?/;

function open(xhr, options) {
  var url = options.url,
      method = options.method,
      serializer = options.serializer,
      params = options.params;
  var requestUrl = url;

  if (!hasRequestBody(method) && params) {
    var qs = (QS_DELIM_REGEXP.test(url) ? '&' : '?') + serializer(params);
    requestUrl = "" + url + qs;
  }

  xhr.open(method, requestUrl);
}

function applyConfig(xhr, options) {
  var method = options.method,
      contentType = options.contentType,
      mimeType = options.mimeType,
      headers = options.headers,
      _options$withCredenti = options.withCredentials,
      withCredentials = _options$withCredenti === void 0 ? false : _options$withCredenti;

  if (withCredentials) {
    xhr.withCredentials = withCredentials;
  }

  if (mimeType) {
    xhr.overrideMimeType(mimeType);
  }

  (0, _forEachOwnProperties["default"])(headers, function (value, header) {
    if (!(0, _isObject["default"])(value)) {
      xhr.setRequestHeader(header, value);
    }
  });

  if (hasRequestBody(method)) {
    xhr.setRequestHeader('Content-Type', contentType + "; charset=UTF-8");
  }

  xhr.setRequestHeader('x-requested-with', 'XMLHttpRequest');
}

var ENCODED_SPACE_REGEXP = /%20/g;

function send(xhr, options) {
  var method = options.method,
      serializer = options.serializer,
      beforeRequest = options.beforeRequest,
      _options$params = options.params,
      params = _options$params === void 0 ? {} : _options$params,
      _options$contentType = options.contentType,
      contentType = _options$contentType === void 0 ? 'application/x-www-form-urlencoded' : _options$contentType;
  var body = null;

  if (hasRequestBody(method)) {
    body = contentType.indexOf('application/x-www-form-urlencoded') > -1 ? serializer(params).replace(ENCODED_SPACE_REGEXP, '+') : JSON.stringify(params);
  }

  xhr.onreadystatechange = function () {
    return handleReadyStateChange(xhr, options);
  };

  executeCallback(beforeRequest, xhr);
  xhr.send(body);
}

function ajax(options) {
  var xhr = new XMLHttpRequest();

  var request = function request(opts) {
    return (0, _forEachArray["default"])([open, applyConfig, send], function (fn) {
      return fn(xhr, opts);
    });
  };

  options = getComputedOptions(ajax.defaults, options);

  if (typeof Promise !== 'undefined') {
    return new Promise(function (resolve, reject) {
      request((0, _extend["default"])(options, {
        resolve: resolve,
        reject: reject
      }));
    });
  }

  request(options);
  return null;
}

ajax.defaults = getDefaultOptions();

ajax._reset = function () {
  ajax.defaults = getDefaultOptions();
};

ajax._request = function (url, method, options) {
  if (options === void 0) {
    options = {};
  }

  return ajax((0, _extend["default"])(options, {
    url: url,
    method: method
  }));
};

(0, _forEachArray["default"])(['get', 'post', 'put', 'delete', 'patch', 'options', 'head'], function (type) {
  ajax[type] = function (url, options) {
    return ajax._request(url, type.toUpperCase(), options);
  };
});
var _default = ajax;
exports["default"] = _default;
module.exports = exports["default"];
