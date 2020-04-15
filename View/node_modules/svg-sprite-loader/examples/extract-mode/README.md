# Extracted sprite example

Extract SVG sprite as separate file with `extract: true` option (see [webpack config](webpack.config.js)).
When loader is in extract mode, the returning value is extracted sprite file URL with symbol id at the end, e.g. `sprite.svg#symbolId`. 
This makes possible to use [SVG stacking technique](https://css-tricks.com/svg-fragment-identifiers-work/#article-header-id-4) which 
 [supported by most of browsers](http://caniuse.com/#feat=svg-fragment) except of Safari (both desktop and mobile) and Android browser prior to 4.4.4.

### [Demo](build/main.html)

### Import from JS

[Input](main.js)
 
```js
import './logo.svg';
```

[Output](build/main.js#L87)

```js
module.exports = 'sprite.svg#logo-usage';
```

### Import from CSS

[Input](main.css)

```css
.logo {background: url('./logo.svg')}
```

[Output](build/main.css)

```css
.logo {background: url('sprite.svg#logo-usage')}
```

### Import from HTML

[Input](main.html)

```html
<img src="./logo.svg" alt="">
```

[Output](build/main.html)

```html
<img src="sprite.svg#logo-usage" alt="">
```

- [sprite.svg](build/sprite-c9cbc8.svg)
- [main.html](build/main.html)
- [main.css](build/main.css)
- [main.js](build/main.js)
