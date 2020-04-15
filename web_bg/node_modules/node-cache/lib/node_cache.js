/*
 * node-cache 4.2.1 ( 2019-07-24 )
 * https://github.com/mpneuried/nodecache
 *
 * Released under the MIT license
 * https://github.com/mpneuried/nodecache/blob/master/LICENSE
 *
 * Maintained by  (  )
*/
(function() {
  // lodash requires
  var EventEmitter, NodeCache, _assignIn, _isArray, _isFunction, _isNumber, _isObject, _isString, _size, _template, clone,
    boundMethodCheck = function(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new Error('Bound instance method accessed before binding'); } },
    indexOf = [].indexOf;

  _assignIn = require("lodash/assignIn");

  _isArray = require("lodash/isArray");

  _isString = require("lodash/isString");

  _isFunction = require("lodash/isFunction");

  _isNumber = require("lodash/isNumber");

  _isObject = require("lodash/isObject");

  _size = require("lodash/size");

  _template = require("lodash/template");

  clone = require("clone");

  EventEmitter = require('events').EventEmitter;

  // generate superclass
  module.exports = NodeCache = (function() {
    class NodeCache extends EventEmitter {
      constructor(options = {}) {
        super();
        // ## get

        // get a cached key and change the stats

        // **Parameters:**

        // * `key` ( String | Number ): cache key
        // * `[cb]` ( Function ): Callback function
        // * `[errorOnMissing=false]` ( Boolean ) return a error to the `cb` or throw it if no `cb` is used. Otherwise the get will return `undefined` on a miss.

        // **Example:**

        //     myCache.get "myKey", ( err, val )->
        //       console.log( err, val )
        //       return

        this.get = this.get.bind(this);
        // ## mget

        // get multiple cached keys at once and change the stats

        // **Parameters:**

        // * `keys` ( String|Number[] ): an array of keys
        // * `[cb]` ( Function ): Callback function

        // **Example:**

        //     myCache.mget [ "foo", "bar" ], ( err, val )->
        //       console.log( err, val )
        //       return

        this.mget = this.mget.bind(this);
        // ## set

        // set a cached key and change the stats

        // **Parameters:**

        // * `key` ( String | Number ): cache key
        // * `value` ( Any ): A element to cache. If the option `option.forceString` is `true` the module trys to translate it to a serialized JSON
        // * `[ ttl ]` ( Number | String ): ( optional ) The time to live in seconds.
        // * `[cb]` ( Function ): Callback function

        // **Example:**

        //     myCache.set "myKey", "my_String Value", ( err, success )->
        //       console.log( err, success )

        //     myCache.set "myKey", "my_String Value", "10", ( err, success )->
        //       console.log( err, success )

        this.set = this.set.bind(this);
        // ## del

        // remove keys

        // **Parameters:**

        // * `keys` ( String | Number | String|Number[] ): cache key to delete or a array of cache keys
        // * `[cb]` ( Function ): Callback function

        // **Return**

        // ( Number ): Number of deleted keys

        // **Example:**

        //     myCache.del( "myKey" )

        //     myCache.del( "myKey", ( err, delCount )->
        //       console.log( err, delCount )
        //       return
        this.del = this.del.bind(this);
        // ## ttl

        // reset or redefine the ttl of a key. `ttl` = 0 means infinite lifetime.
        // If `ttl` is not passed the default ttl is used.
        // If `ttl` < 0 the key will be deleted.

        // **Parameters:**

        // * `key` ( String | Number ): cache key to reset the ttl value
        // * `ttl` ( Number ): ( optional -> options.stdTTL || 0 ) The time to live in seconds
        // * `[cb]` ( Function ): Callback function

        // **Return**

        // ( Boolen ): key found and ttl set

        // **Example:**

        //     myCache.ttl( "myKey" ) // will set ttl to default ttl

        //     myCache.ttl( "myKey", 1000, ( err, keyFound )->
        //       console.log( err, success )

        this.ttl = this.ttl.bind(this);
        // ## getTtl

        // receive the ttl of a key.

        // **Parameters:**

        // * `key` ( String | Number ): cache key to check the ttl value
        // * `[cb]` ( Function ): Callback function

        // **Return**

        // ( Number|undefined ): The timestamp in ms when the key will expire, 0 if it will never expire or undefined if it not exists

        // **Example:**

        //     ts = myCache.getTtl( "myKey" )

        //     myCache.getTtl( "myKey",( err, ttl )->
        //       console.log( err, ttl )
        //       return

        this.getTtl = this.getTtl.bind(this);
        // ## keys

        // list all keys within this cache

        // **Parameters:**

        // * `[cb]` ( Function ): Callback function

        // **Return**

        // ( Array ): An array of all keys

        // **Example:**

        //     _keys = myCache.keys()

        //     # [ "foo", "bar", "fizz", "buzz", "anotherKeys" ]

        this.keys = this.keys.bind(this);
        // ## getStats

        // get the stats

        // **Parameters:**

        // -

        // **Return**

        // ( Object ): Stats data

        // **Example:**

        //     myCache.getStats()
        //     # {
        //     # hits: 0,
        //     # misses: 0,
        //     # keys: 0,
        //     # ksize: 0,
        //     # vsize: 0
        //     # }

        this.getStats = this.getStats.bind(this);
        // ## flushAll

        // flush the whole data and reset the stats

        // **Example:**

        //     myCache.flushAll()

        //     myCache.getStats()
        //     # {
        //     # hits: 0,
        //     # misses: 0,
        //     # keys: 0,
        //     # ksize: 0,
        //     # vsize: 0
        //     # }

        this.flushAll = this.flushAll.bind(this);
        // ## close

        // This will clear the interval timeout which is set on checkperiod option.

        // **Example:**

        //     myCache.close()

        this.close = this.close.bind(this);
        // ## _checkData

        // internal housekeeping method.
        // Check all the cached data and delete the invalid values
        this._checkData = this._checkData.bind(this);
        // ## _check

        // internal method the check the value. If it's not valid any more delete it
        this._check = this._check.bind(this);
        // ## _isInvalidKey

        // internal method to check if the type of a key is either `number` or `string`
        this._isInvalidKey = this._isInvalidKey.bind(this);
        // ## _wrap

        // internal method to wrap a value in an object with some metadata
        this._wrap = this._wrap.bind(this);
        // ## _getValLength

        // internal method to calculate the value length
        this._getValLength = this._getValLength.bind(this);
        // ## _error

        // internal method to handle an error message
        this._error = this._error.bind(this);
        // ## _initErrors

        // internal method to generate error message templates
        this._initErrors = this._initErrors.bind(this);
        this.options = options;
        this._initErrors();
        // container for cached data
        this.data = {};
        // module options
        this.options = _assignIn({
          // convert all elements to string
          forceString: false,
          // used standard size for calculating value size
          objectValueSize: 80,
          promiseValueSize: 80,
          arrayValueSize: 40,
          // standard time to live in seconds. 0 = infinity;
          stdTTL: 0,
          // time in seconds to check all data and delete expired keys
          checkperiod: 600,
          // en/disable cloning of variables. If `true` you'll get a copy of the cached variable. If `false` you'll save and get just the reference
          useClones: true,
          // en/disable throwing errors when trying to `.get` missing or expired values.
          errorOnMissing: false,
          // whether values should be deleted automatically at expiration
          deleteOnExpire: true
        }, this.options);
        // statistics container
        this.stats = {
          hits: 0,
          misses: 0,
          keys: 0,
          ksize: 0,
          vsize: 0
        };
        // pre allocate valid keytypes array
        this.validKeyTypes = ["string", "number"];
        // initalize checking period
        this._checkData();
        return;
      }

      get(key, cb, errorOnMissing) {
        var _err, _ret, err;
        boundMethodCheck(this, NodeCache);
        // handle passing in errorOnMissing without cb
        if (typeof cb === "boolean" && arguments.length === 2) {
          errorOnMissing = cb;
          cb = void 0;
        }
        // handle invalid key types
        if ((err = this._isInvalidKey(key)) != null) {
          if (cb != null) {
            cb(err);
            return;
          } else {
            throw err;
          }
        }
        // get data and incremet stats
        if ((this.data[key] != null) && this._check(key, this.data[key])) {
          this.stats.hits++;
          _ret = this._unwrap(this.data[key]);
          if (cb != null) {
            // return data
            cb(null, _ret);
          }
          return _ret;
        } else {
          // if not found return a error
          this.stats.misses++;
          if (this.options.errorOnMissing || errorOnMissing) {
            _err = this._error("ENOTFOUND", {
              key: key
            }, cb);
            if (_err != null) {
              throw _err;
            }
            return;
          } else {
            if (cb != null) {
              cb(null, void 0);
            }
          }
          return void 0;
        }
      }

      mget(keys, cb) {
        var _err, err, i, key, len, oRet;
        boundMethodCheck(this, NodeCache);
        // convert a string to an array of one key
        if (!_isArray(keys)) {
          _err = this._error("EKEYSTYPE");
          if (cb != null) {
            cb(_err);
          }
          return _err;
        }
        // define return
        oRet = {};
        for (i = 0, len = keys.length; i < len; i++) {
          key = keys[i];
          // handle invalid key types
          if ((err = this._isInvalidKey(key)) != null) {
            if (cb != null) {
              cb(err);
              return;
            } else {
              throw err;
            }
          }
          // get data and increment stats
          if ((this.data[key] != null) && this._check(key, this.data[key])) {
            this.stats.hits++;
            oRet[key] = this._unwrap(this.data[key]);
          } else {
            // if not found return a error
            this.stats.misses++;
          }
        }
        if (cb != null) {
          // return all found keys
          cb(null, oRet);
        }
        return oRet;
      }

      set(key, value, ttl, cb) {
        var err, existent;
        boundMethodCheck(this, NodeCache);
        // force the data to string
        if (this.options.forceString && !_isString(value)) {
          value = JSON.stringify(value);
        }
        // remap the arguments if `ttl` is not passed
        if (arguments.length === 3 && _isFunction(ttl)) {
          cb = ttl;
          ttl = this.options.stdTTL;
        }
        // handle invalid key types
        if ((err = this._isInvalidKey(key)) != null) {
          if (cb != null) {
            cb(err);
            return;
          } else {
            throw err;
          }
        }
        // internal helper variables
        existent = false;
        // remove existing data from stats
        if (this.data[key]) {
          existent = true;
          this.stats.vsize -= this._getValLength(this._unwrap(this.data[key], false));
        }
        // set the value
        this.data[key] = this._wrap(value, ttl);
        this.stats.vsize += this._getValLength(value);
        // only add the keys and key-size if the key is new
        if (!existent) {
          this.stats.ksize += this._getKeyLength(key);
          this.stats.keys++;
        }
        this.emit("set", key, value);
        if (cb != null) {
          // return true
          cb(null, true);
        }
        return true;
      }

      del(keys, cb) {
        var delCount, err, i, key, len, oldVal;
        boundMethodCheck(this, NodeCache);
        // convert keys to an array of itself
        if (!_isArray(keys)) {
          keys = [keys];
        }
        delCount = 0;
        for (i = 0, len = keys.length; i < len; i++) {
          key = keys[i];
          // handle invalid key types
          if ((err = this._isInvalidKey(key)) != null) {
            if (cb != null) {
              cb(err);
              return;
            } else {
              throw err;
            }
          }
          // only delete if existent
          if (this.data[key] != null) {
            // calc the stats
            this.stats.vsize -= this._getValLength(this._unwrap(this.data[key], false));
            this.stats.ksize -= this._getKeyLength(key);
            this.stats.keys--;
            delCount++;
            // delete the value
            oldVal = this.data[key];
            delete this.data[key];
            // return true
            this.emit("del", key, oldVal.v);
          } else {
            // if the key has not been found return an error
            this.stats.misses++;
          }
        }
        if (cb != null) {
          cb(null, delCount);
        }
        return delCount;
      }

      ttl() {
        var arg, args, cb, err, i, key, len, ttl;
        boundMethodCheck(this, NodeCache);
        // change args if only key and callback are passed
        [key, ...args] = arguments;
        for (i = 0, len = args.length; i < len; i++) {
          arg = args[i];
          switch (typeof arg) {
            case "number":
              ttl = arg;
              break;
            case "function":
              cb = arg;
          }
        }
        ttl || (ttl = this.options.stdTTL);
        if (!key) {
          if (cb != null) {
            cb(null, false);
          }
          return false;
        }
        // handle invalid key types
        if ((err = this._isInvalidKey(key)) != null) {
          if (cb != null) {
            cb(err);
            return;
          } else {
            throw err;
          }
        }
        // check for existant data and update the ttl value
        if ((this.data[key] != null) && this._check(key, this.data[key])) {
          // if ttl < 0 delete the key. otherwise reset the value
          if (ttl >= 0) {
            this.data[key] = this._wrap(this.data[key].v, ttl, false);
          } else {
            this.del(key);
          }
          if (cb != null) {
            cb(null, true);
          }
          return true;
        } else {
          if (cb != null) {
            // return false if key has not been found
            cb(null, false);
          }
          return false;
        }
      }

      getTtl(key, cb) {
        var _ttl, err;
        boundMethodCheck(this, NodeCache);
        if (!key) {
          if (cb != null) {
            cb(null, void 0);
          }
          return void 0;
        }
        // handle invalid key types
        if ((err = this._isInvalidKey(key)) != null) {
          if (cb != null) {
            cb(err);
            return;
          } else {
            throw err;
          }
        }
        // check for existant data and update the ttl value
        if ((this.data[key] != null) && this._check(key, this.data[key])) {
          _ttl = this.data[key].t;
          if (cb != null) {
            cb(null, _ttl);
          }
          return _ttl;
        } else {
          if (cb != null) {
            // return undefined if key has not been found
            cb(null, void 0);
          }
          return void 0;
        }
      }

      keys(cb) {
        var _keys;
        boundMethodCheck(this, NodeCache);
        _keys = Object.keys(this.data);
        if (cb != null) {
          cb(null, _keys);
        }
        return _keys;
      }

      getStats() {
        boundMethodCheck(this, NodeCache);
        return this.stats;
      }

      flushAll(_startPeriod = true) {
        boundMethodCheck(this, NodeCache);
        // parameter just for testing

        // set data empty
        this.data = {};
        // reset stats
        this.stats = {
          hits: 0,
          misses: 0,
          keys: 0,
          ksize: 0,
          vsize: 0
        };
        // reset check period
        this._killCheckPeriod();
        this._checkData(_startPeriod);
        this.emit("flush");
      }

      close() {
        boundMethodCheck(this, NodeCache);
        this._killCheckPeriod();
      }

      _checkData(startPeriod = true) {
        var key, ref, value;
        boundMethodCheck(this, NodeCache);
        ref = this.data;
        // run the housekeeping method
        for (key in ref) {
          value = ref[key];
          this._check(key, value);
        }
        if (startPeriod && this.options.checkperiod > 0) {
          this.checkTimeout = setTimeout(this._checkData, this.options.checkperiod * 1000, startPeriod);
          if (this.checkTimeout.unref != null) {
            this.checkTimeout.unref();
          }
        }
      }

      // ## _killCheckPeriod

      // stop the checkdata period. Only needed to abort the script in testing mode.
      _killCheckPeriod() {
        if (this.checkTimeout != null) {
          return clearTimeout(this.checkTimeout);
        }
      }

      _check(key, data) {
        var _retval;
        boundMethodCheck(this, NodeCache);
        _retval = true;
        // data is invalid if the ttl is too old and is not 0
        // console.log data.t < Date.now(), data.t, Date.now()
        if (data.t !== 0 && data.t < Date.now()) {
          if (this.options.deleteOnExpire) {
            _retval = false;
            this.del(key);
          }
          this.emit("expired", key, this._unwrap(data));
        }
        return _retval;
      }

      _isInvalidKey(key) {
        var ref;
        boundMethodCheck(this, NodeCache);
        if (ref = typeof key, indexOf.call(this.validKeyTypes, ref) < 0) {
          return this._error("EKEYTYPE", {
            type: typeof key
          });
        }
      }

      _wrap(value, ttl, asClone = true) {
        var livetime, now, oReturn, ttlMultiplicator;
        boundMethodCheck(this, NodeCache);
        if (!this.options.useClones) {
          asClone = false;
        }
        // define the time to live
        now = Date.now();
        livetime = 0;
        ttlMultiplicator = 1000;
        // use given ttl
        if (ttl === 0) {
          livetime = 0;
        } else if (ttl) {
          livetime = now + (ttl * ttlMultiplicator);
        } else {
          // use standard ttl
          if (this.options.stdTTL === 0) {
            livetime = this.options.stdTTL;
          } else {
            livetime = now + (this.options.stdTTL * ttlMultiplicator);
          }
        }
        // return the wrapped value
        return oReturn = {
          t: livetime,
          v: asClone ? clone(value) : value
        };
      }

      // ## _unwrap

      // internal method to extract get the value out of the wrapped value
      _unwrap(value, asClone = true) {
        if (!this.options.useClones) {
          asClone = false;
        }
        if (value.v != null) {
          if (asClone) {
            return clone(value.v);
          } else {
            return value.v;
          }
        }
        return null;
      }

      // ## _getKeyLength

      // internal method the calculate the key length
      _getKeyLength(key) {
        return key.length;
      }

      _getValLength(value) {
        boundMethodCheck(this, NodeCache);
        if (_isString(value)) {
          // if the value is a String get the real length
          return value.length;
        } else if (this.options.forceString) {
          // force string if it's defined and not passed
          return JSON.stringify(value).length;
        } else if (_isArray(value)) {
          // if the data is an Array multiply each element with a defined default length
          return this.options.arrayValueSize * value.length;
        } else if (_isNumber(value)) {
          return 8;
        } else if (typeof (value != null ? value.then : void 0) === "function") {
          // if the data is a Promise, use defined default
          // (can't calculate actual/resolved value size synchronously)
          return this.options.promiseValueSize;
        } else if (_isObject(value)) {
          // if the data is an Object multiply each element with a defined default length
          return this.options.objectValueSize * _size(value);
        } else {
          // default fallback
          return 0;
        }
      }

      _error(type, data = {}, cb) {
        var error;
        boundMethodCheck(this, NodeCache);
        // generate the error object
        error = new Error();
        error.name = type;
        error.errorcode = type;
        error.message = this.ERRORS[type] != null ? this.ERRORS[type](data) : "-";
        error.data = data;
        if (cb && _isFunction(cb)) {
          // return the error
          cb(error, null);
        } else {
          // if no callback is defined return the error object
          return error;
        }
      }

      _initErrors() {
        var _errMsg, _errT, ref;
        boundMethodCheck(this, NodeCache);
        this.ERRORS = {};
        ref = this._ERRORS;
        for (_errT in ref) {
          _errMsg = ref[_errT];
          this.ERRORS[_errT] = _template(_errMsg);
        }
      }

    };

    NodeCache.prototype._ERRORS = {
      "ENOTFOUND": "Key `<%= key %>` not found",
      "EKEYTYPE": "The key argument has to be of type `string` or `number`. Found: `<%= type %>`",
      "EKEYSTYPE": "The keys argument has to be an array."
    };

    return NodeCache;

  }).call(this);

}).call(this);
