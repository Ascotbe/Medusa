# SVG sprite loader
[![NPM version][version-img]][versions-img] [![Build status][ci-img]][ci-url] [![CodeClimate score][codeclimate-img]][codeclimate-url] [![Documentation score][docs-coverage-img]][docs-coverage-url] [![Dependencies status][deps-img]][deps-url] [![Dev dependencies status][dev-deps-img]][dev-deps-url] [![NPM downloads][downloads-img]][npm-url]

Webpack loader for creating SVG sprites.

> :tada: 2.0 is out, please read the [migration guide & overview](2.0.md).

> :warning: For old v0.x versions see [the README in the v0 branch](https://github.com/kisenka/svg-sprite-loader/blob/v0/README.md).

## Table of contents

- [Why it's cool](#why-its-cool)
- [Installation](#installation)
- [Configuration](#configuration)
  - [`symbolId`](#symbol-id)
  - [`symbolRegExp`](#symbol-regexp)
  - [`esModule`](#es-module)
  - [Runtime configuration](#runtime-configuration)
    - [`spriteModule`](#sprite-module)
    - [`symbolModule`](#symbol-module)
    - [`runtimeGenerator`](#runtime-generator)
    - [`runtimeCompat`](#runtime-compat) (deprecated)
    - [`runtimeOptions`](#runtime-options)
  - [Extract configuration](#extract-configuration)
    - [`extract`](#extract)
    - [`spriteFilename`](#sprite-filename)
    - [`publicPath`](#public-path)
    - [`plainSprite`](#plain-sprite)
    - [`spriteAttrs`](#sprite-attrs)
- [Examples](#examples)
- [Contributing guidelines](#contributing-guidelines)
- [License](#license)
- [Credits](#credits)

## Why it's cool

- **Minimum initial configuration**. Most of the options are configured automatically.
- **Runtime for browser**. Sprites are rendered and injected in pages automatically, you just refer to images via `<svg><use xlink:href="#id"></use></svg>`.
- **Isomorphic runtime for node/browser**. Can render sprites on server or in browser manually.
- **Customizable**. Write/extend runtime module to implement custom sprite behaviour. Write/extend runtime generator to produce your own runtime, e.g. React component configured with imported symbol.
- **External sprite file** is generated for images imported from css/scss/sass/less/styl/html ([SVG stacking technique](https://css-tricks.com/svg-fragment-identifiers-work/#article-header-id-4)).

## Installation

```bash
npm install svg-sprite-loader -D
# via yarn
yarn add svg-sprite-loader -D
```

## Configuration

```js
// webpack 1
{
  test: /\.svg$/,
  loader: 'svg-sprite-loader',
  query: { ... }
}

// webpack 1 multiple loaders
{
  test: /\.svg$/,
  loaders: [
    `svg-sprite-loader?${JSON.stringify({ ... })}`,
    'svg-fill-loader',
    'svgo-loader'
  ]
}

// webpack >= 2
{
  test: /\.svg$/,
  loader: 'svg-sprite-loader',
  options: { ... }
}

// webpack >= 2 multiple loaders
{
  test: /\.svg$/,
  use: [
    { loader: 'svg-sprite-loader', options: { ... } },
    'svg-fill-loader',
    'svgo-loader'
  ]
}
```

<a id="symbol-id"></a>
### `symbolId` (`string | function(path, query)`, default `[name]`)

How `<symbol>` `id` attribute should be named. All patterns from [loader-utils#interpolateName](https://github.com/webpack/loader-utils#interpolatename)
are supported. Also can be a function which accepts 2 args - file path and query string and return symbol id:

```js
{
  symbolId: filePath => path.basename(filePath)
}
```

<a id="symbol-regexp"></a>
### `symbolRegExp` (default `''`)
Passed to the symbolId interpolator to support the [N] pattern in the loader-utils name interpolator

<a id="es-module"></a>
### `esModule` (default `true`, autoconfigured)

Generated export format:
- when `true` loader will produce `export default ...`.
- when `false` the result is `module.exports = ...`.

By default depends on used webpack version: `true` for webpack >= 2, `false` otherwise.

## Runtime configuration

When you require an image, loader transforms it to SVG `<symbol>`, adds it to the special sprite storage and returns class instance
that represents symbol. It contains `id`, `viewBox` and `content` (`id`, `viewBox` and `url` in extract mode)
fields and can later be used for referencing the sprite image, e.g:

```js
import twitterLogo from './logos/twitter.svg';
// twitterLogo === SpriteSymbol<id: string, viewBox: string, content: string>
// Extract mode: SpriteSymbol<id: string, viewBox: string, url: string, toString: Function>

const rendered = `
<svg viewBox="${twitterLogo.viewBox}">
  <use xlink:href="#${twitterLogo.id}" />
</svg>`;
```

When browser event `DOMContentLoaded` is fired, sprite will be automatically rendered and injected in the `document.body`.
If custom behaviour is needed (e.g. a different mounting target) default sprite module could be overridden via `spriteModule` option. Check example below.

<a id="sprite-module"></a>
### `spriteModule` (autoconfigured)

Path to sprite module that will be compiled and executed at runtime.
By default it depends on [`target`](https://webpack.js.org/configuration/target) webpack config option:
- `svg-sprite-loader/runtime/browser-sprite.build` for 'web' target.
- `svg-sprite-loader/runtime/sprite.build` for other targets.

If you need custom behavior, use this option to specify a path of your sprite implementation module.
Path will be resolved relative to the current webpack build folder, e.g. `utils/sprite.js` placed in current project dir should be written as `./utils/sprite`.

Example of sprite with custom mounting target (copypasted from [browser-sprite](https://github.com/kisenka/svg-sprite-loader/blob/master/runtime/browser-sprite.js)):

```js
import BrowserSprite from 'svg-baker-runtime/src/browser-sprite';
import domready from 'domready';

const sprite = new BrowserSprite();
domready(() => sprite.mount('#my-custom-mounting-target'));

export default sprite; // don't forget to export!
```

It's highly recommended to extend default sprite classes:
- [for browser-specific env](https://github.com/kisenka/svg-baker/blob/master/packages/svg-baker-runtime/src/browser-sprite.js)
- [for isomorphic env](https://github.com/kisenka/svg-baker/blob/master/packages/svg-baker-runtime/src/sprite.js)

<a id="symbol-module"></a>
### `symbolModule` (autoconfigured)

Same as `spriteModule`, but for sprite symbol. By default also depends on `target` webpack config option:
- `svg-baker-runtime/browser-symbol` for 'web' target.
- `svg-baker-runtime/symbol` for other targets.

<a id="runtime-generator"></a>
### `runtimeGenerator` ([default generator](https://github.com/kisenka/svg-sprite-loader/blob/master/lib/runtime-generator.js))

Path to node.js script that generates client runtime.
Use this option if you need to produce your own runtime, e.g. React component configured with imported symbol. [Example](https://github.com/kisenka/svg-sprite-loader/tree/master/examples/custom-runtime-generator).

<a id="runtime-compat"></a>
### `runtimeCompat` (default `false`, deprecated)

Should runtime be compatible with earlier v0.x loader versions. This option will be removed in the next major version release.

<a id="runtime-options"></a>
### `runtimeOptions`

Arbitrary data passed to runtime generator. Reserved for future use when other runtime generators will be created.

## Extract configuration

In the extract mode loader should be configured with plugin, otherwise an error is thrown. Example:

```js
// webpack.config.js
const SpriteLoaderPlugin = require('svg-sprite-loader/plugin');

...

{
  plugins: [
    new SpriteLoaderPlugin()
  ]
}
```

<a id="extract"></a>
### `extract` (default `false`, autoconfigured)

Switches loader to the extract mode.
Enabled automatically for images imported from css/scss/sass/less/styl/html files.

<a id="sprite-filename"></a>
### `spriteFilename` (type `string|Function<string>`,default `sprite.svg`)

Filename of extracted sprite. Multiple sprites can be generated by specifying different loader rules restricted with `include` option or
by providing custom function which recieves SVG file absolute path, e.g.:

```js
{
  test: /\.svg$/,
  loader: 'svg-sprite-loader',
  options: {
    extract: true,
    spriteFilename: svgPath => `sprite${svgPath.substr(-4)}`
  }
}
```

`[hash]` in sprite filename will be replaced by it's content hash.
It is also possible to generate sprite for each chunk by using `[chunkname]` pattern in spriteFilename option. This is experimental feature, use it with caution!

<a id="public-path"></a>
### `publicPath` (type: `string`, default: `__webpack_public_path__`)

Custom public path for sprite file.

```js
{
  test: /\.svg$/,
  loader: 'svg-sprite-loader',
  options: {
    extract: true,
    publicPath: '/'
  }
}
```

<a id="plain-sprite"></a>
### Plain sprite

You can render plain sprite in extract mode without styles and usages. Pass `plainSprite: true` option to plugin constructor:

```js
{
  plugins: [
    new SpriteLoaderPlugin({ plainSprite: true })
  ]
}
```

<a id="sprite-attrs"></a>
### Sprite attributes

Sprite `<svg>` tag attributes can be specified via `spriteAttrs` plugin option:

```js
{
  plugins: [
    new SpriteLoaderPlugin({
      plainSprite: true,
      spriteAttrs: {
        id: 'my-custom-sprite-id'
      }
    })
  ]
}
```

## Examples

See [examples](examples) folder.

## Contributing guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE](LICENSE)

## Credits

Huge thanks for [all this people](https://github.com/kisenka/svg-sprite-loader/graphs/contributors).

[npm-url]: https://www.npmjs.com/package/svg-sprite-loader
[version-img]: https://img.shields.io/npm/v/svg-sprite-loader.svg?style=flat-square
[versions-img]: https://libraries.io/npm/svg-sprite-loader/versions
[downloads-img]: https://img.shields.io/npm/dm/svg-sprite-loader.svg?style=flat-square
[deps-url]: https://david-dm.org/kisenka/svg-sprite-loader
[deps-img]: https://img.shields.io/david/kisenka/svg-sprite-loader.svg?style=flat-square
[dev-deps-url]: https://david-dm.org/kisenka/svg-sprite-loader?type=dev
[dev-deps-img]: https://img.shields.io/david/dev/kisenka/svg-sprite-loader.svg?style=flat-square
[ci-url]: https://travis-ci.org/kisenka/svg-sprite-loader
[ci-img]: https://img.shields.io/travis/kisenka/svg-sprite-loader.svg?style=flat-square
[codeclimate-url]: https://codeclimate.com/github/kisenka/svg-sprite-loader
[codeclimate-img]: https://img.shields.io/codeclimate/github/kisenka/svg-sprite-loader.svg?style=flat-square
[docs-coverage-url]: https://inch-ci.org/github/kisenka/svg-sprite-loader
[docs-coverage-img]: https://inch-ci.org/github/kisenka/svg-sprite-loader.svg?branch=master&style=flat-square
