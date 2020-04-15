<img src="https://rawgit.com/f/omelette/master/resources/logo.svg?v1" height="80">

> Omelette is a simple, template based autocompletion tool for Node projects with super easy API.

[![npm version](https://badge.fury.io/js/omelette.svg)](https://badge.fury.io/js/omelette)
[![Build Status](https://travis-ci.org/f/omelette.svg?branch=master)](https://travis-ci.org/f/omelette)

```bash
yarn add omelette
# or
npm install omelette
```

You just have to decide your program name and CLI fragments.

```javascript
omelette`github ${['pull', 'push']} ${['origin', 'upstream']} ${['master', 'develop']}`.init()
```

And you are almost done! The output will be like this:

<img src="https://raw.github.com/f/omelette/master/resources/omelette-new.gif?v1" width="640">

## Quick Start

Implementing omelette is very easy.

```javascript
import * as omelette from 'omelette';

const firstArgument = ({ reply }) => {
  reply([ 'beautiful', 'cruel', 'far' ])
}

const planet = ({ reply }) => {
  reply([ 'world', 'mars', 'pluto' ])
}

omelette`hello|hi ${firstArgument} ${planet}`.init()
```

<img src="https://raw.github.com/f/omelette/master/resources/omelette-new-hello.gif?v1" width="640">

### Simple Event Based API ☕️

It's based on a simple CLI template.

Let's think we have a executable file with the name **githubber**, *in a global path*.

And in our program, code will be:

```javascript
import * as omelette from 'omelette';

// Write your CLI template.
const completion = omelette(`githubber|gh <action> <user> <repo>`);

// Bind events for every template part.
completion.on('action', ({ reply }) => {
  reply([ 'clone', 'update', 'push' ])
})

completion.on('user', ({ reply }) => {
  reply(fs.readdirSync('/Users/'))
})

completion.on('repo', ({ before, reply }) => {
  reply([
    `http://github.com/${before}/helloworld`,
    `http://github.com/${before}/blabla`
  ])
})

// Initialize the omelette.
completion.init()

// If you want to have a setup feature, you can use `omeletteInstance.setupShellInitFile()` function.
if (~process.argv.indexOf('--setup')) {
  completion.setupShellInitFile()
}

// Rest is yours
console.log("Your program's default workflow.")
console.log(process.argv)
```

`complete.reply` is the completion replier. You must pass the options into that method.

### ES6 Template Literal API 🚀

You can use **Template Literals** to define your completion with a simpler (super easy) API.

```javascript
import * as omelette from 'omelette';

// Just pass a template literal to use super easy API.
omelette`hello ${[ 'cruel', 'nice' ]} ${[ 'world', 'mars' ]}`.init()
```

Let's make the example above with ES6 TL:

```javascript
import * as omelette from 'omelette'

// Write your CLI template.
omelette`
  githubber|gh
  
  ${[ 'clone', 'update', 'push' ]}
  ${() => fs.readdirSync('/Users/')} 
  ${({ before }) => [
    `http://github.com/${before}/helloworld`,
    `http://github.com/${before}/blabla`,
  ]}
`.init()
```

Also you can still use lambda functions to make more complex template literals:

#### Advanced Template Literals

```javascript
import * as omelette from 'omelette';

omelette`
  githubber|gh
      ${['pull', 'push', 'star'] /* Direct command list */}
      ${require('some/other/commands') /* Import from another file */}
      ${getFromRemote('http://api.example.com/commands') /* Remote call at the beginning */}
      ${({ reply }) => fetch('http://api.example.com/lazy-commands').then(reply) /* Fetch when argument <tab>bed */}
      ${() => fs.readdirSync("/Users/") /* Access filesystem via Node */}
      ${({ before }) => [ /* Use parameters like `before`, `line`, `fragment` or `reply` */
        `${before}/helloworld`,
        `${before}/blabla`
      ]}
  `.init()

// No extra configuration required.

console.log("Your program's default workflow.")
console.log(process.argv)
```

### Tree API 🌲

You can use `simple objects` as autocompletion definitions:

```javascript
omelette('hello').tree({
  cruel: ['world', 'moon'],
  beautiful: ['mars', 'pluto']
}).init();
```

## Install

### Automated Install

Installing, and making your users install the autocompletion feature is very simple.

