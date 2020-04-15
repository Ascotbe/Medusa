/* global angular */
import dispatchEvent from './dispatch-custom-event';

/**
 * @param {string} eventName
 */
export default function (eventName) {
  angular.module('ng').run(['$rootScope', ($rootScope) => {
    $rootScope.$on('$locationChangeSuccess', (e, newUrl, oldUrl) => {
      dispatchEvent(eventName, { oldUrl, newUrl });
    });
  }]);
}
