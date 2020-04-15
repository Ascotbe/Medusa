# Unidecode for NodeJS
-----------------


__Unidecode__ is __JavaScript port__ of the __perl module [Text::Unicode](http://search.cpan.org/~sburke/Text-Unidecode-0.04/lib/Text/Unidecode.pm)__. It takes UTF-8 data and tries to represent it in US-ASCII characters
(i.e., the universally displayable characters between 0x00 and 0x7F). The representation is almost always an attempt at transliteration
-- i.e., conveying, in Roman letters, the pronunciation expressed by the text in some other writing system.

See [Text::Unicode](http://search.cpan.org/~sburke/Text-Unidecode-0.04/lib/Text/Unidecode.pm) for the original README file, including methodology and limitations.

Note that all the files named 'x??.js' in data are derived directly from the equivalent perl file, and both sets of files are distributed under the perl license not the BSD license.

## Installation

    $ npm install unidecode

## Usage

    $ node
    > var unidecode = require('unidecode');
    > unidecode("aéà)àçé");
    'aea)ace'
    > unidecode("に間違いがないか、再度確認してください。再読み込みしてください。");
    'niJian Wei iganaika, Zai Du Que Ren sitekudasai. Zai Du miIp misitekudasai. '

## [Changelog](/CHANGELOG.md)

## Donate
[Donate Bitcoins](https://coinbase.com/checkouts/fc3041b9d8116e0b98e7d243c4727a30)

__I accept pull-request !__
