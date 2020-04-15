# url-slug

RFC 3986 compliant slug generator with support for multiple languages. It creates safe slugs for use in urls—and can revert them.

## Install

```bash
$ npm install url-slug
```

## Use

```js
var urlSlug = require('url-slug');

// Convert to common slug format, using defaults

urlSlug('Sir James Paul McCartney MBE is an English singer-songwriter');
// sir-james-paul-mc-cartney-mbe-is-an-english-singer-songwriter

// Uppercase with default separator

urlSlug('Comfortably Numb', null, 'uppercase');
// COMFORTABLY-NUMB

// Use an underscore separator and don't touch the string case

urlSlug('á é í ó ú Á É Í Ó Ú ç Ç æ Æ œ Œ ® © € ¥ ª º ¹ ² ½ ¼', '_', false);
// a_e_i_o_u_A_E_I_O_U_c_C_ae_AE_oe_OE_r_c_EU_Y_a_o_1_2_1_2_1_4

// Titlecased without a separator

urlSlug('Red, red wine, stay close to me…', '', 'titlecase');
// RedRedWineStayCloseToMe

// Use a custom separator and uppercase the string (the separator '.' was ignored, because spaces were replaced)

urlSlug('O\'Neill is an American surfboard, surfwear and equipment brand', '.', function (sentence) {
    return sentence.replace(/ /g, '+').toUpperCase();
});
// O+NEILL+IS+AN+AMERICAN+SURFBOARD+SURFWEAR+AND+EQUIPMENT+BRAND

// Automatic reversion of slugs

urlSlug.revert('Replace-every_separator.allowed~andSplitCamelCase');
// Replace every separator allowed and Split Camel Case

// Precise reversion, setting the separator and converting the sentence to title case

urlSlug.revert('this-title-needs-a-title_case', '-', 'titlecase');
// This Title Needs A Title_case

// Create a new instance with its own defaults

var custom = new urlSlug.UrlSlug('~', 'uppercase');

custom.convert('Listen to Fito Páez in Madrid');
// LISTEN~TO~FITO~PAEZ~IN~MADRID
```

## Know

### urlSlug(string[, separator, transform]), UrlSlug.convert(string[, separator, transform])

Converts a sentence into a slug.

- __separator__, defaults to `'-'` — can be any of `'-._~'` characters or an empty string; a `null` or `undefined` value will set the default separator
- __transform__, defaults to `'lowercase'` — can be `'lowercase'`, `'uppercase'`, `'titlecase'` or a custom function; if set to `false`, no transform will take place; a `null` or `undefined` value will set the default transform

### UrlSlug.revert(string[, separator, transform])

Reverts a slug back to a sentence.

- __separator__, defaults to `null` — can be any of `'-._~'` characters or an empty string; a `null` or `undefined` will set to match all possible separator characters and camel case occurrences; an empty string will set to match only camel case occurrences
- __transform__, defaults to `null` — can be `'lowercase'`, `'uppercase'`, `'titlecase'` or a custom function; if set to `false`, `null` or `undefined` no transform will take place

### urlSlug.UrlSlug([separator, transform])

url-slug constructor, use this if you need another instance. If __separator__ or __transform__ are set, they will be used as the default values of the instance.

- __separator__, defaults to `'-'`
- __transform__, defaults to `'lowercase'`

### Builtin transformers

- __UrlSlug.transformers.lowercase__ — lower case
- __UrlSlug.transformers.uppercase__ — UPPER CASE
- __UrlSlug.transformers.titlecase__ — Title Case

## TODO

- Option to keep specific characters
