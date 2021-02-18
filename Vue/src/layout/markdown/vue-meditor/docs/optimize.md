### 代码体积优化


#### 公共代码提取
npm包构建时，三个组件完全独立，没有抽离公共文件，所以，当同一个项目内引入其中的两个或三个组件都引入时，存在一定的重复代码，
主要为`highlight.js`、`marked`、`iconfont`、css样式几个部分。

解决方式：将组件复制到本地项目，打包时将这些文件作为公共文件抽离出来。

**注意**:三个组件中使用的iconfont为同一套，如果只是单纯的使用`preview`组件,
将会引入整个项目所使用的iconfont,可删除iconfont的引入，
重写`input[type="checkbox"]`的样式，preview组件体积将会减少一半，样式文件位于`markdown/assets/css/index.less`。

#### codemirror体积优化
codemirror主要分为主文件、mode相关文件和样式文件，主文件体积异常的大，mode文件目前只选用了css/jsvascript/markdown/meta/xml五个文件，
其中markdown.js和meta.js为必须引用的，项目中已将常见的编程语言代码风格定义为css/js/xml之一，例如less/sass/scss按照css规则解析，html/vue按照xml规则解析。
优化可从一下方面入手
- 减少codemirror主文件体积
- 减少引用的mode依赖

#### highlight.js体积优化

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

#### 专业版编辑器codemirror/simple.js
优化思路：无
#### iconfont 体积优化
只需要preview组件时，避免引入所有icon，参考功能扩展里icon替换方法。

