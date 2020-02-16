var rootUrl = 'https://www.ascotbe.com/Medusa';

var versions = [
	{ title: 'v2.9', path: '/Documentation/' },
]

var latestVersionIndex = 0;
var currentVersionIndex = -1;

versions[latestVersionIndex].title += '';

versions.forEach(function (v, idx) {
    if (v.path) {
        var pathname = window.location.pathname;
        if (pathname.lastIndexOf(v.path) == pathname.length - v.path.length /* pathname.endsWith(v.path) */) {
            currentVersionIndex = idx;
            rootUrl = window.location.origin + pathname.substr(0, pathname.length - v.path.length);
        }
    }
});

versions.forEach(function (v) {
    if (v.path) {
        v.path = rootUrl + v.path;
    }
});

config.nav.push({
    title: '文档版本: ' + versions[currentVersionIndex].title, type: 'dropdown', items: versions
});

if (currentVersionIndex > latestVersionIndex) {
    config.announcement = {
        type: 'danger',
        html: '你当前正在访问的是旧版本插件的文档，内容可能与最新版本不相符，点击&nbsp;<span style="cursor: pointer;" '
            + 'onclick="window.location.assign(\'' + versions[latestVersionIndex].path + '\' + window.location.hash)"'
            + '>这里</span>&nbsp;访问最新文档。'
    };
} else if (currentVersionIndex < latestVersionIndex) {
    config.announcement = {
        type: 'primary',
        html: '你当前正在访问的是测试版插件的文档，测试版本提供了更丰富的功能但可能不稳定，点击&nbsp;<span style="cursor: pointer;" '
            + 'onclick="window.location.assign(\'' + versions[latestVersionIndex].path + '\' + window.location.hash)"'
            + '>这里</span>&nbsp;访问最新稳定版的文档。'
    };
}

docute.init(config);

// Google Analytics
window.ga = window.ga || function () { (ga.q = ga.q || []).push(arguments) }; ga.l = +new Date;
ga('create', 'UA-115509121-1', 'auto');
ga('send', 'pageview');
docute.router.afterEach(function (to) {
    ga('set', 'page', to.fullPath);
    ga('send', 'pageview');
});
