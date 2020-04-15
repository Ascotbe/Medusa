# microargs ![node version](https://img.shields.io/node/v/microargs.svg) [![Build Status](https://travis-ci.org/pawelgalazka/microargs.svg?branch=master)](https://travis-ci.org/pawelgalazka/microargs) [![npm version](https://badge.fury.io/js/microargs.svg)](https://badge.fury.io/js/microargs)
CLI arguments micro parser. Only 38 lines of code, no dependencies.

``` js
#!/usr/bin/env node
const args = require('microargs')(process.argv.slice(2));
console.dir(args);
```

```
$ script.js -a --foo=bar --boo abc def
{
    params: ['abc', 'def'],
    options: { a: true, foo: 'bar', boo: true }
}
