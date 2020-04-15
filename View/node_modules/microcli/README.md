# microcli ![node version](https://img.shields.io/node/v/microcli.svg) [![Build Status](https://travis-ci.org/pawelgalazka/microcli.svg?branch=master)](https://travis-ci.org/pawelgalazka/microcli) [![npm version](https://badge.fury.io/js/microcli.svg)](https://badge.fury.io/js/microcli)
CLI scripts micro engine

```js
#!/usr/bin/env node
const microcli = require('microcli')
const cli = microcli(process.argv, 'Script doc');
cli((options, p1, p2) => {
    console.log('OPTIONS', options)
    console.log('P1', p1)
    console.log('P2', p2)
})
```

```
$ script.js -a --foo=bar --boo abc def
OPTIONS {a: true, foo: 'bar', boo: true }
P1 abc
P2 def

$ script.js --help
Usage: script.js

Script doc
```

### Annotations

```js
#!/usr/bin/env node
const microcli = require('microcli')
const cli = microcli(process.argv, {
  description: 'Basic script description',
  params: ['p1', 'p2'],
  options: {
    a: 'description for a option',
    foo: 'description for foo option'
  },
  examples: 'some examples'
});

cli((options, p1, p2) => {
    console.log('OPTIONS', options)
    console.log('P1', p1)
    console.log('P2', p2)
})
```

```
$ script.js --help
Usage: script.js [options] [p1 p2]

Basic script description

Options:

    -a         description for a option
    --foo      description for foo option
    
Examples:

some examples
```

Annotations plays part also in validating process. So if
option which does not exist in annotations is provided, `microcli` will
throw an error:

```
$ script.js --bar
Illegal option: --bar
Available options: -a --foo
Type "script.js --help" for more information
```

Also each annotation is optional and custom annotations like `examples`
(basically other than description, params and options) will be treated
in `--help` content as additional header with string value.

### Commands
```
$ script.js status --foo abc 
OPTIONS {foo: true}
P abc

$ script.js branch --help
Usage: branch [options] [p]

Basic script description

$ script.js --foo abc
OPTIONS {foo: true}
P abc

```

```js
#!/usr/bin/env node
const microcli = require('microcli')

const main = microcli(process.argv, {
  description: 'base command',
  params: ['p'],
  options: {
    foo: 'foo option'
  }
})

const status = microcli(process.argv.slice(1), {
  description: 'Fake git status',
  params: ['p'],
  options: {
    foo: 'foo option'
  }
})

const branch = microcli(process.argv.slice(1), {
  description: 'Fake git branch',
  params: ['p'],
  options: {
    foo: 'foo option'
  }
})

switch (process.argv[2]) {
  case 'status':
    status((options, p) => {
      console.log('OPTIONS', options)
      console.log('P', p)
    })
    break

  case 'branch':
    branch((options, p) => {
      console.log('OPTIONS', options)
      console.log('P', p)
    })
    break

  default:
    main((options, p) => {
      console.log('OPTIONS', options)
      console.log('P', p)
    })
}
```

### Custom --help

You can provide `help` function to `cli` call, which can generate
custom help message, having annotations object:

```js
#!/usr/bin/env node
const microcli = require('microcli')
const cli = microcli(process.argv, {
  /* some annotations */
}, (scriptName, annotations, logger) => {
  logger.log('Custom --help message') 
});

cli((options, p1, p2) => {
    console.log('OPTIONS', options)
    console.log('P1', p1)
    console.log('P2', p2)
})
```
