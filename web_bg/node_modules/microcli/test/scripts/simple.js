#!/usr/bin/env node
const microcli = require('../../lib/index')
const cli = microcli(process.argv, {
  description: 'Basic script description',
  params: ['p1', 'p2'],
  options: {
    a: 'description for a option',
    foo: 'description for foo option'
  },
  examples: 'some examples'
})

cli((options, p1, p2) => {
  console.log('OPTIONS', options)
  console.log('P1', p1)
  console.log('P2', p2)
})
