# Server side rendering example

When webpack config target option is 'node' svg-sprite-loader will use isomorphic runtime sprite module.
 
### [Demo](build/index.html)

### Input

[main.js](main.js)

```js
import symbol from '../assets/twitter.svg';

// Import sprite instance which already contains twitter logo required above
import sprite from 'svg-sprite-loader/runtime/sprite.build';

// Render sprite
const spriteContent = sprite.stringify();

const pageContent = `
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
${spriteContent}

<svg viewBox="${symbol.viewBox}">
  <use xlink:href="#${symbol.id}"></use>
</svg>
</body>
</html>
`;

console.log(pageContent);
```

### Output

- [build/main.js](build/main.js)
- [build/index.html](build/index.html)
