'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = _default;

var _co = _interopRequireDefault(require("co"));

var _promptBypass = _interopRequireDefault(require("./prompt-bypass"));

var buildInActions = _interopRequireWildcard(require("./actions"));

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = Object.defineProperty && Object.getOwnPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : {}; if (desc.get || desc.set) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } } newObj.default = obj; return newObj; } }

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _default(plopfileApi, flags) {
  let abort; // triggers inquirer with the correct prompts for this generator
  // returns a promise that resolves with the user's answers

  const runGeneratorPrompts = _co.default.wrap(function* (genObject, bypassArr = []) {
    const {
      prompts
    } = genObject;

    if (prompts == null) {
      throw Error(`${genObject.name} has no prompts`);
    }

    if (typeof prompts === 'function') {
      return yield prompts(plopfileApi.inquirer);
    } // handle bypass data when provided


    const [promptsAfterBypass, bypassAnswers] = (0, _promptBypass.default)(prompts, bypassArr, plopfileApi);
    return yield plopfileApi.inquirer.prompt(promptsAfterBypass).then(answers => Object.assign(answers, bypassAnswers));
  }); // Run the actions for this generator


  const runGeneratorActions = _co.default.wrap(function* (genObject, data = {}, hooks = {}) {
    const noop = () => {};

    const {
      onSuccess = noop,
      // runs after each successful action
      onFailure = noop,
      // runs after each failed action
      onComment = noop // runs for each comment line in the actions array

    } = hooks;
    const changes = []; // array of changed made by the actions

    const failures = []; // array of actions that failed

    let {
      actions
    } = genObject; // the list of actions to execute

    const customActionTypes = getCustomActionTypes();
    const actionTypes = Object.assign({}, customActionTypes, buildInActions);
    abort = false; // if action is a function, run it to get our array of actions

    if (typeof actions === 'function') {
      actions = actions(data);
    } // if actions are not defined... we cannot proceed.


    if (actions == null) {
      throw Error(`${genObject.name} has no actions`);
    } // if actions are not an array, invalid!


    if (!(actions instanceof Array)) {
      throw Error(`${genObject.name} has invalid actions`);
    }

    for (let [actionIdx, action] of actions.entries()) {
      // including strings in the actions array is used for commenting
      if (typeof action === 'string' && abort) {
        continue;
      }

      if (typeof action === 'string') {
        onComment(action);
        continue;
      }

      const actionIsFunction = typeof action === 'function';
      const actionCfg = actionIsFunction ? {
        type: 'function'
      } : action;
      const actionLogic = actionIsFunction ? action : actionTypes[actionCfg.type]; // bail out if a previous action aborted

      if (abort) {
        const failure = {
          type: actionCfg.type || '',
          path: actionCfg.path || '',
          error: 'Aborted due to previous action failure'
        };
        onFailure(failure);
        failures.push(failure);
        continue;
      }

      actionCfg.force = flags.force === true || actionCfg.force === true;

      if (typeof actionLogic !== 'function') {
        if (actionCfg.abortOnFail !== false) {
          abort = true;
        }

        const failure = {
          type: actionCfg.type || '',
          path: actionCfg.path || '',
          error: `Invalid action (#${actionIdx + 1})`
        };
        onFailure(failure);
        failures.push(failure);
        continue;
      }

      try {
        const actionResult = yield executeActionLogic(actionLogic, actionCfg, data);
        onSuccess(actionResult);
        changes.push(actionResult);
      } catch (failure) {
        if (actionCfg.abortOnFail !== false) {
          abort = true;
        }

        onFailure(failure);
        failures.push(failure);
      }
    }

    return {
      changes,
      failures
    };
  }); // handle action logic


  const executeActionLogic = _co.default.wrap(function* (action, cfg, data) {
    const type = cfg.type || '';
    let cfgData = cfg.data || {}; // data can also be a function that returns a data object

    if (typeof cfgData === 'function') {
      cfgData = yield cfgData();
    } // track keys that can be applied to the main data scope


    const cfgDataKeys = Object.keys(cfgData).filter(k => typeof data[k] === 'undefined'); // copy config data into main data scope so it's available for templates

    cfgDataKeys.forEach(k => {
      data[k] = cfgData[k];
    });
    return yield Promise.resolve(action(data, cfg, plopfileApi)).then( // show the resolved value in the console
    result => ({
      type,
      path: typeof result === 'string' ? result : JSON.stringify(result)
    }), // a rejected promise is treated as a failure
    err => {
      throw {
        type,
        path: '',
        error: err.message || err.toString()
      };
    }) // cleanup main data scope so config data doesn't leak
    .finally(() => cfgDataKeys.forEach(k => {
      delete data[k];
    }));
  }); // request the list of custom actions from the plopfile


  function getCustomActionTypes() {
    return plopfileApi.getActionTypeList().reduce(function (types, name) {
      types[name] = plopfileApi.getActionType(name);
      return types;
    }, {});
  }

  return {
    runGeneratorActions,
    runGeneratorPrompts
  };
}