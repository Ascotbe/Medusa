#!/usr/bin/env node
const path = require('path')
const fs = require('fs')

const SCRIPT_API_PATH = './node_modules/runjs/lib/script.js'

try {
  fs.accessSync(path.resolve(SCRIPT_API_PATH))
} catch (error) {
  console.error(
    'RunJS not found. Do "npm install runjs --save-dev" or "yarn add --dev runjs" first.'
  )
  process.exit(1)
}

const script = require(path.resolve(SCRIPT_API_PATH))

if (!script.main) {
  console.error(
    'Version of runjs inside your project seems to be not compatible with global run script.'
  )
  console.error('Upgrade your local runjs to >= 4.0')
  process.exit(1)
}

script.main()
