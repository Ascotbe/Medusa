Script Extension for HTML Webpack Plugin
========================================
[![npm version](https://badge.fury.io/js/script-ext-html-webpack-plugin.svg)](http://badge.fury.io/js/script-ext-html-webpack-plugin) [![Dependency Status](https://david-dm.org/numical/script-ext-html-webpack-plugin.svg)](https://david-dm.org/numical/script-ext-html-webpack-plugin) [![Build status](https://travis-ci.org/numical/script-ext-html-webpack-plugin.svg)](https://travis-ci.org/numical/script-ext-html-webpack-plugin) [![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg?style=flat-square)](https://github.com/Flet/semistandard)

[![NPM](https://nodei.co/npm/script-ext-html-webpack-plugin.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/script-ext-html-webpack-plugin/)


Enhances [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin)
functionality with different deployment options for your scripts including:
- [`async`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#Attributes) attribute;
- [`defer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#Attributes) attribute;
- [`type="module"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#Attributes) attribute;
- any custom attributes you wish to add;
- inlining;
- [`preload`](https://www.w3.org/TR/preload/) resource hint;
- [`prefetch`](https://www.w3.org/TR/resource-hints/#dfn-prefetch) resource hint

This is an extension plugin for the [webpack](http://webpack.github.io) plugin [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) - a plugin that simplifies the creation of HTML files to serve your webpack bundles.

The raw [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) incorporates all webpack-generated javascipt as synchronous`<script>` elements in the generated html.  This plugin allows you to:
- add standard and custom attributes to these elements;
- inline the code in the elements;
- add prefetch and preload resource hints for initial and dynamically loaded scripts.

Installation
------------
You must be running webpack (1.x, 2.x, 3.x, 4.x) on node 6+.
Install the plugin with npm:
```shell
$ npm install script-ext-html-webpack-plugin
```
Not that you will need v3.0.6+ or v4.x of [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin)

For those requiring earlier versions of node, please use the [last 1.x version](https://github.com/numical/script-ext-html-webpack-plugin/tree/v1.8.8) of this plugin.  However please note this does not have webpack 4.x support:
```shell
$ npm install script-ext-html-webpack-plugin@1.8.8
```

You may see an `UNMET PEER DEPENDENCY` warnings for webpack and various plugins.

This is fine; in testing, we dynamically download multiple versions of webpack (via the [dynavers](https://github.com/numical/dynavers) module).


Basic Usage
-----------
Add the plugin to your webpack config as follows: 

```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin()
]  
```
The order is important - the plugin must come **after** HtmlWebpackPlugin.

The above configuration will actually do nothing due to the configuration defaults. 

Some more useful scenarios:

All scripts set to `async`:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    defaultAttribute: 'async'
  })
]  
```

All scripts set to `async` except 'first.js' which is sync:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    sync: 'first.js',
    defaultAttribute: 'async'
  })
]  
```

Configuration offers much more complex options:

Configuration
-------------
You must pass a hash of configuration options to the plugin to cause the addition of attributes:
- `inline`: a __script matching pattern__ defining scripts that should be inlined in the html (default: `[]`);
- `sync`: a  __script matching pattern__ defining script names that should have no attribute (default: `[]`);
- `async`: a __script matching pattern__ defining script names that should have an `async` attribute (default: `[]`);
- `defer`: a __script matching pattern__ defining script names that should have a `defer` attribute (default: `[]`);
- `defaultAttribute`: `'sync' | 'async' | 'defer'` The default attribute to set - `'sync'` actually results in no attribute (default: `'sync'`);
- `module`: a __script matching pattern__ defining script names that should have a
`type="module"` attribute (default: `[]`);
- `preload`: a __script matching pattern__ defining scripts that should have accompanying preload resource hints (default: `[]`);
- `prefetch`: a __script matching pattern__ defining scripts that should have accompanying prefetch resource hints (default: `[]`);
- `custom`: a single hash or an array of hashes with the following structure:
    - `test`: a **script matching pattern** defining scripts that should have a custom attribute added;
    - `attribute`: a `String` attribute to add;
    - `value`: (optional) a `String` value for the attribute; if not set the attribute has no value set (equivalent of `true`).

A __script matching pattern__ matches against a script's name.  It can be one of:
- a `String`-  matches if it is a substring of the script name;
- a `RegExp`;
- an array of `String`'s and/or `RegExp`'s - matches if any one element matches;
- a hash with property `test` with a value of one of the above.

In more complicated use cases it may prove difficult to ensure that the pattern matching for different attributes are mutually exclusive.  To prevent confusion, the plugin operates a simple precedence model:

1. if a script name matches the`inline` script matching pattern, it will be inlined;

2. if a script name matches the `sync` script matching pattern, it will have no attribute, *unless* it matched condition 1;

3. if a script name the `async` script matching pattern, it will have the `async` attribute, *unless* it matched conditions 1 or 2;

4. if a script name matches the `defer` script matching pattern, it will have the `defer` attribute, *unless* it matched conditions 1, 2 or 3;

5. if a script name does not match any of the previous conditions, it will have the `defaultAttribute' attribute.

The `module` attribute is independent of conditions 2-5, but will be ignored if the script isinlined.


Dynamically Loaded Scripts
--------------------------
The `preload` and `prefetch` configuration also have allow an additional property in the hash form that can be passed to include dynamically loaded (asynchronous) scripts.  This property is `chunks` and can have one of the following `String` values:
- `initial`: default behaviour, no asynchronour scripts;
- `async`: only asynchronouse scripts;
- `all`: all scripts
Note that you must still supply a `test` __script matching pattern__ which is also applied when selecting scripts.


Configuration Examples
---------------------

All scripts with 'important' in their name are sync and all others set to `defer`:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    sync: 'important'
    defaultAttribute: 'defer'
  })
]  
```

Alternatively, using a regular expression:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    sync: /important/,
    defaultAttribute: 'defer'
  })
]  
```

All scripts with 'mod' in their name are async and type 'module', all others are sync (no explicit setting for this as it is the default):
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    async: 'mod',
    module: 'mod'
  })
]  
```

Script 'startup.js' is inlined whilst all other scripts are async and preloaded:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    inline: 'startup',
    preload: /\.js$/,
    defaultAttribute: 'async'
  })
]  
```

All scripts are preloaded with a ```crossorigin``` attribute set to enable CDN's:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    custom {
      test: /\.js$/,
      attribute: 'crossorigin'
      value: 'anonymous'
    }
    preload: {
      test: /\.js$/
    }
  })
]  
```

All asynchronous scripts are added as `preload` resource hints.  All other scripts are `async`:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    async: /\.js$/
    preload: {
      test: /\.js$/,
      chunks: 'async'
    }
  })
]  
```

All scripts have custom attribute `type='text/paperscript'` and ui.js also has a custom attribute of `id='1235'`:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    custom: [
      {
        test: /\.js$/,
        attribute: 'type',
        value: 'text/paperscript'
      },
      {
        test: 'ui.js',
        attribute: 'id',
        value: '12345'
      }
    ]
  })
]  
```

