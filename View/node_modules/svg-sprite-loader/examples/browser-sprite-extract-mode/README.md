# Default browser runtime example

In browser sprite is rendered and injected in page automatically, you just refer to images via `<svg><use xlink:href="#id"></use></svg>`.

### [Demo](demo.html)

Input

```js
import twitterIcon from '../assets/twitter.svg';
```

Reference in HTML

```html
<svg>
  <use xlink:href="#twitter"></use>
</svg>
```

### Input

- [main.js](main.js)
- [demo.html](demo.html)
- [webpack.config.js](webpack.config.js)

### Output

- [build/main.js](build/main.js)
