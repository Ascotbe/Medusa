<template>
<html lang="en">
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>testing</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
 </head>
 <body>
  <div id="app">
   <div data-reactroot="">
    <div class="ant-layout ant-layout-has-sider" style="min-height: 100vh;">
     <div class="ant-layout">
      <div class="ant-layout-header" style="background: rgb(255, 255, 255); padding: 0px 16px;">
       <div class="ant-row">
        <div class="ant-col-18">
         <h2 style="text-align: center;"></h2>
        </div>
       </div>
      </div>
      <div class="ant-layout-content" style="margin: 0px 16px;">
        <div style="padding: 4px 0px;"></div>
       <div style="padding: 24px; background: rgb(255, 255, 255); min-height: 360px;">
        <div class="profile">
         <div class="ant-row">
          <div class="ant-col-8">
           <div class="profile-left">
            <div class="profile-info">
             <img class="profile-avatar" alt="avatar" src="./avatar.png" />
             <p class="profile-name">394b3902d6b6</p>
             <p class="profile-email">872798462@qq.com</p>
             <p class="profile-operation"><a href="#"><button type="button" class="ant-btn profile-operate ant-btn-primary"><span>Modify Profile</span></button></a><a href="#"><button type="button" class="ant-btn profile-operate"><span>Logout</span></button></a></p>
             <div class="profile-deadline">
              <p>当前时间：{{currentTime}}</p>
             </div>
            </div>
           </div>
          </div>
          <div class="ant-col-16">
           <div class="profile-main">
            <div class="profile-main-info">
             <h1><i class="anticon anticon-contacts" style="font-size: 24px;"></i>
               Profile
               </h1>
             <div class="profile-main-info-box">
              <p><span class="profile-info-option"><i class="anticon anticon-user"></i>
                Username:
                 </span><span class="profile-info-value">394b3902d6b6</span></p>
              <p><span class="profile-info-option"><i class="anticon anticon-heart-o"></i>
                 Nickname:
                 </span><span class="profile-info-value"></span></p>
              <p><span class="profile-info-option"><i class="anticon anticon-mail"></i>
                 Email:
                 </span><span class="profile-info-value">872798462@qq.com</span></p>
              <p><span class="profile-info-option"><i class="anticon anticon-mobile"></i>
                 Mobile:
                 </span><span class="profile-info-value">1234678912</span></p>
              <p><span class="profile-info-option"><i class="anticon anticon-lock"></i>
                 Verification:
                 </span><span class="profile-info-value">Verified</span></p>
              <p><span class="profile-info-option"><i class="anticon anticon-rocket"></i>
                 Identifier:
                 </span><span class="profile-info-value"><span class="profile-badge ant-badge ant-badge-not-a-wrapper"><sup data-show="true" class="ant-scroll-number ant-badge-count" title="test">test</sup></span></span></p>
              <p><span class="profile-info-option"><i class="anticon anticon-key"></i>
                 API Token:
                 </span><span class="profile-info-value"><span class="profile-badge ant-badge ant-badge-not-a-wrapper"><sup data-show="true" class="ant-scroll-number ant-badge-count" title="test1">test</sup></span></span></p>
              <p><span class="profile-info-option"><i class="anticon anticon-hourglass"></i>
                 DNS Rebinding:
                 </span><span class="profile-info-value"></span></p>
              <div data-show="true" class="ant-tag" style="background: rgb(255, 255, 255); border-style: dashed;">
              <!-- <span class="ant-tag-text"><i class="anticon anticon-plus"></i>
                  New DNS
                 </span> -->

              </div>
              <p></p>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div style="position: absolute; top: 0px; left: 0px; width: 100%;">
   <div data-reactroot="">
    <div class="ant-dropdown  ant-dropdown-placement-bottomLeft  ant-dropdown-hidden" style="left: 1527.67px; top: 49.5px; width: 136px;">
     <ul class="ant-dropdown-menu ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-root" role="menu" aria-activedescendant="" tabindex="0">
      <li class="ant-dropdown-menu-item" role="menuitem" aria-selected="false"><a href="http://ceye.io/profile"><i class="anticon anticon-contacts"></i>
         Profile
         </a></li>
      <li class="ant-dropdown-menu-item" role="menuitem" aria-selected="false"><a href="http://api.ceye.io/v1/logout"><i class="anticon anticon-logout"></i>
         Logout
         </a></li>
     </ul>
    </div>
   </div>
  </div>
 </body>
</html>
</template>
<script>
	export default{
		data() {
		    return {
		      timer: "",//定义一个定时器的变量
		      currentTime: new Date(), // 获取当前时间
		    };
		  },
		created() {
		    var _this = this; //声明一个变量指向Vue实例this，保证作用域一致
		    this.timer = setInterval(function() {
		      _this.currentTime = //修改数据date
		        new Date().getFullYear() +
		        "-" +
		        (new Date().getMonth() + 1) +
		        "-" +
		        new Date().getDate() +
		        " " +
		        new Date().getHours() +
		        ":" +
		        new Date().getMinutes() +
		        ": " +
		        new Date().getSeconds();
		    }, 1000);
		  },
		beforeDestroy() {
		    if (this.timer) {
		      clearInterval(this.timer); // 在Vue实例销毁前，清除我们的定时器
		    }
		  }
		}
</script>

<style lang="scss">
html, body, #root {
  height: 100%;
}
#app .logo {
  height: 48px;
  border-radius: 6px;
  margin: 8px 24px;
  text-align: center;
}

.ant-menu > .ant-menu-item {
  font-size: 14px;
}

.ceye-menu {
  font-size: 16px;
}
/*! normalize.css v7.0.0 | MIT License | github.com/necolas/normalize.css */html {
	line-height: 1.15;
	-ms-text-size-adjust: 100%;
	-webkit-text-size-adjust: 100%
}

body {
	margin: 0
}

article,aside,footer,header,nav,section {
	display: block
}

h1 {
	font-size: 2em;
	margin: .67em 0
}

figcaption,figure,main {
	display: block
}

figure {
	margin: 1em 40px
}

hr {
	box-sizing: content-box;
	height: 0;
	overflow: visible
}

pre {
	font-family: monospace,monospace;
	font-size: 1em
}

a {
	background-color: transparent;
	-webkit-text-decoration-skip: objects
}

abbr[title] {
	border-bottom: none;
	text-decoration: underline;
	text-decoration: underline dotted
}

b,strong {
	font-weight: inherit;
	font-weight: bolder
}

code,kbd,samp {
	font-family: monospace,monospace;
	font-size: 1em
}

dfn {
	font-style: italic
}

mark {
	background-color: #ff0;
	color: #000
}

small {
	font-size: 80%
}

sub,sup {
	font-size: 75%;
	line-height: 0;
	position: relative;
	vertical-align: baseline
}

sub {
	bottom: -.25em
}

sup {
	top: -.5em
}

audio,video {
	display: inline-block
}

audio:not([controls]) {
	display: none;
	height: 0
}

img {
	border-style: none
}

svg:not(:root) {
	overflow: hidden
}

button,input,optgroup,select,textarea {
	font-family: sans-serif;
	font-size: 100%;
	line-height: 1.15;
	margin: 0
}

button,input {
	overflow: visible
}

button,select {
	text-transform: none
}[type=reset],[type=submit],button,html [type=button] {
	-webkit-appearance: button
}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner {
	border-style: none;
	padding: 0
}[type=button]:-moz-focusring,[type=reset]:-moz-focusring,[type=submit]:-moz-focusring,button:-moz-focusring {
	outline: 1px dotted ButtonText
}

fieldset {
	padding: .35em .75em .625em
}

legend {
	box-sizing: border-box;
	color: inherit;
	display: table;
	max-width: 100%;
	padding: 0;
	white-space: normal
}

progress {
	display: inline-block;
	vertical-align: baseline
}

textarea {
	overflow: auto
}[type=checkbox],[type=radio] {
	box-sizing: border-box;
	padding: 0
}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button {
	height: auto
}[type=search] {
	-webkit-appearance: textfield;
	outline-offset: -2px
}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration {
	-webkit-appearance: none
}

::-webkit-file-upload-button {
	-webkit-appearance: button;
	font: inherit
}

details,menu {
	display: block
}

summary {
	display: list-item
}

canvas {
	display: inline-block
}[hidden],template {
	display: none
}

@font-face {
	font-family:Helvetica Neue For Number;src:local("Helvetica Neue");unicode-range:u+30-39
}

* {
	-webkit-tap-highlight-color: rgba(0,0,0,0)
}

*,:after,:before {
	box-sizing: border-box
}

body,html {
	width: 100%;
	height: 100%
}

body {
	font-family: Helvetica Neue For Number,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Helvetica Neue,Helvetica,Arial,sans-serif;
	font-size: 12px;
	line-height: 1.5;
	color: rgba(0,0,0,.65);
	background-color: #fff
}

article,aside,blockquote,body,button,code,dd,details,div,dl,dt,fieldset,figcaption,figure,footer,form,h1,h2,h3,h4,h5,h6,header,hgroup,hr,input,legend,li,menu,nav,ol,p,pre,section,td,textarea,th,ul {
	margin: 0;
	padding: 0
}

button,input,select,textarea {
	font-family: inherit;
	font-size: inherit;
	line-height: inherit;
	color: inherit
}

ol,ul {
	list-style: none
}

input::-ms-clear,input::-ms-reveal {
	display: none
}

::-moz-selection {
	background: #108ee9;
	color: #fff
}

::selection {
	background: #108ee9;
	color: #fff
}

h1,h2,h3,h4,h5,h6 {
	color: rgba(0,0,0,.85);
	font-weight: 500
}

a {
	color: #108ee9;
	background: transparent;
	text-decoration: none;
	outline: none;
	cursor: pointer;
	transition: color .3s ease
}

a:focus {
	text-decoration: underline;
	-webkit-text-decoration-skip: ink;
	text-decoration-skip: ink
}

a:hover {
	color: #49a9ee
}

a:active {
	color: #0e77ca
}

a:active,a:hover {
	outline: 0;
	text-decoration: none
}

a[disabled] {
	color: rgba(0,0,0,.25);
	cursor: not-allowed;
	pointer-events: none
}

.ant-divider {
	margin: 0 6px;
	display: inline-block;
	height: 8px;
	width: 1px;
	background: #ccc
}

code,kbd,pre,samp {
	font-family: Consolas,Menlo,Courier,monospace
}

.clearfix {
	zoom: 1
}

.clearfix:after,.clearfix:before {
	content: " ";
	display: table
}

.clearfix:after {
	clear: both;
	visibility: hidden;
	font-size: 0;
	height: 0
}

@font-face {
	font-family:anticon;src:url("https://at.alicdn.com/t/font_zck90zmlh7hf47vi.eot");src:url("https://at.alicdn.com/t/font_zck90zmlh7hf47vi.eot?#iefix") format("embedded-opentype"),url("https://at.alicdn.com/t/font_zck90zmlh7hf47vi.woff") format("woff"),url("https://at.alicdn.com/t/font_zck90zmlh7hf47vi.ttf") format("truetype"),url("https://at.alicdn.com/t/font_zck90zmlh7hf47vi.svg#iconfont") format("svg")
}

.anticon {
	display: inline-block;
	font-style: normal;
	vertical-align: baseline;
	text-align: center;
	text-transform: none;
	line-height: 1;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale
}

.anticon:before {
	display: block;
	font-family: anticon!important
}

.anticon-step-forward:before {
	content: "\E600"
}

.anticon-step-backward:before {
	content: "\E601"
}

.anticon-forward:before {
	content: "\E602"
}

.anticon-backward:before {
	content: "\E603"
}

.anticon-caret-right:before {
	content: "\E604"
}

.anticon-caret-left:before {
	content: "\E605"
}

.anticon-caret-down:before {
	content: "\E606"
}

.anticon-caret-up:before {
	content: "\E607"
}

.anticon-caret-circle-right:before,.anticon-circle-right:before,.anticon-right-circle:before {
	content: "\E608"
}

.anticon-caret-circle-left:before,.anticon-circle-left:before,.anticon-left-circle:before {
	content: "\E609"
}

.anticon-caret-circle-up:before,.anticon-circle-up:before,.anticon-up-circle:before {
	content: "\E60A"
}

.anticon-caret-circle-down:before,.anticon-circle-down:before,.anticon-down-circle:before {
	content: "\E60B"
}

.anticon-right-circle-o:before {
	content: "\E60C"
}

.anticon-caret-circle-o-right:before,.anticon-circle-o-right:before {
	content: "\E60C"
}

.anticon-left-circle-o:before {
	content: "\E60D"
}

.anticon-caret-circle-o-left:before,.anticon-circle-o-left:before {
	content: "\E60D"
}

.anticon-up-circle-o:before {
	content: "\E60E"
}

.anticon-caret-circle-o-up:before,.anticon-circle-o-up:before {
	content: "\E60E"
}

.anticon-down-circle-o:before {
	content: "\E60F"
}

.anticon-caret-circle-o-down:before,.anticon-circle-o-down:before {
	content: "\E60F"
}

.anticon-verticle-left:before {
	content: "\E610"
}

.anticon-verticle-right:before {
	content: "\E611"
}

.anticon-rollback:before {
	content: "\E612"
}

.anticon-retweet:before {
	content: "\E613"
}

.anticon-shrink:before {
	content: "\E614"
}

.anticon-arrow-salt:before,.anticon-arrows-alt:before {
	content: "\E615"
}

.anticon-reload:before {
	content: "\E616"
}

.anticon-double-right:before {
	content: "\E617"
}

.anticon-double-left:before {
	content: "\E618"
}

.anticon-arrow-down:before {
	content: "\E619"
}

.anticon-arrow-up:before {
	content: "\E61A"
}

.anticon-arrow-right:before {
	content: "\E61B"
}

.anticon-arrow-left:before {
	content: "\E61C"
}

.anticon-down:before {
	content: "\E61D"
}

.anticon-up:before {
	content: "\E61E"
}

.anticon-right:before {
	content: "\E61F"
}

.anticon-left:before {
	content: "\E620"
}

.anticon-minus-square-o:before {
	content: "\E621"
}

.anticon-minus-circle:before {
	content: "\E622"
}

.anticon-minus-circle-o:before {
	content: "\E623"
}

.anticon-minus:before {
	content: "\E624"
}

.anticon-plus-circle-o:before {
	content: "\E625"
}

.anticon-plus-circle:before {
	content: "\E626"
}

.anticon-plus:before {
	content: "\E627"
}

.anticon-info-circle:before {
	content: "\E628"
}

.anticon-info-circle-o:before {
	content: "\E629"
}

.anticon-info:before {
	content: "\E62A"
}

.anticon-exclamation:before {
	content: "\E62B"
}

.anticon-exclamation-circle:before {
	content: "\E62C"
}

.anticon-exclamation-circle-o:before {
	content: "\E62D"
}

.anticon-close-circle:before,.anticon-cross-circle:before {
	content: "\E62E"
}

.anticon-close-circle-o:before,.anticon-cross-circle-o:before {
	content: "\E62F"
}

.anticon-check-circle:before {
	content: "\E630"
}

.anticon-check-circle-o:before {
	content: "\E631"
}

.anticon-check:before {
	content: "\E632"
}

.anticon-close:before,.anticon-cross:before {
	content: "\E633"
}

.anticon-customer-service:before,.anticon-customerservice:before {
	content: "\E634"
}

.anticon-credit-card:before {
	content: "\E635"
}

.anticon-code-o:before {
	content: "\E636"
}

.anticon-book:before {
	content: "\E637"
}

.anticon-bar-chart:before {
	content: "\E638"
}

.anticon-bars:before {
	content: "\E639"
}

.anticon-question:before {
	content: "\E63A"
}

.anticon-question-circle:before {
	content: "\E63B"
}

.anticon-question-circle-o:before {
	content: "\E63C"
}

.anticon-pause:before {
	content: "\E63D"
}

.anticon-pause-circle:before {
	content: "\E63E"
}

.anticon-pause-circle-o:before {
	content: "\E63F"
}

.anticon-clock-circle:before {
	content: "\E640"
}

.anticon-clock-circle-o:before {
	content: "\E641"
}

.anticon-swap:before {
	content: "\E642"
}

.anticon-swap-left:before {
	content: "\E643"
}

.anticon-swap-right:before {
	content: "\E644"
}

.anticon-plus-square-o:before {
	content: "\E645"
}

.anticon-frown-circle:before,.anticon-frown:before {
	content: "\E646"
}

.anticon-ellipsis:before {
	content: "\E647"
}

.anticon-copy:before {
	content: "\E648"
}

.anticon-menu-fold:before {
	content: "\E658"
}

.anticon-mail:before {
	content: "\E659"
}

.anticon-logout:before {
	content: "\E65A"
}

.anticon-link:before {
	content: "\E65B"
}

.anticon-area-chart:before {
	content: "\E65C"
}

.anticon-line-chart:before {
	content: "\E65D"
}

.anticon-home:before {
	content: "\E65E"
}

.anticon-laptop:before {
	content: "\E65F"
}

.anticon-star:before {
	content: "\E660"
}

.anticon-star-o:before {
	content: "\E661"
}

.anticon-folder:before {
	content: "\E662"
}

.anticon-filter:before {
	content: "\E663"
}

.anticon-file:before {
	content: "\E664"
}

.anticon-exception:before {
	content: "\E665"
}

.anticon-meh-circle:before,.anticon-meh:before {
	content: "\E666"
}

.anticon-meh-o:before {
	content: "\E667"
}

.anticon-shopping-cart:before {
	content: "\E668"
}

.anticon-save:before {
	content: "\E669"
}

.anticon-user:before {
	content: "\E66A"
}

.anticon-video-camera:before {
	content: "\E66B"
}

.anticon-to-top:before {
	content: "\E66C"
}

.anticon-team:before {
	content: "\E66D"
}

.anticon-tablet:before {
	content: "\E66E"
}

.anticon-solution:before {
	content: "\E66F"
}

.anticon-search:before {
	content: "\E670"
}

.anticon-share-alt:before {
	content: "\E671"
}

.anticon-setting:before {
	content: "\E672"
}

.anticon-poweroff:before {
	content: "\E6D5"
}

.anticon-picture:before {
	content: "\E674"
}

.anticon-phone:before {
	content: "\E675"
}

.anticon-paper-clip:before {
	content: "\E676"
}

.anticon-notification:before {
	content: "\E677"
}

.anticon-mobile:before {
	content: "\E678"
}

.anticon-menu-unfold:before {
	content: "\E679"
}

.anticon-inbox:before {
	content: "\E67A"
}

.anticon-lock:before {
	content: "\E67B"
}

.anticon-qrcode:before {
	content: "\E67C"
}

.anticon-play-circle:before {
	content: "\E6D0"
}

.anticon-play-circle-o:before {
	content: "\E6D1"
}

.anticon-tag:before {
	content: "\E6D2"
}

.anticon-tag-o:before {
	content: "\E6D3"
}

.anticon-tags:before {
	content: "\E67D"
}

.anticon-tags-o:before {
	content: "\E67E"
}

.anticon-cloud-o:before {
	content: "\E67F"
}

.anticon-cloud:before {
	content: "\E680"
}

.anticon-cloud-upload:before {
	content: "\E681"
}

.anticon-cloud-download:before {
	content: "\E682"
}

.anticon-cloud-download-o:before {
	content: "\E683"
}

.anticon-cloud-upload-o:before {
	content: "\E684"
}

.anticon-environment:before {
	content: "\E685"
}

.anticon-environment-o:before {
	content: "\E686"
}

.anticon-eye:before {
	content: "\E687"
}

.anticon-eye-o:before {
	content: "\E688"
}

.anticon-camera:before {
	content: "\E689"
}

.anticon-camera-o:before {
	content: "\E68A"
}

.anticon-windows:before {
	content: "\E68B"
}

.anticon-apple:before {
	content: "\E68C"
}

.anticon-apple-o:before {
	content: "\E6D4"
}

.anticon-android:before {
	content: "\E938"
}

.anticon-android-o:before {
	content: "\E68D"
}

.anticon-aliwangwang:before {
	content: "\E68E"
}

.anticon-aliwangwang-o:before {
	content: "\E68F"
}

.anticon-export:before {
	content: "\E691"
}

.anticon-edit:before {
	content: "\E692"
}

.anticon-circle-down-o:before {
	content: "\E693"
}

.anticon-circle-down-:before {
	content: "\E694"
}

.anticon-appstore-o:before {
	content: "\E695"
}

.anticon-appstore:before {
	content: "\E696"
}

.anticon-scan:before {
	content: "\E697"
}

.anticon-file-text:before {
	content: "\E698"
}

.anticon-folder-open:before {
	content: "\E699"
}

.anticon-hdd:before {
	content: "\E69A"
}

.anticon-ie:before {
	content: "\E69B"
}

.anticon-file-jpg:before {
	content: "\E69C"
}

.anticon-like:before {
	content: "\E64C"
}

.anticon-like-o:before {
	content: "\E69D"
}

.anticon-dislike:before {
	content: "\E64B"
}

.anticon-dislike-o:before {
	content: "\E69E"
}

.anticon-delete:before {
	content: "\E69F"
}

.anticon-enter:before {
	content: "\E6A0"
}

.anticon-pushpin-o:before {
	content: "\E6A1"
}

.anticon-pushpin:before {
	content: "\E6A2"
}

.anticon-heart:before {
	content: "\E6A3"
}

.anticon-heart-o:before {
	content: "\E6A4"
}

.anticon-pay-circle:before {
	content: "\E6A5"
}

.anticon-pay-circle-o:before {
	content: "\E6A6"
}

.anticon-smile-circle:before,.anticon-smile:before {
	content: "\E6A7"
}

.anticon-smile-o:before {
	content: "\E6A8"
}

.anticon-frown-o:before {
	content: "\E6A9"
}

.anticon-calculator:before {
	content: "\E6AA"
}

.anticon-message:before {
	content: "\E6AB"
}

.anticon-chrome:before {
	content: "\E6AC"
}

.anticon-github:before {
	content: "\E6AD"
}

.anticon-file-unknown:before {
	content: "\E6AF"
}

.anticon-file-excel:before {
	content: "\E6B0"
}

.anticon-file-ppt:before {
	content: "\E6B1"
}

.anticon-file-word:before {
	content: "\E6B2"
}

.anticon-file-pdf:before {
	content: "\E6B3"
}

.anticon-desktop:before {
	content: "\E6B4"
}

.anticon-upload:before {
	content: "\E6B6"
}

.anticon-download:before {
	content: "\E6B7"
}

.anticon-pie-chart:before {
	content: "\E6B8"
}

.anticon-unlock:before {
	content: "\E6BA"
}

.anticon-calendar:before {
	content: "\E6BB"
}

.anticon-windows-o:before {
	content: "\E6BC"
}

.anticon-dot-chart:before {
	content: "\E6BD"
}

.anticon-bar-chart:before {
	content: "\E6BE"
}

.anticon-code:before {
	content: "\E6BF"
}

.anticon-api:before {
	content: "\E951"
}

.anticon-plus-square:before {
	content: "\E6C0"
}

.anticon-minus-square:before {
	content: "\E6C1"
}

.anticon-close-square:before {
	content: "\E6C2"
}

.anticon-close-square-o:before {
	content: "\E6C3"
}

.anticon-check-square:before {
	content: "\E6C4"
}

.anticon-check-square-o:before {
	content: "\E6C5"
}

.anticon-fast-backward:before {
	content: "\E6C6"
}

.anticon-fast-forward:before {
	content: "\E6C7"
}

.anticon-up-square:before {
	content: "\E6C8"
}

.anticon-down-square:before {
	content: "\E6C9"
}

.anticon-left-square:before {
	content: "\E6CA"
}

.anticon-right-square:before {
	content: "\E6CB"
}

.anticon-right-square-o:before {
	content: "\E6CC"
}

.anticon-left-square-o:before {
	content: "\E6CD"
}

.anticon-down-square-o:before {
	content: "\E6CE"
}

.anticon-up-square-o:before {
	content: "\E6CF"
}

.anticon-loading:before {
	content: "\E64D"
}

.anticon-loading-3-quarters:before {
	content: "\E6AE"
}

.anticon-bulb:before {
	content: "\E649"
}

.anticon-select:before {
	content: "\E64A"
}

.anticon-addfile:before,.anticon-file-add:before {
	content: "\E910"
}

.anticon-addfolder:before,.anticon-folder-add:before {
	content: "\E914"
}

.anticon-switcher:before {
	content: "\E913"
}

.anticon-rocket:before {
	content: "\E90F"
}

.anticon-dingding:before {
	content: "\E923"
}

.anticon-dingding-o:before {
	content: "\E925"
}

.anticon-bell:before {
	content: "\E64E"
}

.anticon-disconnect:before {
	content: "\E64F"
}

.anticon-database:before {
	content: "\E650"
}

.anticon-compass:before {
	content: "\E6DB"
}

.anticon-barcode:before {
	content: "\E652"
}

.anticon-hourglass:before {
	content: "\E653"
}

.anticon-key:before {
	content: "\E654"
}

.anticon-flag:before {
	content: "\E655"
}

.anticon-layout:before {
	content: "\E656"
}

.anticon-login:before {
	content: "\E657"
}

.anticon-printer:before {
	content: "\E673"
}

.anticon-sound:before {
	content: "\E6E9"
}

.anticon-usb:before {
	content: "\E6D7"
}

.anticon-skin:before {
	content: "\E6D8"
}

.anticon-tool:before {
	content: "\E6D9"
}

.anticon-sync:before {
	content: "\E6DA"
}

.anticon-wifi:before {
	content: "\E6D6"
}

.anticon-car:before {
	content: "\E6DC"
}

.anticon-copyright:before {
	content: "\E6DE"
}

.anticon-schedule:before {
	content: "\E6DF"
}

.anticon-user-add:before {
	content: "\E6ED"
}

.anticon-user-delete:before {
	content: "\E6E0"
}

.anticon-usergroup-add:before {
	content: "\E6DD"
}

.anticon-usergroup-delete:before {
	content: "\E6E1"
}

.anticon-man:before {
	content: "\E6E2"
}

.anticon-woman:before {
	content: "\E6EC"
}

.anticon-shop:before {
	content: "\E6E3"
}

.anticon-gift:before {
	content: "\E6E4"
}

.anticon-idcard:before {
	content: "\E6E5"
}

.anticon-medicine-box:before {
	content: "\E6E6"
}

.anticon-red-envelope:before {
	content: "\E6E7"
}

.anticon-coffee:before {
	content: "\E6E8"
}

.anticon-trademark:before {
	content: "\E651"
}

.anticon-safety:before {
	content: "\E6EA"
}

.anticon-wallet:before {
	content: "\E6EB"
}

.anticon-bank:before {
	content: "\E6EE"
}

.anticon-trophy:before {
	content: "\E6EF"
}

.anticon-contacts:before {
	content: "\E6F0"
}

.anticon-global:before {
	content: "\E6F1"
}

.anticon-shake:before {
	content: "\E94F"
}

.anticon-fork:before {
	content: "\E6F2"
}

.anticon-spin:before {
	display: inline-block;
	-webkit-animation: loadingCircle 1s infinite linear;
	animation: loadingCircle 1s infinite linear
}

.fade-appear,.fade-enter,.fade-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.fade-appear.fade-appear-active,.fade-enter.fade-enter-active {
	-webkit-animation-name: antFadeIn;
	animation-name: antFadeIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.fade-leave.fade-leave-active {
	-webkit-animation-name: antFadeOut;
	animation-name: antFadeOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.fade-appear,.fade-enter {
	opacity: 0
}

.fade-appear,.fade-enter,.fade-leave {
	-webkit-animation-timing-function: linear;
	animation-timing-function: linear
}

@-webkit-keyframes antFadeIn {
	0% {
		opacity: 0
	}

	to {
		opacity: 1
	}
}

@keyframes antFadeIn {
	0% {
		opacity: 0
	}

	to {
		opacity: 1
	}
}

@-webkit-keyframes antFadeOut {
	0% {
		opacity: 1
	}

	to {
		opacity: 0
	}
}

@keyframes antFadeOut {
	0% {
		opacity: 1
	}

	to {
		opacity: 0
	}
}

.move-up-appear,.move-up-enter,.move-up-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.move-up-appear.move-up-appear-active,.move-up-enter.move-up-enter-active {
	-webkit-animation-name: antMoveUpIn;
	animation-name: antMoveUpIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.move-up-leave.move-up-leave-active {
	-webkit-animation-name: antMoveUpOut;
	animation-name: antMoveUpOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.move-up-appear,.move-up-enter {
	opacity: 0;
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.move-up-leave {
	-webkit-animation-timing-function: cubic-bezier(.6,.04,.98,.34);
	animation-timing-function: cubic-bezier(.6,.04,.98,.34)
}

.move-down-appear,.move-down-enter,.move-down-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.move-down-appear.move-down-appear-active,.move-down-enter.move-down-enter-active {
	-webkit-animation-name: antMoveDownIn;
	animation-name: antMoveDownIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.move-down-leave.move-down-leave-active {
	-webkit-animation-name: antMoveDownOut;
	animation-name: antMoveDownOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.move-down-appear,.move-down-enter {
	opacity: 0;
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.move-down-leave {
	-webkit-animation-timing-function: cubic-bezier(.6,.04,.98,.34);
	animation-timing-function: cubic-bezier(.6,.04,.98,.34)
}

.move-left-appear,.move-left-enter,.move-left-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.move-left-appear.move-left-appear-active,.move-left-enter.move-left-enter-active {
	-webkit-animation-name: antMoveLeftIn;
	animation-name: antMoveLeftIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.move-left-leave.move-left-leave-active {
	-webkit-animation-name: antMoveLeftOut;
	animation-name: antMoveLeftOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.move-left-appear,.move-left-enter {
	opacity: 0;
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.move-left-leave {
	-webkit-animation-timing-function: cubic-bezier(.6,.04,.98,.34);
	animation-timing-function: cubic-bezier(.6,.04,.98,.34)
}

.move-right-appear,.move-right-enter,.move-right-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.move-right-appear.move-right-appear-active,.move-right-enter.move-right-enter-active {
	-webkit-animation-name: antMoveRightIn;
	animation-name: antMoveRightIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.move-right-leave.move-right-leave-active {
	-webkit-animation-name: antMoveRightOut;
	animation-name: antMoveRightOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.move-right-appear,.move-right-enter {
	opacity: 0;
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.move-right-leave {
	-webkit-animation-timing-function: cubic-bezier(.6,.04,.98,.34);
	animation-timing-function: cubic-bezier(.6,.04,.98,.34)
}

@-webkit-keyframes antMoveDownIn {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(100%);
		transform: translateY(100%);
		opacity: 0
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}
}

@keyframes antMoveDownIn {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(100%);
		transform: translateY(100%);
		opacity: 0
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}
}

@-webkit-keyframes antMoveDownOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(100%);
		transform: translateY(100%);
		opacity: 0
	}
}

@keyframes antMoveDownOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(100%);
		transform: translateY(100%);
		opacity: 0
	}
}

@-webkit-keyframes antMoveLeftIn {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(-100%);
		transform: translateX(-100%);
		opacity: 0
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0);
		opacity: 1
	}
}

@keyframes antMoveLeftIn {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(-100%);
		transform: translateX(-100%);
		opacity: 0
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0);
		opacity: 1
	}
}

@-webkit-keyframes antMoveLeftOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(-100%);
		transform: translateX(-100%);
		opacity: 0
	}
}

@keyframes antMoveLeftOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(-100%);
		transform: translateX(-100%);
		opacity: 0
	}
}

@-webkit-keyframes antMoveRightIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(100%);
		transform: translateX(100%)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0)
	}
}

@keyframes antMoveRightIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(100%);
		transform: translateX(100%)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0)
	}
}

@-webkit-keyframes antMoveRightOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(100%);
		transform: translateX(100%);
		opacity: 0
	}
}

@keyframes antMoveRightOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(0);
		transform: translateX(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateX(100%);
		transform: translateX(100%);
		opacity: 0
	}
}

@-webkit-keyframes antMoveUpIn {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(-100%);
		transform: translateY(-100%);
		opacity: 0
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}
}

@keyframes antMoveUpIn {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(-100%);
		transform: translateY(-100%);
		opacity: 0
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}
}

@-webkit-keyframes antMoveUpOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(-100%);
		transform: translateY(-100%);
		opacity: 0
	}
}

@keyframes antMoveUpOut {
	0% {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(0);
		transform: translateY(0);
		opacity: 1
	}

	to {
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: translateY(-100%);
		transform: translateY(-100%);
		opacity: 0
	}
}

@-webkit-keyframes loadingCircle {
	0% {
		-webkit-transform-origin: 50% 50%;
		transform-origin: 50% 50%;
		-webkit-transform: rotate(0deg);
		transform: rotate(0deg)
	}

	to {
		-webkit-transform-origin: 50% 50%;
		transform-origin: 50% 50%;
		-webkit-transform: rotate(1turn);
		transform: rotate(1turn)
	}
}

@keyframes loadingCircle {
	0% {
		-webkit-transform-origin: 50% 50%;
		transform-origin: 50% 50%;
		-webkit-transform: rotate(0deg);
		transform: rotate(0deg)
	}

	to {
		-webkit-transform-origin: 50% 50%;
		transform-origin: 50% 50%;
		-webkit-transform: rotate(1turn);
		transform: rotate(1turn)
	}
}

@-webkit-keyframes antSlideUpIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}
}

@keyframes antSlideUpIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}
}

@-webkit-keyframes antSlideUpOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}
}

@keyframes antSlideUpOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}
}

@-webkit-keyframes antSlideDownIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}
}

@keyframes antSlideDownIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}
}

@-webkit-keyframes antSlideDownOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}
}

@keyframes antSlideDownOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 100% 100%;
		transform-origin: 100% 100%;
		-webkit-transform: scaleY(.8);
		transform: scaleY(.8)
	}
}

@-webkit-keyframes antSlideLeftIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}
}

@keyframes antSlideLeftIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}
}

@-webkit-keyframes antSlideLeftOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}
}

@keyframes antSlideLeftOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}
}

@-webkit-keyframes antSlideRightIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}
}

@keyframes antSlideRightIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}
}

@-webkit-keyframes antSlideRightOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}
}

@keyframes antSlideRightOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(1);
		transform: scaleX(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 100% 0;
		transform-origin: 100% 0;
		-webkit-transform: scaleX(.8);
		transform: scaleX(.8)
	}
}

