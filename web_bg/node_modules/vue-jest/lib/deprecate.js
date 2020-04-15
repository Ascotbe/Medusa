const chalk = require('chalk')
const logger = require('./logger')

const replace = (oldThing, newThing) => {
  logger.warn(chalk.bold.yellow('Deprecation Warning:'), '\n')
  logger.warn(chalk.yellow(`Option ${chalk.bold(`"${oldThing}"`)} has been removed, and replaced by ${chalk.bold(`"${newThing}"`)}`), '\n')
  logger.warn(chalk.yellow('This option will be removed in the next major version of `vue-jest`. Please update your configuration.'), '\n')
  logger.warn(chalk.bold.yellow('Configuration Documentation:'))
  logger.warn(chalk.yellow('https://github.com/vuejs/vue-jest'))
}

module.exports = { replace }
