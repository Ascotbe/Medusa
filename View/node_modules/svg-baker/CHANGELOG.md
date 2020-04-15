# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

<a name="1.5.0"></a>
# [1.5.0](https://github.com/JetBrains/svg-mixer/tree/v1/compare/svg-baker@1.4.1...svg-baker@1.5.0) (2019-07-23)


### Features

* add clipPath & mask to "move-from-symbol-to-root" transform defaults ([#61](https://github.com/JetBrains/svg-mixer/tree/v1/issues/61)) ([cbad9e8](https://github.com/JetBrains/svg-mixer/tree/v1/commit/cbad9e8))




<a name="1.4.1"></a>
## [1.4.1](https://github.com/JetBrains/svg-mixer/tree/v1/compare/svg-baker@1.4.0...svg-baker@1.4.1) (2019-04-27)




**Note:** Version bump only for package svg-baker

<a name="1.4.0"></a>
# [1.4.0](https://github.com/JetBrains/svg-mixer/tree/v1/compare/svg-baker@1.2.12...svg-baker@1.4.0) (2018-10-29)


### Bug Fixes

* **compiler:** move symbols sort from sprite-factory to compiler ([4690c75](https://github.com/JetBrains/svg-mixer/tree/v1/commit/4690c75))
* **sprite-factory:** sort symbols by id to get more determined sprite content ([9132e23](https://github.com/JetBrains/svg-mixer/tree/v1/commit/9132e23))
* make symbol.tree getter immutable ([343dc86](https://github.com/JetBrains/svg-mixer/tree/v1/commit/343dc86))
* preserve `fill` and `stroke` attrs when transform svg to symbol ([51cb3d5](https://github.com/JetBrains/svg-mixer/tree/v1/commit/51cb3d5))
* security vulnerability in merge-options dependency ([0482a12](https://github.com/JetBrains/svg-mixer/tree/v1/commit/0482a12))
* sprite move gradients outside symbol ([c6fcab4](https://github.com/JetBrains/svg-mixer/tree/v1/commit/c6fcab4))
* update package info ([7cc1b95](https://github.com/JetBrains/svg-mixer/tree/v1/commit/7cc1b95))
* upgrade merge-options due to severity vulnerabilities ([0538c60](https://github.com/JetBrains/svg-mixer/tree/v1/commit/0538c60))


### Features

* **sprite-factory:** allow to configure usages and styles rendering ([bc63366](https://github.com/JetBrains/svg-mixer/tree/v1/commit/bc63366))
* **svg-to-symbol-transformation:** preserve fill-* and stroke-* attributes ([edda97d](https://github.com/JetBrains/svg-mixer/tree/v1/commit/edda97d))
* add ARIA attrs to whitelist ([e6dd50d](https://github.com/JetBrains/svg-mixer/tree/v1/commit/e6dd50d))




<a name="1.2.8"></a>
## 1.2.8 (2017-06-15)


### Bug Fixes

* Remove DOCTYPE and xml declaration from source ([a380107](https://github.com/kisenka/svg-baker/commit/a380107))



<a name="1.2.7"></a>
## 1.2.7 (2017-05-13)


### Bug Fixes

* **sprite-factory:** dissapearing use tags when sprite is a part of page DOM ([a8c60ee](https://github.com/kisenka/svg-baker/commit/a8c60ee))
