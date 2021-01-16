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
