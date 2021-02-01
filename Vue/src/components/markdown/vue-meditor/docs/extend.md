## 粘贴插入图片

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
## 支持流程图、甘特图等语法

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

## 自定义markdown语法转换

项目内使用的`index.js均为其默认配置功能，如需要特殊转换，可重写其内部的解析方法，即重写其renderer相关方法
[参考文档](https://github.com/markedjs/marked/blob/master/docs/USING_PRO.md)。

## 自动生成文档目录

预览区域和文档预览组件暂不支持自动生成目录，实现自动生成目录思路目前想到的大致有
- 重写`renderer.heading` 方法，为生成的标题添加id，输入特定快捷键，如`[TOC]`时，查找预览区域内的的所有标题标签，分析等级关系，生成目录标签

## icon替换
项目内所有的icon和命名参考`/assets/font/index.html`，替换时需注意，预览区域的checkbox为icon，注意一并替换，
修改`/assets/css/index.less`内的`input[type="checkbox"]`的`:after`样式。
