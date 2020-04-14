#!/usr/bin/env node
const microcli = require('../../lib/index')

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