And so on, to craziness:
```javascript
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    inline: 'startup',  
    sync: [/imp(1|2){1,3}}/, 'initial'],
    defer: ['slow', /big.*andslow/],
    module: [/^((?!sync).)*/, 'mod'],
    prefetch: 'indirectly-referenced.js',
    defaultAttribute: 'async'
  })
]  
```

Any problems with real-world examples, just raise an issue.  


A Note on Script Names
----------------------
In the above examples the actual script names are used to select the deployment option.  You may not wish to couple asset names to your deployment like this.  Instead you can use [Webpack's entry configuration](https://webpack.js.org/concepts/entry-points/#object-syntax) to create aliases that the plugin will then use for its pattern matching. Your `webpack.config.js` will look something like this:
```javascript
entry: {
  a: path.join(__dirname, 'lib/myFunctions.js'),
  b: path.join(__dirname, 'lib/otherFunctions.js'),
  c: path.join(__dirname, 'lib/criticalFuntions.js')
},
output: {
  ...
  filename: '[name].js'
}
plugins: [
  new HtmlWebpackPlugin(),
  new ScriptExtHtmlWebpackPlugin({
    inline: ['c'],  
    defer: ['a', 'b']
  })
]  
```


Inlining
--------
Several notes and caveats apply:
* This feature is for `<script>`'s only. If you wish to inline css please see the sister plugin
[style-ext-html-webpack-plugin](https://github.com/numical/style-ext-html-webpack-plugin).
* Even the simplest script will be wrapped with webpack boilerplate; ensure you minify your javascript if you want your output html to be legible!
* Hot replacement of inlined scripts will only work if caching is [switched off](https://github.com/jantimon/html-webpack-plugin#configuration) for html-webpack-plugin:
```javascript
plugins: [
    new HtmlWebpackPlugin({
      cache: false
    }),
    new ScriptExtHtmlWebpackPlugin({
      inline: ['myinlinedscript.js']
    })
]
```
* An alternative approach, based on jade templates is illustrated in the [HtmlWebpackPlugin inline example](https://github.com/jantimon/html-webpack-plugin/tree/master/examples/inline).


Resource Hints
--------------
In most cases, modern browsers will intelligently preload referenced script assets.
However if you wish, this plugin can add resource hint elements to the `<head>` element of the form:
```html
<link rel="[preload|prefetch]" href="[scriptname]" as="script">
```
Use the `preload` and `prefetch` configuration options.
Where `preload` and `prefetch` patterns overlap, `preload` takes precedence.

Possibly a more compelling use case is to preload/prefetch dynamically loaded scripts generated by Webpack's [code splitting](https://webpack.js.org/guides/code-splitting-require). Since v1.7.0, this plugin can do this - see 'Dynamically Loaded Scripts' above.


Notes:
- custom attributes will be added to resource hints with the same *script matching pattern*.  This is useful for adding such attributes as ```crossorigin="anonymous"``` - see the Configuration Examples above;  
- for more on resource hints, see the [`w3c`](https://www.w3.org/TR/resource-hints) definition;  
- for a more complete solution that allows the preloading\fetching of assets other than scripts, see the [resource-hints-webpack-plugin](https://github.com/jantimon/resource-hints-webpack-plugin).



Change History
--------------

v2.1.x
* custom attributes now added to resource hints too (see [pull request 53](https://github.com/numical/script-ext-html-webpack-plugin/pull/53) for discussion)
* update dependencies

v2.0.x
* support html-webpack-plugin 4.x - huge thanks to [@snadn](https://github.com/snadn)
* support webpack 4.x - huge thanks to [@sherlock1982](https://github.com/sherlock1982)
* node 9.x 10,x, 11.x testing
* remove support for node 4.x and 5.x
* remove Appveyor config
* temororary remove  Handlebars test until loader supports webpack 4.x

v1.8.x
* added custom attributes - now works on inline scripts as well e.g. for CSP nonces, -thanks [@niieani](https://github.com/niieani) and [@phallguy](https://github.com/phallguy)
* compatible with [webpack-config](https://www.npmjs.com/package/webpack-config) - thanks [@avaly](https://github.com/avaly)
* node v8+ and webback 3.x testing
* resource hints handle public paths without end separators - thanks [@albv](https://githun.com/albv)
* updated dependencies (including dev and peer) - thanks [@ai](https://github.com/ai), [@malikshahzad228](https://github.com/malikshahzad228)
* windows-proofed public paths - thanks [@mstijak](https://github.com/mstijak), [@Jesseyx](https://github.com/Jesseyx)
* added appveyor support for windows build and testing - CURRENTLY SWITCHED OFF

v1.7.x
* updated for Webpack 2.5.x and updated all dependencies
* adds asynchronous script resource hints
* fixed [issue 13](https://github.com/numical/script-ext-html-webpack-plugin/issues/13) - inline functionality not working with HtmlWebpackPlugin hashing
* fixed [issue 16](https://github.com/numical/script-ext-html-webpack-plugin/issues/16) - unnecessary <link> closing tag
* fixed [issue 18](https://github.com/numical/script-ext-html-webpack-plugin/issues/18) - added defensive coding against unpopulated event arguments
* refactored for better handling of `publicPath` - thanks [@koalaink](https://github.com/koalaink)

v1.6.x
* works with webpack 2.2.1
* enhanced API (no need to use array), fully backwardly compatible
* refactor in preparation for v2

v1.5.x
* added resource hints
* works with webpack 2.2.0

v1.4.x
* updated internal mechanism to use new(ish) [HtmlWebpackPlugin event](https://github.com/jantimon/html-webpack-plugin#events)
* improved test mechanism and enhanced test coverage
* added support for `publicPath` for inline scripts - thanks [@JustAboutJeff](https://github.com/JustAboutJeff)
* works with 'webpack -p' - thanks [@brandongoode](https://github.com/brandongoode)

v1.3.x
* added `type="text/javascript"` by default, in response to [Safari 9.1.1 bug](https://github.com/jantimon/html-webpack-plugin/issues/309)
* removed experimental status of inline option
* added weback 2.2.x beta support

v1.2.x
* added inline option

v1.1.x
* added `type="module"` option

v1.0.x
* initial release
