var expect = require('chai').expect;
var urlSlug = require('../index');

describe('module', function () {

    it('should include constructor as a property', function () {
        expect(urlSlug.UrlSlug.constructor).to.be.equal(urlSlug.constructor);
    });

    it('should contain convert and revert methods', function () {
        expect(urlSlug.convert).to.be.a('function');
        expect(urlSlug.revert).to.be.a('function');
    });

    it('should call convert if called as a function', function () {
        expect(urlSlug).to.be.equal(urlSlug.convert);
    });

    describe('instance', function () {

        var instance = new urlSlug.UrlSlug;

        it('should contain lowercase, uppercase and titlecase builtin transformers', function () {
            expect(instance.transformers).to.contain.all.keys('lowercase', 'uppercase', 'titlecase');
        });

        it('should set "-" as default separator', function () {
            expect(instance.separator).to.be.equal('-');
        });

        it('should set "lowercase" as default transformer', function () {
            expect(instance.transform).to.be.equal(instance.transformers.lowercase);
        });

        describe('transformers', function () {

            it('should contain a working lowercase', function () {
                expect(instance.transformers.lowercase('TEST STRING')).to.be.equal('test string');
            });

            it('should contain a working uppercase', function () {
                expect(instance.transformers.uppercase('test string')).to.be.equal('TEST STRING');
            });

            it('should contain a working titlecase', function () {
                expect(instance.transformers.titlecase('tesT strinG')).to.be.equal('Test String');
            });

        });

        describe('prepare', function () {

            it('should not accept nothing but a string as a separator', function () {
                expect(instance.prepare.bind(instance, 123)).to.throw(/^Invalid separator, must be a string/);
            });

            it('should accept all characters defined as unreserved in RFC 3986 as a separator', function () {
                expect(instance.prepare.bind(instance, '-._~')).to.not.throw(/^Invalid separator, has invalid characters/);
            });

            it('should not accept a separator character not defined as unreserved in RFC 3986', function () {
                expect(instance.prepare.bind(instance, '+')).to.throw(/^Invalid separator, has invalid characters/);
            });

            it('should accept false as transform', function () {
                expect(instance.prepare.bind(instance, '', false)).not.to.throw(/^Invalid transform, must be a function/);
            });

            it('should accept all builtin presets as transform', function () {
                expect(instance.prepare.bind(instance, '', 'lowercase')).to.not.throw(/^Invalid transform, must be a function/);
                expect(instance.prepare.bind(instance, '', 'uppercase')).to.not.throw(/^Invalid transform, must be a function/);
                expect(instance.prepare.bind(instance, '', 'titlecase')).to.not.throw(/^Invalid transform, must be a function/);
            });

            it('should accept a function as transform', function () {
                expect(instance.prepare.bind(instance, '', function () {})).to.not.throw(/^Invalid transform, must be a function/);
            });

            it('should only accept false, a function or a builtin preset as transform', function () {
                expect(instance.prepare.bind(instance, '', true)).to.throw(/^Invalid transform, must be a builtin transform or a function/);
                expect(instance.prepare.bind(instance, '', 'nonexistent')).to.throw(/^Invalid transform, must be a builtin transform or a function/);
                expect(instance.prepare.bind(instance, '', {})).to.throw(/^Invalid transform, must be a builtin transform or a function/);
            });

            it('should return an object with all available options', function () {
                expect(instance.prepare()).to.contain.all.keys('separator', 'transform');
            });

        });

        describe('convert', function () {

            it('should not accept nothing but a string as input', function () {
                expect(instance.convert.bind(instance, 123)).to.throw(/^Invalid value, must be a string/);
            });

            it('should return a default slug if no options are set', function () {
                expect(instance.convert('Url Slug')).to.be.equal('url-slug');
            });

            it('should remove accents', function () {
                expect(instance.convert('á é í ó ú')).to.be.equal('a-e-i-o-u');
            });

            it('should convert to upper case and use default separator', function () {
                expect(instance.convert('a bronx tale', null, 'uppercase')).to.be.equal('A-BRONX-TALE');
            });

            it('should use underscore separators and title case', function () {
                expect(instance.convert('tom jobim', '_', 'titlecase')).to.be.equal('Tom_Jobim');
            });

            it('should allow multiple characters in separator and not change the case', function () {
                expect(instance.convert('Charly García', '-._~-._~', false)).to.be.equal('Charly-._~-._~Garcia');
            });

            it('should return a camel case string', function () {
                expect(instance.convert('java script', '', 'titlecase')).to.be.equal('JavaScript');
            });

            it('should break a camel case string', function () {
                expect(instance.convert('javaScript')).to.be.equal('java-script');
            });

            it('should return only consonants', function () {
                var transform = function (string) {
                    return string.replace(/[aeiou]/gi, '');
                }
                expect(instance.convert('React', '', transform)).to.be.equal('Rct');
            });

        });

        describe('revert', function () {

            it('should not accept nothing but a string as input', function () {
                expect(instance.revert.bind(instance, 123)).to.throw(/^Invalid value, must be a string/);
            });

            it('should use automatic reversion and maintain input case', function () {
                expect(instance.revert('UrlSlug-url_slug')).to.be.equal('Url Slug url slug');
            });

            it('should break only on camel case and convert input to upper case', function () {
                expect(instance.revert('ClaudioBaglioni_is-Italian', '', 'uppercase')).to.be.equal('CLAUDIO BAGLIONI_IS-ITALIAN');
            });

            it('should return the title of a Pink Floyd track', function () {
                expect(instance.revert('comfortably-._~numb', '-._~', 'titlecase')).to.be.equal('Comfortably Numb');
            });

        });

    });

});