.swing-appear,.swing-enter {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.swing-appear.swing-appear-active,.swing-enter.swing-enter-active {
	-webkit-animation-name: antSwingIn;
	animation-name: antSwingIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

@-webkit-keyframes antSwingIn {
	0%,to {
		-webkit-transform: translateX(0);
		transform: translateX(0)
	}

	20% {
		-webkit-transform: translateX(-10px);
		transform: translateX(-10px)
	}

	40% {
		-webkit-transform: translateX(10px);
		transform: translateX(10px)
	}

	60% {
		-webkit-transform: translateX(-5px);
		transform: translateX(-5px)
	}

	80% {
		-webkit-transform: translateX(5px);
		transform: translateX(5px)
	}
}

@keyframes antSwingIn {
	0%,to {
		-webkit-transform: translateX(0);
		transform: translateX(0)
	}

	20% {
		-webkit-transform: translateX(-10px);
		transform: translateX(-10px)
	}

	40% {
		-webkit-transform: translateX(10px);
		transform: translateX(10px)
	}

	60% {
		-webkit-transform: translateX(-5px);
		transform: translateX(-5px)
	}

	80% {
		-webkit-transform: translateX(5px);
		transform: translateX(5px)
	}
}

.zoom-appear,.zoom-enter,.zoom-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.zoom-appear.zoom-appear-active,.zoom-enter.zoom-enter-active {
	-webkit-animation-name: antZoomIn;
	animation-name: antZoomIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.zoom-leave.zoom-leave-active {
	-webkit-animation-name: antZoomOut;
	animation-name: antZoomOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.zoom-appear,.zoom-enter {
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.zoom-leave {
	-webkit-animation-timing-function: cubic-bezier(.78,.14,.15,.86);
	animation-timing-function: cubic-bezier(.78,.14,.15,.86)
}

.zoom-big-appear,.zoom-big-enter,.zoom-big-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.zoom-big-appear.zoom-big-appear-active,.zoom-big-enter.zoom-big-enter-active {
	-webkit-animation-name: antZoomBigIn;
	animation-name: antZoomBigIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.zoom-big-leave.zoom-big-leave-active {
	-webkit-animation-name: antZoomBigOut;
	animation-name: antZoomBigOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.zoom-big-appear,.zoom-big-enter {
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.zoom-big-leave {
	-webkit-animation-timing-function: cubic-bezier(.78,.14,.15,.86);
	animation-timing-function: cubic-bezier(.78,.14,.15,.86)
}

.zoom-big-fast-appear,.zoom-big-fast-enter,.zoom-big-fast-leave {
	-webkit-animation-duration: .1s;
	animation-duration: .1s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.zoom-big-fast-appear.zoom-big-fast-appear-active,.zoom-big-fast-enter.zoom-big-fast-enter-active {
	-webkit-animation-name: antZoomBigIn;
	animation-name: antZoomBigIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.zoom-big-fast-leave.zoom-big-fast-leave-active {
	-webkit-animation-name: antZoomBigOut;
	animation-name: antZoomBigOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.zoom-big-fast-appear,.zoom-big-fast-enter {
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.zoom-big-fast-leave {
	-webkit-animation-timing-function: cubic-bezier(.78,.14,.15,.86);
	animation-timing-function: cubic-bezier(.78,.14,.15,.86)
}

.zoom-up-appear,.zoom-up-enter,.zoom-up-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.zoom-up-appear.zoom-up-appear-active,.zoom-up-enter.zoom-up-enter-active {
	-webkit-animation-name: antZoomUpIn;
	animation-name: antZoomUpIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.zoom-up-leave.zoom-up-leave-active {
	-webkit-animation-name: antZoomUpOut;
	animation-name: antZoomUpOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.zoom-up-appear,.zoom-up-enter {
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.zoom-up-leave {
	-webkit-animation-timing-function: cubic-bezier(.78,.14,.15,.86);
	animation-timing-function: cubic-bezier(.78,.14,.15,.86)
}

.zoom-down-appear,.zoom-down-enter,.zoom-down-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.zoom-down-appear.zoom-down-appear-active,.zoom-down-enter.zoom-down-enter-active {
	-webkit-animation-name: antZoomDownIn;
	animation-name: antZoomDownIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.zoom-down-leave.zoom-down-leave-active {
	-webkit-animation-name: antZoomDownOut;
	animation-name: antZoomDownOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.zoom-down-appear,.zoom-down-enter {
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.zoom-down-leave {
	-webkit-animation-timing-function: cubic-bezier(.78,.14,.15,.86);
	animation-timing-function: cubic-bezier(.78,.14,.15,.86)
}

.zoom-left-appear,.zoom-left-enter,.zoom-left-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.zoom-left-appear.zoom-left-appear-active,.zoom-left-enter.zoom-left-enter-active {
	-webkit-animation-name: antZoomLeftIn;
	animation-name: antZoomLeftIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.zoom-left-leave.zoom-left-leave-active {
	-webkit-animation-name: antZoomLeftOut;
	animation-name: antZoomLeftOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.zoom-left-appear,.zoom-left-enter {
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.zoom-left-leave {
	-webkit-animation-timing-function: cubic-bezier(.78,.14,.15,.86);
	animation-timing-function: cubic-bezier(.78,.14,.15,.86)
}

.zoom-right-appear,.zoom-right-enter,.zoom-right-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.zoom-right-appear.zoom-right-appear-active,.zoom-right-enter.zoom-right-enter-active {
	-webkit-animation-name: antZoomRightIn;
	animation-name: antZoomRightIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.zoom-right-leave.zoom-right-leave-active {
	-webkit-animation-name: antZoomRightOut;
	animation-name: antZoomRightOut;
	-webkit-animation-play-state: running;
	animation-play-state: running;
	pointer-events: none
}

.zoom-right-appear,.zoom-right-enter {
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	-webkit-animation-timing-function: cubic-bezier(.08,.82,.17,1);
	animation-timing-function: cubic-bezier(.08,.82,.17,1)
}

.zoom-right-leave {
	-webkit-animation-timing-function: cubic-bezier(.78,.14,.15,.86);
	animation-timing-function: cubic-bezier(.78,.14,.15,.86)
}

@-webkit-keyframes antZoomIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(.2);
		transform: scale(.2)
	}

	to {
		opacity: 1;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@keyframes antZoomIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(.2);
		transform: scale(.2)
	}

	to {
		opacity: 1;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@-webkit-keyframes antZoomOut {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform: scale(.2);
		transform: scale(.2)
	}
}

@keyframes antZoomOut {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform: scale(.2);
		transform: scale(.2)
	}
}

@-webkit-keyframes antZoomBigIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@keyframes antZoomBigIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@-webkit-keyframes antZoomBigOut {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@keyframes antZoomBigOut {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@-webkit-keyframes antZoomUpIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@keyframes antZoomUpIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@-webkit-keyframes antZoomUpOut {
	0% {
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@keyframes antZoomUpOut {
	0% {
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 50% 0;
		transform-origin: 50% 0;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@-webkit-keyframes antZoomLeftIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@keyframes antZoomLeftIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@-webkit-keyframes antZoomLeftOut {
	0% {
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@keyframes antZoomLeftOut {
	0% {
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 50%;
		transform-origin: 0 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@-webkit-keyframes antZoomRightIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@keyframes antZoomRightIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@-webkit-keyframes antZoomRightOut {
	0% {
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@keyframes antZoomRightOut {
	0% {
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 100% 50%;
		transform-origin: 100% 50%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@-webkit-keyframes antZoomDownIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@keyframes antZoomDownIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}

	to {
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}
}

@-webkit-keyframes antZoomDownOut {
	0% {
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

@keyframes antZoomDownOut {
	0% {
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(1);
		transform: scale(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 50% 100%;
		transform-origin: 50% 100%;
		-webkit-transform: scale(.8);
		transform: scale(.8)
	}
}

.ant-motion-collapse {
	overflow: hidden
}

.ant-motion-collapse-active {
	transition: height .15s cubic-bezier(.645,.045,.355,1),opacity .15s cubic-bezier(.645,.045,.355,1)!important
}

.ant-notification {
	position: fixed;
	z-index: 1010;
	width: 335px;
	margin-right: 24px
}

.ant-notification-bottomLeft,.ant-notification-topLeft {
	margin-left: 24px;
	margin-right: 0
}

.ant-notification-bottomLeft .ant-notification-fade-appear.ant-notification-fade-appear-active,.ant-notification-bottomLeft .ant-notification-fade-enter.ant-notification-fade-enter-active,.ant-notification-topLeft .ant-notification-fade-appear.ant-notification-fade-appear-active,.ant-notification-topLeft .ant-notification-fade-enter.ant-notification-fade-enter-active {
	-webkit-animation-name: NotificationLeftFadeIn;
	animation-name: NotificationLeftFadeIn
}

.ant-notification-notice {
	padding: 16px;
	border-radius: 4px;
	box-shadow: 0 2px 8px rgba(0,0,0,.2);
	background: #fff;
	line-height: 1.5;
	position: relative;
	margin-bottom: 10px;
	overflow: hidden
}

.ant-notification-notice-message {
	font-size: 14px;
	color: rgba(0,0,0,.85);
	margin-bottom: 4px;
	line-height: 20px;
	display: inline-block
}

.ant-notification-notice-message-single-line-auto-margin {
	width: calc(335px - 16px * 2 - 24px - 48px - 100%);
	background-color: transparent;
	pointer-events: none;
	display: block;
	max-width: 4px
}

.ant-notification-notice-message-single-line-auto-margin:before {
	content: "";
	display: block;
	padding-bottom: 100%
}

.ant-notification-notice-description {
	font-size: 12px
}

.ant-notification-notice-closable .ant-notification-notice-message {
	padding-right: 24px
}

.ant-notification-notice-with-icon .ant-notification-notice-message {
	font-size: 14px;
	margin-left: 48px;
	margin-bottom: 4px
}

.ant-notification-notice-with-icon .ant-notification-notice-description {
	margin-left: 48px;
	font-size: 12px
}

.ant-notification-notice-icon {
	position: absolute;
	font-size: 32px;
	line-height: 32px
}

.ant-notification-notice-icon-success {
	color: #00a854
}

.ant-notification-notice-icon-info {
	color: #108ee9
}

.ant-notification-notice-icon-warning {
	color: #ffbf00
}

.ant-notification-notice-icon-error {
	color: #f04134
}

.ant-notification-notice-close-x:after {
	font-size: 12px;
	content: "\E633";
	font-family: anticon;
	cursor: pointer
}

.ant-notification-notice-close {
	position: absolute;
	right: 16px;
	top: 10px;
	color: rgba(0,0,0,.43);
	outline: none;
	text-decoration: none
}

.ant-notification-notice-close:hover {
	color: #404040
}

.ant-notification-notice-btn {
	float: right;
	margin-top: 16px
}

.ant-notification .notification-fade-effect {
	-webkit-animation-duration: .24s;
	animation-duration: .24s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-timing-function: cubic-bezier(.645,.045,.355,1);
	animation-timing-function: cubic-bezier(.645,.045,.355,1)
}

.ant-notification-fade-appear,.ant-notification-fade-enter {
	opacity: 0;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.ant-notification-fade-appear,.ant-notification-fade-enter,.ant-notification-fade-leave {
	-webkit-animation-duration: .24s;
	animation-duration: .24s;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	-webkit-animation-timing-function: cubic-bezier(.645,.045,.355,1);
	animation-timing-function: cubic-bezier(.645,.045,.355,1)
}

.ant-notification-fade-leave {
	-webkit-animation-duration: .2s;
	animation-duration: .2s;
	-webkit-animation-play-state: paused;
	animation-play-state: paused
}

.ant-notification-fade-appear.ant-notification-fade-appear-active,.ant-notification-fade-enter.ant-notification-fade-enter-active {
	-webkit-animation-name: NotificationFadeIn;
	animation-name: NotificationFadeIn;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

.ant-notification-fade-leave.ant-notification-fade-leave-active {
	-webkit-animation-name: NotificationFadeOut;
	animation-name: NotificationFadeOut;
	-webkit-animation-play-state: running;
	animation-play-state: running
}

@-webkit-keyframes NotificationFadeIn {
	0% {
		opacity: 0;
		left: 335px
	}

	to {
		left: 0;
		opacity: 1
	}
}

@keyframes NotificationFadeIn {
	0% {
		opacity: 0;
		left: 335px
	}

	to {
		left: 0;
		opacity: 1
	}
}

@-webkit-keyframes NotificationLeftFadeIn {
	0% {
		opacity: 0;
		right: 335px
	}

	to {
		right: 0;
		opacity: 1
	}
}

@keyframes NotificationLeftFadeIn {
	0% {
		opacity: 0;
		right: 335px
	}

	to {
		right: 0;
		opacity: 1
	}
}

@-webkit-keyframes NotificationFadeOut {
	0% {
		opacity: 1;
		margin-bottom: 10px;
		padding-top: 16px;
		padding-bottom: 16px;
		max-height: 150px
	}

	to {
		opacity: 0;
		margin-bottom: 0;
		padding-top: 0;
		padding-bottom: 0;
		max-height: 0
	}
}

@keyframes NotificationFadeOut {
	0% {
		opacity: 1;
		margin-bottom: 10px;
		padding-top: 16px;
		padding-bottom: 16px;
		max-height: 150px
	}

	to {
		opacity: 0;
		margin-bottom: 0;
		padding-top: 0;
		padding-bottom: 0;
		max-height: 0
	}
}

.ant-breadcrumb {
	color: rgba(0,0,0,.65);
	font-size: 12px
}

.ant-breadcrumb a {
	color: rgba(0,0,0,.65);
	transition: color .3s
}

.ant-breadcrumb a:hover {
	color: #49a9ee
}

.ant-breadcrumb>span:last-child {
	font-weight: 500;
	color: rgba(0,0,0,.65)
}

.ant-breadcrumb>span:last-child .ant-breadcrumb-separator {
	display: none
}

.ant-breadcrumb-separator {
	margin: 0 8px;
	color: rgba(0,0,0,.3)
}

.ant-breadcrumb-link>.anticon+span {
	margin-left: 4px
}

.ant-menu {
	outline: none;
	margin-bottom: 0;
	padding-left: 0;
	list-style: none;
	z-index: 1050;
	box-shadow: 0 1px 6px rgba(0,0,0,.2);
	color: rgba(0,0,0,.65);
	background: #fff;
	line-height: 46px;
	transition: background .3s,width .2s
}

.ant-menu-hidden {
	display: none
}

.ant-menu-item-group-list {
	margin: 0;
	padding: 0
}

.ant-menu-item-group-title {
	color: rgba(0,0,0,.43);
	font-size: 12px;
	line-height: 1.5;
	padding: 8px 16px;
	transition: all .3s
}

.ant-menu-item,.ant-menu-submenu,.ant-menu-submenu-title {
	cursor: pointer
}

.ant-menu-submenu,.ant-menu-submenu-inline {
	transition: border-color .3s cubic-bezier(.645,.045,.355,1),background .3s cubic-bezier(.645,.045,.355,1),padding .15s cubic-bezier(.645,.045,.355,1)
}

.ant-menu-item,.ant-menu-submenu-title {
	transition: color .3s cubic-bezier(.645,.045,.355,1),border-color .3s cubic-bezier(.645,.045,.355,1),background .3s cubic-bezier(.645,.045,.355,1),padding .15s cubic-bezier(.645,.045,.355,1)
}

.ant-menu-item:active,.ant-menu-submenu-title:active {
	background: #ecf6fd
}

.ant-menu-submenu .ant-menu-sub {
	cursor: auto;
	transition: background .3s cubic-bezier(.645,.045,.355,1),padding .3s cubic-bezier(.645,.045,.355,1)
}

.ant-menu-item>a {
	display: block;
	color: rgba(0,0,0,.65)
}

.ant-menu-item>a:hover {
	color: #108ee9
}

.ant-menu-item>a:focus {
	text-decoration: none
}

.ant-menu-item>a:before {
	position: absolute;
	background-color: transparent;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	content: ""
}

.ant-menu-item-divider {
	height: 1px;
	overflow: hidden;
	background-color: #e9e9e9;
	line-height: 0
}

.ant-menu-item-active,.ant-menu-item:hover,.ant-menu-submenu-active,.ant-menu-submenu-title:hover,.ant-menu:not(.ant-menu-inline) .ant-menu-submenu-open {
	color: #108ee9
}

.ant-menu:not(.ant-menu-inline) .ant-menu-submenu-open {
	z-index: 1050
}

.ant-menu-horizontal .ant-menu-item,.ant-menu-horizontal .ant-menu-submenu {
	margin-top: -1px
}

.ant-menu-horizontal>.ant-menu-item-active,.ant-menu-horizontal>.ant-menu-item:hover,.ant-menu-horizontal>.ant-menu-submenu .ant-menu-submenu-title:hover {
	background-color: transparent
}

.ant-menu-item-selected,.ant-menu-item-selected>a,.ant-menu-item-selected>a:hover {
	color: #108ee9
}

.ant-menu:not(.ant-menu-horizontal) .ant-menu-item-selected {
	background-color: #ecf6fd
}

.ant-menu-horizontal,.ant-menu-inline,.ant-menu-vertical {
	z-index: auto
}

.ant-menu-inline,.ant-menu-vertical {
	border-right: 1px solid #e9e9e9
}

.ant-menu-inline .ant-menu-item,.ant-menu-vertical .ant-menu-item {
	margin-left: -1px;
	left: 1px;
	position: relative;
	z-index: 1
}

.ant-menu-inline .ant-menu-item:after,.ant-menu-vertical .ant-menu-item:after {
	content: "";
	position: absolute;
	right: 0;
	top: 0;
	bottom: 0;
	border-right: 3px solid #108ee9;
	-webkit-transform: scaleY(.0001);
	-ms-transform: scaleY(.0001);
	transform: scaleY(.0001);
	opacity: 0;
	transition: opacity .15s cubic-bezier(.215,.61,.355,1),-webkit-transform .15s cubic-bezier(.215,.61,.355,1);
	transition: transform .15s cubic-bezier(.215,.61,.355,1),opacity .15s cubic-bezier(.215,.61,.355,1);
	transition: transform .15s cubic-bezier(.215,.61,.355,1),opacity .15s cubic-bezier(.215,.61,.355,1),-webkit-transform .15s cubic-bezier(.215,.61,.355,1)
}

.ant-menu-vertical.ant-menu-sub {
	border-right: 0
}

.ant-menu-vertical.ant-menu-sub .ant-menu-item {
	border-right: 0;
	margin-left: 0;
	left: 0
}

.ant-menu-vertical.ant-menu-sub .ant-menu-item:after {
	border-right: 0
}

.ant-menu-vertical.ant-menu-sub>.ant-menu-item:first-child {
	border-radius: 4px 4px 0 0
}

.ant-menu-vertical.ant-menu-sub>.ant-menu-item-group:last-child>.ant-menu-item-group-list:last-child>.ant-menu-item:last-child,.ant-menu-vertical.ant-menu-sub>.ant-menu-item:last-child {
	border-radius: 0 0 4px 4px
}

.ant-menu-vertical.ant-menu-sub>.ant-menu-item:only-child {
	border-radius: 4px
}

.ant-menu-inline {
	width: 100%
}

.ant-menu-inline .ant-menu-item-selected:after,.ant-menu-inline .ant-menu-selected:after {
	transition: opacity .15s cubic-bezier(.645,.045,.355,1),-webkit-transform .15s cubic-bezier(.645,.045,.355,1);
	transition: transform .15s cubic-bezier(.645,.045,.355,1),opacity .15s cubic-bezier(.645,.045,.355,1);
	transition: transform .15s cubic-bezier(.645,.045,.355,1),opacity .15s cubic-bezier(.645,.045,.355,1),-webkit-transform .15s cubic-bezier(.645,.045,.355,1);
	opacity: 1;
	-webkit-transform: scaleY(1);
	-ms-transform: scaleY(1);
	transform: scaleY(1)
}

.ant-menu-submenu-horizontal>.ant-menu {
	top: 100%;
	left: 0;
	position: absolute;
	min-width: 100%;
	margin-top: 7px;
	z-index: 1050
}

.ant-menu-submenu-vertical {
	z-index: 1
}

.ant-menu-submenu-vertical>.ant-menu {
	top: 0;
	left: 100%;
	position: absolute;
	min-width: 160px;
	margin-left: 4px;
	z-index: 1050
}

.ant-menu-item,.ant-menu-submenu-title {
	margin: 0;
	padding: 0 20px;
	position: relative;
	display: block;
	white-space: nowrap
}

.ant-menu-item .anticon,.ant-menu-submenu-title .anticon {
	min-width: 14px;
	margin-right: 8px;
	transition: font-size .15s cubic-bezier(.215,.61,.355,1),margin .3s cubic-bezier(.645,.045,.355,1)
}

.ant-menu-item .anticon+span,.ant-menu-submenu-title .anticon+span {
	transition: opacity .3s cubic-bezier(.645,.045,.355,1),width .3s cubic-bezier(.645,.045,.355,1);
	opacity: 1
}

.ant-menu>.ant-menu-item-divider {
	height: 1px;
	margin: 1px 0;
	overflow: hidden;
	padding: 0;
	line-height: 0;
	background-color: #e9e9e9
}

.ant-menu-submenu {
	position: relative
}

.ant-menu-submenu>.ant-menu {
	background-color: #fff;
	border-radius: 4px
}

.ant-menu-submenu>.ant-menu-submenu-title:after {
	transition: -webkit-transform .3s cubic-bezier(.645,.045,.355,1);
	transition: transform .3s cubic-bezier(.645,.045,.355,1);
	transition: transform .3s cubic-bezier(.645,.045,.355,1),-webkit-transform .3s cubic-bezier(.645,.045,.355,1)
}

.ant-menu-submenu-vertical>.ant-menu-submenu-title:after {
	-ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
	-webkit-transform: rotate(270deg) scale(.75);
	-ms-transform: rotate(270deg) scale(.75);
	transform: rotate(270deg) scale(.75)
}

.ant-menu-submenu-inline>.ant-menu-submenu-title:after,.ant-menu-submenu-vertical>.ant-menu-submenu-title:after {
	font-family: anticon!important;
	font-style: normal;
	vertical-align: baseline;
	text-align: center;
	text-transform: none;
	text-rendering: auto;
	position: absolute;
	content: "\E61D";
	right: 16px
}

.ant-menu-submenu-inline>.ant-menu-submenu-title:after {
	top: 0;
	display: inline-block;
	font-size: 12px;
	font-size: 8px\9;
	-webkit-transform: scale(.66666667) rotate(0deg);
	-ms-transform: scale(.66666667) rotate(0deg);
	transform: scale(.66666667) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1
}

:root .ant-menu-submenu-inline>.ant-menu-submenu-title:after {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-menu-submenu-open.ant-menu-submenu-inline>.ant-menu-submenu-title:after {
	-ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
	-webkit-transform: rotate(180deg) scale(.75);
	-ms-transform: rotate(180deg) scale(.75);
	transform: rotate(180deg) scale(.75)
}

.ant-menu-vertical .ant-menu-submenu-selected,.ant-menu-vertical .ant-menu-submenu-selected>a {
	color: #108ee9
}

.ant-menu-horizontal {
	border: 0;
	border-bottom: 1px solid #e9e9e9;
	box-shadow: none;
	z-index: 0
}

.ant-menu-horizontal>.ant-menu-item,.ant-menu-horizontal>.ant-menu-submenu {
	position: relative;
	top: 1px;
	float: left;
	border-bottom: 2px solid transparent
}

.ant-menu-horizontal>.ant-menu-item-active,.ant-menu-horizontal>.ant-menu-item-open,.ant-menu-horizontal>.ant-menu-item-selected,.ant-menu-horizontal>.ant-menu-item:hover,.ant-menu-horizontal>.ant-menu-submenu-active,.ant-menu-horizontal>.ant-menu-submenu-open,.ant-menu-horizontal>.ant-menu-submenu-selected,.ant-menu-horizontal>.ant-menu-submenu:hover {
	border-bottom: 2px solid #108ee9;
	color: #108ee9
}

.ant-menu-horizontal>.ant-menu-item>a,.ant-menu-horizontal>.ant-menu-submenu>a {
	display: block;
	color: rgba(0,0,0,.65)
}

.ant-menu-horizontal>.ant-menu-item>a:hover,.ant-menu-horizontal>.ant-menu-submenu>a:hover {
	color: #108ee9
}

.ant-menu-horizontal:after {
	content: " ";
	display: block;
	height: 0;
	clear: both
}

.ant-menu-inline .ant-menu-item,.ant-menu-inline .ant-menu-submenu-title,.ant-menu-vertical .ant-menu-item,.ant-menu-vertical .ant-menu-submenu-title {
	padding: 0 16px;
	font-size: 12px;
	line-height: 42px;
	height: 42px;
	overflow: hidden;
	text-overflow: ellipsis
}

.ant-menu-inline-collapsed {
	width: 64px
}

.ant-menu-inline-collapsed>.ant-menu-item,.ant-menu-inline-collapsed>.ant-menu-item-group>.ant-menu-item-group-list>.ant-menu-item,.ant-menu-inline-collapsed>.ant-menu-submenu>.ant-menu-submenu-title {
	left: 0;
	text-overflow: clip;
	padding: 0 24px!important
}

.ant-menu-inline-collapsed>.ant-menu-item-group>.ant-menu-item-group-list>.ant-menu-item:after,.ant-menu-inline-collapsed>.ant-menu-item:after,.ant-menu-inline-collapsed>.ant-menu-submenu>.ant-menu-submenu-title:after {
	display: none
}

.ant-menu-inline-collapsed>.ant-menu-item-group>.ant-menu-item-group-list>.ant-menu-item .anticon,.ant-menu-inline-collapsed>.ant-menu-item .anticon,.ant-menu-inline-collapsed>.ant-menu-submenu>.ant-menu-submenu-title .anticon {
	font-size: 16px;
	line-height: 42px;
	margin: 0
}

.ant-menu-inline-collapsed>.ant-menu-item-group>.ant-menu-item-group-list>.ant-menu-item .anticon+span,.ant-menu-inline-collapsed>.ant-menu-item .anticon+span,.ant-menu-inline-collapsed>.ant-menu-submenu>.ant-menu-submenu-title .anticon+span {
	max-width: 0;
	display: inline-block;
	opacity: 0
}

.ant-menu-inline-collapsed-tooltip {
	pointer-events: none
}

.ant-menu-inline-collapsed-tooltip .anticon {
	display: none
}

.ant-menu-inline-collapsed-tooltip a {
	color: hsla(0,0%,100%,.91)
}

.ant-menu-inline-collapsed .ant-menu-item-group-title {
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis;
	padding-left: 4px;
	padding-right: 4px
}

.ant-menu-item-group-list .ant-menu-item,.ant-menu-item-group-list .ant-menu-submenu-title {
	padding: 0 16px 0 28px
}

.ant-menu-vertical.ant-menu-sub {
	padding: 0
}

.ant-menu-vertical.ant-menu-sub,.ant-menu-vertical.ant-menu-sub>.ant-menu-item,.ant-menu-vertical.ant-menu-sub>.ant-menu-submenu {
	-webkit-transform-origin: 0 0;
	-ms-transform-origin: 0 0;
	transform-origin: 0 0
}

.ant-menu-root.ant-menu-inline,.ant-menu-root.ant-menu-vertical {
	box-shadow: none
}

.ant-menu-sub.ant-menu-inline {
	padding: 0;
	border: 0;
	box-shadow: none;
	border-radius: 0
}

.ant-menu-sub.ant-menu-inline>.ant-menu-item,.ant-menu-sub.ant-menu-inline>.ant-menu-submenu>.ant-menu-submenu-title {
	line-height: 42px;
	height: 42px;
	list-style-type: disc;
	list-style-position: inside
}

.ant-menu-sub.ant-menu-inline .ant-menu-item-group-title {
	padding-left: 32px
}

.ant-menu-item-disabled,.ant-menu-submenu-disabled {
	color: rgba(0,0,0,.25)!important;
	cursor: not-allowed;
	background: none;
	border-color: transparent!important
}

.ant-menu-item-disabled>a,.ant-menu-submenu-disabled>a {
	color: rgba(0,0,0,.25)!important;
	pointer-events: none
}

.ant-menu-item-disabled>.ant-menu-submenu-title,.ant-menu-submenu-disabled>.ant-menu-submenu-title {
	color: rgba(0,0,0,.25)!important;
	cursor: not-allowed
}

.ant-menu-dark,.ant-menu-dark .ant-menu-sub {
	color: hsla(0,0%,100%,.67);
	background: #404040
}

.ant-menu-dark .ant-menu-inline.ant-menu-sub {
	background: #333
}

.ant-menu-dark.ant-menu-horizontal {
	border-bottom-color: #404040
}

.ant-menu-dark.ant-menu-horizontal>.ant-menu-item,.ant-menu-dark.ant-menu-horizontal>.ant-menu-submenu {
	border-color: #404040;
	border-bottom: 0
}

.ant-menu-dark .ant-menu-item,.ant-menu-dark .ant-menu-item-group-title,.ant-menu-dark .ant-menu-item>a {
	color: hsla(0,0%,100%,.67)
}

.ant-menu-dark.ant-menu-inline,.ant-menu-dark.ant-menu-vertical {
	border-right: 0
}

.ant-menu-dark.ant-menu-inline .ant-menu-item,.ant-menu-dark.ant-menu-vertical .ant-menu-item {
	border-right: 0;
	margin-left: 0;
	left: 0
}

.ant-menu-dark.ant-menu-inline .ant-menu-item:after,.ant-menu-dark.ant-menu-vertical .ant-menu-item:after {
	border-right: 0
}

.ant-menu-dark .ant-menu-item-active,.ant-menu-dark .ant-menu-item:hover,.ant-menu-dark .ant-menu-submenu-active,.ant-menu-dark .ant-menu-submenu-selected,.ant-menu-dark .ant-menu-submenu-title:hover,.ant-menu-dark:not(.ant-menu-inline) .ant-menu-submenu-open {
	background-color: transparent;
	color: #fff
}

.ant-menu-dark .ant-menu-item-active>a,.ant-menu-dark .ant-menu-item:hover>a,.ant-menu-dark .ant-menu-submenu-active>a,.ant-menu-dark .ant-menu-submenu-selected>a,.ant-menu-dark .ant-menu-submenu-title:hover>a,.ant-menu-dark:not(.ant-menu-inline) .ant-menu-submenu-open>a {
	color: #fff
}

.ant-menu-dark .ant-menu-item-selected {
	border-right: 0;
	color: #fff
}

.ant-menu-dark .ant-menu-item-selected:after {
	border-right: 0
}

.ant-menu-dark .ant-menu-item-selected>a,.ant-menu-dark .ant-menu-item-selected>a:hover {
	color: #fff
}

.ant-menu.ant-menu-dark .ant-menu-item-selected {
	background-color: #108ee9
}

.ant-menu-dark .ant-menu-item-disabled,.ant-menu-dark .ant-menu-item-disabled>a,.ant-menu-dark .ant-menu-submenu-disabled,.ant-menu-dark .ant-menu-submenu-disabled>a {
	opacity: .8;
	color: hsla(0,0%,100%,.35)!important
}

.ant-menu-dark .ant-menu-item-disabled>.ant-menu-submenu-title,.ant-menu-dark .ant-menu-submenu-disabled>.ant-menu-submenu-title {
	color: hsla(0,0%,100%,.35)!important
}

.ant-tooltip {
	position: absolute;
	z-index: 1060;
	display: block;
	visibility: visible;
	font-size: 12px;
	line-height: 1.5
}

.ant-tooltip-hidden {
	display: none
}

.ant-tooltip-placement-top,.ant-tooltip-placement-topLeft,.ant-tooltip-placement-topRight {
	padding-bottom: 8px
}

.ant-tooltip-placement-right,.ant-tooltip-placement-rightBottom,.ant-tooltip-placement-rightTop {
	padding-left: 8px
}

.ant-tooltip-placement-bottom,.ant-tooltip-placement-bottomLeft,.ant-tooltip-placement-bottomRight {
	padding-top: 8px
}

.ant-tooltip-placement-left,.ant-tooltip-placement-leftBottom,.ant-tooltip-placement-leftTop {
	padding-right: 8px
}

.ant-tooltip-inner {
	max-width: 250px;
	padding: 8px 10px;
	color: #fff;
	text-align: left;
	text-decoration: none;
	background-color: rgba(0,0,0,.75);
	border-radius: 4px;
	box-shadow: 0 1px 6px rgba(0,0,0,.2);
	min-height: 34px
}

.ant-tooltip-arrow {
	position: absolute;
	width: 0;
	height: 0;
	border-color: transparent;
	border-style: solid
}

.ant-tooltip-placement-top .ant-tooltip-arrow,.ant-tooltip-placement-topLeft .ant-tooltip-arrow,.ant-tooltip-placement-topRight .ant-tooltip-arrow {
	bottom: 3px;
	border-width: 5px 5px 0;
	border-top-color: rgba(0,0,0,.75)
}

.ant-tooltip-placement-top .ant-tooltip-arrow {
	left: 50%;
	margin-left: -5px
}

.ant-tooltip-placement-topLeft .ant-tooltip-arrow {
	left: 16px
}

.ant-tooltip-placement-topRight .ant-tooltip-arrow {
	right: 16px
}

.ant-tooltip-placement-right .ant-tooltip-arrow,.ant-tooltip-placement-rightBottom .ant-tooltip-arrow,.ant-tooltip-placement-rightTop .ant-tooltip-arrow {
	left: 3px;
	border-width: 5px 5px 5px 0;
	border-right-color: rgba(0,0,0,.75)
}

.ant-tooltip-placement-right .ant-tooltip-arrow {
	top: 50%;
	margin-top: -5px
}

.ant-tooltip-placement-rightTop .ant-tooltip-arrow {
	top: 8px
}

.ant-tooltip-placement-rightBottom .ant-tooltip-arrow {
	bottom: 8px
}

.ant-tooltip-placement-left .ant-tooltip-arrow,.ant-tooltip-placement-leftBottom .ant-tooltip-arrow,.ant-tooltip-placement-leftTop .ant-tooltip-arrow {
	right: 3px;
	border-width: 5px 0 5px 5px;
	border-left-color: rgba(0,0,0,.75)
}

.ant-tooltip-placement-left .ant-tooltip-arrow {
	top: 50%;
	margin-top: -5px
}

.ant-tooltip-placement-leftTop .ant-tooltip-arrow {
	top: 8px
}

.ant-tooltip-placement-leftBottom .ant-tooltip-arrow {
	bottom: 8px
}

.ant-tooltip-placement-bottom .ant-tooltip-arrow,.ant-tooltip-placement-bottomLeft .ant-tooltip-arrow,.ant-tooltip-placement-bottomRight .ant-tooltip-arrow {
	top: 3px;
	border-width: 0 5px 5px;
	border-bottom-color: rgba(0,0,0,.75)
}

.ant-tooltip-placement-bottom .ant-tooltip-arrow {
	left: 50%;
	margin-left: -5px
}

.ant-tooltip-placement-bottomLeft .ant-tooltip-arrow {
	left: 16px
}

.ant-tooltip-placement-bottomRight .ant-tooltip-arrow {
	right: 16px
}

.ant-layout {
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-orient: vertical;
	-webkit-box-direction: normal;
	-ms-flex-direction: column;
	flex-direction: column;
	-webkit-box-flex: 1;
	-ms-flex: auto;
	flex: auto;
	background: #ececec
}

.ant-layout.ant-layout-has-sider {
	-webkit-box-orient: horizontal;
	-webkit-box-direction: normal;
	-ms-flex-direction: row;
	flex-direction: row
}

.ant-layout.ant-layout-has-sider>.ant-layout,.ant-layout.ant-layout-has-sider>.ant-layout-content {
	overflow-x: hidden
}

.ant-layout-footer,.ant-layout-header {
	-webkit-box-flex: 0;
	-ms-flex: 0 0 auto;
	flex: 0 0 auto
}

// .ant-layout-header {
// 	background: #404040;
// 	padding: 0 50px;
// 	height: 64px;
// 	line-height: 64px
// }
// 上方空隙

.ant-layout-footer {
	padding: 24px 50px;
	color: rgba(0,0,0,.65);
	font-size: 12px
}

.ant-layout-content {
	-webkit-box-flex: 1;
	-ms-flex: auto;
	flex: auto
}

.ant-layout-sider {
	transition: all .2s;
	position: relative;
	background: #404040;
	min-width: 0
}

.ant-layout-sider-has-trigger {
	padding-bottom: 48px
}

// .ant-layout-sider-right {
// 	-webkit-box-ordinal-group: 2;
// 	-ms-flex-order: 1;
// 	order: 1
// }

// .ant-layout-sider-trigger {
// 	position: fixed;
// 	text-align: center;
// 	bottom: 0;
// 	cursor: pointer;
// 	height: 48px;
// 	line-height: 48px;
// 	color: #fff;
// 	background: #404040;
// 	z-index: 1;
// 	transition: all .15s cubic-bezier(.645,.045,.355,1)
// }

.ant-layout-sider-zero-width>* {
	overflow: hidden
}

.ant-layout-sider-zero-width-trigger {
	position: absolute;
	top: 64px;
	right: -36px;
	text-align: center;
	width: 36px;
	height: 42px;
	line-height: 42px;
	background: #404040;
	color: #fff;
	font-size: 18px;
	border-radius: 0 4px 4px 0;
	cursor: pointer;
	transition: background .3s ease
}

.ant-layout-sider-zero-width-trigger:hover {
	background: #535353
}

.ant-row {
	position: relative;
	margin-left: 0;
	margin-right: 0;
	height: auto;
	zoom: 1;
	display: block
}

.ant-row:after,.ant-row:before {
	content: " ";
	display: table
}

.ant-row:after {
	clear: both;
	visibility: hidden;
	font-size: 0;
	height: 0
}

.ant-row-flex {
	-webkit-box-orient: horizontal;
	-webkit-box-direction: normal;
	-ms-flex-flow: row wrap;
	flex-flow: row wrap
}

.ant-row-flex,.ant-row-flex:after,.ant-row-flex:before {
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex
}

.ant-row-flex-start {
	-webkit-box-pack: start;
	-ms-flex-pack: start;
	justify-content: flex-start
}

.ant-row-flex-center {
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center
}

.ant-row-flex-end {
	-webkit-box-pack: end;
	-ms-flex-pack: end;
	justify-content: flex-end
}

.ant-row-flex-space-between {
	-webkit-box-pack: justify;
	-ms-flex-pack: justify;
	justify-content: space-between
}

.ant-row-flex-space-around {
	-ms-flex-pack: distribute;
	justify-content: space-around
}

.ant-row-flex-top {
	-webkit-box-align: start;
	-ms-flex-align: start;
	align-items: flex-start
}

.ant-row-flex-middle {
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center
}

.ant-row-flex-bottom {
	-webkit-box-align: end;
	-ms-flex-align: end;
	align-items: flex-end
}

.ant-col {
	position: relative;
	display: block
}

.ant-col-1,.ant-col-2,.ant-col-3,.ant-col-4,.ant-col-5,.ant-col-6,.ant-col-7,.ant-col-8,.ant-col-9,.ant-col-10,.ant-col-11,.ant-col-12,.ant-col-13,.ant-col-14,.ant-col-15,.ant-col-16,.ant-col-17,.ant-col-18,.ant-col-19,.ant-col-20,.ant-col-21,.ant-col-22,.ant-col-23,.ant-col-24,.ant-col-lg-1,.ant-col-lg-2,.ant-col-lg-3,.ant-col-lg-4,.ant-col-lg-5,.ant-col-lg-6,.ant-col-lg-7,.ant-col-lg-8,.ant-col-lg-9,.ant-col-lg-10,.ant-col-lg-11,.ant-col-lg-12,.ant-col-lg-13,.ant-col-lg-14,.ant-col-lg-15,.ant-col-lg-16,.ant-col-lg-17,.ant-col-lg-18,.ant-col-lg-19,.ant-col-lg-20,.ant-col-lg-21,.ant-col-lg-22,.ant-col-lg-23,.ant-col-lg-24,.ant-col-md-1,.ant-col-md-2,.ant-col-md-3,.ant-col-md-4,.ant-col-md-5,.ant-col-md-6,.ant-col-md-7,.ant-col-md-8,.ant-col-md-9,.ant-col-md-10,.ant-col-md-11,.ant-col-md-12,.ant-col-md-13,.ant-col-md-14,.ant-col-md-15,.ant-col-md-16,.ant-col-md-17,.ant-col-md-18,.ant-col-md-19,.ant-col-md-20,.ant-col-md-21,.ant-col-md-22,.ant-col-md-23,.ant-col-md-24,.ant-col-sm-1,.ant-col-sm-2,.ant-col-sm-3,.ant-col-sm-4,.ant-col-sm-5,.ant-col-sm-6,.ant-col-sm-7,.ant-col-sm-8,.ant-col-sm-9,.ant-col-sm-10,.ant-col-sm-11,.ant-col-sm-12,.ant-col-sm-13,.ant-col-sm-14,.ant-col-sm-15,.ant-col-sm-16,.ant-col-sm-17,.ant-col-sm-18,.ant-col-sm-19,.ant-col-sm-20,.ant-col-sm-21,.ant-col-sm-22,.ant-col-sm-23,.ant-col-sm-24,.ant-col-xs-1,.ant-col-xs-2,.ant-col-xs-3,.ant-col-xs-4,.ant-col-xs-5,.ant-col-xs-6,.ant-col-xs-7,.ant-col-xs-8,.ant-col-xs-9,.ant-col-xs-10,.ant-col-xs-11,.ant-col-xs-12,.ant-col-xs-13,.ant-col-xs-14,.ant-col-xs-15,.ant-col-xs-16,.ant-col-xs-17,.ant-col-xs-18,.ant-col-xs-19,.ant-col-xs-20,.ant-col-xs-21,.ant-col-xs-22,.ant-col-xs-23,.ant-col-xs-24 {
	position: relative;
	min-height: 1px;
	padding-left: 0;
	padding-right: 0
}

.ant-col-1,.ant-col-2,.ant-col-3,.ant-col-4,.ant-col-5,.ant-col-6,.ant-col-7,.ant-col-8,.ant-col-9,.ant-col-10,.ant-col-11,.ant-col-12,.ant-col-13,.ant-col-14,.ant-col-15,.ant-col-16,.ant-col-17,.ant-col-18,.ant-col-19,.ant-col-20,.ant-col-21,.ant-col-22,.ant-col-23,.ant-col-24 {
	float: left;
	-webkit-box-flex: 0;
	-ms-flex: 0 0 auto;
	flex: 0 0 auto
}

.ant-col-24 {
	display: block;
	width: 100%
}

.ant-col-push-24 {
	left: 100%
}

.ant-col-pull-24 {
	right: 100%
}

.ant-col-offset-24 {
	margin-left: 100%
}

.ant-col-order-24 {
	-webkit-box-ordinal-group: 25;
	-ms-flex-order: 24;
	order: 24
}

.ant-col-23 {
	display: block;
	width: 95.83333333%
}

.ant-col-push-23 {
	left: 95.83333333%
}

.ant-col-pull-23 {
	right: 95.83333333%
}

.ant-col-offset-23 {
	margin-left: 95.83333333%
}

.ant-col-order-23 {
	-webkit-box-ordinal-group: 24;
	-ms-flex-order: 23;
	order: 23
}

.ant-col-22 {
	display: block;
	width: 91.66666667%
}

.ant-col-push-22 {
	left: 91.66666667%
}

.ant-col-pull-22 {
	right: 91.66666667%
}

.ant-col-offset-22 {
	margin-left: 91.66666667%
}

.ant-col-order-22 {
	-webkit-box-ordinal-group: 23;
	-ms-flex-order: 22;
	order: 22
}

.ant-col-21 {
	display: block;
	width: 87.5%
}

.ant-col-push-21 {
	left: 87.5%
}

.ant-col-pull-21 {
	right: 87.5%
}

.ant-col-offset-21 {
	margin-left: 87.5%
}

.ant-col-order-21 {
	-webkit-box-ordinal-group: 22;
	-ms-flex-order: 21;
	order: 21
}

.ant-col-20 {
	display: block;
	width: 83.33333333%
}

.ant-col-push-20 {
	left: 83.33333333%
}

.ant-col-pull-20 {
	right: 83.33333333%
}

.ant-col-offset-20 {
	margin-left: 83.33333333%
}

.ant-col-order-20 {
	-webkit-box-ordinal-group: 21;
	-ms-flex-order: 20;
	order: 20
}

.ant-col-19 {
	display: block;
	width: 79.16666667%
}

.ant-col-push-19 {
	left: 79.16666667%
}

.ant-col-pull-19 {
	right: 79.16666667%
}

.ant-col-offset-19 {
	margin-left: 79.16666667%
}

.ant-col-order-19 {
	-webkit-box-ordinal-group: 20;
	-ms-flex-order: 19;
	order: 19
}

.ant-col-18 {
	display: block;
	width: 75%
}

.ant-col-push-18 {
	left: 75%
}

.ant-col-pull-18 {
	right: 75%
}

.ant-col-offset-18 {
	margin-left: 75%
}

.ant-col-order-18 {
	-webkit-box-ordinal-group: 19;
	-ms-flex-order: 18;
	order: 18
}

.ant-col-17 {
	display: block;
	width: 70.83333333%
}

.ant-col-push-17 {
	left: 70.83333333%
}

.ant-col-pull-17 {
	right: 70.83333333%
}

.ant-col-offset-17 {
	margin-left: 70.83333333%
}

.ant-col-order-17 {
	-webkit-box-ordinal-group: 18;
	-ms-flex-order: 17;
	order: 17
}

.ant-col-16 {
	display: block;
	width: 66.66666667%
}

.ant-col-push-16 {
	left: 66.66666667%
}

.ant-col-pull-16 {
	right: 66.66666667%
}

.ant-col-offset-16 {
	margin-left: 66.66666667%
}

.ant-col-order-16 {
	-webkit-box-ordinal-group: 17;
	-ms-flex-order: 16;
	order: 16
}

.ant-col-15 {
	display: block;
	width: 62.5%
}

.ant-col-push-15 {
	left: 62.5%
}

.ant-col-pull-15 {
	right: 62.5%
}

.ant-col-offset-15 {
	margin-left: 62.5%
}

.ant-col-order-15 {
	-webkit-box-ordinal-group: 16;
	-ms-flex-order: 15;
	order: 15
}

.ant-col-14 {
	display: block;
	width: 58.33333333%
}

.ant-col-push-14 {
	left: 58.33333333%
}

.ant-col-pull-14 {
	right: 58.33333333%
}

.ant-col-offset-14 {
	margin-left: 58.33333333%
}

.ant-col-order-14 {
	-webkit-box-ordinal-group: 15;
	-ms-flex-order: 14;
	order: 14
}

.ant-col-13 {
	display: block;
	width: 54.16666667%
}

.ant-col-push-13 {
	left: 54.16666667%
}

.ant-col-pull-13 {
	right: 54.16666667%
}

.ant-col-offset-13 {
	margin-left: 54.16666667%
}

.ant-col-order-13 {
	-webkit-box-ordinal-group: 14;
	-ms-flex-order: 13;
	order: 13
}

.ant-col-12 {
	display: block;
	width: 50%
}

.ant-col-push-12 {
	left: 50%
}

.ant-col-pull-12 {
	right: 50%
}

.ant-col-offset-12 {
	margin-left: 50%
}

.ant-col-order-12 {
	-webkit-box-ordinal-group: 13;
	-ms-flex-order: 12;
	order: 12
}

.ant-col-11 {
	display: block;
	width: 45.83333333%
}

.ant-col-push-11 {
	left: 45.83333333%
}

.ant-col-pull-11 {
	right: 45.83333333%
}

.ant-col-offset-11 {
	margin-left: 45.83333333%
}

.ant-col-order-11 {
	-webkit-box-ordinal-group: 12;
	-ms-flex-order: 11;
	order: 11
}

.ant-col-10 {
	display: block;
	width: 41.66666667%
}

.ant-col-push-10 {
	left: 41.66666667%
}

.ant-col-pull-10 {
	right: 41.66666667%
}

.ant-col-offset-10 {
	margin-left: 41.66666667%
}

.ant-col-order-10 {
	-webkit-box-ordinal-group: 11;
	-ms-flex-order: 10;
	order: 10
}

.ant-col-9 {
	display: block;
	width: 37.5%
}

.ant-col-push-9 {
	left: 37.5%
}

.ant-col-pull-9 {
	right: 37.5%
}

.ant-col-offset-9 {
	margin-left: 37.5%
}

.ant-col-order-9 {
	-webkit-box-ordinal-group: 10;
	-ms-flex-order: 9;
	order: 9
}

.ant-col-8 {
	display: block;
	width: 33.33333333%
}

.ant-col-push-8 {
	left: 33.33333333%
}

.ant-col-pull-8 {
	right: 33.33333333%
}

.ant-col-offset-8 {
	margin-left: 33.33333333%
}

.ant-col-order-8 {
	-webkit-box-ordinal-group: 9;
	-ms-flex-order: 8;
	order: 8
}

.ant-col-7 {
	display: block;
	width: 29.16666667%
}

.ant-col-push-7 {
	left: 29.16666667%
}

.ant-col-pull-7 {
	right: 29.16666667%
}

.ant-col-offset-7 {
	margin-left: 29.16666667%
}

.ant-col-order-7 {
	-webkit-box-ordinal-group: 8;
	-ms-flex-order: 7;
	order: 7
}

.ant-col-6 {
	display: block;
	width: 25%
}

.ant-col-push-6 {
	left: 25%
}

.ant-col-pull-6 {
	right: 25%
}

.ant-col-offset-6 {
	margin-left: 25%
}

.ant-col-order-6 {
	-webkit-box-ordinal-group: 7;
	-ms-flex-order: 6;
	order: 6
}

.ant-col-5 {
	display: block;
	width: 20.83333333%
}

.ant-col-push-5 {
	left: 20.83333333%
}

.ant-col-pull-5 {
	right: 20.83333333%
}

.ant-col-offset-5 {
	margin-left: 20.83333333%
}

.ant-col-order-5 {
	-webkit-box-ordinal-group: 6;
	-ms-flex-order: 5;
	order: 5
}

.ant-col-4 {
	display: block;
	width: 16.66666667%
}

.ant-col-push-4 {
	left: 16.66666667%
}

.ant-col-pull-4 {
	right: 16.66666667%
}

.ant-col-offset-4 {
	margin-left: 16.66666667%
}

.ant-col-order-4 {
	-webkit-box-ordinal-group: 5;
	-ms-flex-order: 4;
	order: 4
}

.ant-col-3 {
	display: block;
	width: 12.5%
}

.ant-col-push-3 {
	left: 12.5%
}

.ant-col-pull-3 {
	right: 12.5%
}

.ant-col-offset-3 {
	margin-left: 12.5%
}

.ant-col-order-3 {
	-webkit-box-ordinal-group: 4;
	-ms-flex-order: 3;
	order: 3
}

.ant-col-2 {
	display: block;
	width: 8.33333333%
}

.ant-col-push-2 {
	left: 8.33333333%
}

.ant-col-pull-2 {
	right: 8.33333333%
}

.ant-col-offset-2 {
	margin-left: 8.33333333%
}

.ant-col-order-2 {
	-webkit-box-ordinal-group: 3;
	-ms-flex-order: 2;
	order: 2
}

.ant-col-1 {
	display: block;
	width: 4.16666667%
}

.ant-col-push-1 {
	left: 4.16666667%
}

.ant-col-pull-1 {
	right: 4.16666667%
}

.ant-col-offset-1 {
	margin-left: 4.16666667%
}

.ant-col-order-1 {
	-webkit-box-ordinal-group: 2;
	-ms-flex-order: 1;
	order: 1
}

.ant-col-0 {
	display: none
}

.ant-col-offset-0 {
	margin-left: 0
}

.ant-col-order-0 {
	-webkit-box-ordinal-group: 1;
	-ms-flex-order: 0;
	order: 0
}

.ant-col-xs-1,.ant-col-xs-2,.ant-col-xs-3,.ant-col-xs-4,.ant-col-xs-5,.ant-col-xs-6,.ant-col-xs-7,.ant-col-xs-8,.ant-col-xs-9,.ant-col-xs-10,.ant-col-xs-11,.ant-col-xs-12,.ant-col-xs-13,.ant-col-xs-14,.ant-col-xs-15,.ant-col-xs-16,.ant-col-xs-17,.ant-col-xs-18,.ant-col-xs-19,.ant-col-xs-20,.ant-col-xs-21,.ant-col-xs-22,.ant-col-xs-23,.ant-col-xs-24 {
	float: left;
	-webkit-box-flex: 0;
	-ms-flex: 0 0 auto;
	flex: 0 0 auto
}

.ant-col-xs-24 {
	display: block;
	width: 100%
}

.ant-col-xs-push-24 {
	left: 100%
}

.ant-col-xs-pull-24 {
	right: 100%
}

.ant-col-xs-offset-24 {
	margin-left: 100%
}

.ant-col-xs-order-24 {
	-webkit-box-ordinal-group: 25;
	-ms-flex-order: 24;
	order: 24
}

.ant-col-xs-23 {
	display: block;
	width: 95.83333333%
}

.ant-col-xs-push-23 {
	left: 95.83333333%
}

.ant-col-xs-pull-23 {
	right: 95.83333333%
}

.ant-col-xs-offset-23 {
	margin-left: 95.83333333%
}

.ant-col-xs-order-23 {
	-webkit-box-ordinal-group: 24;
	-ms-flex-order: 23;
	order: 23
}

.ant-col-xs-22 {
	display: block;
	width: 91.66666667%
}

.ant-col-xs-push-22 {
	left: 91.66666667%
}

.ant-col-xs-pull-22 {
	right: 91.66666667%
}

.ant-col-xs-offset-22 {
	margin-left: 91.66666667%
}

.ant-col-xs-order-22 {
	-webkit-box-ordinal-group: 23;
	-ms-flex-order: 22;
	order: 22
}

.ant-col-xs-21 {
	display: block;
	width: 87.5%
}

.ant-col-xs-push-21 {
	left: 87.5%
}

.ant-col-xs-pull-21 {
	right: 87.5%
}

.ant-col-xs-offset-21 {
	margin-left: 87.5%
}

.ant-col-xs-order-21 {
	-webkit-box-ordinal-group: 22;
	-ms-flex-order: 21;
	order: 21
}

.ant-col-xs-20 {
	display: block;
	width: 83.33333333%
}

.ant-col-xs-push-20 {
	left: 83.33333333%
}

.ant-col-xs-pull-20 {
	right: 83.33333333%
}

.ant-col-xs-offset-20 {
	margin-left: 83.33333333%
}

.ant-col-xs-order-20 {
	-webkit-box-ordinal-group: 21;
	-ms-flex-order: 20;
	order: 20
}

.ant-col-xs-19 {
	display: block;
	width: 79.16666667%
}

.ant-col-xs-push-19 {
	left: 79.16666667%
}

.ant-col-xs-pull-19 {
	right: 79.16666667%
}

.ant-col-xs-offset-19 {
	margin-left: 79.16666667%
}

.ant-col-xs-order-19 {
	-webkit-box-ordinal-group: 20;
	-ms-flex-order: 19;
	order: 19
}

.ant-col-xs-18 {
	display: block;
	width: 75%
}

.ant-col-xs-push-18 {
	left: 75%
}

.ant-col-xs-pull-18 {
	right: 75%
}

.ant-col-xs-offset-18 {
	margin-left: 75%
}

.ant-col-xs-order-18 {
	-webkit-box-ordinal-group: 19;
	-ms-flex-order: 18;
	order: 18
}

.ant-col-xs-17 {
	display: block;
	width: 70.83333333%
}

.ant-col-xs-push-17 {
	left: 70.83333333%
}

.ant-col-xs-pull-17 {
	right: 70.83333333%
}

.ant-col-xs-offset-17 {
	margin-left: 70.83333333%
}

.ant-col-xs-order-17 {
	-webkit-box-ordinal-group: 18;
	-ms-flex-order: 17;
	order: 17
}

.ant-col-xs-16 {
	display: block;
	width: 66.66666667%
}

.ant-col-xs-push-16 {
	left: 66.66666667%
}

.ant-col-xs-pull-16 {
	right: 66.66666667%
}

.ant-col-xs-offset-16 {
	margin-left: 66.66666667%
}

.ant-col-xs-order-16 {
	-webkit-box-ordinal-group: 17;
	-ms-flex-order: 16;
	order: 16
}

.ant-col-xs-15 {
	display: block;
	width: 62.5%
}

.ant-col-xs-push-15 {
	left: 62.5%
}

.ant-col-xs-pull-15 {
	right: 62.5%
}

.ant-col-xs-offset-15 {
	margin-left: 62.5%
}

.ant-col-xs-order-15 {
	-webkit-box-ordinal-group: 16;
	-ms-flex-order: 15;
	order: 15
}

.ant-col-xs-14 {
	display: block;
	width: 58.33333333%
}

.ant-col-xs-push-14 {
	left: 58.33333333%
}

.ant-col-xs-pull-14 {
	right: 58.33333333%
}

.ant-col-xs-offset-14 {
	margin-left: 58.33333333%
}

.ant-col-xs-order-14 {
	-webkit-box-ordinal-group: 15;
	-ms-flex-order: 14;
	order: 14
}

.ant-col-xs-13 {
	display: block;
	width: 54.16666667%
}

.ant-col-xs-push-13 {
	left: 54.16666667%
}

.ant-col-xs-pull-13 {
	right: 54.16666667%
}

.ant-col-xs-offset-13 {
	margin-left: 54.16666667%
}

.ant-col-xs-order-13 {
	-webkit-box-ordinal-group: 14;
	-ms-flex-order: 13;
	order: 13
}

.ant-col-xs-12 {
	display: block;
	width: 50%
}

.ant-col-xs-push-12 {
	left: 50%
}

.ant-col-xs-pull-12 {
	right: 50%
}

.ant-col-xs-offset-12 {
	margin-left: 50%
}

.ant-col-xs-order-12 {
	-webkit-box-ordinal-group: 13;
	-ms-flex-order: 12;
	order: 12
}

.ant-col-xs-11 {
	display: block;
	width: 45.83333333%
}

.ant-col-xs-push-11 {
	left: 45.83333333%
}

.ant-col-xs-pull-11 {
	right: 45.83333333%
}

.ant-col-xs-offset-11 {
	margin-left: 45.83333333%
}

.ant-col-xs-order-11 {
	-webkit-box-ordinal-group: 12;
	-ms-flex-order: 11;
	order: 11
}

.ant-col-xs-10 {
	display: block;
	width: 41.66666667%
}

.ant-col-xs-push-10 {
	left: 41.66666667%
}

.ant-col-xs-pull-10 {
	right: 41.66666667%
}

.ant-col-xs-offset-10 {
	margin-left: 41.66666667%
}

.ant-col-xs-order-10 {
	-webkit-box-ordinal-group: 11;
	-ms-flex-order: 10;
	order: 10
}

.ant-col-xs-9 {
	display: block;
	width: 37.5%
}

.ant-col-xs-push-9 {
	left: 37.5%
}

.ant-col-xs-pull-9 {
	right: 37.5%
}

.ant-col-xs-offset-9 {
	margin-left: 37.5%
}

.ant-col-xs-order-9 {
	-webkit-box-ordinal-group: 10;
	-ms-flex-order: 9;
	order: 9
}

.ant-col-xs-8 {
	display: block;
	width: 33.33333333%
}

.ant-col-xs-push-8 {
	left: 33.33333333%
}

.ant-col-xs-pull-8 {
	right: 33.33333333%
}

.ant-col-xs-offset-8 {
	margin-left: 33.33333333%
}

.ant-col-xs-order-8 {
	-webkit-box-ordinal-group: 9;
	-ms-flex-order: 8;
	order: 8
}

.ant-col-xs-7 {
	display: block;
	width: 29.16666667%
}

.ant-col-xs-push-7 {
	left: 29.16666667%
}

.ant-col-xs-pull-7 {
	right: 29.16666667%
}

.ant-col-xs-offset-7 {
	margin-left: 29.16666667%
}

.ant-col-xs-order-7 {
	-webkit-box-ordinal-group: 8;
	-ms-flex-order: 7;
	order: 7
}

.ant-col-xs-6 {
	display: block;
	width: 25%
}

.ant-col-xs-push-6 {
	left: 25%
}

.ant-col-xs-pull-6 {
	right: 25%
}

.ant-col-xs-offset-6 {
	margin-left: 25%
}

.ant-col-xs-order-6 {
	-webkit-box-ordinal-group: 7;
	-ms-flex-order: 6;
	order: 6
}

.ant-col-xs-5 {
	display: block;
	width: 20.83333333%
}

.ant-col-xs-push-5 {
	left: 20.83333333%
}

.ant-col-xs-pull-5 {
	right: 20.83333333%
}

.ant-col-xs-offset-5 {
	margin-left: 20.83333333%
}

.ant-col-xs-order-5 {
	-webkit-box-ordinal-group: 6;
	-ms-flex-order: 5;
	order: 5
}

.ant-col-xs-4 {
	display: block;
	width: 16.66666667%
}

.ant-col-xs-push-4 {
	left: 16.66666667%
}

.ant-col-xs-pull-4 {
	right: 16.66666667%
}

.ant-col-xs-offset-4 {
	margin-left: 16.66666667%
}

.ant-col-xs-order-4 {
	-webkit-box-ordinal-group: 5;
	-ms-flex-order: 4;
	order: 4
}

.ant-col-xs-3 {
	display: block;
	width: 12.5%
}

.ant-col-xs-push-3 {
	left: 12.5%
}

.ant-col-xs-pull-3 {
	right: 12.5%
}

.ant-col-xs-offset-3 {
	margin-left: 12.5%
}

.ant-col-xs-order-3 {
	-webkit-box-ordinal-group: 4;
	-ms-flex-order: 3;
	order: 3
}

.ant-col-xs-2 {
	display: block;
	width: 8.33333333%
}

.ant-col-xs-push-2 {
	left: 8.33333333%
}

.ant-col-xs-pull-2 {
	right: 8.33333333%
}

.ant-col-xs-offset-2 {
	margin-left: 8.33333333%
}

.ant-col-xs-order-2 {
	-webkit-box-ordinal-group: 3;
	-ms-flex-order: 2;
	order: 2
}

.ant-col-xs-1 {
	display: block;
	width: 4.16666667%
}

.ant-col-xs-push-1 {
	left: 4.16666667%
}

.ant-col-xs-pull-1 {
	right: 4.16666667%
}

.ant-col-xs-offset-1 {
	margin-left: 4.16666667%
}

.ant-col-xs-order-1 {
	-webkit-box-ordinal-group: 2;
	-ms-flex-order: 1;
	order: 1
}

.ant-col-xs-0 {
	display: none
}

.ant-col-push-0 {
	left: auto
}

.ant-col-pull-0 {
	right: auto
}

.ant-col-xs-push-0 {
	left: auto
}

.ant-col-xs-pull-0 {
	right: auto
}

.ant-col-xs-offset-0 {
	margin-left: 0
}

.ant-col-xs-order-0 {
	-webkit-box-ordinal-group: 1;
	-ms-flex-order: 0;
	order: 0
}

@media (min-width:768px) {
	.ant-col-sm-1,.ant-col-sm-2,.ant-col-sm-3,.ant-col-sm-4,.ant-col-sm-5,.ant-col-sm-6,.ant-col-sm-7,.ant-col-sm-8,.ant-col-sm-9,.ant-col-sm-10,.ant-col-sm-11,.ant-col-sm-12,.ant-col-sm-13,.ant-col-sm-14,.ant-col-sm-15,.ant-col-sm-16,.ant-col-sm-17,.ant-col-sm-18,.ant-col-sm-19,.ant-col-sm-20,.ant-col-sm-21,.ant-col-sm-22,.ant-col-sm-23,.ant-col-sm-24 {
		float: left;
		-webkit-box-flex: 0;
		-ms-flex: 0 0 auto;
		flex: 0 0 auto
	}

	.ant-col-sm-24 {
		display: block;
		width: 100%
	}

	.ant-col-sm-push-24 {
		left: 100%
	}

	.ant-col-sm-pull-24 {
		right: 100%
	}

	.ant-col-sm-offset-24 {
		margin-left: 100%
	}

	.ant-col-sm-order-24 {
		-webkit-box-ordinal-group: 25;
		-ms-flex-order: 24;
		order: 24
	}

	.ant-col-sm-23 {
		display: block;
		width: 95.83333333%
	}

	.ant-col-sm-push-23 {
		left: 95.83333333%
	}

	.ant-col-sm-pull-23 {
		right: 95.83333333%
	}

	.ant-col-sm-offset-23 {
		margin-left: 95.83333333%
	}

	.ant-col-sm-order-23 {
		-webkit-box-ordinal-group: 24;
		-ms-flex-order: 23;
		order: 23
	}

	.ant-col-sm-22 {
		display: block;
		width: 91.66666667%
	}

	.ant-col-sm-push-22 {
		left: 91.66666667%
	}

	.ant-col-sm-pull-22 {
		right: 91.66666667%
	}

	.ant-col-sm-offset-22 {
		margin-left: 91.66666667%
	}

	.ant-col-sm-order-22 {
		-webkit-box-ordinal-group: 23;
		-ms-flex-order: 22;
		order: 22
	}

	.ant-col-sm-21 {
		display: block;
		width: 87.5%
	}

	.ant-col-sm-push-21 {
		left: 87.5%
	}

	.ant-col-sm-pull-21 {
		right: 87.5%
	}

	.ant-col-sm-offset-21 {
		margin-left: 87.5%
	}

	.ant-col-sm-order-21 {
		-webkit-box-ordinal-group: 22;
		-ms-flex-order: 21;
		order: 21
	}

	.ant-col-sm-20 {
		display: block;
		width: 83.33333333%
	}

	.ant-col-sm-push-20 {
		left: 83.33333333%
	}

	.ant-col-sm-pull-20 {
		right: 83.33333333%
	}

	.ant-col-sm-offset-20 {
		margin-left: 83.33333333%
	}

	.ant-col-sm-order-20 {
		-webkit-box-ordinal-group: 21;
		-ms-flex-order: 20;
		order: 20
	}

	.ant-col-sm-19 {
		display: block;
		width: 79.16666667%
	}

	.ant-col-sm-push-19 {
		left: 79.16666667%
	}

	.ant-col-sm-pull-19 {
		right: 79.16666667%
	}

	.ant-col-sm-offset-19 {
		margin-left: 79.16666667%
	}

	.ant-col-sm-order-19 {
		-webkit-box-ordinal-group: 20;
		-ms-flex-order: 19;
		order: 19
	}

	.ant-col-sm-18 {
		display: block;
		width: 75%
	}

	.ant-col-sm-push-18 {
		left: 75%
	}

	.ant-col-sm-pull-18 {
		right: 75%
	}

	.ant-col-sm-offset-18 {
		margin-left: 75%
	}

	.ant-col-sm-order-18 {
		-webkit-box-ordinal-group: 19;
		-ms-flex-order: 18;
		order: 18
	}

	.ant-col-sm-17 {
		display: block;
		width: 70.83333333%
	}

	.ant-col-sm-push-17 {
		left: 70.83333333%
	}

	.ant-col-sm-pull-17 {
		right: 70.83333333%
	}

	.ant-col-sm-offset-17 {
		margin-left: 70.83333333%
	}

	.ant-col-sm-order-17 {
		-webkit-box-ordinal-group: 18;
		-ms-flex-order: 17;
		order: 17
	}

	.ant-col-sm-16 {
		display: block;
		width: 66.66666667%
	}

	.ant-col-sm-push-16 {
		left: 66.66666667%
	}

	.ant-col-sm-pull-16 {
		right: 66.66666667%
	}

	.ant-col-sm-offset-16 {
		margin-left: 66.66666667%
	}

	.ant-col-sm-order-16 {
		-webkit-box-ordinal-group: 17;
		-ms-flex-order: 16;
		order: 16
	}

	.ant-col-sm-15 {
		display: block;
		width: 62.5%
	}

	.ant-col-sm-push-15 {
		left: 62.5%
	}

	.ant-col-sm-pull-15 {
		right: 62.5%
	}

	.ant-col-sm-offset-15 {
		margin-left: 62.5%
	}

	.ant-col-sm-order-15 {
		-webkit-box-ordinal-group: 16;
		-ms-flex-order: 15;
		order: 15
	}

	.ant-col-sm-14 {
		display: block;
		width: 58.33333333%
	}

	.ant-col-sm-push-14 {
		left: 58.33333333%
	}

	.ant-col-sm-pull-14 {
		right: 58.33333333%
	}

	.ant-col-sm-offset-14 {
		margin-left: 58.33333333%
	}

	.ant-col-sm-order-14 {
		-webkit-box-ordinal-group: 15;
		-ms-flex-order: 14;
		order: 14
	}

	.ant-col-sm-13 {
		display: block;
		width: 54.16666667%
	}

	.ant-col-sm-push-13 {
		left: 54.16666667%
	}

	.ant-col-sm-pull-13 {
		right: 54.16666667%
	}

	.ant-col-sm-offset-13 {
		margin-left: 54.16666667%
	}

	.ant-col-sm-order-13 {
		-webkit-box-ordinal-group: 14;
		-ms-flex-order: 13;
		order: 13
	}

	.ant-col-sm-12 {
		display: block;
		width: 50%
	}

	.ant-col-sm-push-12 {
		left: 50%
	}

	.ant-col-sm-pull-12 {
		right: 50%
	}

	.ant-col-sm-offset-12 {
		margin-left: 50%
	}

	.ant-col-sm-order-12 {
		-webkit-box-ordinal-group: 13;
		-ms-flex-order: 12;
		order: 12
	}

	.ant-col-sm-11 {
		display: block;
		width: 45.83333333%
	}

	.ant-col-sm-push-11 {
		left: 45.83333333%
	}

	.ant-col-sm-pull-11 {
		right: 45.83333333%
	}

	.ant-col-sm-offset-11 {
		margin-left: 45.83333333%
	}

	.ant-col-sm-order-11 {
		-webkit-box-ordinal-group: 12;
		-ms-flex-order: 11;
		order: 11
	}

	.ant-col-sm-10 {
		display: block;
		width: 41.66666667%
	}

	.ant-col-sm-push-10 {
		left: 41.66666667%
	}

	.ant-col-sm-pull-10 {
		right: 41.66666667%
	}

	.ant-col-sm-offset-10 {
		margin-left: 41.66666667%
	}

	.ant-col-sm-order-10 {
		-webkit-box-ordinal-group: 11;
		-ms-flex-order: 10;
		order: 10
	}

	.ant-col-sm-9 {
		display: block;
		width: 37.5%
	}

	.ant-col-sm-push-9 {
		left: 37.5%
	}

	.ant-col-sm-pull-9 {
		right: 37.5%
	}

	.ant-col-sm-offset-9 {
		margin-left: 37.5%
	}

	.ant-col-sm-order-9 {
		-webkit-box-ordinal-group: 10;
		-ms-flex-order: 9;
		order: 9
	}

	.ant-col-sm-8 {
		display: block;
		width: 33.33333333%
	}

	.ant-col-sm-push-8 {
		left: 33.33333333%
	}

	.ant-col-sm-pull-8 {
		right: 33.33333333%
	}

	.ant-col-sm-offset-8 {
		margin-left: 33.33333333%
	}

	.ant-col-sm-order-8 {
		-webkit-box-ordinal-group: 9;
		-ms-flex-order: 8;
		order: 8
	}

	.ant-col-sm-7 {
		display: block;
		width: 29.16666667%
	}

	.ant-col-sm-push-7 {
		left: 29.16666667%
	}

	.ant-col-sm-pull-7 {
		right: 29.16666667%
	}

	.ant-col-sm-offset-7 {
		margin-left: 29.16666667%
	}

	.ant-col-sm-order-7 {
		-webkit-box-ordinal-group: 8;
		-ms-flex-order: 7;
		order: 7
	}

	.ant-col-sm-6 {
		display: block;
		width: 25%
	}

	.ant-col-sm-push-6 {
		left: 25%
	}

	.ant-col-sm-pull-6 {
		right: 25%
	}

	.ant-col-sm-offset-6 {
		margin-left: 25%
	}

	.ant-col-sm-order-6 {
		-webkit-box-ordinal-group: 7;
		-ms-flex-order: 6;
		order: 6
	}

	.ant-col-sm-5 {
		display: block;
		width: 20.83333333%
	}

	.ant-col-sm-push-5 {
		left: 20.83333333%
	}

	.ant-col-sm-pull-5 {
		right: 20.83333333%
	}

	.ant-col-sm-offset-5 {
		margin-left: 20.83333333%
	}

	.ant-col-sm-order-5 {
		-webkit-box-ordinal-group: 6;
		-ms-flex-order: 5;
		order: 5
	}

	.ant-col-sm-4 {
		display: block;
		width: 16.66666667%
	}

	.ant-col-sm-push-4 {
		left: 16.66666667%
	}

	.ant-col-sm-pull-4 {
		right: 16.66666667%
	}

	.ant-col-sm-offset-4 {
		margin-left: 16.66666667%
	}

	.ant-col-sm-order-4 {
		-webkit-box-ordinal-group: 5;
		-ms-flex-order: 4;
		order: 4
	}

	.ant-col-sm-3 {
		display: block;
		width: 12.5%
	}

	.ant-col-sm-push-3 {
		left: 12.5%
	}

	.ant-col-sm-pull-3 {
		right: 12.5%
	}

	.ant-col-sm-offset-3 {
		margin-left: 12.5%
	}

	.ant-col-sm-order-3 {
		-webkit-box-ordinal-group: 4;
		-ms-flex-order: 3;
		order: 3
	}

	.ant-col-sm-2 {
		display: block;
		width: 8.33333333%
	}

	.ant-col-sm-push-2 {
		left: 8.33333333%
	}

	.ant-col-sm-pull-2 {
		right: 8.33333333%
	}

	.ant-col-sm-offset-2 {
		margin-left: 8.33333333%
	}

	.ant-col-sm-order-2 {
		-webkit-box-ordinal-group: 3;
		-ms-flex-order: 2;
		order: 2
	}

	.ant-col-sm-1 {
		display: block;
		width: 4.16666667%
	}

	.ant-col-sm-push-1 {
		left: 4.16666667%
	}

	.ant-col-sm-pull-1 {
		right: 4.16666667%
	}

	.ant-col-sm-offset-1 {
		margin-left: 4.16666667%
	}

	.ant-col-sm-order-1 {
		-webkit-box-ordinal-group: 2;
		-ms-flex-order: 1;
		order: 1
	}

	.ant-col-sm-0 {
		display: none
	}

	.ant-col-push-0 {
		left: auto
	}

	.ant-col-pull-0 {
		right: auto
	}

	.ant-col-sm-push-0 {
		left: auto
	}

	.ant-col-sm-pull-0 {
		right: auto
	}

	.ant-col-sm-offset-0 {
		margin-left: 0
	}

	.ant-col-sm-order-0 {
		-webkit-box-ordinal-group: 1;
		-ms-flex-order: 0;
		order: 0
	}
}

@media (min-width:992px) {
	.ant-col-md-1,.ant-col-md-2,.ant-col-md-3,.ant-col-md-4,.ant-col-md-5,.ant-col-md-6,.ant-col-md-7,.ant-col-md-8,.ant-col-md-9,.ant-col-md-10,.ant-col-md-11,.ant-col-md-12,.ant-col-md-13,.ant-col-md-14,.ant-col-md-15,.ant-col-md-16,.ant-col-md-17,.ant-col-md-18,.ant-col-md-19,.ant-col-md-20,.ant-col-md-21,.ant-col-md-22,.ant-col-md-23,.ant-col-md-24 {
		float: left;
		-webkit-box-flex: 0;
		-ms-flex: 0 0 auto;
		flex: 0 0 auto
	}

	.ant-col-md-24 {
		display: block;
		width: 100%
	}

	.ant-col-md-push-24 {
		left: 100%
	}

	.ant-col-md-pull-24 {
		right: 100%
	}

	.ant-col-md-offset-24 {
		margin-left: 100%
	}

	.ant-col-md-order-24 {
		-webkit-box-ordinal-group: 25;
		-ms-flex-order: 24;
		order: 24
	}

	.ant-col-md-23 {
		display: block;
		width: 95.83333333%
	}

	.ant-col-md-push-23 {
		left: 95.83333333%
	}

	.ant-col-md-pull-23 {
		right: 95.83333333%
	}

	.ant-col-md-offset-23 {
		margin-left: 95.83333333%
	}

	.ant-col-md-order-23 {
		-webkit-box-ordinal-group: 24;
		-ms-flex-order: 23;
		order: 23
	}

	.ant-col-md-22 {
		display: block;
		width: 91.66666667%
	}

	.ant-col-md-push-22 {
		left: 91.66666667%
	}

	.ant-col-md-pull-22 {
		right: 91.66666667%
	}

	.ant-col-md-offset-22 {
		margin-left: 91.66666667%
	}

	.ant-col-md-order-22 {
		-webkit-box-ordinal-group: 23;
		-ms-flex-order: 22;
		order: 22
	}

	.ant-col-md-21 {
		display: block;
		width: 87.5%
	}

	.ant-col-md-push-21 {
		left: 87.5%
	}

	.ant-col-md-pull-21 {
		right: 87.5%
	}

	.ant-col-md-offset-21 {
		margin-left: 87.5%
	}

	.ant-col-md-order-21 {
		-webkit-box-ordinal-group: 22;
		-ms-flex-order: 21;
		order: 21
	}

	.ant-col-md-20 {
		display: block;
		width: 83.33333333%
	}

	.ant-col-md-push-20 {
		left: 83.33333333%
	}

	.ant-col-md-pull-20 {
		right: 83.33333333%
	}

	.ant-col-md-offset-20 {
		margin-left: 83.33333333%
	}

	.ant-col-md-order-20 {
		-webkit-box-ordinal-group: 21;
		-ms-flex-order: 20;
		order: 20
	}

	.ant-col-md-19 {
		display: block;
		width: 79.16666667%
	}

	.ant-col-md-push-19 {
		left: 79.16666667%
	}

	.ant-col-md-pull-19 {
		right: 79.16666667%
	}

	.ant-col-md-offset-19 {
		margin-left: 79.16666667%
	}

	.ant-col-md-order-19 {
		-webkit-box-ordinal-group: 20;
		-ms-flex-order: 19;
		order: 19
	}

	.ant-col-md-18 {
		display: block;
		width: 75%
	}

	.ant-col-md-push-18 {
		left: 75%
	}

	.ant-col-md-pull-18 {
		right: 75%
	}

	.ant-col-md-offset-18 {
		margin-left: 75%
	}

	.ant-col-md-order-18 {
		-webkit-box-ordinal-group: 19;
		-ms-flex-order: 18;
		order: 18
	}

	.ant-col-md-17 {
		display: block;
		width: 70.83333333%
	}

	.ant-col-md-push-17 {
		left: 70.83333333%
	}

	.ant-col-md-pull-17 {
		right: 70.83333333%
	}

	.ant-col-md-offset-17 {
		margin-left: 70.83333333%
	}

	.ant-col-md-order-17 {
		-webkit-box-ordinal-group: 18;
		-ms-flex-order: 17;
		order: 17
	}

	.ant-col-md-16 {
		display: block;
		width: 66.66666667%
	}

	.ant-col-md-push-16 {
		left: 66.66666667%
	}

	.ant-col-md-pull-16 {
		right: 66.66666667%
	}

	.ant-col-md-offset-16 {
		margin-left: 66.66666667%
	}

	.ant-col-md-order-16 {
		-webkit-box-ordinal-group: 17;
		-ms-flex-order: 16;
		order: 16
	}

	.ant-col-md-15 {
		display: block;
		width: 62.5%
	}

	.ant-col-md-push-15 {
		left: 62.5%
	}

	.ant-col-md-pull-15 {
		right: 62.5%
	}

	.ant-col-md-offset-15 {
		margin-left: 62.5%
	}

	.ant-col-md-order-15 {
		-webkit-box-ordinal-group: 16;
		-ms-flex-order: 15;
		order: 15
	}

	.ant-col-md-14 {
		display: block;
		width: 58.33333333%
	}

	.ant-col-md-push-14 {
		left: 58.33333333%
	}

	.ant-col-md-pull-14 {
		right: 58.33333333%
	}

	.ant-col-md-offset-14 {
		margin-left: 58.33333333%
	}

	.ant-col-md-order-14 {
		-webkit-box-ordinal-group: 15;
		-ms-flex-order: 14;
		order: 14
	}

	.ant-col-md-13 {
		display: block;
		width: 54.16666667%
	}

	.ant-col-md-push-13 {
		left: 54.16666667%
	}

	.ant-col-md-pull-13 {
		right: 54.16666667%
	}

	.ant-col-md-offset-13 {
		margin-left: 54.16666667%
	}

	.ant-col-md-order-13 {
		-webkit-box-ordinal-group: 14;
		-ms-flex-order: 13;
		order: 13
	}

	.ant-col-md-12 {
		display: block;
		width: 50%
	}

	.ant-col-md-push-12 {
		left: 50%
	}

	.ant-col-md-pull-12 {
		right: 50%
	}

	.ant-col-md-offset-12 {
		margin-left: 50%
	}

	.ant-col-md-order-12 {
		-webkit-box-ordinal-group: 13;
		-ms-flex-order: 12;
		order: 12
	}

	.ant-col-md-11 {
		display: block;
		width: 45.83333333%
	}

	.ant-col-md-push-11 {
		left: 45.83333333%
	}

	.ant-col-md-pull-11 {
		right: 45.83333333%
	}

	.ant-col-md-offset-11 {
		margin-left: 45.83333333%
	}

	.ant-col-md-order-11 {
		-webkit-box-ordinal-group: 12;
		-ms-flex-order: 11;
		order: 11
	}

	.ant-col-md-10 {
		display: block;
		width: 41.66666667%
	}

	.ant-col-md-push-10 {
		left: 41.66666667%
	}

	.ant-col-md-pull-10 {
		right: 41.66666667%
	}

	.ant-col-md-offset-10 {
		margin-left: 41.66666667%
	}

	.ant-col-md-order-10 {
		-webkit-box-ordinal-group: 11;
		-ms-flex-order: 10;
		order: 10
	}

	.ant-col-md-9 {
		display: block;
		width: 37.5%
	}

	.ant-col-md-push-9 {
		left: 37.5%
	}

	.ant-col-md-pull-9 {
		right: 37.5%
	}

	.ant-col-md-offset-9 {
		margin-left: 37.5%
	}

	.ant-col-md-order-9 {
		-webkit-box-ordinal-group: 10;
		-ms-flex-order: 9;
		order: 9
	}

	.ant-col-md-8 {
		display: block;
		width: 33.33333333%
	}

	.ant-col-md-push-8 {
		left: 33.33333333%
	}

	.ant-col-md-pull-8 {
		right: 33.33333333%
	}

	.ant-col-md-offset-8 {
		margin-left: 33.33333333%
	}

	.ant-col-md-order-8 {
		-webkit-box-ordinal-group: 9;
		-ms-flex-order: 8;
		order: 8
	}

	.ant-col-md-7 {
		display: block;
		width: 29.16666667%
	}

	.ant-col-md-push-7 {
		left: 29.16666667%
	}

	.ant-col-md-pull-7 {
		right: 29.16666667%
	}

	.ant-col-md-offset-7 {
		margin-left: 29.16666667%
	}

	.ant-col-md-order-7 {
		-webkit-box-ordinal-group: 8;
		-ms-flex-order: 7;
		order: 7
	}

	.ant-col-md-6 {
		display: block;
		width: 25%
	}

	.ant-col-md-push-6 {
		left: 25%
	}

	.ant-col-md-pull-6 {
		right: 25%
	}

	.ant-col-md-offset-6 {
		margin-left: 25%
	}

	.ant-col-md-order-6 {
		-webkit-box-ordinal-group: 7;
		-ms-flex-order: 6;
		order: 6
	}

	.ant-col-md-5 {
		display: block;
		width: 20.83333333%
	}

	.ant-col-md-push-5 {
		left: 20.83333333%
	}

	.ant-col-md-pull-5 {
		right: 20.83333333%
	}

	.ant-col-md-offset-5 {
		margin-left: 20.83333333%
	}

	.ant-col-md-order-5 {
		-webkit-box-ordinal-group: 6;
		-ms-flex-order: 5;
		order: 5
	}

	.ant-col-md-4 {
		display: block;
		width: 16.66666667%
	}

	.ant-col-md-push-4 {
		left: 16.66666667%
	}

	.ant-col-md-pull-4 {
		right: 16.66666667%
	}

	.ant-col-md-offset-4 {
		margin-left: 16.66666667%
	}

	.ant-col-md-order-4 {
		-webkit-box-ordinal-group: 5;
		-ms-flex-order: 4;
		order: 4
	}

	.ant-col-md-3 {
		display: block;
		width: 12.5%
	}

	.ant-col-md-push-3 {
		left: 12.5%
	}

	.ant-col-md-pull-3 {
		right: 12.5%
	}

	.ant-col-md-offset-3 {
		margin-left: 12.5%
	}

	.ant-col-md-order-3 {
		-webkit-box-ordinal-group: 4;
		-ms-flex-order: 3;
		order: 3
	}

	.ant-col-md-2 {
		display: block;
		width: 8.33333333%
	}

	.ant-col-md-push-2 {
		left: 8.33333333%
	}

	.ant-col-md-pull-2 {
		right: 8.33333333%
	}

	.ant-col-md-offset-2 {
		margin-left: 8.33333333%
	}

	.ant-col-md-order-2 {
		-webkit-box-ordinal-group: 3;
		-ms-flex-order: 2;
		order: 2
	}

	.ant-col-md-1 {
		display: block;
		width: 4.16666667%
	}

	.ant-col-md-push-1 {
		left: 4.16666667%
	}

	.ant-col-md-pull-1 {
		right: 4.16666667%
	}

	.ant-col-md-offset-1 {
		margin-left: 4.16666667%
	}

	.ant-col-md-order-1 {
		-webkit-box-ordinal-group: 2;
		-ms-flex-order: 1;
		order: 1
	}

	.ant-col-md-0 {
		display: none
	}

	.ant-col-push-0 {
		left: auto
	}

	.ant-col-pull-0 {
		right: auto
	}

	.ant-col-md-push-0 {
		left: auto
	}

	.ant-col-md-pull-0 {
		right: auto
	}

	.ant-col-md-offset-0 {
		margin-left: 0
	}

	.ant-col-md-order-0 {
		-webkit-box-ordinal-group: 1;
		-ms-flex-order: 0;
		order: 0
	}
}

@media (min-width:1200px) {
	.ant-col-lg-1,.ant-col-lg-2,.ant-col-lg-3,.ant-col-lg-4,.ant-col-lg-5,.ant-col-lg-6,.ant-col-lg-7,.ant-col-lg-8,.ant-col-lg-9,.ant-col-lg-10,.ant-col-lg-11,.ant-col-lg-12,.ant-col-lg-13,.ant-col-lg-14,.ant-col-lg-15,.ant-col-lg-16,.ant-col-lg-17,.ant-col-lg-18,.ant-col-lg-19,.ant-col-lg-20,.ant-col-lg-21,.ant-col-lg-22,.ant-col-lg-23,.ant-col-lg-24 {
		float: left;
		-webkit-box-flex: 0;
		-ms-flex: 0 0 auto;
		flex: 0 0 auto
	}

	.ant-col-lg-24 {
		display: block;
		width: 100%
	}

	.ant-col-lg-push-24 {
		left: 100%
	}

	.ant-col-lg-pull-24 {
		right: 100%
	}

	.ant-col-lg-offset-24 {
		margin-left: 100%
	}

	.ant-col-lg-order-24 {
		-webkit-box-ordinal-group: 25;
		-ms-flex-order: 24;
		order: 24
	}

	.ant-col-lg-23 {
		display: block;
		width: 95.83333333%
	}

	.ant-col-lg-push-23 {
		left: 95.83333333%
	}

	.ant-col-lg-pull-23 {
		right: 95.83333333%
	}

	.ant-col-lg-offset-23 {
		margin-left: 95.83333333%
	}

	.ant-col-lg-order-23 {
		-webkit-box-ordinal-group: 24;
		-ms-flex-order: 23;
		order: 23
	}

	.ant-col-lg-22 {
		display: block;
		width: 91.66666667%
	}

	.ant-col-lg-push-22 {
		left: 91.66666667%
	}

	.ant-col-lg-pull-22 {
		right: 91.66666667%
	}

	.ant-col-lg-offset-22 {
		margin-left: 91.66666667%
	}

	.ant-col-lg-order-22 {
		-webkit-box-ordinal-group: 23;
		-ms-flex-order: 22;
		order: 22
	}

	.ant-col-lg-21 {
		display: block;
		width: 87.5%
	}

	.ant-col-lg-push-21 {
		left: 87.5%
	}

	.ant-col-lg-pull-21 {
		right: 87.5%
	}

	.ant-col-lg-offset-21 {
		margin-left: 87.5%
	}

	.ant-col-lg-order-21 {
		-webkit-box-ordinal-group: 22;
		-ms-flex-order: 21;
		order: 21
	}

	.ant-col-lg-20 {
		display: block;
		width: 83.33333333%
	}

	.ant-col-lg-push-20 {
		left: 83.33333333%
	}

	.ant-col-lg-pull-20 {
		right: 83.33333333%
	}

	.ant-col-lg-offset-20 {
		margin-left: 83.33333333%
	}

	.ant-col-lg-order-20 {
		-webkit-box-ordinal-group: 21;
		-ms-flex-order: 20;
		order: 20
	}

	.ant-col-lg-19 {
		display: block;
		width: 79.16666667%
	}

	.ant-col-lg-push-19 {
		left: 79.16666667%
	}

	.ant-col-lg-pull-19 {
		right: 79.16666667%
	}

	.ant-col-lg-offset-19 {
		margin-left: 79.16666667%
	}

	.ant-col-lg-order-19 {
		-webkit-box-ordinal-group: 20;
		-ms-flex-order: 19;
		order: 19
	}

	.ant-col-lg-18 {
		display: block;
		width: 75%
	}

	.ant-col-lg-push-18 {
		left: 75%
	}

	.ant-col-lg-pull-18 {
		right: 75%
	}

	.ant-col-lg-offset-18 {
		margin-left: 75%
	}

	.ant-col-lg-order-18 {
		-webkit-box-ordinal-group: 19;
		-ms-flex-order: 18;
		order: 18
	}

	.ant-col-lg-17 {
		display: block;
		width: 70.83333333%
	}

	.ant-col-lg-push-17 {
		left: 70.83333333%
	}

	.ant-col-lg-pull-17 {
		right: 70.83333333%
	}

	.ant-col-lg-offset-17 {
		margin-left: 70.83333333%
	}

	.ant-col-lg-order-17 {
		-webkit-box-ordinal-group: 18;
		-ms-flex-order: 17;
		order: 17
	}

	.ant-col-lg-16 {
		display: block;
		width: 66.66666667%
	}

	.ant-col-lg-push-16 {
		left: 66.66666667%
	}

	.ant-col-lg-pull-16 {
		right: 66.66666667%
	}

	.ant-col-lg-offset-16 {
		margin-left: 66.66666667%
	}

	.ant-col-lg-order-16 {
		-webkit-box-ordinal-group: 17;
		-ms-flex-order: 16;
		order: 16
	}

	.ant-col-lg-15 {
		display: block;
		width: 62.5%
	}

	.ant-col-lg-push-15 {
		left: 62.5%
	}

	.ant-col-lg-pull-15 {
		right: 62.5%
	}

	.ant-col-lg-offset-15 {
		margin-left: 62.5%
	}

	.ant-col-lg-order-15 {
		-webkit-box-ordinal-group: 16;
		-ms-flex-order: 15;
		order: 15
	}

	.ant-col-lg-14 {
		display: block;
		width: 58.33333333%
	}

	.ant-col-lg-push-14 {
		left: 58.33333333%
	}

	.ant-col-lg-pull-14 {
		right: 58.33333333%
	}

	.ant-col-lg-offset-14 {
		margin-left: 58.33333333%
	}

	.ant-col-lg-order-14 {
		-webkit-box-ordinal-group: 15;
		-ms-flex-order: 14;
		order: 14
	}

	.ant-col-lg-13 {
		display: block;
		width: 54.16666667%
	}

	.ant-col-lg-push-13 {
		left: 54.16666667%
	}

	.ant-col-lg-pull-13 {
		right: 54.16666667%
	}

	.ant-col-lg-offset-13 {
		margin-left: 54.16666667%
	}

	.ant-col-lg-order-13 {
		-webkit-box-ordinal-group: 14;
		-ms-flex-order: 13;
		order: 13
	}

	.ant-col-lg-12 {
		display: block;
		width: 50%
	}

	.ant-col-lg-push-12 {
		left: 50%
	}

	.ant-col-lg-pull-12 {
		right: 50%
	}

	.ant-col-lg-offset-12 {
		margin-left: 50%
	}

	.ant-col-lg-order-12 {
		-webkit-box-ordinal-group: 13;
		-ms-flex-order: 12;
		order: 12
	}

	.ant-col-lg-11 {
		display: block;
		width: 45.83333333%
	}

	.ant-col-lg-push-11 {
		left: 45.83333333%
	}

	.ant-col-lg-pull-11 {
		right: 45.83333333%
	}

	.ant-col-lg-offset-11 {
		margin-left: 45.83333333%
	}

	.ant-col-lg-order-11 {
		-webkit-box-ordinal-group: 12;
		-ms-flex-order: 11;
		order: 11
	}

	.ant-col-lg-10 {
		display: block;
		width: 41.66666667%
	}

	.ant-col-lg-push-10 {
		left: 41.66666667%
	}

	.ant-col-lg-pull-10 {
		right: 41.66666667%
	}

	.ant-col-lg-offset-10 {
		margin-left: 41.66666667%
	}

	.ant-col-lg-order-10 {
		-webkit-box-ordinal-group: 11;
		-ms-flex-order: 10;
		order: 10
	}

	.ant-col-lg-9 {
		display: block;
		width: 37.5%
	}

	.ant-col-lg-push-9 {
		left: 37.5%
	}

	.ant-col-lg-pull-9 {
		right: 37.5%
	}

	.ant-col-lg-offset-9 {
		margin-left: 37.5%
	}

	.ant-col-lg-order-9 {
		-webkit-box-ordinal-group: 10;
		-ms-flex-order: 9;
		order: 9
	}

	.ant-col-lg-8 {
		display: block;
		width: 33.33333333%
	}

	.ant-col-lg-push-8 {
		left: 33.33333333%
	}

	.ant-col-lg-pull-8 {
		right: 33.33333333%
	}

	.ant-col-lg-offset-8 {
		margin-left: 33.33333333%
	}

	.ant-col-lg-order-8 {
		-webkit-box-ordinal-group: 9;
		-ms-flex-order: 8;
		order: 8
	}

	.ant-col-lg-7 {
		display: block;
		width: 29.16666667%
	}

	.ant-col-lg-push-7 {
		left: 29.16666667%
	}

	.ant-col-lg-pull-7 {
		right: 29.16666667%
	}

	.ant-col-lg-offset-7 {
		margin-left: 29.16666667%
	}

	.ant-col-lg-order-7 {
		-webkit-box-ordinal-group: 8;
		-ms-flex-order: 7;
		order: 7
	}

	.ant-col-lg-6 {
		display: block;
		width: 25%
	}

	.ant-col-lg-push-6 {
		left: 25%
	}

	.ant-col-lg-pull-6 {
		right: 25%
	}

	.ant-col-lg-offset-6 {
		margin-left: 25%
	}

	.ant-col-lg-order-6 {
		-webkit-box-ordinal-group: 7;
		-ms-flex-order: 6;
		order: 6
	}

	.ant-col-lg-5 {
		display: block;
		width: 20.83333333%
	}

	.ant-col-lg-push-5 {
		left: 20.83333333%
	}

	.ant-col-lg-pull-5 {
		right: 20.83333333%
	}

	.ant-col-lg-offset-5 {
		margin-left: 20.83333333%
	}

	.ant-col-lg-order-5 {
		-webkit-box-ordinal-group: 6;
		-ms-flex-order: 5;
		order: 5
	}

	.ant-col-lg-4 {
		display: block;
		width: 16.66666667%
	}

	.ant-col-lg-push-4 {
		left: 16.66666667%
	}

	.ant-col-lg-pull-4 {
		right: 16.66666667%
	}

	.ant-col-lg-offset-4 {
		margin-left: 16.66666667%
	}

	.ant-col-lg-order-4 {
		-webkit-box-ordinal-group: 5;
		-ms-flex-order: 4;
		order: 4
	}

	.ant-col-lg-3 {
		display: block;
		width: 12.5%
	}

	.ant-col-lg-push-3 {
		left: 12.5%
	}

	.ant-col-lg-pull-3 {
		right: 12.5%
	}

	.ant-col-lg-offset-3 {
		margin-left: 12.5%
	}

	.ant-col-lg-order-3 {
		-webkit-box-ordinal-group: 4;
		-ms-flex-order: 3;
		order: 3
	}

	.ant-col-lg-2 {
		display: block;
		width: 8.33333333%
	}

	.ant-col-lg-push-2 {
		left: 8.33333333%
	}

	.ant-col-lg-pull-2 {
		right: 8.33333333%
	}

	.ant-col-lg-offset-2 {
		margin-left: 8.33333333%
	}

	.ant-col-lg-order-2 {
		-webkit-box-ordinal-group: 3;
		-ms-flex-order: 2;
		order: 2
	}

	.ant-col-lg-1 {
		display: block;
		width: 4.16666667%
	}

	.ant-col-lg-push-1 {
		left: 4.16666667%
	}

	.ant-col-lg-pull-1 {
		right: 4.16666667%
	}

	.ant-col-lg-offset-1 {
		margin-left: 4.16666667%
	}

	.ant-col-lg-order-1 {
		-webkit-box-ordinal-group: 2;
		-ms-flex-order: 1;
		order: 1
	}

	.ant-col-lg-0 {
		display: none
	}

	.ant-col-push-0 {
		left: auto
	}

	.ant-col-pull-0 {
		right: auto
	}

	.ant-col-lg-push-0 {
		left: auto
	}

	.ant-col-lg-pull-0 {
		right: auto
	}

	.ant-col-lg-offset-0 {
		margin-left: 0
	}

	.ant-col-lg-order-0 {
		-webkit-box-ordinal-group: 1;
		-ms-flex-order: 0;
		order: 0
	}
}

@media (min-width:1600px) {
	.ant-col-xl-1,.ant-col-xl-2,.ant-col-xl-3,.ant-col-xl-4,.ant-col-xl-5,.ant-col-xl-6,.ant-col-xl-7,.ant-col-xl-8,.ant-col-xl-9,.ant-col-xl-10,.ant-col-xl-11,.ant-col-xl-12,.ant-col-xl-13,.ant-col-xl-14,.ant-col-xl-15,.ant-col-xl-16,.ant-col-xl-17,.ant-col-xl-18,.ant-col-xl-19,.ant-col-xl-20,.ant-col-xl-21,.ant-col-xl-22,.ant-col-xl-23,.ant-col-xl-24 {
		float: left;
		-webkit-box-flex: 0;
		-ms-flex: 0 0 auto;
		flex: 0 0 auto
	}

	.ant-col-xl-24 {
		display: block;
		width: 100%
	}

	.ant-col-xl-push-24 {
		left: 100%
	}

	.ant-col-xl-pull-24 {
		right: 100%
	}

	.ant-col-xl-offset-24 {
		margin-left: 100%
	}

	.ant-col-xl-order-24 {
		-webkit-box-ordinal-group: 25;
		-ms-flex-order: 24;
		order: 24
	}

	.ant-col-xl-23 {
		display: block;
		width: 95.83333333%
	}

	.ant-col-xl-push-23 {
		left: 95.83333333%
	}

	.ant-col-xl-pull-23 {
		right: 95.83333333%
	}

	.ant-col-xl-offset-23 {
		margin-left: 95.83333333%
	}

	.ant-col-xl-order-23 {
		-webkit-box-ordinal-group: 24;
		-ms-flex-order: 23;
		order: 23
	}

	.ant-col-xl-22 {
		display: block;
		width: 91.66666667%
	}

	.ant-col-xl-push-22 {
		left: 91.66666667%
	}

	.ant-col-xl-pull-22 {
		right: 91.66666667%
	}

	.ant-col-xl-offset-22 {
		margin-left: 91.66666667%
	}

	.ant-col-xl-order-22 {
		-webkit-box-ordinal-group: 23;
		-ms-flex-order: 22;
		order: 22
	}

	.ant-col-xl-21 {
		display: block;
		width: 87.5%
	}

	.ant-col-xl-push-21 {
		left: 87.5%
	}

	.ant-col-xl-pull-21 {
		right: 87.5%
	}

	.ant-col-xl-offset-21 {
		margin-left: 87.5%
	}

	.ant-col-xl-order-21 {
		-webkit-box-ordinal-group: 22;
		-ms-flex-order: 21;
		order: 21
	}

	.ant-col-xl-20 {
		display: block;
		width: 83.33333333%
	}

	.ant-col-xl-push-20 {
		left: 83.33333333%
	}

	.ant-col-xl-pull-20 {
		right: 83.33333333%
	}

	.ant-col-xl-offset-20 {
		margin-left: 83.33333333%
	}

	.ant-col-xl-order-20 {
		-webkit-box-ordinal-group: 21;
		-ms-flex-order: 20;
		order: 20
	}

	.ant-col-xl-19 {
		display: block;
		width: 79.16666667%
	}

	.ant-col-xl-push-19 {
		left: 79.16666667%
	}

	.ant-col-xl-pull-19 {
		right: 79.16666667%
	}

	.ant-col-xl-offset-19 {
		margin-left: 79.16666667%
	}

	.ant-col-xl-order-19 {
		-webkit-box-ordinal-group: 20;
		-ms-flex-order: 19;
		order: 19
	}

	.ant-col-xl-18 {
		display: block;
		width: 75%
	}

	.ant-col-xl-push-18 {
		left: 75%
	}

	.ant-col-xl-pull-18 {
		right: 75%
	}

	.ant-col-xl-offset-18 {
		margin-left: 75%
	}

	.ant-col-xl-order-18 {
		-webkit-box-ordinal-group: 19;
		-ms-flex-order: 18;
		order: 18
	}

	.ant-col-xl-17 {
		display: block;
		width: 70.83333333%
	}

	.ant-col-xl-push-17 {
		left: 70.83333333%
	}

	.ant-col-xl-pull-17 {
		right: 70.83333333%
	}

	.ant-col-xl-offset-17 {
		margin-left: 70.83333333%
	}

	.ant-col-xl-order-17 {
		-webkit-box-ordinal-group: 18;
		-ms-flex-order: 17;
		order: 17
	}

	.ant-col-xl-16 {
		display: block;
		width: 66.66666667%
	}

	.ant-col-xl-push-16 {
		left: 66.66666667%
	}

	.ant-col-xl-pull-16 {
		right: 66.66666667%
	}

	.ant-col-xl-offset-16 {
		margin-left: 66.66666667%
	}

	.ant-col-xl-order-16 {
		-webkit-box-ordinal-group: 17;
		-ms-flex-order: 16;
		order: 16
	}

	.ant-col-xl-15 {
		display: block;
		width: 62.5%
	}

	.ant-col-xl-push-15 {
		left: 62.5%
	}

	.ant-col-xl-pull-15 {
		right: 62.5%
	}

	.ant-col-xl-offset-15 {
		margin-left: 62.5%
	}

	.ant-col-xl-order-15 {
		-webkit-box-ordinal-group: 16;
		-ms-flex-order: 15;
		order: 15
	}

	.ant-col-xl-14 {
		display: block;
		width: 58.33333333%
	}

	.ant-col-xl-push-14 {
		left: 58.33333333%
	}

	.ant-col-xl-pull-14 {
		right: 58.33333333%
	}

	.ant-col-xl-offset-14 {
		margin-left: 58.33333333%
	}

	.ant-col-xl-order-14 {
		-webkit-box-ordinal-group: 15;
		-ms-flex-order: 14;
		order: 14
	}

	.ant-col-xl-13 {
		display: block;
		width: 54.16666667%
	}

	.ant-col-xl-push-13 {
		left: 54.16666667%
	}

	.ant-col-xl-pull-13 {
		right: 54.16666667%
	}

	.ant-col-xl-offset-13 {
		margin-left: 54.16666667%
	}

	.ant-col-xl-order-13 {
		-webkit-box-ordinal-group: 14;
		-ms-flex-order: 13;
		order: 13
	}

	.ant-col-xl-12 {
		display: block;
		width: 50%
	}

	.ant-col-xl-push-12 {
		left: 50%
	}

	.ant-col-xl-pull-12 {
		right: 50%
	}

	.ant-col-xl-offset-12 {
		margin-left: 50%
	}

	.ant-col-xl-order-12 {
		-webkit-box-ordinal-group: 13;
		-ms-flex-order: 12;
		order: 12
	}

	.ant-col-xl-11 {
		display: block;
		width: 45.83333333%
	}

	.ant-col-xl-push-11 {
		left: 45.83333333%
	}

	.ant-col-xl-pull-11 {
		right: 45.83333333%
	}

	.ant-col-xl-offset-11 {
		margin-left: 45.83333333%
	}

	.ant-col-xl-order-11 {
		-webkit-box-ordinal-group: 12;
		-ms-flex-order: 11;
		order: 11
	}

	.ant-col-xl-10 {
		display: block;
		width: 41.66666667%
	}

	.ant-col-xl-push-10 {
		left: 41.66666667%
	}

	.ant-col-xl-pull-10 {
		right: 41.66666667%
	}

	.ant-col-xl-offset-10 {
		margin-left: 41.66666667%
	}

	.ant-col-xl-order-10 {
		-webkit-box-ordinal-group: 11;
		-ms-flex-order: 10;
		order: 10
	}

	.ant-col-xl-9 {
		display: block;
		width: 37.5%
	}

	.ant-col-xl-push-9 {
		left: 37.5%
	}

	.ant-col-xl-pull-9 {
		right: 37.5%
	}

	.ant-col-xl-offset-9 {
		margin-left: 37.5%
	}

	.ant-col-xl-order-9 {
		-webkit-box-ordinal-group: 10;
		-ms-flex-order: 9;
		order: 9
	}

	.ant-col-xl-8 {
		display: block;
		width: 33.33333333%
	}

	.ant-col-xl-push-8 {
		left: 33.33333333%
	}

	.ant-col-xl-pull-8 {
		right: 33.33333333%
	}

	.ant-col-xl-offset-8 {
		margin-left: 33.33333333%
	}

	.ant-col-xl-order-8 {
		-webkit-box-ordinal-group: 9;
		-ms-flex-order: 8;
		order: 8
	}

	.ant-col-xl-7 {
		display: block;
		width: 29.16666667%
	}

	.ant-col-xl-push-7 {
		left: 29.16666667%
	}

	.ant-col-xl-pull-7 {
		right: 29.16666667%
	}

	.ant-col-xl-offset-7 {
		margin-left: 29.16666667%
	}

	.ant-col-xl-order-7 {
		-webkit-box-ordinal-group: 8;
		-ms-flex-order: 7;
		order: 7
	}

	.ant-col-xl-6 {
		display: block;
		width: 25%
	}

	.ant-col-xl-push-6 {
		left: 25%
	}

	.ant-col-xl-pull-6 {
		right: 25%
	}

	.ant-col-xl-offset-6 {
		margin-left: 25%
	}

	.ant-col-xl-order-6 {
		-webkit-box-ordinal-group: 7;
		-ms-flex-order: 6;
		order: 6
	}

	.ant-col-xl-5 {
		display: block;
		width: 20.83333333%
	}

	.ant-col-xl-push-5 {
		left: 20.83333333%
	}

	.ant-col-xl-pull-5 {
		right: 20.83333333%
	}

	.ant-col-xl-offset-5 {
		margin-left: 20.83333333%
	}

	.ant-col-xl-order-5 {
		-webkit-box-ordinal-group: 6;
		-ms-flex-order: 5;
		order: 5
	}

	.ant-col-xl-4 {
		display: block;
		width: 16.66666667%
	}

	.ant-col-xl-push-4 {
		left: 16.66666667%
	}

	.ant-col-xl-pull-4 {
		right: 16.66666667%
	}

	.ant-col-xl-offset-4 {
		margin-left: 16.66666667%
	}

	.ant-col-xl-order-4 {
		-webkit-box-ordinal-group: 5;
		-ms-flex-order: 4;
		order: 4
	}

	.ant-col-xl-3 {
		display: block;
		width: 12.5%
	}

	.ant-col-xl-push-3 {
		left: 12.5%
	}

	.ant-col-xl-pull-3 {
		right: 12.5%
	}

	.ant-col-xl-offset-3 {
		margin-left: 12.5%
	}

	.ant-col-xl-order-3 {
		-webkit-box-ordinal-group: 4;
		-ms-flex-order: 3;
		order: 3
	}

	.ant-col-xl-2 {
		display: block;
		width: 8.33333333%
	}

	.ant-col-xl-push-2 {
		left: 8.33333333%
	}

	.ant-col-xl-pull-2 {
		right: 8.33333333%
	}

	.ant-col-xl-offset-2 {
		margin-left: 8.33333333%
	}

	.ant-col-xl-order-2 {
		-webkit-box-ordinal-group: 3;
		-ms-flex-order: 2;
		order: 2
	}

	.ant-col-xl-1 {
		display: block;
		width: 4.16666667%
	}

	.ant-col-xl-push-1 {
		left: 4.16666667%
	}

	.ant-col-xl-pull-1 {
		right: 4.16666667%
	}

	.ant-col-xl-offset-1 {
		margin-left: 4.16666667%
	}

	.ant-col-xl-order-1 {
		-webkit-box-ordinal-group: 2;
		-ms-flex-order: 1;
		order: 1
	}

	.ant-col-xl-0 {
		display: none
	}

	.ant-col-push-0 {
		left: auto
	}

	.ant-col-pull-0 {
		right: auto
	}

	.ant-col-xl-push-0 {
		left: auto
	}

	.ant-col-xl-pull-0 {
		right: auto
	}

	.ant-col-xl-offset-0 {
		margin-left: 0
	}

	.ant-col-xl-order-0 {
		-webkit-box-ordinal-group: 1;
		-ms-flex-order: 0;
		order: 0
	}
}

.ant-btn {
	display: inline-block;
	margin-bottom: 0;
	font-weight: 500;
	text-align: center;
	-ms-touch-action: manipulation;
	touch-action: manipulation;
	cursor: pointer;
	background-image: none;
	border: 1px solid transparent;
	white-space: nowrap;
	line-height: 1.15;
	padding: 0 15px;
	font-size: 12px;
	border-radius: 4px;
	height: 28px;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	transition: all .3s cubic-bezier(.645,.045,.355,1);
	position: relative;
	color: rgba(0,0,0,.65);
	background-color: #fff;
	border-color: #d9d9d9
}

.ant-btn>.anticon {
	line-height: 1
}

.ant-btn,.ant-btn:active,.ant-btn:focus {
	outline: 0
}

.ant-btn:not([disabled]):hover {
	text-decoration: none
}

.ant-btn:not([disabled]):active {
	outline: 0;
	transition: none
}

.ant-btn.disabled,.ant-btn[disabled] {
	cursor: not-allowed
}

.ant-btn.disabled>*,.ant-btn[disabled]>* {
	pointer-events: none
}

.ant-btn-lg {
	padding: 0 15px;
	font-size: 14px;
	border-radius: 4px;
	height: 32px
}

.ant-btn-sm {
	padding: 0 7px;
	font-size: 12px;
	border-radius: 4px;
	height: 22px
}

.ant-btn>a:only-child {
	color: currentColor
}

.ant-btn>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn:focus,.ant-btn:hover {
	color: #108ee9;
	background-color: #fff;
	border-color: #108ee9
}

.ant-btn:focus>a:only-child,.ant-btn:hover>a:only-child {
	color: currentColor
}

.ant-btn:focus>a:only-child:after,.ant-btn:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn.active,.ant-btn:active {
	color: #0e77ca;
	background-color: #fff;
	border-color: #0e77ca
}

.ant-btn.active>a:only-child,.ant-btn:active>a:only-child {
	color: currentColor
}

.ant-btn.active>a:only-child:after,.ant-btn:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn.disabled,.ant-btn.disabled.active,.ant-btn.disabled:active,.ant-btn.disabled:focus,.ant-btn.disabled:hover,.ant-btn[disabled],.ant-btn[disabled].active,.ant-btn[disabled]:active,.ant-btn[disabled]:focus,.ant-btn[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn.disabled.active>a:only-child,.ant-btn.disabled:active>a:only-child,.ant-btn.disabled:focus>a:only-child,.ant-btn.disabled:hover>a:only-child,.ant-btn.disabled>a:only-child,.ant-btn[disabled].active>a:only-child,.ant-btn[disabled]:active>a:only-child,.ant-btn[disabled]:focus>a:only-child,.ant-btn[disabled]:hover>a:only-child,.ant-btn[disabled]>a:only-child {
	color: currentColor
}

.ant-btn.disabled.active>a:only-child:after,.ant-btn.disabled:active>a:only-child:after,.ant-btn.disabled:focus>a:only-child:after,.ant-btn.disabled:hover>a:only-child:after,.ant-btn.disabled>a:only-child:after,.ant-btn[disabled].active>a:only-child:after,.ant-btn[disabled]:active>a:only-child:after,.ant-btn[disabled]:focus>a:only-child:after,.ant-btn[disabled]:hover>a:only-child:after,.ant-btn[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn.active,.ant-btn:active,.ant-btn:focus,.ant-btn:hover {
	background: #fff
}

.ant-btn>i,.ant-btn>span {
	pointer-events: none
}

.ant-btn-primary {
	color: #fff;
	background-color: #108ee9;
	border-color: #108ee9
}

.ant-btn-primary>a:only-child {
	color: currentColor
}

.ant-btn-primary>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-primary:focus,.ant-btn-primary:hover {
	color: #fff;
	background-color: #49a9ee;
	border-color: #49a9ee
}

.ant-btn-primary:focus>a:only-child,.ant-btn-primary:hover>a:only-child {
	color: currentColor
}

.ant-btn-primary:focus>a:only-child:after,.ant-btn-primary:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-primary.active,.ant-btn-primary:active {
	color: #fff;
	background-color: #0e77ca;
	border-color: #0e77ca
}

.ant-btn-primary.active>a:only-child,.ant-btn-primary:active>a:only-child {
	color: currentColor
}

.ant-btn-primary.active>a:only-child:after,.ant-btn-primary:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-primary.disabled,.ant-btn-primary.disabled.active,.ant-btn-primary.disabled:active,.ant-btn-primary.disabled:focus,.ant-btn-primary.disabled:hover,.ant-btn-primary[disabled],.ant-btn-primary[disabled].active,.ant-btn-primary[disabled]:active,.ant-btn-primary[disabled]:focus,.ant-btn-primary[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn-primary.disabled.active>a:only-child,.ant-btn-primary.disabled:active>a:only-child,.ant-btn-primary.disabled:focus>a:only-child,.ant-btn-primary.disabled:hover>a:only-child,.ant-btn-primary.disabled>a:only-child,.ant-btn-primary[disabled].active>a:only-child,.ant-btn-primary[disabled]:active>a:only-child,.ant-btn-primary[disabled]:focus>a:only-child,.ant-btn-primary[disabled]:hover>a:only-child,.ant-btn-primary[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-primary.disabled.active>a:only-child:after,.ant-btn-primary.disabled:active>a:only-child:after,.ant-btn-primary.disabled:focus>a:only-child:after,.ant-btn-primary.disabled:hover>a:only-child:after,.ant-btn-primary.disabled>a:only-child:after,.ant-btn-primary[disabled].active>a:only-child:after,.ant-btn-primary[disabled]:active>a:only-child:after,.ant-btn-primary[disabled]:focus>a:only-child:after,.ant-btn-primary[disabled]:hover>a:only-child:after,.ant-btn-primary[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-group .ant-btn-primary:not(:first-child):not(:last-child) {
	border-right-color: #0e77ca;
	border-left-color: #0e77ca
}

.ant-btn-group .ant-btn-primary:not(:first-child):not(:last-child):disabled {
	border-color: #d9d9d9
}

.ant-btn-group .ant-btn-primary:first-child:not(:last-child) {
	border-right-color: #0e77ca
}

.ant-btn-group .ant-btn-primary:first-child:not(:last-child)[disabled] {
	border-right-color: #d9d9d9
}

.ant-btn-group .ant-btn-primary+.ant-btn-primary,.ant-btn-group .ant-btn-primary:last-child:not(:first-child) {
	border-left-color: #0e77ca
}

.ant-btn-group .ant-btn-primary+.ant-btn-primary[disabled],.ant-btn-group .ant-btn-primary:last-child:not(:first-child)[disabled] {
	border-left-color: #d9d9d9
}

.ant-btn-ghost {
	color: rgba(0,0,0,.65);
	background-color: transparent;
	border-color: #d9d9d9
}

.ant-btn-ghost>a:only-child {
	color: currentColor
}

.ant-btn-ghost>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-ghost:focus,.ant-btn-ghost:hover {
	color: #108ee9;
	background-color: transparent;
	border-color: #108ee9
}

.ant-btn-ghost:focus>a:only-child,.ant-btn-ghost:hover>a:only-child {
	color: currentColor
}

.ant-btn-ghost:focus>a:only-child:after,.ant-btn-ghost:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-ghost.active,.ant-btn-ghost:active {
	color: #0e77ca;
	background-color: transparent;
	border-color: #0e77ca
}

.ant-btn-ghost.active>a:only-child,.ant-btn-ghost:active>a:only-child {
	color: currentColor
}

.ant-btn-ghost.active>a:only-child:after,.ant-btn-ghost:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-ghost.disabled,.ant-btn-ghost.disabled.active,.ant-btn-ghost.disabled:active,.ant-btn-ghost.disabled:focus,.ant-btn-ghost.disabled:hover,.ant-btn-ghost[disabled],.ant-btn-ghost[disabled].active,.ant-btn-ghost[disabled]:active,.ant-btn-ghost[disabled]:focus,.ant-btn-ghost[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn-ghost.disabled.active>a:only-child,.ant-btn-ghost.disabled:active>a:only-child,.ant-btn-ghost.disabled:focus>a:only-child,.ant-btn-ghost.disabled:hover>a:only-child,.ant-btn-ghost.disabled>a:only-child,.ant-btn-ghost[disabled].active>a:only-child,.ant-btn-ghost[disabled]:active>a:only-child,.ant-btn-ghost[disabled]:focus>a:only-child,.ant-btn-ghost[disabled]:hover>a:only-child,.ant-btn-ghost[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-ghost.disabled.active>a:only-child:after,.ant-btn-ghost.disabled:active>a:only-child:after,.ant-btn-ghost.disabled:focus>a:only-child:after,.ant-btn-ghost.disabled:hover>a:only-child:after,.ant-btn-ghost.disabled>a:only-child:after,.ant-btn-ghost[disabled].active>a:only-child:after,.ant-btn-ghost[disabled]:active>a:only-child:after,.ant-btn-ghost[disabled]:focus>a:only-child:after,.ant-btn-ghost[disabled]:hover>a:only-child:after,.ant-btn-ghost[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-dashed {
	color: rgba(0,0,0,.65);
	background-color: #fff;
	border-color: #d9d9d9;
	border-style: dashed
}

.ant-btn-dashed>a:only-child {
	color: currentColor
}

.ant-btn-dashed>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-dashed:focus,.ant-btn-dashed:hover {
	color: #108ee9;
	background-color: #fff;
	border-color: #108ee9
}

.ant-btn-dashed:focus>a:only-child,.ant-btn-dashed:hover>a:only-child {
	color: currentColor
}

.ant-btn-dashed:focus>a:only-child:after,.ant-btn-dashed:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-dashed.active,.ant-btn-dashed:active {
	color: #0e77ca;
	background-color: #fff;
	border-color: #0e77ca
}

.ant-btn-dashed.active>a:only-child,.ant-btn-dashed:active>a:only-child {
	color: currentColor
}

.ant-btn-dashed.active>a:only-child:after,.ant-btn-dashed:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-dashed.disabled,.ant-btn-dashed.disabled.active,.ant-btn-dashed.disabled:active,.ant-btn-dashed.disabled:focus,.ant-btn-dashed.disabled:hover,.ant-btn-dashed[disabled],.ant-btn-dashed[disabled].active,.ant-btn-dashed[disabled]:active,.ant-btn-dashed[disabled]:focus,.ant-btn-dashed[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn-dashed.disabled.active>a:only-child,.ant-btn-dashed.disabled:active>a:only-child,.ant-btn-dashed.disabled:focus>a:only-child,.ant-btn-dashed.disabled:hover>a:only-child,.ant-btn-dashed.disabled>a:only-child,.ant-btn-dashed[disabled].active>a:only-child,.ant-btn-dashed[disabled]:active>a:only-child,.ant-btn-dashed[disabled]:focus>a:only-child,.ant-btn-dashed[disabled]:hover>a:only-child,.ant-btn-dashed[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-dashed.disabled.active>a:only-child:after,.ant-btn-dashed.disabled:active>a:only-child:after,.ant-btn-dashed.disabled:focus>a:only-child:after,.ant-btn-dashed.disabled:hover>a:only-child:after,.ant-btn-dashed.disabled>a:only-child:after,.ant-btn-dashed[disabled].active>a:only-child:after,.ant-btn-dashed[disabled]:active>a:only-child:after,.ant-btn-dashed[disabled]:focus>a:only-child:after,.ant-btn-dashed[disabled]:hover>a:only-child:after,.ant-btn-dashed[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-danger {
	color: #f04134;
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn-danger>a:only-child {
	color: currentColor
}

.ant-btn-danger>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-danger:focus,.ant-btn-danger:hover {
	color: #fff;
	background-color: #f04134;
	border-color: #f04134
}

.ant-btn-danger:focus>a:only-child,.ant-btn-danger:hover>a:only-child {
	color: currentColor
}

.ant-btn-danger:focus>a:only-child:after,.ant-btn-danger:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-danger.active,.ant-btn-danger:active {
	color: #fff;
	background-color: #d73435;
	border-color: #d73435
}

.ant-btn-danger.active>a:only-child,.ant-btn-danger:active>a:only-child {
	color: currentColor
}

.ant-btn-danger.active>a:only-child:after,.ant-btn-danger:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-danger.disabled,.ant-btn-danger.disabled.active,.ant-btn-danger.disabled:active,.ant-btn-danger.disabled:focus,.ant-btn-danger.disabled:hover,.ant-btn-danger[disabled],.ant-btn-danger[disabled].active,.ant-btn-danger[disabled]:active,.ant-btn-danger[disabled]:focus,.ant-btn-danger[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn-danger.disabled.active>a:only-child,.ant-btn-danger.disabled:active>a:only-child,.ant-btn-danger.disabled:focus>a:only-child,.ant-btn-danger.disabled:hover>a:only-child,.ant-btn-danger.disabled>a:only-child,.ant-btn-danger[disabled].active>a:only-child,.ant-btn-danger[disabled]:active>a:only-child,.ant-btn-danger[disabled]:focus>a:only-child,.ant-btn-danger[disabled]:hover>a:only-child,.ant-btn-danger[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-danger.disabled.active>a:only-child:after,.ant-btn-danger.disabled:active>a:only-child:after,.ant-btn-danger.disabled:focus>a:only-child:after,.ant-btn-danger.disabled:hover>a:only-child:after,.ant-btn-danger.disabled>a:only-child:after,.ant-btn-danger[disabled].active>a:only-child:after,.ant-btn-danger[disabled]:active>a:only-child:after,.ant-btn-danger[disabled]:focus>a:only-child:after,.ant-btn-danger[disabled]:hover>a:only-child:after,.ant-btn-danger[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-circle,.ant-btn-circle-outline {
	width: 28px;
	padding: 0;
	font-size: 14px;
	border-radius: 50%;
	height: 28px
}

.ant-btn-circle-outline.ant-btn-lg,.ant-btn-circle.ant-btn-lg {
	width: 32px;
	padding: 0;
	font-size: 16px;
	border-radius: 50%;
	height: 32px
}

.ant-btn-circle-outline.ant-btn-sm,.ant-btn-circle.ant-btn-sm {
	width: 22px;
	padding: 0;
	font-size: 12px;
	border-radius: 50%;
	height: 22px
}

.ant-btn:before {
	position: absolute;
	top: -1px;
	left: -1px;
	bottom: -1px;
	right: -1px;
	background: #fff;
	opacity: .35;
	content: "";
	border-radius: inherit;
	z-index: 1;
	transition: opacity .2s;
	pointer-events: none;
	display: none
}

.ant-btn .anticon {
	transition: margin-left .3s cubic-bezier(.645,.045,.355,1)
}

.ant-btn.ant-btn-loading:before {
	display: block
}

.ant-btn.ant-btn-loading:not(.ant-btn-circle):not(.ant-btn-circle-outline) {
	padding-left: 29px;
	pointer-events: none;
	position: relative
}

.ant-btn.ant-btn-loading:not(.ant-btn-circle):not(.ant-btn-circle-outline) .anticon {
	margin-left: -14px
}

.ant-btn-sm.ant-btn-loading:not(.ant-btn-circle):not(.ant-btn-circle-outline) {
	padding-left: 24px
}

.ant-btn-sm.ant-btn-loading:not(.ant-btn-circle):not(.ant-btn-circle-outline) .anticon {
	margin-left: -17px
}

.ant-btn-group {
	position: relative;
	display: inline-block
}

.ant-btn-group>.ant-btn {
	position: relative;
	z-index: 1
}

.ant-btn-group>.ant-btn.active,.ant-btn-group>.ant-btn:active,.ant-btn-group>.ant-btn:focus,.ant-btn-group>.ant-btn:hover {
	z-index: 2
}

.ant-btn-group>.ant-btn:disabled {
	z-index: 0
}

.ant-btn-group-lg>.ant-btn {
	padding: 0 15px;
	font-size: 14px;
	border-radius: 4px;
	height: 32px
}

.ant-btn-group-sm>.ant-btn {
	padding: 0 7px;
	font-size: 12px;
	border-radius: 4px;
	height: 22px
}

.ant-btn-group-sm>.ant-btn>.anticon {
	font-size: 12px
}

.ant-btn+.ant-btn-group,.ant-btn-group+.ant-btn,.ant-btn-group+.ant-btn-group,.ant-btn-group .ant-btn+.ant-btn {
	margin-left: -1px
}

.ant-btn-group .ant-btn:not(:first-child):not(:last-child) {
	border-radius: 0;
	padding-left: 8px;
	padding-right: 8px
}

.ant-btn-group>.ant-btn:first-child {
	margin-left: 0
}

.ant-btn-group>.ant-btn:first-child:not(:last-child) {
	border-bottom-right-radius: 0;
	border-top-right-radius: 0;
	padding-right: 8px
}

.ant-btn-group>.ant-btn:last-child:not(:first-child) {
	border-bottom-left-radius: 0;
	border-top-left-radius: 0;
	padding-left: 8px
}

.ant-btn-group>.ant-btn-group {
	float: left
}

.ant-btn-group>.ant-btn-group:not(:first-child):not(:last-child)>.ant-btn {
	border-radius: 0
}

.ant-btn-group>.ant-btn-group:first-child:not(:last-child)>.ant-btn:last-child {
	border-bottom-right-radius: 0;
	border-top-right-radius: 0;
	padding-right: 8px
}

.ant-btn-group>.ant-btn-group:last-child:not(:first-child)>.ant-btn:first-child {
	border-bottom-left-radius: 0;
	border-top-left-radius: 0;
	padding-left: 8px
}

.ant-btn:not(.ant-btn-circle):not(.ant-btn-circle-outline).ant-btn-icon-only {
	padding-left: 8px;
	padding-right: 8px
}

.ant-btn:active>span,.ant-btn:focus>span {
	position: relative
}

.ant-btn>.anticon+span,.ant-btn>span+.anticon {
	margin-left: .5em
}

.ant-btn-clicked:after {
	content: "";
	position: absolute;
	top: -1px;
	left: -1px;
	bottom: -1px;
	right: -1px;
	border-radius: inherit;
	border: 0 solid #108ee9;
	opacity: .4;
	-webkit-animation: buttonEffect .4s;
	animation: buttonEffect .4s;
	display: block
}

.ant-btn-danger.ant-btn-clicked:after {
	border-color: #f04134
}

.ant-btn-background-ghost {
	background: transparent!important;
	border-color: #fff;
	color: #fff
}

.ant-btn-background-ghost.ant-btn-primary {
	color: #108ee9;
	background-color: transparent;
	border-color: #108ee9
}

.ant-btn-background-ghost.ant-btn-primary>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-background-ghost.ant-btn-primary:focus,.ant-btn-background-ghost.ant-btn-primary:hover {
	color: #49a9ee;
	background-color: transparent;
	border-color: #49a9ee
}

.ant-btn-background-ghost.ant-btn-primary:focus>a:only-child,.ant-btn-background-ghost.ant-btn-primary:hover>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-background-ghost.ant-btn-primary.active,.ant-btn-background-ghost.ant-btn-primary:active {
	color: #0e77ca;
	background-color: transparent;
	border-color: #0e77ca
}

.ant-btn-background-ghost.ant-btn-primary.active>a:only-child,.ant-btn-background-ghost.ant-btn-primary:active>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-background-ghost.ant-btn-primary.disabled,.ant-btn-background-ghost.ant-btn-primary.disabled.active,.ant-btn-background-ghost.ant-btn-primary.disabled:active,.ant-btn-background-ghost.ant-btn-primary.disabled:focus,.ant-btn-background-ghost.ant-btn-primary.disabled:hover,.ant-btn-background-ghost.ant-btn-primary[disabled],.ant-btn-background-ghost.ant-btn-primary[disabled].active,.ant-btn-background-ghost.ant-btn-primary[disabled]:active,.ant-btn-background-ghost.ant-btn-primary[disabled]:focus,.ant-btn-background-ghost.ant-btn-primary[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn-background-ghost.ant-btn-primary.disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled].active>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]:active>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]:focus>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]:hover>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary.disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled].active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-background-ghost.ant-btn-danger {
	color: #f04134;
	background-color: transparent;
	border-color: #f04134
}

.ant-btn-background-ghost.ant-btn-danger>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-background-ghost.ant-btn-danger:focus,.ant-btn-background-ghost.ant-btn-danger:hover {
	color: #f46e65;
	background-color: transparent;
	border-color: #f46e65
}

.ant-btn-background-ghost.ant-btn-danger:focus>a:only-child,.ant-btn-background-ghost.ant-btn-danger:hover>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-background-ghost.ant-btn-danger.active,.ant-btn-background-ghost.ant-btn-danger:active {
	color: #d73435;
	background-color: transparent;
	border-color: #d73435
}

.ant-btn-background-ghost.ant-btn-danger.active>a:only-child,.ant-btn-background-ghost.ant-btn-danger:active>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-btn-background-ghost.ant-btn-danger.disabled,.ant-btn-background-ghost.ant-btn-danger.disabled.active,.ant-btn-background-ghost.ant-btn-danger.disabled:active,.ant-btn-background-ghost.ant-btn-danger.disabled:focus,.ant-btn-background-ghost.ant-btn-danger.disabled:hover,.ant-btn-background-ghost.ant-btn-danger[disabled],.ant-btn-background-ghost.ant-btn-danger[disabled].active,.ant-btn-background-ghost.ant-btn-danger[disabled]:active,.ant-btn-background-ghost.ant-btn-danger[disabled]:focus,.ant-btn-background-ghost.ant-btn-danger[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-btn-background-ghost.ant-btn-danger.disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled].active>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]:active>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]:focus>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]:hover>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger.disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled].active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

@-webkit-keyframes buttonEffect {
	to {
		opacity: 0;
		top: -6px;
		left: -6px;
		bottom: -6px;
		right: -6px;
		border-width: 6px
	}
}

@keyframes buttonEffect {
	to {
		opacity: 0;
		top: -6px;
		left: -6px;
		bottom: -6px;
		right: -6px;
		border-width: 6px
	}
}

.ant-dropdown {
	position: absolute;
	left: -9999px;
	top: -9999px;
	z-index: 1050;
	display: block;
	font-size: 12px;
	font-weight: 400;
	line-height: 1.5
}

.ant-dropdown-wrap {
	position: relative
}

.ant-dropdown-wrap .ant-btn>.anticon-down {
	display: inline-block;
	font-size: 12px;
	font-size: 10px\9;
	-webkit-transform: scale(.83333333) rotate(0deg);
	-ms-transform: scale(.83333333) rotate(0deg);
	transform: scale(.83333333) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1
}

:root .ant-dropdown-wrap .ant-btn>.anticon-down {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-dropdown-wrap .anticon-down:before {
	transition: -webkit-transform .2s ease;
	transition: transform .2s ease;
	transition: transform .2s ease,-webkit-transform .2s ease
}

.ant-dropdown-wrap-open .anticon-down:before {
	-webkit-transform: rotate(180deg);
	-ms-transform: rotate(180deg);
	transform: rotate(180deg)
}

.ant-dropdown-hidden,.ant-dropdown-menu-hidden {
	display: none
}

.ant-dropdown-menu {
	outline: none;
	position: relative;
	list-style-type: none;
	padding: 0;
	margin: 0;
	text-align: left;
	background-color: #fff;
	border-radius: 4px;
	box-shadow: 0 1px 6px rgba(0,0,0,.2);
	background-clip: padding-box
}

.ant-dropdown-menu-item,.ant-dropdown-menu-submenu-title {
	padding: 7px 8px;
	margin: 0;
	clear: both;
	font-size: 12px;
	font-weight: 400;
	color: rgba(0,0,0,.65);
	white-space: nowrap;
	cursor: pointer;
	transition: all .3s
}

.ant-dropdown-menu-item>a,.ant-dropdown-menu-submenu-title>a {
	color: rgba(0,0,0,.65);
	display: block;
	padding: 7px 8px;
	margin: -7px -8px;
	transition: all .3s
}

.ant-dropdown-menu-item>a:focus,.ant-dropdown-menu-submenu-title>a:focus {
	text-decoration: none
}

.ant-dropdown-menu-item-selected,.ant-dropdown-menu-item-selected>a,.ant-dropdown-menu-submenu-title-selected,.ant-dropdown-menu-submenu-title-selected>a {
	color: #108ee9;
	background-color: #ecf6fd
}

.ant-dropdown-menu-item:hover,.ant-dropdown-menu-submenu-title:hover {
	background-color: #ecf6fd
}

.ant-dropdown-menu-item-disabled,.ant-dropdown-menu-submenu-title-disabled {
	color: rgba(0,0,0,.25);
	cursor: not-allowed
}

.ant-dropdown-menu-item-disabled:hover,.ant-dropdown-menu-submenu-title-disabled:hover {
	color: rgba(0,0,0,.25);
	background-color: #fff;
	cursor: not-allowed
}

.ant-dropdown-menu-item:first-child,.ant-dropdown-menu-item:first-child>a,.ant-dropdown-menu-submenu-title:first-child,.ant-dropdown-menu-submenu-title:first-child>a {
	border-radius: 4px 4px 0 0
}

.ant-dropdown-menu-item:last-child,.ant-dropdown-menu-item:last-child>a,.ant-dropdown-menu-submenu-title:last-child,.ant-dropdown-menu-submenu-title:last-child>a {
	border-radius: 0 0 4px 4px
}

.ant-dropdown-menu-item:only-child,.ant-dropdown-menu-item:only-child>a,.ant-dropdown-menu-submenu-title:only-child,.ant-dropdown-menu-submenu-title:only-child>a {
	border-radius: 4px
}

.ant-dropdown-menu-item-divider,.ant-dropdown-menu-submenu-title-divider {
	height: 1px;
	overflow: hidden;
	background-color: #e9e9e9;
	line-height: 0
}

.ant-dropdown-menu-submenu-title:after {
	font-family: anticon!important;
	position: absolute;
	content: "\E61F";
	right: 8px;
	color: rgba(0,0,0,.43);
	display: inline-block;
	font-size: 12px;
	font-size: 10px\9;
	-webkit-transform: scale(.83333333) rotate(0deg);
	-ms-transform: scale(.83333333) rotate(0deg);
	transform: scale(.83333333) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1
}

:root .ant-dropdown-menu-submenu-title:after {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-dropdown-menu-submenu-vertical {
	position: relative
}

.ant-dropdown-menu-submenu-vertical>.ant-dropdown-menu {
	top: 0;
	left: 100%;
	position: absolute;
	min-width: 100%;
	margin-left: 4px;
	-webkit-transform-origin: 0 0;
	-ms-transform-origin: 0 0;
	transform-origin: 0 0
}

.ant-dropdown-menu-submenu.ant-dropdown-menu-submenu-disabled .ant-dropdown-menu-submenu-title,.ant-dropdown-menu-submenu.ant-dropdown-menu-submenu-disabled .ant-dropdown-menu-submenu-title:after {
	color: rgba(0,0,0,.25)
}

.ant-dropdown-menu-submenu:first-child .ant-dropdown-menu-submenu-title {
	border-radius: 4px 4px 0 0
}

.ant-dropdown-menu-submenu:last-child .ant-dropdown-menu-submenu-title {
	border-radius: 0 0 4px 4px
}

.ant-dropdown.slide-down-appear.slide-down-appear-active.ant-dropdown-placement-bottomCenter,.ant-dropdown.slide-down-appear.slide-down-appear-active.ant-dropdown-placement-bottomLeft,.ant-dropdown.slide-down-appear.slide-down-appear-active.ant-dropdown-placement-bottomRight,.ant-dropdown.slide-down-enter.slide-down-enter-active.ant-dropdown-placement-bottomCenter,.ant-dropdown.slide-down-enter.slide-down-enter-active.ant-dropdown-placement-bottomLeft,.ant-dropdown.slide-down-enter.slide-down-enter-active.ant-dropdown-placement-bottomRight {
	-webkit-animation-name: antSlideUpIn;
	animation-name: antSlideUpIn
}

.ant-dropdown.slide-up-appear.slide-up-appear-active.ant-dropdown-placement-topCenter,.ant-dropdown.slide-up-appear.slide-up-appear-active.ant-dropdown-placement-topLeft,.ant-dropdown.slide-up-appear.slide-up-appear-active.ant-dropdown-placement-topRight,.ant-dropdown.slide-up-enter.slide-up-enter-active.ant-dropdown-placement-topCenter,.ant-dropdown.slide-up-enter.slide-up-enter-active.ant-dropdown-placement-topLeft,.ant-dropdown.slide-up-enter.slide-up-enter-active.ant-dropdown-placement-topRight {
	-webkit-animation-name: antSlideDownIn;
	animation-name: antSlideDownIn
}

.ant-dropdown.slide-down-leave.slide-down-leave-active.ant-dropdown-placement-bottomCenter,.ant-dropdown.slide-down-leave.slide-down-leave-active.ant-dropdown-placement-bottomLeft,.ant-dropdown.slide-down-leave.slide-down-leave-active.ant-dropdown-placement-bottomRight {
	-webkit-animation-name: antSlideUpOut;
	animation-name: antSlideUpOut
}

.ant-dropdown.slide-up-leave.slide-up-leave-active.ant-dropdown-placement-topCenter,.ant-dropdown.slide-up-leave.slide-up-leave-active.ant-dropdown-placement-topLeft,.ant-dropdown.slide-up-leave.slide-up-leave-active.ant-dropdown-placement-topRight {
	-webkit-animation-name: antSlideDownOut;
	animation-name: antSlideDownOut
}

.ant-dropdown-link .anticon-down,.ant-dropdown-trigger .anticon-down {
	display: inline-block;
	font-size: 12px;
	font-size: 10px\9;
	-webkit-transform: scale(.83333333) rotate(0deg);
	-ms-transform: scale(.83333333) rotate(0deg);
	transform: scale(.83333333) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1
}

:root .ant-dropdown-link .anticon-down,:root .ant-dropdown-trigger .anticon-down {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-dropdown-button {
	white-space: nowrap
}

.ant-dropdown-button.ant-btn-group>.ant-btn:last-child:not(:first-child) {
	padding-right: 8px
}

.ant-dropdown-button .anticon-down {
	display: inline-block;
	font-size: 12px;
	font-size: 10px\9;
	-webkit-transform: scale(.83333333) rotate(0deg);
	-ms-transform: scale(.83333333) rotate(0deg);
	transform: scale(.83333333) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1
}

:root .ant-dropdown-button .anticon-down {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-dropdown-menu-dark,.ant-dropdown-menu-dark .ant-dropdown-menu {
	background: #404040
}

.ant-dropdown-menu-dark .ant-dropdown-menu-item,.ant-dropdown-menu-dark .ant-dropdown-menu-item:after,.ant-dropdown-menu-dark .ant-dropdown-menu-item>a,.ant-dropdown-menu-dark .ant-dropdown-menu-item>a:after,.ant-dropdown-menu-dark .ant-dropdown-menu-submenu-title,.ant-dropdown-menu-dark .ant-dropdown-menu-submenu-title:after {
	color: hsla(0,0%,100%,.67)
}

.ant-dropdown-menu-dark .ant-dropdown-menu-item:hover,.ant-dropdown-menu-dark .ant-dropdown-menu-item>a:hover,.ant-dropdown-menu-dark .ant-dropdown-menu-submenu-title:hover {
	color: #fff;
	background: transparent
}

.ant-dropdown-menu-dark .ant-dropdown-menu-item-selected,.ant-dropdown-menu-dark .ant-dropdown-menu-item-selected:hover,.ant-dropdown-menu-dark .ant-dropdown-menu-item-selected>a {
	background: #108ee9;
	color: #fff
}

@font-face {
	font-family:octicons-link;src:url(data:font/woff;charset=utf-8;base64,d09GRgABAAAAAAZwABAAAAAACFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEU0lHAAAGaAAAAAgAAAAIAAAAAUdTVUIAAAZcAAAACgAAAAoAAQAAT1MvMgAAAyQAAABJAAAAYFYEU3RjbWFwAAADcAAAAEUAAACAAJThvmN2dCAAAATkAAAABAAAAAQAAAAAZnBnbQAAA7gAAACyAAABCUM+8IhnYXNwAAAGTAAAABAAAAAQABoAI2dseWYAAAFsAAABPAAAAZwcEq9taGVhZAAAAsgAAAA0AAAANgh4a91oaGVhAAADCAAAABoAAAAkCA8DRGhtdHgAAAL8AAAADAAAAAwGAACfbG9jYQAAAsAAAAAIAAAACABiATBtYXhwAAACqAAAABgAAAAgAA8ASm5hbWUAAAToAAABQgAAAlXu73sOcG9zdAAABiwAAAAeAAAAME3QpOBwcmVwAAAEbAAAAHYAAAB/aFGpk3jaTY6xa8JAGMW/O62BDi0tJLYQincXEypYIiGJjSgHniQ6umTsUEyLm5BV6NDBP8Tpts6F0v+k/0an2i+itHDw3v2+9+DBKTzsJNnWJNTgHEy4BgG3EMI9DCEDOGEXzDADU5hBKMIgNPZqoD3SilVaXZCER3/I7AtxEJLtzzuZfI+VVkprxTlXShWKb3TBecG11rwoNlmmn1P2WYcJczl32etSpKnziC7lQyWe1smVPy/Lt7Kc+0vWY/gAgIIEqAN9we0pwKXreiMasxvabDQMM4riO+qxM2ogwDGOZTXxwxDiycQIcoYFBLj5K3EIaSctAq2kTYiw+ymhce7vwM9jSqO8JyVd5RH9gyTt2+J/yUmYlIR0s04n6+7Vm1ozezUeLEaUjhaDSuXHwVRgvLJn1tQ7xiuVv/ocTRF42mNgZGBgYGbwZOBiAAFGJBIMAAizAFoAAABiAGIAznjaY2BkYGAA4in8zwXi+W2+MjCzMIDApSwvXzC97Z4Ig8N/BxYGZgcgl52BCSQKAA3jCV8CAABfAAAAAAQAAEB42mNgZGBg4f3vACQZQABIMjKgAmYAKEgBXgAAeNpjYGY6wTiBgZWBg2kmUxoDA4MPhGZMYzBi1AHygVLYQUCaawqDA4PChxhmh/8ODDEsvAwHgMKMIDnGL0x7gJQCAwMAJd4MFwAAAHjaY2BgYGaA4DAGRgYQkAHyGMF8NgYrIM3JIAGVYYDT+AEjAwuDFpBmA9KMDEwMCh9i/v8H8sH0/4dQc1iAmAkALaUKLgAAAHjaTY9LDsIgEIbtgqHUPpDi3gPoBVyRTmTddOmqTXThEXqrob2gQ1FjwpDvfwCBdmdXC5AVKFu3e5MfNFJ29KTQT48Ob9/lqYwOGZxeUelN2U2R6+cArgtCJpauW7UQBqnFkUsjAY/kOU1cP+DAgvxwn1chZDwUbd6CFimGXwzwF6tPbFIcjEl+vvmM/byA48e6tWrKArm4ZJlCbdsrxksL1AwWn/yBSJKpYbq8AXaaTb8AAHja28jAwOC00ZrBeQNDQOWO//sdBBgYGRiYWYAEELEwMTE4uzo5Zzo5b2BxdnFOcALxNjA6b2ByTswC8jYwg0VlNuoCTWAMqNzMzsoK1rEhNqByEyerg5PMJlYuVueETKcd/89uBpnpvIEVomeHLoMsAAe1Id4AAAAAAAB42oWQT07CQBTGv0JBhagk7HQzKxca2sJCE1hDt4QF+9JOS0nbaaYDCQfwCJ7Au3AHj+LO13FMmm6cl7785vven0kBjHCBhfpYuNa5Ph1c0e2Xu3jEvWG7UdPDLZ4N92nOm+EBXuAbHmIMSRMs+4aUEd4Nd3CHD8NdvOLTsA2GL8M9PODbcL+hD7C1xoaHeLJSEao0FEW14ckxC+TU8TxvsY6X0eLPmRhry2WVioLpkrbp84LLQPGI7c6sOiUzpWIWS5GzlSgUzzLBSikOPFTOXqly7rqx0Z1Q5BAIoZBSFihQYQOOBEdkCOgXTOHA07HAGjGWiIjaPZNW13/+lm6S9FT7rLHFJ6fQbkATOG1j2OFMucKJJsxIVfQORl+9Jyda6Sl1dUYhSCm1dyClfoeDve4qMYdLEbfqHf3O/AdDumsjAAB42mNgYoAAZQYjBmyAGYQZmdhL8zLdDEydARfoAqIAAAABAAMABwAKABMAB///AA8AAQAAAAAAAAAAAAAAAAABAAAAAA==) format("woff")
}

.markdown-body {
	-ms-text-size-adjust: 100%;
	-webkit-text-size-adjust: 100%;
	color: #24292e;
	font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif;
	font-size: 16px;
	line-height: 1.5;
	word-wrap: break-word
}

.markdown-body .pl-c {
	color: #6a737d
}

.markdown-body .pl-c1,.markdown-body .pl-s .pl-v {
	color: #005cc5
}

.markdown-body .pl-e,.markdown-body .pl-en {
	color: #6f42c1
}

.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi {
	color: #24292e
}

.markdown-body .pl-ent {
	color: #22863a
}

.markdown-body .pl-k {
	color: #d73a49
}

.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre {
	color: #032f62
}

.markdown-body .pl-smw,.markdown-body .pl-v {
	color: #e36209
}

.markdown-body .pl-bu {
	color: #b31d28
}

.markdown-body .pl-ii {
	color: #fafbfc;
	background-color: #b31d28
}

.markdown-body .pl-c2 {
	color: #fafbfc;
	background-color: #d73a49
}

.markdown-body .pl-c2:before {
	content: "^M"
}

.markdown-body .pl-sr .pl-cce {
	font-weight: 700;
	color: #22863a
}

.markdown-body .pl-ml {
	color: #735c0f
}

.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms {
	font-weight: 700;
	color: #005cc5
}

.markdown-body .pl-mi {
	font-style: italic;
	color: #24292e
}

.markdown-body .pl-mb {
	font-weight: 700;
	color: #24292e
}

.markdown-body .pl-md {
	color: #b31d28;
	background-color: #ffeef0
}

.markdown-body .pl-mi1 {
	color: #22863a;
	background-color: #f0fff4
}

.markdown-body .pl-mc {
	color: #e36209;
	background-color: #ffebda
}

.markdown-body .pl-mi2 {
	color: #f6f8fa;
	background-color: #005cc5
}

.markdown-body .pl-mdr {
	font-weight: 700;
	color: #6f42c1
}

.markdown-body .pl-ba {
	color: #586069
}

.markdown-body .pl-sg {
	color: #959da5
}

.markdown-body .pl-corl {
	text-decoration: underline;
	color: #032f62
}

.markdown-body .octicon {
	display: inline-block;
	vertical-align: text-top;
	fill: currentColor
}

.markdown-body a {
	background-color: transparent;
	-webkit-text-decoration-skip: objects
}

.markdown-body a:active,.markdown-body a:hover {
	outline-width: 0
}

.markdown-body strong {
	font-weight: inherit;
	font-weight: bolder
}

.markdown-body h1 {
	margin: .67em 0
}

.markdown-body img {
	border-style: none
}

.markdown-body svg:not(:root) {
	overflow: hidden
}

.markdown-body code,.markdown-body kbd,.markdown-body pre {
	font-family: monospace,monospace;
	font-size: 1em
}

.markdown-body hr {
	box-sizing: content-box;
	overflow: visible
}

.markdown-body input {
	font: inherit;
	margin: 0;
	overflow: visible
}

.markdown-body [type=checkbox] {
	box-sizing: border-box;
	padding: 0
}

.markdown-body * {
	box-sizing: border-box
}

.markdown-body input {
	font-family: inherit;
	font-size: inherit;
	line-height: inherit
}

.markdown-body a {
	color: #0366d6;
	text-decoration: none
}

.markdown-body a:hover {
	text-decoration: underline
}

.markdown-body strong {
	font-weight: 600
}

.markdown-body hr {
	height: 0;
	margin: 15px 0;
	overflow: hidden;
	background: transparent;
	border-bottom: 1px solid #dfe2e5
}

.markdown-body hr:after,.markdown-body hr:before {
	display: table;
	content: ""
}

.markdown-body hr:after {
	clear: both
}

.markdown-body table {
	border-spacing: 0;
	border-collapse: collapse
}

.markdown-body td,.markdown-body th {
	padding: 0
}

.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6 {
	margin-top: 0;
	margin-bottom: 0
}

.markdown-body h1 {
	font-size: 32px;
	font-weight: 600
}

.markdown-body h2 {
	font-size: 24px;
	font-weight: 600
}

.markdown-body h3 {
	font-size: 20px;
	font-weight: 600
}

.markdown-body h4 {
	font-size: 16px;
	font-weight: 600
}

.markdown-body h5 {
	font-size: 14px;
	font-weight: 600
}

.markdown-body h6 {
	font-size: 12px;
	font-weight: 600
}

.markdown-body p {
	margin-top: 0;
	margin-bottom: 10px
}

.markdown-body blockquote {
	margin: 0
}

.markdown-body ol,.markdown-body ul {
	padding-left: 0;
	margin-top: 0;
	margin-bottom: 0
}

.markdown-body ol ol,.markdown-body ul ol {
	list-style-type: lower-roman
}

.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol {
	list-style-type: lower-alpha
}

.markdown-body dd {
	margin-left: 0
}

.markdown-body code {
	font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,Courier,monospace;
	font-size: 12px
}

.markdown-body pre {
	margin-top: 0;
	margin-bottom: 0;
	font: 12px SFMono-Regular,Consolas,Liberation Mono,Menlo,Courier,monospace
}

.markdown-body .octicon {
	vertical-align: text-bottom
}

.markdown-body .pl-0 {
	padding-left: 0!important
}

.markdown-body .pl-1 {
	padding-left: 4px!important
}

.markdown-body .pl-2 {
	padding-left: 8px!important
}

.markdown-body .pl-3 {
	padding-left: 16px!important
}

.markdown-body .pl-4 {
	padding-left: 24px!important
}

.markdown-body .pl-5 {
	padding-left: 32px!important
}

.markdown-body .pl-6 {
	padding-left: 40px!important
}

.markdown-body:after,.markdown-body:before {
	display: table;
	content: ""
}

.markdown-body:after {
	clear: both
}

.markdown-body>:first-child {
	margin-top: 0!important
}

.markdown-body>:last-child {
	margin-bottom: 0!important
}

.markdown-body a:not([href]) {
	color: inherit;
	text-decoration: none
}

.markdown-body .anchor {
	float: left;
	padding-right: 4px;
	margin-left: -20px;
	line-height: 1
}

.markdown-body .anchor:focus {
	outline: none
}

.markdown-body blockquote,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul {
	margin-top: 0;
	margin-bottom: 16px
}

.markdown-body hr {
	height: .25em;
	padding: 0;
	margin: 24px 0;
	background-color: #e1e4e8;
	border: 0
}

.markdown-body blockquote {
	padding: 0 1em;
	color: #6a737d;
	border-left: .25em solid #dfe2e5
}

.markdown-body blockquote>:first-child {
	margin-top: 0
}

.markdown-body blockquote>:last-child {
	margin-bottom: 0
}

.markdown-body kbd {
	font-size: 11px;
	border: 1px solid #c6cbd1;
	border-bottom-color: #959da5;
	box-shadow: inset 0 -1px 0 #959da5
}

.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6 {
	margin-top: 24px;
	margin-bottom: 16px;
	font-weight: 600;
	line-height: 1.25
}

.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link {
	color: #1b1f23;
	vertical-align: middle;
	visibility: hidden
}

.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor {
	text-decoration: none
}

.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link {
	visibility: visible
}

.markdown-body h1 {
	font-size: 2em
}

.markdown-body h1,.markdown-body h2 {
	padding-bottom: .3em;
	border-bottom: 1px solid #eaecef
}

.markdown-body h2 {
	font-size: 1.5em
}

.markdown-body h3 {
	font-size: 1.25em
}

.markdown-body h4 {
	font-size: 1em
}

.markdown-body h5 {
	font-size: .875em
}

.markdown-body h6 {
	font-size: .85em;
	color: #6a737d
}

.markdown-body ol,.markdown-body ul {
	padding-left: 2em
}

.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul {
	margin-top: 0;
	margin-bottom: 0
}

.markdown-body li>p {
	margin-top: 16px
}

.markdown-body li+li {
	margin-top: .25em
}

.markdown-body dl {
	padding: 0
}

.markdown-body dl dt {
	padding: 0;
	margin-top: 16px;
	font-size: 1em;
	font-style: italic;
	font-weight: 600
}

.markdown-body dl dd {
	padding: 0 16px;
	margin-bottom: 16px
}

.markdown-body table {
	display: block;
	width: 100%;
	overflow: auto
}

.markdown-body table th {
	font-weight: 600
}

.markdown-body table td,.markdown-body table th {
	padding: 6px 13px;
	border: 1px solid #dfe2e5
}

.markdown-body table tr {
	background-color: #fff;
	border-top: 1px solid #c6cbd1
}

.markdown-body table tr:nth-child(2n) {
	background-color: #f6f8fa
}

.markdown-body img {
	max-width: 100%;
	box-sizing: content-box;
	background-color: #fff
}

.markdown-body code {
	padding: 0;
	padding-top: .2em;
	padding-bottom: .2em;
	margin: 0;
	font-size: 85%;
	background-color: rgba(27,31,35,.05);
	border-radius: 3px
}

.markdown-body code:after,.markdown-body code:before {
	letter-spacing: -.2em;
	content: "\A0"
}

.markdown-body pre {
	word-wrap: normal
}

.markdown-body pre>code {
	padding: 0;
	margin: 0;
	font-size: 100%;
	word-break: normal;
	white-space: pre;
	background: transparent;
	border: 0
}

.markdown-body .highlight {
	margin-bottom: 16px
}

.markdown-body .highlight pre {
	margin-bottom: 0;
	word-break: normal
}

.markdown-body .highlight pre,.markdown-body pre {
	padding: 16px;
	overflow: auto;
	font-size: 85%;
	line-height: 1.45;
	background-color: #f6f8fa;
	border-radius: 3px
}

.markdown-body pre code {
	display: inline;
	max-width: auto;
	padding: 0;
	margin: 0;
	overflow: visible;
	line-height: inherit;
	word-wrap: normal;
	background-color: transparent;
	border: 0
}

.markdown-body pre code:after,.markdown-body pre code:before {
	content: normal
}

.markdown-body .full-commit .btn-outline:not(:disabled):hover {
	color: #005cc5;
	border-color: #005cc5
}

.markdown-body kbd {
	display: inline-block;
	padding: 3px 5px;
	font: 11px SFMono-Regular,Consolas,Liberation Mono,Menlo,Courier,monospace;
	line-height: 10px;
	color: #444d56;
	vertical-align: middle;
	background-color: #fafbfc;
	border: 1px solid #d1d5da;
	border-bottom-color: #c6cbd1;
	border-radius: 3px;
	box-shadow: inset 0 -1px 0 #c6cbd1
}

.markdown-body :checked+.radio-label {
	position: relative;
	z-index: 1;
	border-color: #0366d6
}

.markdown-body .task-list-item {
	list-style-type: none
}

.markdown-body .task-list-item+.task-list-item {
	margin-top: 3px
}

.markdown-body .task-list-item input {
	margin: 0 .2em .25em -1.6em;
	vertical-align: middle
}

.markdown-body hr {
	border-bottom-color: #eee
}

@media screen and (min-width:768px) {
	#content_0_0:before {
		background-image: url(https://images.seebug.org/ceye-bg.jpg);
		background-blend-mode: normal;
		background-color: #fff
	}

	#content_0_0 {
		border-style: none
	}

	#content_0_0-title {
		left: 0
	}

	#content_0_0-wrapper {
		top: 34%
	}

	#nav_0_0 {
		background-color: rgba(40,40,40,.6);
		position: fixed
	}

	#content_2_0 {
		background-color: #fff
	}

	#content_2_0-content {
		color: #404040;
		font-size: 14px
	}

	#content_2_0-title {
		color: #404040
	}

	#content_3_0-content {
		font-size: 14px
	}
}

body,html {
	font-family: PingFang SC,Helvetica Neue,Helvetica,Hiragino Sans GB,Microsoft YaHei,\\5FAE\8F6F\96C5\9ED1,Arial,sans-serif
}

body video {
	display: block
}

.text-center {
	text-align: center
}

a {
	transition: color .45s cubic-bezier(.215,.61,.355,1)
}

h1,h2,h3,h4 {
	color: #404040
}

#react-content {
	width: 100%;
	overflow: hidden
}

#page-404 {
	min-height: 680px;
	text-align: center;
	padding-top: 10%;
	color: #999
}

#page-404 h1 {
	text-shadow: -1px -1px 4px #666;
	font-size: 200px
}

#nprogress .bar {
	background: #108ee9
}

#nprogress .peg {
	box-shadow: 0 0 10px #108ee9,0 0 5px #108ee9
}

#nprogress .spinner-icon {
	border-top-color: #108ee9;
	border-left-color: #108ee9
}

.content-wrapper>.tween-one-leaving,.queue-anim-leaving {
	position: absolute!important;
	width: 100%
}

.video {
	max-width: 800px
}

.templates-wrapper {
	user-select: none
}

.is-edit * {
	pointer-events: none
}

#react-content {
	min-height: 100%
}

.content-template-wrapper {
	width: 100%;
	background: #fff;
	height: 100vh;
	border-color: #666;
	position: relative
}

.content-template-wrapper .content-template {
	width: 100%;
	max-width: 1200px;
	height: 100%;
	margin: auto;
	position: relative
}

.content-template-wrapper .content-template h1 {
	font-size: 32px;
	font-weight: 400;
	color: #404040;
	line-height: 48px
}

.content-template-wrapper .content-template>p {
	font-size: 12px;
	margin: 20px auto
}

.content-half-wrapper {
	height: 50vh
}

@media screen and (max-width:767px) {
	.content-template-wrapper .content-template h1 {
		font-size: 24px
	}
}

.header0 {
	height: 64px;
	background: rgba(51,51,51,.95);
	width: 100%;
	z-index: 970;
	box-shadow: 0 5px 8px rgba(0,0,0,.15);
	position: relative;
	top: 0
}

.header0-logo {
	display: inline-block;
	position: absolute;
	left: 4%;
	width: 150px;
	line-height: 64px
}

.header0-logo img {
	vertical-align: middle;
	display: inline-block
}

.header0-logo a {
	display: block
}

.header0-nav {
	float: right;
	margin-right: 4%;
	line-height: 64px;
	position: relative
}

.header0-nav .ant-menu-horizontal {
	border-bottom-color: transparent
}

.header0-nav .ant-menu {
	background: transparent;
	color: #fff;
	line-height: 62px
}

.header0-nav .ant-menu li {
	float: left;
	text-align: center;
	width: 100px
}

.header0-nav .ant-menu-horizontal>.ant-menu-item-active {
	color: #34aff3;
	border-bottom-color: #34aff3
}

@media screen and (max-width:767px) {
	.header0-logo {
		z-index: 101
	}

	.header0-phone-nav {
		width: 16px;
		height: 14px;
		cursor: pointer;
		position: absolute;
		top: 0;
		bottom: 0;
		margin: auto;
		right: 20px
	}

	.header0-phone-nav-bar {
		position: relative;
		z-index: 100
	}

	.header0-phone-nav-bar em {
		display: block;
		width: 100%;
		height: 2px;
		background: #fff;
		margin-top: 4px;
		transition: transform .3s cubic-bezier(.645,.045,.355,1),opacity .3s cubic-bezier(.645,.045,.355,1)
	}

	.header0-phone-nav-bar :first-child {
		margin-top: 0
	}

	.header0-phone-nav.open .header0-phone-nav-bar em:first-child {
		transform: translateY(6px) rotate(45deg)
	}

	.header0-phone-nav.open .header0-phone-nav-bar em:nth-child(2) {
		opacity: 0
	}

	.header0-phone-nav.open .header0-phone-nav-bar em:nth-child(3) {
		transform: translateY(-6px) rotate(-45deg)
	}

	.header0-phone-nav.open .header0-phone-nav-text {
		opacity: 1;
		pointer-events: auto;
		transition-timing-function: cubic-bezier(.215,.61,.355,1)
	}

	.header0-phone-nav-text {
		position: fixed;
		top: 0;
		right: 0;
		width: 100%;
		height: 100%;
		padding-top: 64px;
		opacity: 0;
		transition: opacity .3s cubic-bezier(.55,.055,.675,.19);
		pointer-events: none;
		background: #404040
	}

	.header0-phone-nav-text .ant-menu-item-selected {
		border: none
	}
}

.banner0 {
	width: 100%;
	height: 100vh;
	position: relative;
	text-align: center;
	border-color: #666
}

.banner0:before {
	background-image: url("https://images.seebug.org/ceye-bg.jpg");
	background-size: cover;
	background-position: 50%;
	position: fixed;
	display: block;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	width: 100%;
	height: 100%;
	content: "";
	z-index: -1
}

.banner0-wrapper {
	display: inline-block;
	position: absolute;
	top: 20%;
	margin: auto;
	left: 0;
	right: 0;
	font-size: 14px;
	color: #fff;
	width: 550px
}

.banner0-wrapper .queue-anim-leaving {
	position: relative!important;
	width: auto
}

.banner0-wrapper .title {
	width: 350px;
	left: 30px;
	margin: auto;
	display: inline-block;
	font-size: 40px;
	position: relative
}

.banner0-wrapper h1 {
	margin: 10px auto
}

.banner0-wrapper p {
	margin-bottom: 20px;
	word-wrap: break-word
}

.banner0-wrapper button {
	border: 1px solid #fff;
	color: #fff;
	background: transparent;
	box-shadow: 0 0 0 transparent;
	transition: background .45s cubic-bezier(.215,.61,.355,1),box-shadow .45s cubic-bezier(.215,.61,.355,1);
	line-height: 36px;
	font-size: 16px;
	height: 36px
}

.banner0-wrapper button span {
	text-shadow: 0 0 0 transparent;
	transition: text-shadow .45s cubic-bezier(.215,.61,.355,1)
}

.banner0-wrapper button:hover {
	color: #fff;
	border-color: #fff;
	background: hsla(0,0%,100%,.1);
	box-shadow: 0 0 10px rgba(50,250,255,.75)
}

.banner0-wrapper button:hover span {
	text-shadow: 1px 1px 3px rgba(0,0,0,.35)
}

.banner0-icon {
	bottom: 20px;
	font-size: 24px;
	position: absolute;
	left: 50%;
	margin-left: -12px;
	color: #fff
}

@media screen and (max-width:767px) {
	.banner0-wrapper {
		width: 90%
	}

	.banner0-wrapper .title {
		width: 90%;
		left: 0
	}

	.banner0:before {
		background-attachment: inherit
	}
}

.content0-img {
	height: 100%;
	width: 40%;
	overflow: hidden;
	position: absolute;
	left: 0
}

.content0-img span {
	display: inline-block;
	position: absolute;
	width: 55%;
	right: 10%;
	line-height: 50vh;
	height: 50vh;
	margin: auto;
	top: 0;
	bottom: 0
}

.content0-img span img {
	vertical-align: middle
}

.content0-text {
	display: block;
	width: 55%;
	height: 150px;
	vertical-align: top;
	position: absolute;
	top: 0;
	bottom: 0;
	margin: auto;
	right: 0
}

.content0-text h1,.content0-text p {
	position: relative!important;
	width: 75%
}

.content0-text h1 {
	font-size: 32px;
	font-weight: 400;
	color: #404040
}

.content0-text p {
	margin-top: 20px
}

@media screen and (max-width:767px) {
	.content0-wrapper {
		height: 400px
	}

	.content0-wrapper .content0 {
		overflow: hidden;
		width: 90%;
		margin: auto
	}

	.content0-wrapper .content0-img,.content0-wrapper .content0-text {
		width: 100%;
		display: block;
		position: relative;
		text-align: center
	}

	.content0-wrapper .content0-img {
		height: 200px;
		margin: 20px auto
	}

	.content0-wrapper .content0-img span {
		right: 0;
		left: 0;
		margin: auto;
		width: 180px;
		height: 200px;
		line-height: 200px
	}

	.content0-wrapper .content0-text {
		height: 140px;
		margin-bottom: 20px
	}

	.content0-wrapper .content0-text h1,.content0-wrapper .content0-text p {
		width: 100%;
		top: auto
	}

	.content0-wrapper .content0-text h1 {
		margin: 10px auto;
		font-size: 24px
	}
}

.content1-img {
	height: 100%;
	width: 40%;
	overflow: hidden;
	position: absolute;
	right: 0
}

.content1-img span {
	display: block;
	position: absolute;
	width: 55%;
	left: 10%;
	line-height: 50vh;
	height: 50vh;
	margin: auto;
	top: 0;
	bottom: 0
}

.content1-img span img {
	vertical-align: middle
}

.content1-text {
	display: block;
	width: 55%;
	height: 150px;
	vertical-align: top;
	position: absolute;
	top: 0;
	bottom: 0;
	margin: auto
}

.content1-text h1,.content1-text p {
	position: relative!important;
	width: 75%;
	float: right
}

.content1-text h1 {
	font-size: 32px;
	font-weight: 400;
	color: #404040
}

.content1-text p {
	margin-top: 20px
}

@media screen and (max-width:767px) {
	.content1-wrapper {
		height: 400px
	}

	.content1-wrapper .content1 {
		overflow: hidden;
		width: 90%;
		margin: auto
	}

	.content1-wrapper .content1-img,.content1-wrapper .content1-text {
		width: 100%;
		display: block;
		position: relative;
		text-align: center
	}

	.content1-wrapper .content1-img {
		margin: 20px auto;
		height: 200px
	}

	.content1-wrapper .content1-img span {
		right: 0;
		left: 0;
		margin: auto;
		width: 180px;
		height: 200px;
		line-height: 200px
	}

	.content1-wrapper .content1-text {
		height: 140px;
		margin-top: 20px
	}

	.content1-wrapper .content1-text h1,.content1-wrapper .content1-text p {
		width: 100%;
		top: auto
	}

	.content1-wrapper .content1-text p {
		margin-top: 20px
	}

	.content1-wrapper .content1-text h1 {
		font-size: 24px
	}
}

.content2>h1,.content2>p {
	text-align: center;
	position: relative;
	top: 15%
}

.content2-contentWrapper {
	position: relative;
	top: 20%;
	height: 60%
}

.content2-contentWrapper ul>li {
	display: inline-block;
	width: 33.33%;
	padding: 6% 5% 0;
	vertical-align: top
}

.content2-contentWrapper ul>li .img {
	display: inline-block;
	width: 15%;
	vertical-align: top
}

.content2-contentWrapper ul>li .text {
	width: 85%;
	display: inline-block;
	padding-left: 8%
}

@media screen and (max-width:767px) {
	.content2-wrapper {
		height: 920px
	}

	.content2-wrapper .content2 {
		overflow: hidden;
		width: 90%;
		margin: auto
	}

	.content2-wrapper .content2>h1,.content2-wrapper .content2>p {
		position: relative;
		top: auto
	}

	.content2-wrapper .content2>h1 {
		margin: 40px auto 20px;
		font-size: 24px
	}

	.content2-wrapper .content2-contentWrapper {
		top: auto;
		margin: 20px auto;
		height: auto
	}

	.content2-wrapper .content2-contentWrapper ul>li {
		position: relative;
		width: 90%;
		margin: auto;
		display: block
	}

	.content2-wrapper .content2-contentWrapper ul>li h1 {
		font-size: 20px
	}

	.content2-wrapper .content2-contentWrapper ul>li.queue-anim-leaving {
		position: relative!important
	}
}

.footer0 {
	background-color: #333;
	text-align: center;
	height: 80px;
	line-height: 80px;
	color: #666;
	overflow: hidden;
	position: relative
}

@media screen and (max-width:767px) {
	.footer0>div {
		width: 90%;
		margin: auto
	}
}

.footer-content {
	position: relative;
	text-align: center
}

.content-width {
	margin: 0 auto;
	padding: 0 13px;
	width: 1200px
}

.footer-left {
	position: absolute;
	left: 0;
	top: 0
}

.footer-right {
	position: absolute;
	left: auto;
	top: 0;
	right: 0;
	color: #aaa
}

.footer-logo {
	margin-right: 20px;
	vertical-align: middle
}

.footer-copyright {
	font-size: 12px;
	color: #aaa
}

.ant-spin {
	color: #108ee9;
	vertical-align: middle;
	text-align: center;
	opacity: 0;
	position: absolute;
	transition: -webkit-transform .3s cubic-bezier(.78,.14,.15,.86);
	transition: transform .3s cubic-bezier(.78,.14,.15,.86);
	transition: transform .3s cubic-bezier(.78,.14,.15,.86),-webkit-transform .3s cubic-bezier(.78,.14,.15,.86);
	font-size: 12px;
	display: none
}

.ant-spin-spinning {
	opacity: 1;
	position: static;
	display: inline-block
}

.ant-spin-nested-loading {
	position: relative
}

.ant-spin-nested-loading>div>.ant-spin {
	position: absolute;
	height: 100%;
	max-height: 320px;
	width: 100%;
	z-index: 4
}

.ant-spin-nested-loading>div>.ant-spin .ant-spin-dot {
	position: absolute;
	top: 50%;
	left: 50%;
	margin: -10px
}

.ant-spin-nested-loading>div>.ant-spin .ant-spin-text {
	position: absolute;
	top: 50%;
	width: 100%;
	padding-top: 6px
}

.ant-spin-nested-loading>div>.ant-spin.ant-spin-show-text .ant-spin-dot {
	margin-top: -20px
}

.ant-spin-nested-loading>div>.ant-spin-sm .ant-spin-dot {
	margin: -7px
}

.ant-spin-nested-loading>div>.ant-spin-sm .ant-spin-text {
	padding-top: 3px
}

.ant-spin-nested-loading>div>.ant-spin-sm.ant-spin-show-text .ant-spin-dot {
	margin-top: -17px
}

.ant-spin-nested-loading>div>.ant-spin-lg .ant-spin-dot {
	margin: -16px
}

.ant-spin-nested-loading>div>.ant-spin-lg .ant-spin-text {
	padding-top: 12px
}

.ant-spin-nested-loading>div>.ant-spin-lg.ant-spin-show-text .ant-spin-dot {
	margin-top: -26px
}

.ant-spin-container {
	position: relative
}

.ant-spin-blur {
	overflow: hidden;
	opacity: .7;
	-webkit-filter: blur(.5px);
	filter: blur(.5px);
	filter: progid\:DXImageTransform\.Microsoft\.Blur(PixelRadius\=1,MakeShadow\=false);
	-webkit-transform: translateZ(0)
}

.ant-spin-blur:after {
	content: "";
	position: absolute;
	left: 0;
	right: 0;
	top: 0;
	bottom: 0;
	background: #fff;
	opacity: .3;
	transition: all .3s;
	z-index: 10
}

.ant-spin-tip {
	color: rgba(0,0,0,.43)
}

.ant-spin-dot {
	position: relative;
	display: inline-block;
	width: 20px;
	height: 20px;
	-webkit-transform: rotate(45deg);
	-ms-transform: rotate(45deg);
	transform: rotate(45deg);
	-webkit-animation: antRotate 1.2s infinite linear;
	animation: antRotate 1.2s infinite linear
}

.ant-spin-dot i {
	width: 9px;
	height: 9px;
	border-radius: 100%;
	background-color: #108ee9;
	-webkit-transform: scale(.75);
	-ms-transform: scale(.75);
	transform: scale(.75);
	display: block;
	position: absolute;
	opacity: .3;
	-webkit-animation: antSpinMove 1s infinite linear alternate;
	animation: antSpinMove 1s infinite linear alternate;
	-webkit-transform-origin: 50% 50%;
	-ms-transform-origin: 50% 50%;
	transform-origin: 50% 50%
}

.ant-spin-dot i:first-child {
	left: 0;
	top: 0
}

.ant-spin-dot i:nth-child(2) {
	right: 0;
	top: 0;
	-webkit-animation-delay: .4s;
	animation-delay: .4s
}

.ant-spin-dot i:nth-child(3) {
	right: 0;
	bottom: 0;
	-webkit-animation-delay: .8s;
	animation-delay: .8s
}

.ant-spin-dot i:nth-child(4) {
	left: 0;
	bottom: 0;
	-webkit-animation-delay: 1.2s;
	animation-delay: 1.2s
}

.ant-spin-sm .ant-spin-dot {
	width: 14px;
	height: 14px
}

.ant-spin-sm .ant-spin-dot i {
	width: 6px;
	height: 6px
}

.ant-spin-lg .ant-spin-dot {
	width: 32px;
	height: 32px
}

.ant-spin-lg .ant-spin-dot i {
	width: 14px;
	height: 14px
}

.ant-spin.ant-spin-show-text .ant-spin-text {
	display: block
}

@media (-ms-high-contrast:active),(-ms-high-contrast:none) {
	.ant-spin-blur {
		background: #fff;
		opacity: .5
	}
}

@-webkit-keyframes antSpinMove {
	to {
		opacity: 1
	}
}

@keyframes antSpinMove {
	to {
		opacity: 1
	}
}

@-webkit-keyframes antRotate {
	to {
		-webkit-transform: rotate(405deg);
		transform: rotate(405deg)
	}
}

@keyframes antRotate {
	to {
		-webkit-transform: rotate(405deg);
		transform: rotate(405deg)
	}
}

.ant-input-search-icon {
	cursor: pointer;
	transition: all .3s;
	font-size: 14px
}

.ant-input-search-icon:hover {
	color: #108ee9
}

.ant-search-input-wrapper {
	display: inline-block;
	vertical-align: middle
}

.ant-search-input.ant-input-group .ant-input:first-child,.ant-search-input.ant-input-group .ant-select:first-child {
	border-radius: 4px;
	position: absolute;
	top: -1px;
	width: 100%
}

.ant-search-input.ant-input-group .ant-input:first-child {
	padding-right: 36px
}

.ant-search-input .ant-search-btn {
	color: rgba(0,0,0,.65);
	background-color: #fff;
	border-color: #d9d9d9;
	border-radius: 0 3px 3px 0;
	left: -1px;
	position: relative;
	border-width: 0 0 0 1px;
	z-index: 2;
	padding-left: 8px;
	padding-right: 8px
}

.ant-search-input .ant-search-btn>a:only-child {
	color: currentColor
}

.ant-search-input .ant-search-btn>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input .ant-search-btn:focus,.ant-search-input .ant-search-btn:hover {
	color: #108ee9;
	background-color: #fff;
	border-color: #108ee9
}

.ant-search-input .ant-search-btn:focus>a:only-child,.ant-search-input .ant-search-btn:hover>a:only-child {
	color: currentColor
}

.ant-search-input .ant-search-btn:focus>a:only-child:after,.ant-search-input .ant-search-btn:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input .ant-search-btn.active,.ant-search-input .ant-search-btn:active {
	color: #0e77ca;
	background-color: #fff;
	border-color: #0e77ca
}

.ant-search-input .ant-search-btn.active>a:only-child,.ant-search-input .ant-search-btn:active>a:only-child {
	color: currentColor
}

.ant-search-input .ant-search-btn.active>a:only-child:after,.ant-search-input .ant-search-btn:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input .ant-search-btn.disabled,.ant-search-input .ant-search-btn.disabled.active,.ant-search-input .ant-search-btn.disabled:active,.ant-search-input .ant-search-btn.disabled:focus,.ant-search-input .ant-search-btn.disabled:hover,.ant-search-input .ant-search-btn[disabled],.ant-search-input .ant-search-btn[disabled].active,.ant-search-input .ant-search-btn[disabled]:active,.ant-search-input .ant-search-btn[disabled]:focus,.ant-search-input .ant-search-btn[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-search-input .ant-search-btn.disabled.active>a:only-child,.ant-search-input .ant-search-btn.disabled:active>a:only-child,.ant-search-input .ant-search-btn.disabled:focus>a:only-child,.ant-search-input .ant-search-btn.disabled:hover>a:only-child,.ant-search-input .ant-search-btn.disabled>a:only-child,.ant-search-input .ant-search-btn[disabled].active>a:only-child,.ant-search-input .ant-search-btn[disabled]:active>a:only-child,.ant-search-input .ant-search-btn[disabled]:focus>a:only-child,.ant-search-input .ant-search-btn[disabled]:hover>a:only-child,.ant-search-input .ant-search-btn[disabled]>a:only-child {
	color: currentColor
}

.ant-search-input .ant-search-btn.disabled.active>a:only-child:after,.ant-search-input .ant-search-btn.disabled:active>a:only-child:after,.ant-search-input .ant-search-btn.disabled:focus>a:only-child:after,.ant-search-input .ant-search-btn.disabled:hover>a:only-child:after,.ant-search-input .ant-search-btn.disabled>a:only-child:after,.ant-search-input .ant-search-btn[disabled].active>a:only-child:after,.ant-search-input .ant-search-btn[disabled]:active>a:only-child:after,.ant-search-input .ant-search-btn[disabled]:focus>a:only-child:after,.ant-search-input .ant-search-btn[disabled]:hover>a:only-child:after,.ant-search-input .ant-search-btn[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input .ant-search-btn.active,.ant-search-input .ant-search-btn:active,.ant-search-input .ant-search-btn:focus,.ant-search-input .ant-search-btn:hover {
	background: #fff
}

.ant-search-input .ant-search-btn:hover {
	border-color: #d9d9d9
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty,.ant-search-input:hover .ant-search-btn-noempty {
	color: #fff;
	background-color: #108ee9;
	border-color: #108ee9
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty>a:only-child,.ant-search-input:hover .ant-search-btn-noempty>a:only-child {
	color: currentColor
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:focus,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:hover,.ant-search-input:hover .ant-search-btn-noempty:focus,.ant-search-input:hover .ant-search-btn-noempty:hover {
	color: #fff;
	background-color: #49a9ee;
	border-color: #49a9ee
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:focus>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:hover>a:only-child,.ant-search-input:hover .ant-search-btn-noempty:focus>a:only-child,.ant-search-input:hover .ant-search-btn-noempty:hover>a:only-child {
	color: currentColor
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:focus>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:hover>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty:focus>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty:hover>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.active,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:active,.ant-search-input:hover .ant-search-btn-noempty.active,.ant-search-input:hover .ant-search-btn-noempty:active {
	color: #fff;
	background-color: #0e77ca;
	border-color: #0e77ca
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.active>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:active>a:only-child,.ant-search-input:hover .ant-search-btn-noempty.active>a:only-child,.ant-search-input:hover .ant-search-btn-noempty:active>a:only-child {
	color: currentColor
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.active>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty:active>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty.active>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty:active>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled.active,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:active,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:focus,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:hover,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled],.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled].active,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:active,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:focus,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:hover,.ant-search-input:hover .ant-search-btn-noempty.disabled,.ant-search-input:hover .ant-search-btn-noempty.disabled.active,.ant-search-input:hover .ant-search-btn-noempty.disabled:active,.ant-search-input:hover .ant-search-btn-noempty.disabled:focus,.ant-search-input:hover .ant-search-btn-noempty.disabled:hover,.ant-search-input:hover .ant-search-btn-noempty[disabled],.ant-search-input:hover .ant-search-btn-noempty[disabled].active,.ant-search-input:hover .ant-search-btn-noempty[disabled]:active,.ant-search-input:hover .ant-search-btn-noempty[disabled]:focus,.ant-search-input:hover .ant-search-btn-noempty[disabled]:hover {
	color: rgba(0,0,0,.25);
	background-color: #f7f7f7;
	border-color: #d9d9d9
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled.active>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:active>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:focus>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:hover>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled].active>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:active>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:focus>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:hover>a:only-child,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]>a:only-child,.ant-search-input:hover .ant-search-btn-noempty.disabled.active>a:only-child,.ant-search-input:hover .ant-search-btn-noempty.disabled:active>a:only-child,.ant-search-input:hover .ant-search-btn-noempty.disabled:focus>a:only-child,.ant-search-input:hover .ant-search-btn-noempty.disabled:hover>a:only-child,.ant-search-input:hover .ant-search-btn-noempty.disabled>a:only-child,.ant-search-input:hover .ant-search-btn-noempty[disabled].active>a:only-child,.ant-search-input:hover .ant-search-btn-noempty[disabled]:active>a:only-child,.ant-search-input:hover .ant-search-btn-noempty[disabled]:focus>a:only-child,.ant-search-input:hover .ant-search-btn-noempty[disabled]:hover>a:only-child,.ant-search-input:hover .ant-search-btn-noempty[disabled]>a:only-child {
	color: currentColor
}

.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled.active>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:active>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:focus>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled:hover>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty.disabled>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled].active>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:active>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:focus>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]:hover>a:only-child:after,.ant-search-input.ant-search-input-focus .ant-search-btn-noempty[disabled]>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty.disabled.active>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty.disabled:active>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty.disabled:focus>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty.disabled:hover>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty.disabled>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty[disabled].active>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty[disabled]:active>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty[disabled]:focus>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty[disabled]:hover>a:only-child:after,.ant-search-input:hover .ant-search-btn-noempty[disabled]>a:only-child:after {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
	background: transparent
}

.ant-search-input .ant-select-combobox .ant-select-selection__rendered {
	margin-right: 29px
}

.ant-input {
	position: relative;
	display: inline-block;
	padding: 4px 7px;
	width: 100%;
	height: 28px;
	font-size: 12px;
	line-height: 1.5;
	color: rgba(0,0,0,.65);
	background-color: #fff;
	background-image: none;
	border: 1px solid #d9d9d9;
	border-radius: 4px;
	transition: all .3s
}

.ant-input::-moz-placeholder {
	color: rgba(0,0,0,.25);
	opacity: 1
}

.ant-input:-ms-input-placeholder {
	color: rgba(0,0,0,.25)
}

.ant-input::-webkit-input-placeholder {
	color: rgba(0,0,0,.25)
}

.ant-input:focus,.ant-input:hover {
	border-color: #49a9ee
}

.ant-input:focus {
	outline: 0;
	box-shadow: 0 0 0 2px rgba(16,142,233,.2)
}

.ant-input-disabled {
	background-color: #f7f7f7;
	opacity: 1;
	cursor: not-allowed;
	color: rgba(0,0,0,.25)
}

.ant-input-disabled:hover {
	border-color: #e2e2e2
}

textarea.ant-input {
	max-width: 100%;
	height: auto;
	vertical-align: bottom;
	transition: all .3s,height 0s
}

.ant-input-lg {
	padding: 6px 7px;
	height: 32px
}

.ant-input-sm {
	padding: 1px 7px;
	height: 22px
}

.ant-input-group {
	position: relative;
	display: table;
	border-collapse: separate;
	border-spacing: 0;
	width: 100%
}

.ant-input-group[class*=col-] {
	float: none;
	padding-left: 0;
	padding-right: 0
}

.ant-input-group>[class*=col-] {
	padding-right: 8px
}

.ant-input-group>[class*=col-]:last-child {
	padding-right: 0
}

.ant-input-group-addon,.ant-input-group-wrap,.ant-input-group>.ant-input {
	display: table-cell
}

.ant-input-group-addon:not(:first-child):not(:last-child),.ant-input-group-wrap:not(:first-child):not(:last-child),.ant-input-group>.ant-input:not(:first-child):not(:last-child) {
	border-radius: 0
}

.ant-input-group-addon,.ant-input-group-wrap {
	width: 1px;
	white-space: nowrap;
	vertical-align: middle
}

.ant-input-group-wrap>* {
	display: block!important
}

.ant-input-group .ant-input {
	float: left;
	width: 100%;
	margin-bottom: 0
}

.ant-input-group .ant-input:focus {
	z-index: 1
}

.ant-input-group-addon {
	padding: 4px 7px;
	font-size: 12px;
	font-weight: 400;
	line-height: 1;
	color: rgba(0,0,0,.65);
	text-align: center;
	background-color: #eee;
	border: 1px solid #d9d9d9;
	border-radius: 4px;
	position: relative;
	transition: all .3s
}

.ant-input-group-addon .ant-select {
	margin: -5px -7px
}

.ant-input-group-addon .ant-select .ant-select-selection {
	background-color: inherit;
	margin: -1px;
	border: 1px solid transparent;
	box-shadow: none
}

.ant-input-group-addon .ant-select-focused .ant-select-selection,.ant-input-group-addon .ant-select-open .ant-select-selection {
	color: #108ee9
}

.ant-input-group-addon>i:only-child:after {
	position: absolute;
	content: "";
	top: 0;
	left: 0;
	right: 0;
	bottom: 0
}

.ant-input-group-addon:first-child,.ant-input-group-addon:first-child .ant-select .ant-select-selection,.ant-input-group>.ant-input:first-child,.ant-input-group>.ant-input:first-child .ant-select .ant-select-selection {
	border-bottom-right-radius: 0;
	border-top-right-radius: 0
}

.ant-input-group>.ant-input-affix-wrapper:not(:first-child) .ant-input {
	border-bottom-left-radius: 0;
	border-top-left-radius: 0
}

.ant-input-group>.ant-input-affix-wrapper:not(:last-child) .ant-input {
	border-bottom-right-radius: 0;
	border-top-right-radius: 0
}

.ant-input-group-addon:first-child {
	border-right: 0
}

.ant-input-group-addon:last-child {
	border-left: 0
}

.ant-input-group-addon:last-child,.ant-input-group-addon:last-child .ant-select .ant-select-selection,.ant-input-group>.ant-input:last-child,.ant-input-group>.ant-input:last-child .ant-select .ant-select-selection {
	border-bottom-left-radius: 0;
	border-top-left-radius: 0
}

.ant-input-group-lg .ant-input,.ant-input-group-lg>.ant-input-group-addon {
	padding: 6px 7px;
	height: 32px
}

.ant-input-group-sm .ant-input,.ant-input-group-sm>.ant-input-group-addon {
	padding: 1px 7px;
	height: 22px
}

.ant-input-group-lg .ant-select-selection--single {
	height: 32px
}

.ant-input-group-sm .ant-select-selection--single {
	height: 22px
}

.ant-input-group .ant-input-affix-wrapper {
	display: table-cell;
	width: 100%;
	float: left
}

.ant-input-group.ant-input-group-compact {
	display: inline-block;
	zoom: 1
}

.ant-input-group.ant-input-group-compact:after,.ant-input-group.ant-input-group-compact:before {
	content: " ";
	display: table
}

.ant-input-group.ant-input-group-compact:after {
	clear: both;
	visibility: hidden;
	font-size: 0;
	height: 0
}

.ant-input-group.ant-input-group-compact>* {
	border-radius: 0;
	border-right-width: 0;
	vertical-align: middle;
	float: none;
	display: inline-block
}

.ant-input-group.ant-input-group-compact .ant-input {
	float: none;
	z-index: auto
}

.ant-input-group.ant-input-group-compact>.ant-calendar-picker .ant-input,.ant-input-group.ant-input-group-compact>.ant-cascader-picker .ant-input,.ant-input-group.ant-input-group-compact>.ant-mention-wrapper .ant-mention-editor,.ant-input-group.ant-input-group-compact>.ant-select-auto-complete .ant-input,.ant-input-group.ant-input-group-compact>.ant-select>.ant-select-selection,.ant-input-group.ant-input-group-compact>.ant-time-picker .ant-time-picker-input {
	border-radius: 0;
	border-right-width: 0
}

.ant-input-group.ant-input-group-compact>.ant-calendar-picker:first-child .ant-input,.ant-input-group.ant-input-group-compact>.ant-cascader-picker:first-child .ant-input,.ant-input-group.ant-input-group-compact>.ant-mention-wrapper:first-child .ant-mention-editor,.ant-input-group.ant-input-group-compact>.ant-select-auto-complete:first-child .ant-input,.ant-input-group.ant-input-group-compact>.ant-select:first-child>.ant-select-selection,.ant-input-group.ant-input-group-compact>.ant-time-picker:first-child .ant-time-picker-input,.ant-input-group.ant-input-group-compact>:first-child {
	border-top-left-radius: 4px;
	border-bottom-left-radius: 4px
}

.ant-input-group.ant-input-group-compact>.ant-calendar-picker:last-child .ant-input,.ant-input-group.ant-input-group-compact>.ant-cascader-picker:last-child .ant-input,.ant-input-group.ant-input-group-compact>.ant-mention-wrapper:last-child .ant-mention-editor,.ant-input-group.ant-input-group-compact>.ant-select-auto-complete:last-child .ant-input,.ant-input-group.ant-input-group-compact>.ant-select:last-child>.ant-select-selection,.ant-input-group.ant-input-group-compact>.ant-time-picker:last-child .ant-time-picker-input,.ant-input-group.ant-input-group-compact>:last-child {
	border-top-right-radius: 4px;
	border-bottom-right-radius: 4px;
	border-right-width: 1px
}

.ant-input-group-wrapper {
	display: inline-block;
	vertical-align: top;
	width: 100%
}

.ant-input-affix-wrapper {
	position: relative;
	display: inline-block;
	width: 100%
}

.ant-input-affix-wrapper .ant-input {
	z-index: 1
}

.ant-input-affix-wrapper:hover .ant-input:not(.ant-input-disabled) {
	border-color: #49a9ee
}

.ant-input-affix-wrapper .ant-input-prefix,.ant-input-affix-wrapper .ant-input-suffix {
	position: absolute;
	top: 50%;
	-webkit-transform: translateY(-50%);
	-ms-transform: translateY(-50%);
	transform: translateY(-50%);
	z-index: 2;
	line-height: 0;
	color: rgba(0,0,0,.65)
}

.ant-input-affix-wrapper .ant-input-prefix {
	left: 7px
}

.ant-input-affix-wrapper .ant-input-suffix {
	right: 7px
}

.ant-input-affix-wrapper .ant-input:not(:first-child) {
	padding-left: 24px
}

.ant-input-affix-wrapper .ant-input:not(:last-child) {
	padding-right: 24px
}

.ant-input-affix-wrapper .ant-input {
	min-height: 100%
}

.ant-tag {
	display: inline-block;
	line-height: 20px;
	height: 22px;
	padding: 0 8px;
	border-radius: 4px;
	border: 1px solid #e9e9e9;
	background: #f3f3f3;
	font-size: 12px;
	transition: all .3s cubic-bezier(.215,.61,.355,1);
	opacity: 1;
	margin-right: 8px;
	cursor: pointer;
	white-space: nowrap
}

.ant-tag:hover {
	opacity: .85
}

.ant-tag,.ant-tag a,.ant-tag a:hover {
	color: rgba(0,0,0,.65)
}

.ant-tag-text a:first-child:last-child {
	display: inline-block;
	margin: 0 -8px;
	padding: 0 8px
}

.ant-tag .anticon-cross {
	display: inline-block;
	font-size: 12px;
	font-size: 10px\9;
	-webkit-transform: scale(.83333333) rotate(0deg);
	-ms-transform: scale(.83333333) rotate(0deg);
	transform: scale(.83333333) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1;
	cursor: pointer;
	font-weight: 700;
	margin-left: 3px;
	transition: all .3s cubic-bezier(.215,.61,.355,1);
	opacity: .66
}

:root .ant-tag .anticon-cross {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-tag .anticon-cross:hover {
	opacity: 1
}

.ant-tag-has-color {
	border-color: transparent
}

.ant-tag-has-color,.ant-tag-has-color .anticon-cross,.ant-tag-has-color .anticon-cross:hover,.ant-tag-has-color a,.ant-tag-has-color a:hover {
	color: #fff
}

.ant-tag-checkable {
	background-color: transparent;
	border-color: transparent
}

.ant-tag-checkable:not(.ant-tag-checkable-checked):hover {
	color: #108ee9
}

.ant-tag-checkable-checked,.ant-tag-checkable:active {
	color: #fff
}

.ant-tag-checkable-checked {
	background-color: #108ee9
}

.ant-tag-checkable:active {
	background-color: #0e77ca
}

.ant-tag-close {
	width: 0!important;
	padding: 0;
	margin: 0
}

.ant-tag-zoom-appear,.ant-tag-zoom-enter {
	-webkit-animation: antFadeIn .2s cubic-bezier(.78,.14,.15,.86);
	animation: antFadeIn .2s cubic-bezier(.78,.14,.15,.86);
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both
}

.ant-tag-zoom-leave {
	-webkit-animation: antZoomOut .3s cubic-bezier(.78,.14,.15,.86);
	animation: antZoomOut .3s cubic-bezier(.78,.14,.15,.86);
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both
}

.ant-tag-pink {
	color: #f5317f;
	background: #fdd8e7;
	border-color: #fdd8e7
}

.ant-tag-pink-inverse {
	background: #f5317f;
	border-color: #f5317f;
	color: #fff
}

.ant-tag-red {
	color: #f04134;
	background: #fcdbd9;
	border-color: #fcdbd9
}

.ant-tag-red-inverse {
	background: #f04134;
	border-color: #f04134;
	color: #fff
}

.ant-tag-orange {
	color: #f56a00;
	background: #fde3cf;
	border-color: #fde3cf
}

.ant-tag-orange-inverse {
	background: #f56a00;
	border-color: #f56a00;
	color: #fff
}

.ant-tag-yellow {
	color: #ffbf00;
	background: #fff3cf;
	border-color: #fff3cf
}

.ant-tag-yellow-inverse {
	background: #ffbf00;
	border-color: #ffbf00;
	color: #fff
}

.ant-tag-cyan {
	color: #00a2ae;
	background: #cfedf0;
	border-color: #cfedf0
}

.ant-tag-cyan-inverse {
	background: #00a2ae;
	border-color: #00a2ae;
	color: #fff
}

.ant-tag-green {
	color: #00a854;
	background: #cfefdf;
	border-color: #cfefdf
}

.ant-tag-green-inverse {
	background: #00a854;
	border-color: #00a854;
	color: #fff
}

.ant-tag-blue {
	color: #108ee9;
	background: #d2eafb;
	border-color: #d2eafb
}

.ant-tag-blue-inverse {
	background: #108ee9;
	border-color: #108ee9;
	color: #fff
}

.ant-tag-purple {
	color: #7265e6;
	background: #e4e2fa;
	border-color: #e4e2fa
}

.ant-tag-purple-inverse {
	background: #7265e6;
	border-color: #7265e6;
	color: #fff
}

.ant-badge {
	position: relative;
	display: inline-block;
	line-height: 1;
	vertical-align: middle
}

.ant-badge-count {
	position: absolute;
	-webkit-transform: translateX(-50%);
	-ms-transform: translateX(-50%);
	transform: translateX(-50%);
	top: -10px;
	height: 20px;
	border-radius: 10px;
	min-width: 20px;
	background: #f04134;
	color: #fff;
	line-height: 20px;
	text-align: center;
	padding: 0 6px;
	font-size: 12px;
	white-space: nowrap;
	-webkit-transform-origin: -10% center;
	-ms-transform-origin: -10% center;
	transform-origin: -10% center;
	font-family: tahoma
}

.ant-badge-count a,.ant-badge-count a:hover {
	color: #fff
}

.ant-badge-dot {
	position: absolute;
	-webkit-transform: translateX(-50%);
	-ms-transform: translateX(-50%);
	transform: translateX(-50%);
	-webkit-transform-origin: 0 center;
	-ms-transform-origin: 0 center;
	transform-origin: 0 center;
	top: -4px;
	height: 8px;
	width: 8px;
	border-radius: 100%;
	background: #f04134;
	z-index: 10;
	box-shadow: 0 0 0 1px #fff
}

.ant-badge-status {
	line-height: inherit;
	vertical-align: baseline
}

.ant-badge-status-dot {
	width: 8px;
	height: 8px;
	display: inline-block;
	border-radius: 50%
}

.ant-badge-status-success {
	background-color: #00a854
}

.ant-badge-status-processing {
	background-color: #108ee9;
	position: relative
}

.ant-badge-status-processing:after {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	border-radius: 50%;
	border: 1px solid #108ee9;
	content: "";
	-webkit-animation: antStatusProcessing 1.2s infinite ease-in-out;
	animation: antStatusProcessing 1.2s infinite ease-in-out
}

.ant-badge-status-default {
	background-color: #d9d9d9
}

.ant-badge-status-error {
	background-color: #f04134
}

.ant-badge-status-warning {
	background-color: #ffbf00
}

.ant-badge-status-text {
	color: rgba(0,0,0,.65);
	font-size: 12px;
	margin-left: 8px
}

.ant-badge-zoom-appear,.ant-badge-zoom-enter {
	-webkit-animation: antZoomBadgeIn .3s cubic-bezier(.12,.4,.29,1.46);
	animation: antZoomBadgeIn .3s cubic-bezier(.12,.4,.29,1.46);
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both
}

.ant-badge-zoom-leave {
	-webkit-animation: antZoomBadgeOut .3s cubic-bezier(.71,-.46,.88,.6);
	animation: antZoomBadgeOut .3s cubic-bezier(.71,-.46,.88,.6);
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both
}

.ant-badge-not-a-wrapper .ant-badge-count {
	top: auto;
	display: block;
	position: relative;
	-webkit-transform: none!important;
	-ms-transform: none!important;
	transform: none!important
}

@-webkit-keyframes antStatusProcessing {
	0% {
		-webkit-transform: scale(.8);
		transform: scale(.8);
		opacity: .5
	}

	to {
		-webkit-transform: scale(2.4);
		transform: scale(2.4);
		opacity: 0
	}
}

@keyframes antStatusProcessing {
	0% {
		-webkit-transform: scale(.8);
		transform: scale(.8);
		opacity: .5
	}

	to {
		-webkit-transform: scale(2.4);
		transform: scale(2.4);
		opacity: 0
	}
}

.ant-scroll-number {
	overflow: hidden
}

.ant-scroll-number-only {
	display: inline-block;
	transition: all .3s cubic-bezier(.645,.045,.355,1);
	height: 20px
}

.ant-scroll-number-only>p {
	height: 20px
}

@-webkit-keyframes antZoomBadgeIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(0) translateX(-50%);
		transform: scale(0) translateX(-50%)
	}

	to {
		-webkit-transform: scale(1) translateX(-50%);
		transform: scale(1) translateX(-50%)
	}
}

@keyframes antZoomBadgeIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(0) translateX(-50%);
		transform: scale(0) translateX(-50%)
	}

	to {
		-webkit-transform: scale(1) translateX(-50%);
		transform: scale(1) translateX(-50%)
	}
}

@-webkit-keyframes antZoomBadgeOut {
	0% {
		-webkit-transform: scale(1) translateX(-50%);
		transform: scale(1) translateX(-50%)
	}

	to {
		opacity: 0;
		-webkit-transform: scale(0) translateX(-50%);
		transform: scale(0) translateX(-50%)
	}
}

@keyframes antZoomBadgeOut {
	0% {
		-webkit-transform: scale(1) translateX(-50%);
		transform: scale(1) translateX(-50%)
	}

	to {
		opacity: 0;
		-webkit-transform: scale(0) translateX(-50%);
		transform: scale(0) translateX(-50%)
	}
}

.profile .ant-row>div {
	background: transparent;
	border: 0
}

.profile-left,.profile-right {
	padding: 5px 0
}

.profile-info {
	padding: 42px;
	height: 500px;
	width: 380px;
	background: #fff;
	text-align: center
}

.profile-avatar {
	display: inline-block;
	width: 125px;
	height: 125px;
	border-radius: 50%;
	overflow: hidden;
	border: 0;
	font-size: 0
}

.profile-name {
	font-size: 24px;
	line-height: 1.5;
	font-weight: 700;
	color: #000
}

.profile-email {
	font-size: 14px;
	color: #888
}

.profile-operation {
	margin: 30px 24px;
	display: -ms-flexbox;
	display: flex;
	-ms-flex-pack: justify;
	justify-content: space-between
}

.profile-operate {
	width: 110px
}

.profile-deadline {
	position: relative;
	margin-bottom: 30px;
	text-align: left
}

.profile-deadline p {
	padding-bottom: 8px;
	height: 48px;
	line-height: 40px;
	border-bottom: 4px solid #9ca4bf
}

.profile-main {
	padding: 24px 48px
}

.profile-main h1 {
	margin: 15px 0;
	padding-left: 15px;
	height: 26px;
	line-height: 26px;
	border-left: 5px solid #267ce1;
	font-size: 24px
}

.profile-main-info-box {
	font-size: 14px;
	line-height: 48px
}

.profile-info-option {
	display: inline-block;
	width: 140px;
	color: #000
}

.profile-info-value {
	color: #888
}

.profile-badge .ant-badge-count {
	background-color: #929292
}

.ant-table-wrapper {
	zoom: 1
}

.ant-table-wrapper:after,.ant-table-wrapper:before {
	content: " ";
	display: table
}

.ant-table-wrapper:after {
	clear: both;
	visibility: hidden;
	font-size: 0;
	height: 0
}

.ant-table {
	font-size: 12px;
	color: rgba(0,0,0,.65);
	overflow: hidden;
	position: relative;
	border-radius: 4px 4px 0 0
}

.ant-table-body {
	transition: opacity .3s ease
}

.ant-table table {
	width: 100%;
	border-collapse: separate;
	border-spacing: 0;
	text-align: left;
	border-radius: 4px 4px 0 0;
	overflow: hidden
}

.ant-table-thead>tr>th {
	background: #f7f7f7;
	font-weight: 500;
	transition: background .3s ease;
	text-align: left;
	color: rgba(0,0,0,.85)
}

.ant-table-thead>tr>th[colspan] {
	text-align: center
}

.ant-table-thead>tr>th .ant-table-filter-icon,.ant-table-thead>tr>th .anticon-filter {
	position: relative;
	margin-left: 4px;
	font-size: 12px;
	cursor: pointer;
	color: #999;
	transition: all .3s;
	width: 14px
}

.ant-table-thead>tr>th .ant-table-filter-icon:hover,.ant-table-thead>tr>th .anticon-filter:hover {
	color: rgba(0,0,0,.65)
}

.ant-table-thead>tr>th .ant-table-filter-icon:after,.ant-table-thead>tr>th .anticon-filter:after {
	content: "";
	position: absolute;
	width: 14px;
	height: 50px;
	left: 0;
	top: -19px
}

.ant-table-thead>tr>th .ant-table-filter-selected.anticon-filter {
	color: #108ee9
}

.ant-table-tbody>tr>td {
	border-bottom: 1px solid #e9e9e9;
	transition: all .3s
}

.ant-table-tbody>tr,.ant-table-thead>tr {
	transition: all .3s
}

.ant-table-tbody>tr.ant-table-row-hover>td,.ant-table-tbody>tr:hover>td,.ant-table-thead>tr.ant-table-row-hover>td,.ant-table-thead>tr:hover>td {
	background: #ecf6fd
}

.ant-table-thead>tr:hover {
	background: none
}

.ant-table-footer {
	padding: 16px 8px;
	background: #f7f7f7;
	border-radius: 0 0 4px 4px;
	position: relative
}

.ant-table-footer:before {
	content: "";
	height: 1px;
	background: #f7f7f7;
	position: absolute;
	top: -1px;
	width: 100%;
	left: 0
}

.ant-table.ant-table-bordered .ant-table-footer {
	border: 1px solid #e9e9e9
}

.ant-table-title {
	padding: 16px 0;
	position: relative;
	top: 1px;
	border-radius: 4px 4px 0 0
}

.ant-table.ant-table-bordered .ant-table-title {
	border: 1px solid #e9e9e9;
	padding-left: 8px;
	padding-right: 8px
}

.ant-table-title+.ant-table-content {
	position: relative;
	border-radius: 4px 4px 0 0;
	overflow: hidden
}

.ant-table-bordered .ant-table-title+.ant-table-content,.ant-table-bordered .ant-table-title+.ant-table-content table,.ant-table-without-column-header .ant-table-title+.ant-table-content,.ant-table-without-column-header table {
	border-radius: 0
}

.ant-table-tbody>tr.ant-table-row-selected {
	background: #fafafa
}

.ant-table-thead>tr>th.ant-table-column-sort {
	background: #eee
}

.ant-table-tbody>tr>td,.ant-table-thead>tr>th {
	padding: 16px 8px;
	word-break: break-all
}

.ant-table-thead>tr>th.ant-table-selection-column-custom {
	padding-left: 16px;
	padding-right: 0
}

.ant-table-tbody>tr>td.ant-table-selection-column,.ant-table-thead>tr>th.ant-table-selection-column {
	text-align: center;
	min-width: 62px;
	width: 62px
}

.ant-table-expand-icon-th,.ant-table-row-expand-icon-cell {
	text-align: center;
	min-width: 50px;
	width: 50px
}

.ant-table-header {
	background: #f7f7f7;
	overflow: hidden
}

.ant-table-header table {
	border-radius: 4px 4px 0 0
}

.ant-table-loading {
	position: relative
}

.ant-table-loading .ant-table-body {
	background: #fff;
	opacity: .5
}

.ant-table-loading .ant-table-spin-holder {
	height: 20px;
	line-height: 20px;
	left: 50%;
	top: 50%;
	margin-left: -30px;
	position: absolute
}

.ant-table-loading .ant-table-with-pagination {
	margin-top: -20px
}

.ant-table-loading .ant-table-without-pagination {
	margin-top: 10px
}

.ant-table-middle .ant-table-footer,.ant-table-middle .ant-table-tbody>tr>td,.ant-table-middle .ant-table-thead>tr>th,.ant-table-middle .ant-table-title {
	padding: 10px 8px
}

.ant-table-middle .ant-table-column-sorter-up:after {
	top: -13px;
	height: 13px
}

.ant-table-middle .ant-table-column-sorter-down:after {
	bottom: -11px;
	height: 13px
}

.ant-table-middle .ant-table-thead>tr>th .ant-table-filter-icon:after,.ant-table-middle .ant-table-thead>tr>th .anticon-filter:after {
	height: 38px;
	top: -13px
}

.ant-table-small {
	border: 1px solid #e9e9e9;
	border-radius: 4px
}

.ant-table-small .ant-table-body>table,.ant-table-small .ant-table-header>table {
	border: 0;
	padding: 0 8px
}

.ant-table-small .ant-table-thead>tr>th {
	background: #fff;
	border-bottom: 1px solid #e9e9e9
}

.ant-table-small .ant-table-tbody>tr>td {
	padding: 6px 8px
}

.ant-table-small .ant-table-footer,.ant-table-small .ant-table-thead>tr>th,.ant-table-small .ant-table-title {
	padding: 10px 8px
}

.ant-table-small .ant-table-title {
	border-bottom: 1px solid #e9e9e9;
	top: 0
}

.ant-table-small .ant-table-header {
	background: #fff
}

.ant-table-small .ant-table-placeholder,.ant-table-small .ant-table-row:last-child td {
	border-bottom: 0
}

.ant-table-small .ant-table-column-sorter-up:after {
	top: -14px;
	height: 13px
}

.ant-table-small .ant-table-column-sorter-down:after {
	bottom: -11px;
	height: 13px
}

.ant-table-small .ant-table-thead>tr>th .ant-table-filter-icon:after,.ant-table-small .ant-table-thead>tr>th .anticon-filter:after {
	height: 39px;
	top: -14px
}

.ant-table-column-sorter {
	position: relative;
	margin-left: 4px;
	display: inline-block;
	width: 14px;
	height: 1em;
	vertical-align: middle;
	text-align: center
}

.ant-table-column-sorter-down,.ant-table-column-sorter-up {
	line-height: 4px;
	display: block;
	width: 14px;
	cursor: pointer
}

.ant-table-column-sorter-down:hover .anticon,.ant-table-column-sorter-up:hover .anticon {
	color: rgba(0,0,0,.65)
}

.ant-table-column-sorter-down.on .anticon-caret-down,.ant-table-column-sorter-down.on .anticon-caret-up,.ant-table-column-sorter-up.on .anticon-caret-down,.ant-table-column-sorter-up.on .anticon-caret-up {
	color: #108ee9
}

.ant-table-column-sorter-down:after,.ant-table-column-sorter-up:after {
	position: absolute;
	content: "";
	height: 20px;
	width: 14px;
	left: 0
}

.ant-table-column-sorter-up:after {
	top: -19px
}

.ant-table-column-sorter-down:after {
	bottom: -17px
}

.ant-table-column-sorter .anticon-caret-down,.ant-table-column-sorter .anticon-caret-up {
	display: inline-block;
	font-size: 12px;
	font-size: 8px\9;
	-webkit-transform: scale(.66666667) rotate(0deg);
	-ms-transform: scale(.66666667) rotate(0deg);
	transform: scale(.66666667) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1;
	line-height: 4px;
	height: 4px;
	color: #999;
	transition: all .3s
}

:root .ant-table-column-sorter .anticon-caret-down,:root .ant-table-column-sorter .anticon-caret-up {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-table-bordered .ant-table-body>table,.ant-table-bordered .ant-table-fixed-left table,.ant-table-bordered .ant-table-fixed-right table,.ant-table-bordered .ant-table-header>table {
	border: 1px solid #e9e9e9;
	border-right: 0;
	border-bottom: 0
}

.ant-table-bordered.ant-table-empty .ant-table-placeholder {
	border-left: 1px solid #e9e9e9;
	border-right: 1px solid #e9e9e9
}

.ant-table-bordered.ant-table-fixed-header .ant-table-header>table {
	border-bottom: 0
}

.ant-table-bordered.ant-table-fixed-header .ant-table-body>table {
	border-top: 0;
	border-top-left-radius: 0;
	border-top-right-radius: 0
}

.ant-table-bordered.ant-table-fixed-header .ant-table-body-inner>table {
	border-top: 0
}

.ant-table-bordered.ant-table-fixed-header .ant-table-placeholder {
	border: 0
}

.ant-table-bordered .ant-table-thead>tr>th {
	border-bottom: 1px solid #e9e9e9
}

.ant-table-bordered .ant-table-tbody>tr>td,.ant-table-bordered .ant-table-thead>tr>th {
	border-right: 1px solid #e9e9e9
}

.ant-table-bordered.ant-table-small {
	border-right: 0
}

.ant-table-bordered.ant-table-small .ant-table-body>table,.ant-table-bordered.ant-table-small .ant-table-fixed-left table,.ant-table-bordered.ant-table-small .ant-table-fixed-right table,.ant-table-bordered.ant-table-small .ant-table-header>table {
	border: 0;
	padding: 0
}

.ant-table-bordered.ant-table-small .ant-table-title {
	border: 0;
	border-bottom: 1px solid #e9e9e9;
	border-right: 1px solid #e9e9e9
}

.ant-table-bordered.ant-table-small .ant-table-footer {
	border: 0;
	border-top: 1px solid #e9e9e9;
	border-right: 1px solid #e9e9e9
}

.ant-table-bordered.ant-table-small .ant-table-footer:before {
	display: none
}

.ant-table-bordered.ant-table-small .ant-table-placeholder {
	border-left: 0;
	border-bottom: 0
}

.ant-table-placeholder {
	position: relative;
	padding: 16px 8px;
	background: #fff;
	border-bottom: 1px solid #e9e9e9;
	text-align: center;
	font-size: 12px;
	color: rgba(0,0,0,.43);
	z-index: 1
}

.ant-table-placeholder .anticon {
	margin-right: 4px
}

.ant-table-pagination {
	margin: 16px 0;
	float: right
}

.ant-table-filter-dropdown {
	min-width: 96px;
	margin-left: -8px;
	background: #fff;
	border-radius: 4px;
	box-shadow: 0 1px 6px rgba(0,0,0,.2)
}

.ant-table-filter-dropdown .ant-dropdown-menu {
	border: 0;
	box-shadow: none;
	border-radius: 4px 4px 0 0
}

.ant-table-filter-dropdown .ant-dropdown-menu-without-submenu {
	max-height: 400px;
	overflow-x: hidden
}

.ant-table-filter-dropdown .ant-dropdown-menu-item>label+span {
	padding: 0
}

.ant-table-filter-dropdown .ant-dropdown-menu-sub {
	border-radius: 4px;
	box-shadow: 0 1px 6px rgba(0,0,0,.2)
}

.ant-table-filter-dropdown .ant-dropdown-menu .ant-dropdown-submenu-contain-selected .ant-dropdown-menu-submenu-title:after {
	color: #108ee9;
	font-weight: 700;
	text-shadow: 0 0 2px #d2eafb
}

.ant-table-filter-dropdown .ant-dropdown-menu-item {
	overflow: hidden
}

.ant-table-filter-dropdown>.ant-dropdown-menu>.ant-dropdown-menu-item:last-child,.ant-table-filter-dropdown>.ant-dropdown-menu>.ant-dropdown-menu-submenu:last-child .ant-dropdown-menu-submenu-title {
	border-radius: 0
}

.ant-table-filter-dropdown-btns {
	overflow: hidden;
	padding: 7px 8px;
	border-top: 1px solid #e9e9e9
}

.ant-table-filter-dropdown-link {
	color: #108ee9
}

.ant-table-filter-dropdown-link:hover {
	color: #49a9ee
}

.ant-table-filter-dropdown-link:active {
	color: #0e77ca
}

.ant-table-filter-dropdown-link.confirm {
	float: left
}

.ant-table-filter-dropdown-link.clear {
	float: right
}

.ant-table-selection-select-all-custom {
	margin-right: 4px!important
}

.ant-table-selection .anticon-down {
	color: #999;
	transition: all .3s
}

.ant-table-selection-menu {
	min-width: 96px;
	margin-top: 5px;
	margin-left: -30px;
	background: #fff;
	border-radius: 4px;
	box-shadow: 0 1px 6px rgba(0,0,0,.2)
}

.ant-table-selection-menu .ant-action-down {
	color: #999
}

.ant-table-selection-down {
	cursor: pointer;
	padding: 0;
	display: inline-block;
	line-height: 1
}

.ant-table-selection-down:hover .anticon-down {
	color: #666
}

.ant-table-row-expand-icon {
	cursor: pointer;
	display: inline-block;
	width: 17px;
	height: 17px;
	text-align: center;
	line-height: 14px;
	border: 1px solid #e9e9e9;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	background: #fff
}

.ant-table-row-expanded:after {
	content: "-"
}

.ant-table-row-collapsed:after {
	content: "+"
}

.ant-table-row-spaced {
	visibility: hidden
}

.ant-table-row-spaced:after {
	content: "."
}

.ant-table-row[class*=ant-table-row-level-0] .ant-table-selection-column>span {
	display: inline-block
}

tr.ant-table-expanded-row,tr.ant-table-expanded-row:hover {
	background: #fbfbfb
}

.ant-table .ant-table-row-indent+.ant-table-row-expand-icon {
	margin-right: 8px
}

.ant-table-scroll {
	overflow: auto;
	overflow-x: hidden
}

.ant-table-scroll table {
	width: auto;
	min-width: 100%
}

.ant-table-body-inner {
	height: 100%
}

.ant-table-fixed-header>.ant-table-content>.ant-table-scroll>.ant-table-body {
	position: relative;
	background: #fff
}

.ant-table-fixed-header .ant-table-body-inner {
	overflow: scroll
}

.ant-table-fixed-header .ant-table-scroll .ant-table-header {
	overflow: scroll;
	padding-bottom: 20px;
	margin-bottom: -20px
}

.ant-table-fixed-left,.ant-table-fixed-right {
	position: absolute;
	top: 0;
	overflow: hidden;
	transition: box-shadow .3s ease;
	border-radius: 0
}

.ant-table-fixed-left table,.ant-table-fixed-right table {
	width: auto;
	background: #fff
}

.ant-table-fixed-header .ant-table-fixed-left .ant-table-body-outer .ant-table-fixed,.ant-table-fixed-header .ant-table-fixed-right .ant-table-body-outer .ant-table-fixed {
	border-radius: 0
}

.ant-table-fixed-left {
	left: 0;
	box-shadow: 6px 0 6px -4px rgba(0,0,0,.2)
}

.ant-table-fixed-left .ant-table-header {
	overflow-y: hidden
}

.ant-table-fixed-left .ant-table-body-inner {
	margin-right: -20px;
	padding-right: 20px
}

.ant-table-fixed-header .ant-table-fixed-left .ant-table-body-inner {
	padding-right: 0
}

.ant-table-fixed-left,.ant-table-fixed-left table {
	border-radius: 4px 0 0 0
}

.ant-table-fixed-right {
	right: 0;
	box-shadow: -6px 0 6px -4px rgba(0,0,0,.2)
}

.ant-table-fixed-right,.ant-table-fixed-right table {
	border-radius: 0 4px 0 0
}

.ant-table-fixed-right .ant-table-expanded-row {
	color: transparent;
	pointer-events: none
}

.ant-table.ant-table-scroll-position-left .ant-table-fixed-left,.ant-table.ant-table-scroll-position-right .ant-table-fixed-right {
	box-shadow: none
}

.ant-radio-group {
	display: inline-block;
	font-size: 12px
}

.ant-radio-wrapper {
	font-size: 12px;
	margin-right: 8px
}

.ant-radio,.ant-radio-wrapper {
	display: inline-block;
	position: relative;
	white-space: nowrap;
	cursor: pointer
}

.ant-radio {
	outline: none;
	line-height: 1;
	vertical-align: text-bottom
}

.ant-radio-focused .ant-radio-inner,.ant-radio-wrapper:hover .ant-radio .ant-radio-inner,.ant-radio:hover .ant-radio-inner {
	border-color: #108ee9
}

.ant-radio-checked:after {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	border-radius: 50%;
	border: 1px solid #108ee9;
	content: "";
	-webkit-animation: antRadioEffect .36s ease-in-out;
	animation: antRadioEffect .36s ease-in-out;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	visibility: hidden
}

.ant-radio-wrapper:hover .ant-radio:after,.ant-radio:hover:after {
	visibility: visible
}

.ant-radio-inner {
	position: relative;
	top: 0;
	left: 0;
	display: block;
	width: 14px;
	height: 14px;
	border-radius: 14px;
	border: 1px solid #d9d9d9;
	background-color: #fff;
	transition: all .3s
}

.ant-radio-inner:after {
	position: absolute;
	width: 6px;
	height: 6px;
	left: 3px;
	top: 3px;
	border-radius: 4px;
	display: table;
	border-top: 0;
	border-left: 0;
	content: " ";
	background-color: #108ee9;
	opacity: 0;
	-webkit-transform: scale(0);
	-ms-transform: scale(0);
	transform: scale(0);
	transition: all .3s cubic-bezier(.78,.14,.15,.86)
}

.ant-radio-input {
	position: absolute;
	left: 0;
	z-index: 1;
	cursor: pointer;
	opacity: 0;
	top: 0;
	bottom: 0;
	right: 0
}

.ant-radio-checked .ant-radio-inner {
	border-color: #108ee9
}

.ant-radio-checked .ant-radio-inner:after {
	-webkit-transform: scale(1);
	-ms-transform: scale(1);
	transform: scale(1);
	opacity: 1;
	transition: all .3s cubic-bezier(.78,.14,.15,.86)
}

.ant-radio-disabled .ant-radio-inner {
	border-color: #d9d9d9!important;
	background-color: #f7f7f7
}

.ant-radio-disabled .ant-radio-inner:after {
	background-color: #ccc
}

.ant-radio-disabled .ant-radio-input {
	cursor: not-allowed
}

.ant-radio-disabled+span {
	color: rgba(0,0,0,.25);
	cursor: not-allowed
}

span.ant-radio+* {
	padding-left: 8px;
	padding-right: 8px
}

.ant-radio-button-wrapper {
	margin: 0;
	height: 28px;
	line-height: 26px;
	color: rgba(0,0,0,.65);
	display: inline-block;
	transition: all .3s ease;
	cursor: pointer;
	border: 1px solid #d9d9d9;
	border-left: 0;
	background: #fff;
	padding: 0 16px;
	position: relative
}

.ant-radio-button-wrapper a {
	color: rgba(0,0,0,.65)
}

.ant-radio-button-wrapper>.ant-radio-button {
	margin-left: 0;
	display: block;
	width: 0;
	height: 0
}

.ant-radio-group-large .ant-radio-button-wrapper {
	height: 32px;
	line-height: 30px
}

.ant-radio-group-small .ant-radio-button-wrapper {
	height: 22px;
	line-height: 20px;
	padding: 0 12px
}

.ant-radio-group-small .ant-radio-button-wrapper:first-child {
	border-radius: 2px 0 0 2px
}

.ant-radio-group-small .ant-radio-button-wrapper:last-child {
	border-radius: 0 2px 2px 0
}

.ant-radio-button-wrapper:not(:first-child):before {
	content: "";
	display: block;
	top: 0;
	left: -1px;
	width: 1px;
	height: 100%;
	position: absolute;
	background-color: #d9d9d9
}

.ant-radio-button-wrapper:first-child {
	border-radius: 4px 0 0 4px;
	border-left: 1px solid #d9d9d9
}

.ant-radio-button-wrapper:last-child {
	border-radius: 0 4px 4px 0
}

.ant-radio-button-wrapper:first-child:last-child {
	border-radius: 4px
}

.ant-radio-button-wrapper-focused,.ant-radio-button-wrapper:hover {
	color: #108ee9;
	position: relative
}

.ant-radio-button-wrapper .ant-radio-inner,.ant-radio-button-wrapper input[type=checkbox],.ant-radio-button-wrapper input[type=radio] {
	opacity: 0;
	filter: alpha(opacity=0);
	width: 0;
	height: 0
}

.ant-radio-button-wrapper-checked {
	background: #fff;
	border-color: #108ee9;
	color: #108ee9;
	box-shadow: -1px 0 0 0 #108ee9;
	z-index: 1
}

.ant-radio-button-wrapper-checked:before {
	background-color: #108ee9!important;
	opacity: .1
}

.ant-radio-button-wrapper-checked:first-child {
	border-color: #108ee9;
	box-shadow: none!important
}

.ant-radio-button-wrapper-checked:hover {
	border-color: #49a9ee;
	box-shadow: -1px 0 0 0 #49a9ee;
	color: #49a9ee
}

.ant-radio-button-wrapper-checked:active {
	border-color: #0e77ca;
	box-shadow: -1px 0 0 0 #0e77ca;
	color: #0e77ca
}

.ant-radio-button-wrapper-disabled {
	cursor: not-allowed
}

.ant-radio-button-wrapper-disabled,.ant-radio-button-wrapper-disabled:first-child,.ant-radio-button-wrapper-disabled:hover {
	border-color: #d9d9d9;
	background-color: #f7f7f7;
	color: rgba(0,0,0,.25)
}

.ant-radio-button-wrapper-disabled:first-child {
	border-left-color: #d9d9d9
}

.ant-radio-button-wrapper-disabled.ant-radio-button-wrapper-checked {
	color: #fff;
	background-color: #e6e6e6;
	border-color: #d9d9d9;
	box-shadow: none
}

@-webkit-keyframes antRadioEffect {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1);
		opacity: .5
	}

	to {
		-webkit-transform: scale(1.6);
		transform: scale(1.6);
		opacity: 0
	}
}

@keyframes antRadioEffect {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1);
		opacity: .5
	}

	to {
		-webkit-transform: scale(1.6);
		transform: scale(1.6);
		opacity: 0
	}
}

@-webkit-keyframes antCheckboxEffect {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1);
		opacity: .5
	}

	to {
		-webkit-transform: scale(1.6);
		transform: scale(1.6);
		opacity: 0
	}
}

@keyframes antCheckboxEffect {
	0% {
		-webkit-transform: scale(1);
		transform: scale(1);
		opacity: .5
	}

	to {
		-webkit-transform: scale(1.6);
		transform: scale(1.6);
		opacity: 0
	}
}

.ant-checkbox {
	white-space: nowrap;
	cursor: pointer;
	outline: none;
	display: inline-block;
	line-height: 1;
	position: relative;
	vertical-align: text-bottom
}

.ant-checkbox-input:focus+.ant-checkbox-inner,.ant-checkbox-wrapper:hover .ant-checkbox-inner,.ant-checkbox:hover .ant-checkbox-inner {
	border-color: #108ee9
}

.ant-checkbox-checked:after {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	border-radius: 2px;
	border: 1px solid #108ee9;
	content: "";
	-webkit-animation: antCheckboxEffect .36s ease-in-out;
	animation: antCheckboxEffect .36s ease-in-out;
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both;
	visibility: hidden
}

.ant-checkbox-wrapper:hover .ant-checkbox:after,.ant-checkbox:hover:after {
	visibility: visible
}

.ant-checkbox-inner {
	position: relative;
	top: 0;
	left: 0;
	display: block;
	width: 14px;
	height: 14px;
	border: 1px solid #d9d9d9;
	border-radius: 2px;
	background-color: #fff;
	transition: all .3s
}

.ant-checkbox-inner:after {
	-webkit-transform: rotate(45deg) scale(0);
	-ms-transform: rotate(45deg) scale(0);
	transform: rotate(45deg) scale(0);
	position: absolute;
	left: 4px;
	top: 1px;
	display: table;
	width: 5px;
	height: 8px;
	border: 2px solid #fff;
	border-top: 0;
	border-left: 0;
	content: " ";
	transition: all .1s cubic-bezier(.71,-.46,.88,.6)
}

.ant-checkbox-input {
	position: absolute;
	left: 0;
	z-index: 1;
	cursor: pointer;
	opacity: 0;
	filter: alpha(opacity=0);
	top: 0;
	bottom: 0;
	right: 0;
	width: 100%;
	height: 100%
}

.ant-checkbox-indeterminate .ant-checkbox-inner:after {
	content: " ";
	-webkit-transform: scale(1);
	-ms-transform: scale(1);
	transform: scale(1);
	position: absolute;
	left: 2px;
	top: 5px;
	width: 8px;
	height: 1px
}

.ant-checkbox-indeterminate.ant-checkbox-disabled .ant-checkbox-inner:after {
	border-color: rgba(0,0,0,.25)
}

.ant-checkbox-checked .ant-checkbox-inner:after {
	-webkit-transform: rotate(45deg) scale(1);
	-ms-transform: rotate(45deg) scale(1);
	transform: rotate(45deg) scale(1);
	position: absolute;
	left: 4px;
	top: 1px;
	display: table;
	width: 5px;
	height: 8px;
	border: 2px solid #fff;
	border-top: 0;
	border-left: 0;
	content: " ";
	transition: all .2s cubic-bezier(.12,.4,.29,1.46) .1s
}

.ant-checkbox-checked .ant-checkbox-inner,.ant-checkbox-indeterminate .ant-checkbox-inner {
	background-color: #108ee9;
	border-color: #108ee9
}

.ant-checkbox-disabled {
	cursor: not-allowed
}

.ant-checkbox-disabled.ant-checkbox-checked .ant-checkbox-inner:after {
	-webkit-animation-name: none;
	animation-name: none;
	border-color: rgba(0,0,0,.25)
}

.ant-checkbox-disabled .ant-checkbox-input {
	cursor: not-allowed
}

.ant-checkbox-disabled .ant-checkbox-inner {
	border-color: #d9d9d9!important;
	background-color: #f7f7f7
}

.ant-checkbox-disabled .ant-checkbox-inner:after {
	-webkit-animation-name: none;
	animation-name: none;
	border-color: #f7f7f7
}

.ant-checkbox-disabled+span {
	color: rgba(0,0,0,.25);
	cursor: not-allowed
}

.ant-checkbox-wrapper {
	cursor: pointer;
	font-size: 12px;
	display: inline-block
}

.ant-checkbox-wrapper:not(:last-child) {
	margin-right: 8px
}

.ant-checkbox+span,.ant-checkbox-wrapper+span {
	padding-left: 8px;
	padding-right: 8px
}

.ant-checkbox-group {
	font-size: 12px
}

.ant-checkbox-group-item {
	display: inline-block
}

@media \0screen {
	.ant-checkbox-checked .ant-checkbox-inner:after,.ant-checkbox-checked .ant-checkbox-inner:before {
		font-family: anticon;
		text-rendering: optimizeLegibility;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		content: "\E632";
		font-weight: 700;
		font-size: 8px;
		border: 0;
		color: #fff;
		left: 2px;
		top: 3px;
		position: absolute
	}
}

.ant-pagination {
	font-size: 12px
}

.ant-pagination:after {
	content: " ";
	display: block;
	height: 0;
	clear: both;
	overflow: hidden;
	visibility: hidden
}

.ant-pagination-item,.ant-pagination-total-text {
	display: inline-block;
	vertical-align: middle;
	height: 28px;
	line-height: 28px;
	margin-right: 8px
}

.ant-pagination-item {
	cursor: pointer;
	border-radius: 4px;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	min-width: 28px;
	text-align: center;
	list-style: none;
	border: 1px solid #d9d9d9;
	background-color: #fff;
	font-family: Arial;
	outline: 0
}

.ant-pagination-item a {
	text-decoration: none;
	color: rgba(0,0,0,.65);
	transition: none;
	margin: 0 6px
}

.ant-pagination-item:focus,.ant-pagination-item:hover {
	transition: all .3s;
	border-color: #108ee9
}

.ant-pagination-item:focus a,.ant-pagination-item:hover a {
	color: #108ee9
}

.ant-pagination-item-active {
	background-color: #108ee9;
	border-color: #108ee9
}

.ant-pagination-item-active:focus,.ant-pagination-item-active:hover {
	background-color: #49a9ee;
	border-color: #49a9ee
}

.ant-pagination-item-active:focus a,.ant-pagination-item-active:hover a,.ant-pagination-item-active a {
	color: #fff
}

.ant-pagination-jump-next,.ant-pagination-jump-prev {
	outline: 0
}

.ant-pagination-jump-next:after,.ant-pagination-jump-prev:after {
	content: "\2022\2022\2022";
	display: block;
	letter-spacing: 2px;
	color: rgba(0,0,0,.25);
	text-align: center
}

.ant-pagination-jump-next:focus:after,.ant-pagination-jump-next:hover:after,.ant-pagination-jump-prev:focus:after,.ant-pagination-jump-prev:hover:after {
	color: #108ee9;
	display: inline-block;
	font-size: 12px;
	font-size: 8px\9;
	-webkit-transform: scale(.66666667) rotate(0deg);
	-ms-transform: scale(.66666667) rotate(0deg);
	transform: scale(.66666667) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1;
	letter-spacing: -1px;
	font-family: anticon
}

:root .ant-pagination-jump-next:focus:after,:root .ant-pagination-jump-next:hover:after,:root .ant-pagination-jump-prev:focus:after,:root .ant-pagination-jump-prev:hover:after {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-pagination-jump-prev:focus:after,.ant-pagination-jump-prev:hover:after {
	content: "\E620\E620"
}

.ant-pagination-jump-next:focus:after,.ant-pagination-jump-next:hover:after {
	content: "\E61F\E61F"
}

.ant-pagination-jump-next,.ant-pagination-jump-prev,.ant-pagination-prev {
	margin-right: 8px
}

.ant-pagination-jump-next,.ant-pagination-jump-prev,.ant-pagination-next,.ant-pagination-prev {
	font-family: Arial;
	cursor: pointer;
	color: rgba(0,0,0,.65);
	border-radius: 4px;
	list-style: none;
	min-width: 28px;
	height: 28px;
	line-height: 28px;
	text-align: center;
	transition: all .3s;
	display: inline-block;
	vertical-align: middle
}

.ant-pagination-next,.ant-pagination-prev {
	outline: 0
}

.ant-pagination-next a,.ant-pagination-prev a {
	color: rgba(0,0,0,.65);
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

.ant-pagination-next:hover a,.ant-pagination-prev:hover a {
	color: #108ee9
}

.ant-pagination-next .ant-pagination-item-link,.ant-pagination-prev .ant-pagination-item-link {
	border: 1px solid #d9d9d9;
	background-color: #fff;
	border-radius: 4px;
	outline: none;
	display: block;
	transition: all .3s
}

.ant-pagination-next .ant-pagination-item-link:after,.ant-pagination-prev .ant-pagination-item-link:after {
	display: inline-block;
	font-size: 12px;
	font-size: 8px\9;
	-webkit-transform: scale(.66666667) rotate(0deg);
	-ms-transform: scale(.66666667) rotate(0deg);
	transform: scale(.66666667) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1;
	display: block;
	height: 26px;
	line-height: 26px;
	font-family: anticon;
	text-align: center;
	font-weight: 500
}

:root .ant-pagination-next .ant-pagination-item-link:after,:root .ant-pagination-prev .ant-pagination-item-link:after {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-pagination-next:focus .ant-pagination-item-link,.ant-pagination-next:hover .ant-pagination-item-link,.ant-pagination-prev:focus .ant-pagination-item-link,.ant-pagination-prev:hover .ant-pagination-item-link {
	border-color: #108ee9;
	color: #108ee9
}

.ant-pagination-prev .ant-pagination-item-link:after {
	content: "\E620";
	display: block
}

.ant-pagination-next .ant-pagination-item-link:after {
	content: "\E61F";
	display: block
}

.ant-pagination-disabled,.ant-pagination-disabled:focus,.ant-pagination-disabled:hover {
	cursor: not-allowed
}

.ant-pagination-disabled .ant-pagination-item-link,.ant-pagination-disabled:focus .ant-pagination-item-link,.ant-pagination-disabled:focus a,.ant-pagination-disabled:hover .ant-pagination-item-link,.ant-pagination-disabled:hover a,.ant-pagination-disabled a {
	border-color: #d9d9d9;
	color: rgba(0,0,0,.25);
	cursor: not-allowed
}

.ant-pagination-slash {
	margin: 0 10px 0 5px
}

.ant-pagination-options {
	display: inline-block;
	vertical-align: middle;
	margin-left: 16px
}

.ant-pagination-options-size-changer {
	display: inline-block;
	margin-right: 8px
}

.ant-pagination-options-quick-jumper {
	display: inline-block;
	height: 28px;
	line-height: 28px
}

.ant-pagination-options-quick-jumper input {
	position: relative;
	display: inline-block;
	padding: 4px 7px;
	width: 100%;
	height: 28px;
	font-size: 12px;
	line-height: 1.5;
	color: rgba(0,0,0,.65);
	background-color: #fff;
	background-image: none;
	border: 1px solid #d9d9d9;
	border-radius: 4px;
	transition: all .3s;
	margin: 0 8px;
	width: 50px
}

.ant-pagination-options-quick-jumper input::-moz-placeholder {
	color: rgba(0,0,0,.25);
	opacity: 1
}

.ant-pagination-options-quick-jumper input:-ms-input-placeholder {
	color: rgba(0,0,0,.25)
}

.ant-pagination-options-quick-jumper input::-webkit-input-placeholder {
	color: rgba(0,0,0,.25)
}

.ant-pagination-options-quick-jumper input:hover {
	border-color: #49a9ee
}

.ant-pagination-options-quick-jumper input:focus {
	border-color: #49a9ee;
	outline: 0;
	box-shadow: 0 0 0 2px rgba(16,142,233,.2)
}

.ant-pagination-options-quick-jumper input-disabled {
	background-color: #f7f7f7;
	opacity: 1;
	cursor: not-allowed;
	color: rgba(0,0,0,.25)
}

.ant-pagination-options-quick-jumper input-disabled:hover {
	border-color: #e2e2e2
}

textarea.ant-pagination-options-quick-jumper input {
	max-width: 100%;
	height: auto;
	vertical-align: bottom;
	transition: all .3s,height 0s
}

.ant-pagination-options-quick-jumper input-lg {
	padding: 6px 7px;
	height: 32px
}

.ant-pagination-options-quick-jumper input-sm {
	padding: 1px 7px;
	height: 22px
}

.ant-pagination-simple .ant-pagination-next,.ant-pagination-simple .ant-pagination-prev {
	height: 24px;
	line-height: 24px;
	vertical-align: top
}

.ant-pagination-simple .ant-pagination-next .ant-pagination-item-link,.ant-pagination-simple .ant-pagination-prev .ant-pagination-item-link {
	border: 0;
	height: 24px
}

.ant-pagination-simple .ant-pagination-next .ant-pagination-item-link:after,.ant-pagination-simple .ant-pagination-prev .ant-pagination-item-link:after {
	line-height: 24px
}

.ant-pagination-simple .ant-pagination-simple-pager {
	display: inline-block;
	margin-right: 8px
}

.ant-pagination-simple .ant-pagination-simple-pager input {
	margin-right: 8px;
	box-sizing: border-box;
	background-color: #fff;
	border-radius: 4px;
	border: 1px solid #d9d9d9;
	outline: none;
	padding: 0 6px;
	height: 24px;
	text-align: center;
	transition: border-color .3s
}

.ant-pagination-simple .ant-pagination-simple-pager input:hover {
	border-color: #108ee9
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-total-text {
	height: 20px;
	line-height: 20px
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-item {
	border: 0;
	margin: 0;
	min-width: 20px;
	height: 20px;
	line-height: 20px
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-next,.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-prev {
	margin: 0;
	min-width: 20px;
	height: 20px;
	line-height: 20px
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-next .ant-pagination:not(.ant-pagination-simple)-item-link,.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-prev .ant-pagination:not(.ant-pagination-simple)-item-link {
	border: 0
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-jump-next,.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-jump-prev,.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-next .ant-pagination:not(.ant-pagination-simple)-item-link:after,.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-prev .ant-pagination:not(.ant-pagination-simple)-item-link:after {
	height: 20px;
	line-height: 20px
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-options {
	margin-left: 8px
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-options-quick-jumper {
	height: 20px;
	line-height: 20px
}

.ant-pagination:not(.ant-pagination-simple).mini .ant-pagination:not(.ant-pagination-simple)-options-quick-jumper input {
	padding: 1px 7px;
	height: 22px;
	width: 44px
}

@media only screen and (max-width:1024px) {
	.ant-pagination-item-after-jump-prev,.ant-pagination-item-before-jump-next {
		display: none
	}
}

.ant-select {
	box-sizing: border-box;
	display: inline-block;
	position: relative;
	color: rgba(0,0,0,.65);
	font-size: 12px
}

.ant-select>ul>li>a {
	padding: 0;
	background-color: #fff
}

.ant-select-arrow {
	font-style: normal;
	vertical-align: baseline;
	text-align: center;
	text-transform: none;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	position: absolute;
	top: 50%;
	right: 8px;
	line-height: 1;
	margin-top: -6px;
	color: rgba(0,0,0,.43);
	display: inline-block;
	font-size: 12px;
	font-size: 9px\9;
	-webkit-transform: scale(.75) rotate(0deg);
	-ms-transform: scale(.75) rotate(0deg);
	transform: scale(.75) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1
}

.ant-select-arrow:before {
	display: block;
	font-family: anticon!important
}

:root .ant-select-arrow {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-select-arrow * {
	display: none
}

.ant-select-arrow:before {
	content: "\E61D";
	transition: -webkit-transform .2s ease;
	transition: transform .2s ease;
	transition: transform .2s ease,-webkit-transform .2s ease
}

.ant-select-selection {
	outline: none;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	box-sizing: border-box;
	display: block;
	background-color: #fff;
	border-radius: 4px;
	border: 1px solid #d9d9d9;
	transition: all .3s cubic-bezier(.645,.045,.355,1)
}

.ant-select-selection:hover {
	border-color: #49a9ee
}

.ant-select-focused .ant-select-selection,.ant-select-selection:active,.ant-select-selection:focus {
	border-color: #49a9ee;
	outline: 0;
	box-shadow: 0 0 0 2px rgba(16,142,233,.2)
}

.ant-select-selection__clear {
	display: inline-block;
	font-style: normal;
	vertical-align: baseline;
	text-align: center;
	text-transform: none;
	text-rendering: auto;
	opacity: 0;
	position: absolute;
	right: 8px;
	z-index: 1;
	background: #fff;
	top: 50%;
	font-size: 12px;
	color: rgba(0,0,0,.25);
	width: 12px;
	height: 12px;
	margin-top: -6px;
	line-height: 12px;
	cursor: pointer;
	transition: color .3s ease,opacity .15s ease
}

.ant-select-selection__clear:before {
	display: block;
	font-family: anticon;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	content: "\E62E"
}

.ant-select-selection__clear:hover {
	color: rgba(0,0,0,.43)
}

.ant-select-selection:hover .ant-select-selection__clear {
	opacity: 1
}

.ant-select-selection-selected-value {
	float: left;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	max-width: 100%;
	padding-right: 14px
}

.ant-select-disabled {
	color: rgba(0,0,0,.25)
}

.ant-select-disabled .ant-select-selection {
	background: #f7f7f7;
	cursor: not-allowed
}

.ant-select-disabled .ant-select-selection:active,.ant-select-disabled .ant-select-selection:focus,.ant-select-disabled .ant-select-selection:hover {
	border-color: #d9d9d9;
	box-shadow: none
}

.ant-select-disabled .ant-select-selection__clear {
	display: none;
	visibility: hidden;
	pointer-events: none
}

.ant-select-disabled .ant-select-selection--multiple .ant-select-selection__choice {
	background: #eee;
	color: #aaa;
	padding-right: 10px
}

.ant-select-disabled .ant-select-selection--multiple .ant-select-selection__choice__remove {
	display: none
}

.ant-select-selection--single {
	height: 28px;
	position: relative;
	cursor: pointer
}

.ant-select-selection__rendered {
	display: block;
	margin-left: 7px;
	margin-right: 7px;
	position: relative;
	line-height: 26px
}

.ant-select-selection__rendered:after {
	content: ".";
	visibility: hidden;
	pointer-events: none;
	display: inline-block;
	width: 0
}

.ant-select-lg .ant-select-selection--single {
	height: 32px
}

.ant-select-lg .ant-select-selection__rendered {
	line-height: 30px
}

.ant-select-lg .ant-select-selection--multiple {
	min-height: 32px
}

.ant-select-lg .ant-select-selection--multiple .ant-select-selection__rendered li {
	height: 24px;
	line-height: 24px
}

.ant-select-lg .ant-select-selection--multiple .ant-select-selection__clear {
	top: 16px
}

.ant-select-sm .ant-select-selection--single {
	height: 22px
}

.ant-select-sm .ant-select-selection__rendered {
	line-height: 20px
}

.ant-select-sm .ant-select-selection--multiple {
	min-height: 22px
}

.ant-select-sm .ant-select-selection--multiple .ant-select-selection__rendered li {
	height: 14px;
	line-height: 14px
}

.ant-select-sm .ant-select-selection--multiple .ant-select-selection__clear {
	top: 11px
}

.ant-select-disabled .ant-select-selection__choice__remove {
	color: rgba(0,0,0,.25);
	cursor: default
}

.ant-select-disabled .ant-select-selection__choice__remove:hover {
	color: rgba(0,0,0,.25)
}

.ant-select-search__field__wrap {
	display: inline-block;
	position: relative
}

.ant-select-search__field__placeholder,.ant-select-selection__placeholder {
	position: absolute;
	top: 50%;
	left: 0;
	right: 9px;
	color: rgba(0,0,0,.25);
	line-height: 20px;
	height: 20px;
	max-width: 100%;
	margin-top: -10px;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	text-align: left
}

.ant-select-search__field__placeholder {
	left: 8px
}

.ant-select-search--inline {
	position: absolute;
	height: 100%;
	width: 100%
}

.ant-select-selection--multiple .ant-select-search--inline {
	float: left;
	position: static
}

.ant-select-search--inline .ant-select-search__field__wrap {
	width: 100%;
	height: 100%
}

.ant-select-search--inline .ant-select-search__field {
	border-width: 0;
	font-size: 100%;
	height: 100%;
	width: 100%;
	background: transparent;
	outline: 0;
	border-radius: 4px
}

.ant-select-search--inline .ant-select-search__field__mirror {
	position: absolute;
	top: 0;
	left: -9999px;
	white-space: pre;
	pointer-events: none
}

.ant-select-search--inline>i {
	float: right
}

.ant-select-selection--multiple {
	min-height: 28px;
	cursor: text;
	padding-bottom: 3px;
	zoom: 1
}

.ant-select-selection--multiple:after,.ant-select-selection--multiple:before {
	content: " ";
	display: table
}

.ant-select-selection--multiple:after {
	clear: both;
	visibility: hidden;
	font-size: 0;
	height: 0
}

.ant-select-selection--multiple .ant-select-search--inline {
	width: auto;
	padding: 0;
	max-width: 100%
}

.ant-select-selection--multiple .ant-select-search--inline .ant-select-search__field {
	max-width: 100%;
	width: .75em
}

.ant-select-selection--multiple .ant-select-selection__rendered {
	margin-left: 5px;
	margin-bottom: -3px;
	height: auto
}

.ant-select-selection--multiple .ant-select-selection__rendered>ul>li,.ant-select-selection--multiple>ul>li {
	margin-top: 3px;
	height: 20px;
	line-height: 20px
}

.ant-select-selection--multiple .ant-select-selection__choice {
	color: rgba(0,0,0,.65);
	background-color: #f3f3f3;
	border-radius: 4px;
	cursor: default;
	float: left;
	margin-right: 4px;
	max-width: 99%;
	position: relative;
	overflow: hidden;
	transition: padding .3s cubic-bezier(.645,.045,.355,1);
	padding: 0 20px 0 10px
}

.ant-select-selection--multiple .ant-select-selection__choice__disabled {
	padding: 0 10px
}

.ant-select-selection--multiple .ant-select-selection__choice__content {
	display: inline-block;
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
	max-width: 100%;
	transition: margin .3s cubic-bezier(.645,.045,.355,1)
}

.ant-select-selection--multiple .ant-select-selection__choice__remove {
	font-style: normal;
	vertical-align: baseline;
	text-align: center;
	text-transform: none;
	line-height: 1;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: rgba(0,0,0,.43);
	line-height: inherit;
	cursor: pointer;
	font-weight: 700;
	transition: all .3s cubic-bezier(.645,.045,.355,1);
	display: inline-block;
	font-size: 12px;
	font-size: 8px\9;
	-webkit-transform: scale(.66666667) rotate(0deg);
	-ms-transform: scale(.66666667) rotate(0deg);
	transform: scale(.66666667) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1;
	position: absolute;
	right: 4px;
	padding: 0 0 0 8px
}

.ant-select-selection--multiple .ant-select-selection__choice__remove:before {
	display: block;
	font-family: anticon!important
}

:root .ant-select-selection--multiple .ant-select-selection__choice__remove {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-select-selection--multiple .ant-select-selection__choice__remove:hover {
	color: #404040
}

.ant-select-selection--multiple .ant-select-selection__choice__remove:before {
	content: "\E633"
}

.ant-select-selection--multiple .ant-select-selection__clear {
	top: 14px
}

.ant-select-allow-clear .ant-select-selection--multiple .ant-select-selection__rendered {
	margin-right: 20px
}

.ant-select-open .ant-select-arrow {
	-ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
	-ms-transform: rotate(180deg)
}

.ant-select-open .ant-select-arrow:before {
	-webkit-transform: rotate(180deg);
	-ms-transform: rotate(180deg);
	transform: rotate(180deg)
}

.ant-select-open .ant-select-selection {
	border-color: #49a9ee;
	outline: 0;
	box-shadow: 0 0 0 2px rgba(16,142,233,.2)
}

.ant-select-combobox .ant-select-arrow {
	display: none
}

.ant-select-combobox .ant-select-search--inline {
	height: 100%;
	width: 100%;
	float: none
}

.ant-select-combobox .ant-select-search__field__wrap {
	width: 100%;
	height: 100%
}

.ant-select-combobox .ant-select-search__field {
	width: 100%;
	height: 100%;
	position: relative;
	z-index: 1;
	transition: all .3s cubic-bezier(.645,.045,.355,1);
	box-shadow: none
}

.ant-select-combobox.ant-select-allow-clear .ant-select-selection:hover .ant-select-selection__rendered {
	margin-right: 20px
}

.ant-select-dropdown {
	background-color: #fff;
	box-shadow: 0 1px 6px rgba(0,0,0,.2);
	border-radius: 4px;
	box-sizing: border-box;
	z-index: 1050;
	left: -9999px;
	top: -9999px;
	position: absolute;
	outline: none;
	overflow: hidden;
	font-size: 12px
}

.ant-select-dropdown.slide-up-appear.slide-up-appear-active.ant-select-dropdown-placement-bottomLeft,.ant-select-dropdown.slide-up-enter.slide-up-enter-active.ant-select-dropdown-placement-bottomLeft {
	-webkit-animation-name: antSlideUpIn;
	animation-name: antSlideUpIn
}

.ant-select-dropdown.slide-up-appear.slide-up-appear-active.ant-select-dropdown-placement-topLeft,.ant-select-dropdown.slide-up-enter.slide-up-enter-active.ant-select-dropdown-placement-topLeft {
	-webkit-animation-name: antSlideDownIn;
	animation-name: antSlideDownIn
}

.ant-select-dropdown.slide-up-leave.slide-up-leave-active.ant-select-dropdown-placement-bottomLeft {
	-webkit-animation-name: antSlideUpOut;
	animation-name: antSlideUpOut
}

.ant-select-dropdown.slide-up-leave.slide-up-leave-active.ant-select-dropdown-placement-topLeft {
	-webkit-animation-name: antSlideDownOut;
	animation-name: antSlideDownOut
}

.ant-select-dropdown-hidden {
	display: none
}

.ant-select-dropdown-menu {
	outline: none;
	margin-bottom: 0;
	padding-left: 0;
	list-style: none;
	max-height: 250px;
	overflow: auto
}

.ant-select-dropdown-menu-item-group-list {
	margin: 0;
	padding: 0
}

.ant-select-dropdown-menu-item-group-list>.ant-select-dropdown-menu-item {
	padding-left: 16px
}

.ant-select-dropdown-menu-item-group-title {
	color: rgba(0,0,0,.43);
	line-height: 1.5;
	padding: 8px
}

.ant-select-dropdown-menu-item {
	position: relative;
	display: block;
	padding: 7px 8px;
	font-weight: 400;
	color: rgba(0,0,0,.65);
	white-space: nowrap;
	cursor: pointer;
	overflow: hidden;
	transition: background .3s ease
}

.ant-select-dropdown-menu-item:hover {
	background-color: #ecf6fd
}

.ant-select-dropdown-menu-item-disabled {
	color: rgba(0,0,0,.25);
	cursor: not-allowed
}

.ant-select-dropdown-menu-item-disabled:hover {
	color: rgba(0,0,0,.25);
	background-color: #fff;
	cursor: not-allowed
}

.ant-select-dropdown-menu-item-selected,.ant-select-dropdown-menu-item-selected:hover {
	background-color: #f7f7f7;
	font-weight: 600;
	color: rgba(0,0,0,.65)
}

.ant-select-dropdown-menu-item-active {
	background-color: #ecf6fd
}

.ant-select-dropdown-menu-item-divider {
	height: 1px;
	margin: 1px 0;
	overflow: hidden;
	background-color: #e5e5e5;
	line-height: 0
}

.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item:after {
	font-family: anticon;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	content: "\E632";
	color: transparent;
	display: inline-block;
	font-size: 12px;
	font-size: 10px\9;
	-webkit-transform: scale(.83333333) rotate(0deg);
	-ms-transform: scale(.83333333) rotate(0deg);
	transform: scale(.83333333) rotate(0deg);
	-ms-filter: "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=1, M12=0, M21=0, M22=1)";
	zoom: 1;
	transition: all .2s ease;
	position: absolute;
	top: 50%;
	-webkit-transform: translateY(-50%);
	-ms-transform: translateY(-50%);
	transform: translateY(-50%);
	right: 8px;
	font-weight: 700;
	text-shadow: 0 .1px 0,.1px 0 0,0 -.1px 0,-.1px 0
}

:root .ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item:after {
	-webkit-filter: none;
	filter: none;
	font-size: 12px
}

.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item:hover:after {
	color: #ddd
}

.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item-disabled:after {
	display: none
}

.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item-selected:after,.ant-select-dropdown.ant-select-dropdown--multiple .ant-select-dropdown-menu-item-selected:hover:after {
	color: #108ee9;
	display: inline-block
}

.ant-select-dropdown-container-open .ant-select-dropdown,.ant-select-dropdown-open .ant-select-dropdown {
	display: block
}

.ant-popover {
	position: absolute;
	top: 0;
	left: 0;
	z-index: 1030;
	cursor: auto;
	-webkit-user-select: text;
	-moz-user-select: text;
	-ms-user-select: text;
	user-select: text;
	white-space: normal;
	font-size: 12px;
	line-height: 1.5;
	font-weight: 400;
	text-align: left
}

.ant-popover:after {
	content: "";
	position: absolute;
	background: hsla(0,0%,100%,.01)
}

.ant-popover-hidden {
	display: none
}

.ant-popover-placement-top,.ant-popover-placement-topLeft,.ant-popover-placement-topRight {
	padding-bottom: 8px
}

.ant-popover-placement-right,.ant-popover-placement-rightBottom,.ant-popover-placement-rightTop {
	padding-left: 8px
}

.ant-popover-placement-bottom,.ant-popover-placement-bottomLeft,.ant-popover-placement-bottomRight {
	padding-top: 8px
}

.ant-popover-placement-left,.ant-popover-placement-leftBottom,.ant-popover-placement-leftTop {
	padding-right: 8px
}

.ant-popover-inner {
	background-color: #fff;
	background-clip: padding-box;
	border-radius: 4px;
	box-shadow: 0 1px 6px rgba(0,0,0,.2)
}

.ant-popover-title {
	min-width: 177px;
	margin: 0;
	min-height: 32px;
	border-bottom: 1px solid #e9e9e9;
	font-weight: 500
}

.ant-popover-inner-content,.ant-popover-title {
	padding: 8px 16px;
	color: rgba(0,0,0,.65)
}

.ant-popover-message {
	padding: 8px 0 16px;
	font-size: 12px;
	color: rgba(0,0,0,.65)
}

.ant-popover-message>.anticon {
	color: #ffbf00;
	line-height: 17px;
	position: absolute
}

.ant-popover-message-title {
	padding-left: 20px
}

.ant-popover-buttons {
	text-align: right;
	margin-bottom: 8px
}

.ant-popover-buttons button {
	margin-left: 8px
}

.ant-popover-arrow,.ant-popover-arrow:after {
	position: absolute;
	display: block;
	width: 0;
	height: 0;
	border-color: transparent;
	border-style: solid
}

.ant-popover-arrow {
	border-width: 5px
}

.ant-popover-arrow:after {
	border-width: 4px;
	content: ""
}

.ant-popover-placement-top>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-topLeft>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-topRight>.ant-popover-content>.ant-popover-arrow {
	border-bottom-width: 0;
	border-top-color: hsla(0,0%,85%,.7);
	bottom: 3px
}

.ant-popover-placement-top>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-topLeft>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-topRight>.ant-popover-content>.ant-popover-arrow:after {
	content: " ";
	bottom: 1px;
	margin-left: -4px;
	border-bottom-width: 0;
	border-top-color: #fff
}

.ant-popover-placement-top>.ant-popover-content>.ant-popover-arrow {
	left: 50%;
	margin-left: -5px
}

.ant-popover-placement-topLeft>.ant-popover-content>.ant-popover-arrow {
	left: 16px
}

.ant-popover-placement-topRight>.ant-popover-content>.ant-popover-arrow {
	right: 16px
}

.ant-popover-placement-right>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-rightBottom>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-rightTop>.ant-popover-content>.ant-popover-arrow {
	left: 3px;
	border-left-width: 0;
	border-right-color: hsla(0,0%,85%,.7)
}

.ant-popover-placement-right>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-rightBottom>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-rightTop>.ant-popover-content>.ant-popover-arrow:after {
	content: " ";
	left: 1px;
	bottom: -4px;
	border-left-width: 0;
	border-right-color: #fff
}

.ant-popover-placement-right>.ant-popover-content>.ant-popover-arrow {
	top: 50%;
	margin-top: -5px
}

.ant-popover-placement-rightTop>.ant-popover-content>.ant-popover-arrow {
	top: 12px
}

.ant-popover-placement-rightBottom>.ant-popover-content>.ant-popover-arrow {
	bottom: 12px
}

.ant-popover-placement-bottom>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-bottomLeft>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-bottomRight>.ant-popover-content>.ant-popover-arrow {
	border-top-width: 0;
	border-bottom-color: hsla(0,0%,85%,.7);
	top: 3px
}

.ant-popover-placement-bottom>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-bottomLeft>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-bottomRight>.ant-popover-content>.ant-popover-arrow:after {
	content: " ";
	top: 1px;
	margin-left: -4px;
	border-top-width: 0;
	border-bottom-color: #fff
}

.ant-popover-placement-bottom>.ant-popover-content>.ant-popover-arrow {
	left: 50%;
	margin-left: -5px
}

.ant-popover-placement-bottomLeft>.ant-popover-content>.ant-popover-arrow {
	left: 16px
}

.ant-popover-placement-bottomRight>.ant-popover-content>.ant-popover-arrow {
	right: 16px
}

.ant-popover-placement-left>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-leftBottom>.ant-popover-content>.ant-popover-arrow,.ant-popover-placement-leftTop>.ant-popover-content>.ant-popover-arrow {
	right: 3px;
	border-right-width: 0;
	border-left-color: hsla(0,0%,85%,.7)
}

.ant-popover-placement-left>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-leftBottom>.ant-popover-content>.ant-popover-arrow:after,.ant-popover-placement-leftTop>.ant-popover-content>.ant-popover-arrow:after {
	content: " ";
	right: 1px;
	border-right-width: 0;
	border-left-color: #fff;
	bottom: -4px
}

.ant-popover-placement-left>.ant-popover-content>.ant-popover-arrow {
	top: 50%;
	margin-top: -5px
}

.ant-popover-placement-leftTop>.ant-popover-content>.ant-popover-arrow {
	top: 12px
}

.ant-popover-placement-leftBottom>.ant-popover-content>.ant-popover-arrow {
	bottom: 12px
}

.ant-message {
	font-size: 12px;
	position: fixed;
	z-index: 1010;
	width: 100%;
	top: 16px;
	left: 0;
	pointer-events: none
}

.ant-message-notice {
	padding: 8px;
	text-align: center
}

.ant-message-notice:first-child {
	margin-top: -8px
}

.ant-message-notice-content {
	padding: 8px 16px;
	border-radius: 4px;
	box-shadow: 0 2px 8px rgba(0,0,0,.2);
	background: #fff;
	display: inline-block;
	pointer-events: all
}

.ant-message-success .anticon {
	color: #00a854
}

.ant-message-error .anticon {
	color: #f04134
}

.ant-message-warning .anticon {
	color: #ffbf00
}

.ant-message-info .anticon,.ant-message-loading .anticon {
	color: #108ee9
}

.ant-message .anticon {
	margin-right: 8px;
	font-size: 14px;
	top: 1px;
	position: relative
}

.ant-message-notice.move-up-leave.move-up-leave-active {
	-webkit-animation-name: MessageMoveOut;
	animation-name: MessageMoveOut;
	overflow: hidden;
	-webkit-animation-duration: .3s;
	animation-duration: .3s
}

@-webkit-keyframes MessageMoveOut {
	0% {
		opacity: 1;
		max-height: 150px;
		padding: 8px
	}

	to {
		opacity: 0;
		max-height: 0;
		padding: 0
	}
}

@keyframes MessageMoveOut {
	0% {
		opacity: 1;
		max-height: 150px;
		padding: 8px
	}

	to {
		opacity: 0;
		max-height: 0;
		padding: 0
	}
}

.ant-alert {
	position: relative;
	padding: 8px 48px 8px 38px;
	border-radius: 4px;
	color: rgba(0,0,0,.65);
	font-size: 12px;
	line-height: 1.5
}

.ant-alert.ant-alert-no-icon {
	padding: 8px 48px 8px 16px
}

.ant-alert-icon {
	font-size: 14px;
	top: 10px;
	left: 16px;
	position: absolute
}

.ant-alert-description {
	font-size: 12px;
	line-height: 21px;
	display: none
}

.ant-alert-success {
	border: 1px solid #cfefdf;
	background-color: #ebf8f2
}

.ant-alert-success .ant-alert-icon {
	color: #00a854
}

.ant-alert-info {
	border: 1px solid #d2eafb;
	background-color: #ecf6fd
}

.ant-alert-info .ant-alert-icon {
	color: #108ee9
}

.ant-alert-warning {
	border: 1px solid #fff3cf;
	background-color: #fffaeb
}

.ant-alert-warning .ant-alert-icon {
	color: #ffbf00
}

.ant-alert-error {
	border: 1px solid #fcdbd9;
	background-color: #fef0ef
}

.ant-alert-error .ant-alert-icon {
	color: #f04134
}

.ant-alert-close-icon {
	font-size: 12px;
	position: absolute;
	right: 16px;
	top: 10px;
	height: 12px;
	line-height: 12px;
	overflow: hidden;
	cursor: pointer
}

.ant-alert-close-icon .anticon-cross {
	color: rgba(0,0,0,.43);
	transition: color .3s ease
}

.ant-alert-close-icon .anticon-cross:hover {
	color: #404040
}

.ant-alert-close-text {
	position: absolute;
	right: 16px
}

.ant-alert-with-description {
	padding: 16px 16px 16px 60px;
	position: relative;
	border-radius: 4px;
	color: rgba(0,0,0,.65);
	line-height: 1.5
}

.ant-alert-with-description.ant-alert-no-icon {
	padding: 16px
}

.ant-alert-with-description .ant-alert-icon {
	position: absolute;
	top: 16px;
	left: 20px;
	font-size: 24px
}

.ant-alert-with-description .ant-alert-close-icon {
	position: absolute;
	top: 16px;
	right: 16px;
	cursor: pointer;
	font-size: 12px
}

.ant-alert-with-description .ant-alert-message {
	font-size: 14px;
	color: rgba(0,0,0,.85);
	display: block;
	margin-bottom: 4px
}

.ant-alert-with-description .ant-alert-description {
	display: block
}

.ant-alert.ant-alert-close {
	height: 0!important;
	margin: 0;
	padding-top: 0;
	padding-bottom: 0;
	transition: all .3s cubic-bezier(.78,.14,.15,.86);
	-webkit-transform-origin: 50% 0;
	-ms-transform-origin: 50% 0;
	transform-origin: 50% 0
}

.ant-alert-slide-up-leave {
	-webkit-animation: antAlertSlideUpOut .3s cubic-bezier(.78,.14,.15,.86);
	animation: antAlertSlideUpOut .3s cubic-bezier(.78,.14,.15,.86);
	-webkit-animation-fill-mode: both;
	animation-fill-mode: both
}

.ant-alert-banner {
	border-radius: 0;
	border: 0;
	margin-bottom: 0
}

@-webkit-keyframes antAlertSlideUpIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(0);
		transform: scaleY(0)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}
}

@keyframes antAlertSlideUpIn {
	0% {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(0);
		transform: scaleY(0)
	}

	to {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}
}

@-webkit-keyframes antAlertSlideUpOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(0);
		transform: scaleY(0)
	}
}

@keyframes antAlertSlideUpOut {
	0% {
		opacity: 1;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(1);
		transform: scaleY(1)
	}

	to {
		opacity: 0;
		-webkit-transform-origin: 0 0;
		transform-origin: 0 0;
		-webkit-transform: scaleY(0);
		transform: scaleY(0)
	}
}

.custom-filter-dropdown {
	padding: 8px;
	border-radius: 6px;
	background: #fff;
	box-shadow: 0 1px 6px rgba(0,0,0,.2)
}

.custom-filter-dropdown input {
	width: 130px;
	margin-right: 8px
}

.highlight {
	color: #f50
}

.table-record-wrapper {
	position: relative;
	background: #abc3ff;
	overflow: hidden;
	height: 500px
}

.table-record {
	margin: 40px auto;
	box-shadow: 0 10px 40px #506cb2;
	width: 60%;
	min-width: 550px;
	height: 420px;
	background: #f4f4f4;
	border-radius: 6px;
	overflow: hidden
}

.table-record-table-wrapper {
	width: 80%;
	display: inline-block;
	overflow: auto;
	height: 18%
}

.table-dnsrecord-table .ant-table-thead>tr>th,.table-httprecord-table .ant-table-thead>tr>th {
	background: #e5e5e5;
	padding: 10px 8px;
	display: inline-block
}

.table-dnsrecord-table .ant-table-tbody>tr,.table-httprecord-table .ant-table-tbody>tr {
	background: #fff
}

.table-dnsrecord-table .ant-table-tbody>tr>td,.table-httprecord-table .ant-table-tbody>tr>td {
	padding: 10px 8px;
	display: inline-block;
	vertical-align: bottom
}

.table-dnsrecord-table .ant-table-tbody>tr,.table-dnsrecord-table .ant-table-thead>tr,.table-httprecord-table .ant-table-tbody>tr,.table-httprecord-table .ant-table-thead>tr {
	display: block;
	transition: none
}

.table-dnsrecord-table .ant-table-tbody>tr>td:first-child,.table-dnsrecord-table .ant-table-thead>tr>th:first-child {
	width: 15%
}

.table-dnsrecord-table .ant-table-tbody>tr>td:nth-child(2),.table-dnsrecord-table .ant-table-thead>tr>th:nth-child(2) {
	width: 40%
}

.table-dnsrecord-table .ant-table-tbody>tr>td:nth-child(3),.table-dnsrecord-table .ant-table-thead>tr>th:nth-child(3) {
	width: 30%
}

.table-dnsrecord-table .ant-table-tbody>tr>td:nth-child(4),.table-dnsrecord-table .ant-table-thead>tr>th:nth-child(4) {
	width: 15%
}

.table-httprecord-table .ant-table-tbody>tr>td:first-child,.table-httprecord-table .ant-table-thead>tr>th:first-child {
	width: 5%
}

.table-httprecord-table .ant-table-tbody>tr>td:nth-child(2),.table-httprecord-table .ant-table-thead>tr>th:nth-child(2) {
	width: 24%
}

.table-httprecord-table .ant-table-tbody>tr>td:nth-child(3),.table-httprecord-table .ant-table-thead>tr>th:nth-child(3) {
	width: 10%
}

.table-httprecord-table .ant-table-tbody>tr>td:nth-child(4),.table-httprecord-table .ant-table-thead>tr>th:nth-child(4) {
	width: 6%
}

.table-httprecord-table .ant-table-tbody>tr>td:nth-child(5),.table-httprecord-table .ant-table-thead>tr>th:nth-child(5) {
	width: 10%
}

.table-httprecord-table .ant-table-tbody>tr>td:nth-child(6),.table-httprecord-table .ant-table-thead>tr>th:nth-child(6) {
	width: 23%
}

.table-httprecord-table .ant-table-tbody>tr>td:nth-child(7),.table-httprecord-table .ant-table-thead>tr>th:nth-child(7) {
	width: 10%
}

.table-httprecord-table .ant-table-tbody>tr>td:nth-child(8),.table-httprecord-table .ant-table-thead>tr>th:nth-child(8) {
	width: 12%
}

@media screen and (max-width:414px) {
	.table-record {
		transform: scale(.65) translateX(12px);
		transform-origin: left center
	}
}

@media screen and (max-width:375px) {
	.table-record {
		transform: scale(.6) translateX(7px)
	}
}

@media screen and (max-width:320px) {
	.table-record {
		transform: scale(.5) translateX(12px)
	}
}

</style>
