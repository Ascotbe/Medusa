# posthtml-rename-id

[PostHTML](https://github.com/posthtml/posthtml) plugin to rename id attributes 
and it's references. Inspired by [grunt-svgstore](https://github.com/FWeinb/grunt-svgstore).

Handle following cases:

- `href="#id"` and `xlink:href="#id"`
- `style` attribute values like `style="fill: url(#id)"`
- `<style>` tag values like `.selector {fill: url(#id)"}`
- any other attribute value like `attr="url(#id)"`

## Demo

Input
```html
<style>
.selector {fill: url(#qwe)}
</style>

<div id="qwe"></div>
<a href="#qwe"></a>
```

Output
```html
<style>
.selector {fill: url(#prefix_qwe)}
</style>

<div id="prefix_qwe"></div>
<a href="#prefix_qwe"></a>
```

## Install

```sh
npm install posthtml-rename-id
```

## Usage

```js
const posthtml = require('posthtml');
const rename = require('posthtml-rename-id');

posthtml()
  .use(rename('prefix_[id]'))
  .process('<div id="qwe"></div> <a href="#qwe"></a>')
  .then(({ html }) => {
    console.log(html); // <div id="prefix_qwe"></div> <a href="#prefix_qwe"></a>
  });
```

## Configuration

### `pattern`

> Type: `string | function`<br>
> Default: `'[id]'`

Renaming pattern. `[id]` placeholder can be used as current id of an element.
If `pattern` provided as a function it will be called with current id as first argument.
Function should return the new id as string (`[id]` can be used as well).

## Examples

Uppercase all ids:
```js
posthtml([
  renameId(id => id.toUpperCase())
]);
```

Rename all ids to `elem_{counter}`:
```js
let c = 0;
posthtml([
  renameId((id) => { c++; return 'elem_' + c; })
]);
```

## LICENSE

[MIT](https://github.com/JetBrains/svg-mixer/blob/master/LICENSE)
