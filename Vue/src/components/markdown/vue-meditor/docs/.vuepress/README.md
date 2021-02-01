
## vue-markdown
### [使用文档](https://zhaoxuhui1122.github.io/vue-markdown-docs/)

一款使用marked和highlight.js开发的一款markdown编辑器，除常见markdown语法外，支持快捷输入、图片粘贴、代码复制、全屏编辑、预览等功能。
```vue
<template>
    <div class="simple">
        <Markdown :height="400" theme="oneDark"/>
    </div>
</template>

<script>
    import Markdown from 'src/components/simple/simple';
    export default {
        name: "simple",
        components:{
            Markdown
        }
    }
</script>

```