You can use simply use `setupShellInitFile` function.

```javascript
// If you want to write file,
complete.setupShellInitFile('~/.my_bash_profile')
```

If you use Bash, it will create a file at `~/.<program-name>/completion.sh` and
append a loader code to `~/.bash_profile` file.

If you use Zsh, it appends a loader code to `~/.zshrc` file.

If you use Fish, it appends a loader code to `~/.config/fish/config.fish` file.

*TL;DR: It does the Manual Install part, basically.*

### Manual Install

*(You should add these instructions to your project's README)*

In **zsh**, you can write these:

```bash
echo '. <(./githubber --completion)' >> .zshrc
```

In **bash**, you should write:

```bash
./githubber --completion >> ~/githubber.completion.sh
echo 'source ~/githubber.completion.sh' >> .bash_profile
```

In **fish**, you can write:

```bash
echo 'githubber --completion-fish | source' >> ~/.config/fish/config.fish
```

That's all!

Now you have an autocompletion system for your CLI tool.

## Additions

There are some useful additions for omelette.


### Parameters

Callbacks have two parameters:

  - The fragment name (e.g.`command` of `<command>` template) *(only in global event)*
  - The meta data
    - `fragment`: The number of fragment.
    - `before`: The previous word.
    - `line`: The whole command line buffer allow you to parse and reply as you wish.
    - `reply`: This is the reply function to use *this-less* API.

### Global Event

You also can be able to listen all fragments by "complete" event.

```javascript
complete.on('complete', (fragment, { reply }) => reply(["hello", "world"]));
```

### Numbered Arguments

You also can listen events by its order.

```javascript
complete.on('$1', ({ reply }) => reply(["hello", "world"]))
```

### Autocompletion Tree

You can create **completion tree** to more complex autocompletions.

```js
omelette('hello').tree({
  how: {
    much: {
      is: {
        this: ['car'],
        that: ['house'],
      }
    }
    are: ['you'],
    many: ['cars', 'houses'],
  },
  where: {
    are: {
      you: ['from'],
      the: ['houses', 'cars'],
    },
    is: {
      // You can also add some logic with defining functions:
      your() {
        return ['house', 'car'];
      },
    }
  },
}).init()
```

Now you will be able to use your completion as tree.

<img src="https://raw.github.com/f/omelette/master/resources/omelette-tree-new.gif?v1" width="640">

> Thanks [@jblandry](https://github.com/jblandry) for the idea.

#### Advanced Tree Implementations

You can seperate your autocompletion by importing objects from another file:

```js
omelette('hello').tree(require('./autocompletion-tree.js')).init();
```

### Short Names

You can set short name of an executable:

In this example, `githubber` is long and `gh` is shorter examples.

```javascript
omelette('githubber|gh <module> <command> <suboption>');
```

## Test

Now, you can try it in your shell.

```bash
git clone https://github.com/f/omelette
cd omelette/example
alias githubber="./githubber" # The app should be global, completion will search it on global level.
./githubber --setup --debug # --setup is not provided by omelette, you should proxy it.
# (reload bash, or source ~/.bash_profile or ~/.config/fish/config.fish)
omelette-debug-githubber # See Debugging section
githubber<tab>
ghb<tab> # short alias
gh<tab> # short alias
```

### Debugging

`--debug` option generates a function called `omlette-debug-<programname>`.
(`omlette-debug-githubber` in this example).

When you run `omlette-debug-<programname>`, it will create aliases for your
application. (`githubber` and `gh` in this example).

Long name,

```bash
$ githubber<tab>
clone update push
```

Or short name:

```bash
$ gh<tab>
clone update push
```

Then you can start easily.

```bash
$ ./githubber<tab>
clone update push
```

```bash
$ ./githubber cl<tab>
$ ./githubber clone<tab>
Guest fka
```

```bash
$ ./githubber clone fka<tab>
$ ./githubber clone fka http://github.com/fka/<tab>
http://github.com/fka/helloworld
http://github.com/fka/blabla
```

## Who uses?

**Windows Azure** uses Omelette to support autocompletion in [azure-cli](https://github.com/WindowsAzure/azure-sdk-tools-xplat).

## Contribute

I need your contributions to make that work better!

## License

This project licensed under MIT.
