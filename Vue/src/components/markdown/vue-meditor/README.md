## 简介
一款使用marked和highlight.js开发的一款markdown编辑器，除常见markdown语法外，支持快捷输入、图片粘贴、代码复制、全屏编辑、预览等功能。

使用起来简单方便，只需几行代码，即可在你的页面上引入一个markdown编辑器，编辑区支持像专业编辑器那样。

编辑器涵盖了常用的markdown编辑器功能，可通过已有属性进行配置，对编辑器功能和样式进行基本的配置，也可根据需求进行深度定制。
#### [项目地址](https://github.com/zhaoxuhui1122/vue-markdown)
#### [文档地址](https://zhaoxuhui1122.github.io/vue-markdown-docs/)
**示例**
![image.png](https://upload-images.jianshu.io/upload_images/9390764-f6b0840eca057d61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 特点
- 使用简单，只需要安装npm包，引入项目即可使用，不需要繁琐的初始化配置。
- 方便扩展，根据实际需求，支持常见的功能配置，也可根据实际需求进行深度定制。
- 体积小，加载速度快，npm包删除了highlight.js和codemirror里的依赖。
- 灵活的主题，默认支持四种代码块风格，也可根据实际需求定制自己的主题样式
- 功能强大，支持专业版的编辑器，使用codemirror实现编辑窗口，可识别markdown语法
- 键盘事件监听，如保存、粘贴、回车时上次输入语法判断等
- 可扩展性强，除了提供的属性配置编辑器，也可直接在原有组件基础上进行二次开发

## 实现思路

通过监听文本输入区域内内容的变化，实时将输入的markdown语法进行编译，并渲染到预览区域。

编辑器大致分为头部菜单栏、左侧内容输入区域、右侧预览区域三个部分。
头部菜单主要为定自定义标题区域和菜单按钮，菜单按钮可通过配置文件进行显示和隐藏；左侧编辑区域，简单版使用textarea开发，满足基本需求，
专业版使用codemirror开发，编辑区域支持手动输入文本和通过头部菜单插入；右侧预览区域可实时预览输入文本，并可通过菜单按钮，进行编辑区域和预览区域的切换。

## 安装方式
### 使用npm安装

1. 安装依赖
```
npm i -S vue-meditor
```

### 将组件复制到项目内
1. 将git仓库代码拉到本地
```
git clone https://github.com/zhaoxuhui1122/vue-markdown.git
```

2. 复制src文件夹下内容至components文件夹下

## 在项目使用
#### npm包安装时
简单版
```js
import Markdown from 'vue-meditor'
```
专业版
```js
import { MarkdownPro } from 'vue-meditor'
```
预览组件
```js
import { MarkdownPreview } from 'vue-meditor'
```
#### 复制组件到本地时（推荐）
简单版
```js
import Markdown from '@/components/markdown/...';
```
专业版 
```js
import MarkdownPro from '@/components/markdown/pro';
```
预览组件
```js
import MarkdownPreview from '@/components/markdown/preview';
```

#### 在页面内使用
```vue
<template>
    <div class="markdown">
        <Markdown/>
    </div>
</template>

<script>
    import Markdown from 'vue-meditor';
    
    export default {
        name: "markdown",
        components: {
            Markdown
        }
    }
</script>
```
## API
### 编辑器基本属性
#### value
- Type: `String/Number`
- Default: `''`

编辑器输入的文本，支持通过`v-dodel`数据双向绑定设置编辑器内容和获取编辑器的值。

#### width
- Type: `String/Number`
- Default: `auto`

编辑器的初始化宽度。

#### height
- Type: `Number`
- Default: `600`

编辑器的初始化高度。

#### bordered
- Type: `Boolean`
- Default: `true`

编辑器是否含有边框。

#### toolbars
- Type: `Object`
- Default: `参见下表`

头部菜单按钮，通过设置true or false控制决定是否显示，目前配置支持持控制按钮显示隐藏，后续将支持根据配置显示排列顺序。

名称 | 说明 | 默认是否显示
---|---|---
strong|粗体|是
italic|斜体|是
overline |删除线|是
h1 |标题1|是
h2 |标题2|是
h3 |标题3|是
h4|标题4|否
h5 |标题5|否
h6 |标题6|否
hr |分割线|是
quote|引用|是
ul |无序列表|是
ol|有序列表|是
code |代码块|是
link |链接|是
image|image|是
table |表格|是
checked|已完成列表|是
notChecked |未完成列表|是
preview|预览|是
split|分屏模式切换|是
print |打印|否
theme|主题切换|是
fullscreen |全屏|是
exportmd|导出为*.md文件|是
importmd|导入本地*.md文件|是
save|保存按钮|否
clear|清空内容|否


#### theme
- Type: `String`
- Default: `light`

编辑器代码块主题，目前支持`light`、`dark`、`oneDark`、`gitHub`四种代码块风格，可通过自定义theme并修改样式文件进行主题定制。

自定义theme时，预览区域的会增加一个为`markdown-theme-[theme]`的`class`。


#### autoSave
- Type: `Boolean`
- Default: `false`

是否开启自动保存，设置为开启时可通过绑定`on-save`事件获取编辑器内的值和代码块主题。
```vue
<Markdown @on-save="handleOnSave"/>
```
```js
 handleOnSave({value, theme}){
        console.log(value, theme);
    }
```
#### interval
- Type: `Number`
- Default: `10000`

自动保存间隔时间，单位：`mm`，默认10000mm，需要`autoSave = true`时才有效。

#### exportFileName
- Type: `String`
- Default: `unnamed`

导出的md文件名称，默认unnamed.md。

#### markedOptions
- Type: `Object`
- Default: `{}`

marked配置项,可以根据需求自定义。

```vue
<Markdown :markedOptions="{baseUrl:'http://***.oss-cn-shanghai.aliyuncs.com/'}"/>
```
#### isPreview
- Type: `Boolean`
- Default: `false`

是否是预览模式，开启时可作为一个预览组件使用，与预览组件功能一致。

#### copyCode
- Type: `Boolean`
- Default: `true`

是否支持复制代码块内的内容。

#### copyBtnText
- Type: `String`
- Default: `复制代码`

复制代码按钮显示文字。


### 预览组件基本属性
#### initialValue
- Type: `String/Number`
- Default: `''`

预览组件初始化内容，支持动态更新。

#### theme
- Type: `String`
- Default: `light`

代码块主题,与编辑器编辑器代码块主题一致。

#### markedOptions
- Type: `Object`
- Default: `{}`

marked配置项,与编辑器内该配置一致。

#### copyCode
- Type: `Boolean`
- Default: `true`

是否支持复制代码块内的内容。


#### copyBtnText
- Type: `String`
- Default: `复制代码`

复制代码按钮显示文字。
### on-ready
编辑器初始化完成时触发，返回值为`Object`，包含组件本身和`insertContent`方法。

#### on-save
编辑器保存事件，自动保存或者手动保存时触发，支持`ctrl+s`或`command+s`触发保存，返回值类型为`Object`，包含当前输入值`value`和选择的代码块主题`theme`。


#### on-paste-image	

监听编辑器粘贴图片事件，在编辑区域内手动粘贴图片时触发，可用于支持粘贴插入图片文件，返回`file`文件，上传文件后可结合`on-ready`事件内返回的`insertContent`插入图片。

#### on-copy 
复制代码块内容，触发时返回当前代码块的text，copyCode开启时才有效。

## 二次开发
### 粘贴插入图片

`on-paste-image`虽然可以支持图片粘贴事件的监听，但不会处理图片上传至服务器并将链接插入编辑器这段逻辑。

目前如果想要支持粘贴插入图片，需要在`on-paste-image`方法里上传图片文件，拿到图片地址后，使用`on-ready`方法里返回的insertContent方法插入图片。

上述操作显得过于复杂，可以直接在源码里扩展mixins里的`handlePaste`方法,图片上传完成后，直接调用`this.insertContent`方法插入图片。

修改`/markdown/mixins/common.js`

```js
handlePaste(_, e) {// 粘贴图片
    const { clipboardData = {} } = e;
    const { types = [], items } = clipboardData;
    let item = null;
    for (let i = 0; i < types.length; i++) {
        if (types[i] === 'Files') {
            item = items[i];
            break;
        }
    }
    if (item) {
        const file = item.getAsFile();
        if (/image/gi.test(file.type)) {
            e.preventDefault();
            // 1.上传操作
            // 2.插入图片 this.insertContent(`![image](imgUrl)`)
        }
    }
}
```
### 支持流程图、甘特图等语法

目前编辑器只支持常见code语法，如果需要实现如流程图等功能，需要进一步扩展，以实现一个简单的流程图为例，具体实现思路如下：

默认情况下，markedjs会使用renderer.code方法对输入的代码块进行解析，并会借助`highlight.js`支持语法高亮。
可以将流程图语法输入到代码块内，并标明语言，重写marked.Renderer的code解析方法，结合结合`flowchart.js`路程图代码进行解析，返回文本内容。

修改`/markdown/libs/js/simple.js

```js
import hljs from './hljs';
import index from 'index';
import {parse} from 'flowchart.js'

hljs.initHighlightingOnLoad();

const renderer = new index.Renderer();
renderer.code = (code, language) => {
    if (language === 'flow') {// 流程图
        const dom = document.createElement('div');
        const flowchart = parse(code);
        flowchart.drawSVG(dom, {/*相关配置*/});
        return  dom.innerHTML;
    } else {// 默认解析
        return `<pre class="hljs"><code class="${language}">${hljs.highlightAuto(code).value}</code></pre>`
    }
}
export default index.setOptions({
    renderer,
    gfm: true,
    tables: true,
    breaks: false,
    pedantic: false,
    sanitize: false,
    smartLists: true,
    highlight: function (code) {
        return hljs.highlightAuto(code).value;
    }
})
```

### 自定义markdown语法转换

项目内使用的`index.js均为其默认配置功能，如需要特殊转换，可重写其内部的解析方法，即重写其renderer相关方法
[参考文档](https://github.com/markedjs/marked/blob/master/docs/USING_PRO.md)。

## 自动生成文档目录

预览区域和文档预览组件暂不支持自动生成目录，实现自动生成目录思路目前想到的大致有
- 重写`renderer.heading` 方法，为生成的标题添加id，输入特定快捷键，如`[TOC]`时，查找预览区域内的的所有标题标签，分析等级关系，生成目录标签

### icon替换
项目内所有的icon和命名参考`/assets/font/index.html`，替换时需注意，预览区域的checkbox为icon，注意一并替换，
修改`/assets/css/index.less`内的`input[type="checkbox"]`的`:after`样式。

## 代码体积优化


### 公共代码提取
npm包构建时，三个组件完全独立，没有抽离公共文件，所以，当同一个项目内引入其中的两个或三个组件都引入时，存在一定的重复代码，
主要为`highlight.js`、`marked`、`iconfont`、css样式几个部分。

解决方式：将组件复制到本地项目，打包时将这些文件作为公共文件抽离出来。

**注意**:三个组件中使用的iconfont为同一套，如果只是单纯的使用`preview`组件,
将会引入整个项目所使用的iconfont,可删除iconfont的引入，
重写`input[type="checkbox"]`的样式，preview组件体积将会减少一半，样式文件位于`markdown/assets/css/index.less`。

### codemirror体积优化
codemirror主要分为主文件、mode相关文件和样式文件，主文件体积异常的大，mode文件目前只选用了css/jsvascript/markdown/meta/xml五个文件，
其中markdown.js和meta.js为必须引用的，项目中已将常见的编程语言代码风格定义为css/js/xml之一，例如less/sass/scss按照css规则解析，html/vue按照xml规则解析。
优化可从一下方面入手
- 减少codemirror主文件体积
- 减少引用的mode依赖

### highlight.js体积优化

highlight.js原本体积也是较大的，主要原因为，编译时为支持各种代码语言，引入了相应的解析文件，
项目内已根据常见的代码语言进行了一次筛选，进行按需引入，可根据自身需求，再次对引用文件进行删减

参见`src/markdown/libs/js/hljs.js`,目前支持的语言有
```js
import hljs from 'highlight.js/lib/highlight'

import javascript from 'highlight.js/lib/languages/javascript'
import java from 'highlight.js/lib/languages/java';
import css from 'highlight.js/lib/languages/css';
import less from 'highlight.js/lib/languages/less';
import go from 'highlight.js/lib/languages/go';
import markdown from src;
import php from 'highlight.js/lib/languages/php';
import python from 'highlight.js/lib/languages/python';
import ruby from 'highlight.js/lib/languages/ruby';
import stylus from 'highlight.js/lib/languages/stylus';
import typescript from 'highlight.js/lib/languages/typescript';
import xml from 'highlight.js/lib/languages/xml';

const languages = {
    javascript,
    java,
    css,
    less,
    markdown,
    go,
    php,
    python,
    ruby,
    stylus,
    typescript,
    xml
}
Object.keys(languages).forEach(key => {
    hljs.registerLanguage(key, languages[key])
})

export default hljs;
```

### 专业版编辑器codemirror/simple.js
优化思路：无
#### iconfont 体积优化
只需要preview组件时，避免引入所有icon，参考功能扩展里icon替换方法。

## 升级路线
- 普通版编辑器对选中文本进行操作功能
- 文档目录功能
- 优化专业版编辑器体积
- react版开发
- ...

## 问题反馈

对于功能上的缺陷、使用方法和希望扩展的功能，可以提 [Issues](https://github.com/zhaoxuhui1122/vue-markdown/issues)。

##  license: `MIT`
