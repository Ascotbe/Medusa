# TOAST UI Tools: Code Snippet
> Group of utility methods to make ease with developing javascript applications.

[![GitHub release](https://img.shields.io/github/release/nhn/tui.code-snippet.svg)](https://github.com/nhn/tui.code-snippet/releases/latest)
[![npm](https://img.shields.io/npm/v/tui-code-snippet.svg)](https://www.npmjs.com/package/tui-code-snippet)
[![GitHub license](https://img.shields.io/github/license/nhn/tui.code-snippet.svg)](https://github.com/nhn/tui.code-snippet/blob/production/LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](https://github.com/nhn/tui.code-snippet/labels/help%20wanted)
[![code with hearth by NHN](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-NHN-ff1414.svg)](https://github.com/nhn)


## 🚩 Table of Contents
* [Documents](#-documents)
* [Features](#-features)
* [Install](#-install)
* [Usage](#-usage)
  * [Bundle](#bundle)
* [Browser Support](#-browser-support)
* [Pull Request Steps](#-pull-request-steps)
* [Contributing](#-contributing)
* [TOAST UI Family](#-toast-ui-family)
* [License](#-license)


## 📙 Documents

* [APIs](https://nhn.github.io/tui.code-snippet/latest/)
* [v2.0 Migration Guide](https://github.com/nhn/tui.code-snippet/blob/v2.1.0/docs/v2.0-migration-guide.md)

You can also see the older versions of API page on the [releases page](https://github.com/nhn/tui.code-snippet/releases).


## 🎨 Features

* ajax
  * Send the Ajax request
* array
  * Handle arrays
* browser
  * Detect browser
* collection
  * Process collections
  * Support util methods for collections
* customEvents
  * Add/Remove/fire custom events
* defineClass
  * Define classes
* domEvent
  * Add, remove, fire DOM events
  * Control mouse events
* domUtil
  * Control the information of DOM
  * Add, remove, find DOM class name
* enum
  * Manage constant value
  * Make immutability values but IE8 low
* formatDate
  * Format date strings
* inheritance
  * Simple inheritance (Nicholas C. Zakas, YUI Library)
  * Call supur constructor of superclass
  * Have to get inheritance before define child
  * Use mixin and inner object
* object
  * Support utils to control object
* request
  * Request image ping
* string
  * Support utils such as decodeHTMLEntity, encodeHTMLEntity
* tricks
  * Creates a debounced function and a throttled function
* type
  * Check data type


## 💾 Install

TOAST UI products can be used by using the package manager or downloading the source directly. However, we highly recommend using the package manager.

### Via Package Manager

TOAST UI products are registered in two package managers, [npm](https://www.npmjs.com/).
You can conveniently install it using the commands provided by each package manager.
When using npm, be sure to use it in the environment [Node.js](https://nodejs.org/) is installed.

#### npm

``` sh
$ npm install --save tui-code-snippet # Latest version
$ npm install --save tui-code-snippet@<version> # Specific version
```

### Download Source Files

* [Download all sources for each version](https://github.com/nhn/tui.code-snippet/releases)


## 🔨 Usage

Import only functions that you need in your code:

```javascript
var func = require('tui-code-snippet/<folder>/<function>');

// for example,
var inArray = require('tui-code-snippet/array/inArray');
var customEvents = require('tui-code-snippet/customEvents/customEvents');
```

The folder structure can be found [here](https://github.com/nhn/tui.code-snippet/tree/master).

### Bundle

Since v2.0, it does not provide bundle files. If you need a bundle file, you should make it yourself using the command `npm run bundle`.

```sh
$ git clone https://github.com/nhn/tui.code-snippet.git
$ cd tui.code-snippet
$ npm install
$ npm run bundle
```

After executing `npm run bundle`, the uncompressed(`tui-code-snippet.js`) and minified(`tui-code-snippet.min.js`) files are created in the `dist` folder.

```
tui.code-snippet/
├─ dist
│  ├─ tui-code-snippet.js
│  ├─ tui-code-snippet.min.js
├─ ...
```

The entry file is `index.js`. When you do not modify `index.js`, all methods of tui.code-snippet will be included in the bundle file. To bundle the methods you need, remove other methods in the entry file.

```javascript
// index.js
// for example, you need inArray, forEach and isArray methods only.
require('./array/inArray');
require('./collection/forEach');
require('./type/isArray');
```


## 🌏 Browser Support

| <img src="https://user-images.githubusercontent.com/1215767/34348387-a2e64588-ea4d-11e7-8267-a43365103afe.png" alt="Chrome" width="16px" height="16px" /> Chrome | <img src="https://user-images.githubusercontent.com/1215767/34348590-250b3ca2-ea4f-11e7-9efb-da953359321f.png" alt="IE" width="16px" height="16px" /> Internet Explorer | <img src="https://user-images.githubusercontent.com/1215767/34348380-93e77ae8-ea4d-11e7-8696-9a989ddbbbf5.png" alt="Edge" width="16px" height="16px" /> Edge | <img src="https://user-images.githubusercontent.com/1215767/34348394-a981f892-ea4d-11e7-9156-d128d58386b9.png" alt="Safari" width="16px" height="16px" /> Safari | <img src="https://user-images.githubusercontent.com/1215767/34348383-9e7ed492-ea4d-11e7-910c-03b39d52f496.png" alt="Firefox" width="16px" height="16px" /> Firefox |
| :---------: | :---------: | :---------: | :---------: | :---------: |
| Yes | 8+ | Yes | Yes | Yes |


## 🔧 Pull Request Steps

TOAST UI products are open source, so you can create a pull request(PR) after you fix issues.
Run npm scripts and develop yourself with the following process.

### Setup

Fork `master` branch into your personal repository.
Clone it to local computer. Install node modules.
Before starting development, you should check to have any errors.

``` sh
$ git clone https://github.com/{your-personal-repo}/tui.code-snippet.git
$ cd tui.code-snippet
$ npm install
$ npm run test
```

### Develop

Let's start development!
Don't miss adding test cases and then make green rights.

#### Run karma test

``` sh
$ npm run test
```

### Pull Request

Before PR, check to test lastly and then check any errors.
If it has no error, commit and then push it!

For more information on PR's step, please see links of Contributing section.


## 💬 Contributing
* [Code of Conduct](https://github.com/nhn/tui.code-snippet/blob/master/CODE_OF_CONDUCT.md)
* [Contributing guideline](https://github.com/nhn/tui.code-snippet/blob/master/CONTRIBUTING.md)
* [Issue guideline](https://github.com/nhn/tui.code-snippet/blob/master/docs/ISSUE_TEMPLATE.md)
* [Commit convention](https://github.com/nhn/tui.code-snippet/blob/master/docs/COMMIT_MESSAGE_CONVENTION.md)


## 🍞 TOAST UI Family

* [TOAST UI Editor](https://github.com/nhn/tui.editor)
* [TOAST UI Calendar](https://github.com/nhn/tui.calendar)
* [TOAST UI Chart](https://github.com/nhn/tui.chart)
* [TOAST UI Image-Editor](https://github.com/nhn/tui.image-editor)
* [TOAST UI Grid](https://github.com/nhn/tui.grid)
* [TOAST UI Components](https://github.com/nhn)


## 📜 License
This software is licensed under the [MIT License](https://github.com/nhn/tui.code-snippet/blob/master/LICENSE) © [NHN](https://github.com/nhn).