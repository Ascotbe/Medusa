# jest-environment-jsdom-fifteen

[Jest](https://jestjs.io) by default uses [JSDOM](https://github.com/jsdom/jsdom) 11 to support Node 6. This package uses JSDOM 15, which supports Node >= 8, and does not support Node 6 ([and will therefore not be used in Jest any time soon](https://github.com/kentcdodds/dom-testing-library/issues/115#issuecomment-428314737)).

If you need a newer JSDOM than the one that ships with Jest, install this package using `npm install --save-dev jest-environment-jsdom-fifteen` or `yarn add jest-environment-jsdom-fifteen --dev`, and edit your Jest config like so:

```json
{
  "testEnvironment": "jest-environment-jsdom-fifteen"
}
```

If you would like to use JSDOM 14, see https://github.com/ianschmitz/jest-environment-jsdom-fourteen.
