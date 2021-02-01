## 编辑器基本属性
### value
- Type: `String/Number`
- Default: `''`

编辑器输入的文本，支持通过`v-dodel`数据双向绑定设置编辑器内容和获取编辑器的值。

### width
- Type: `String/Number`
- Default: `auto`

编辑器的初始化宽度。

### height
- Type: `Number`
- Default: `600`

编辑器的初始化高度。

### bordered
- Type: `Boolean`
- Default: `true`

编辑器是否含有边框。

### toolbars
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
uploadImage|本地图片|否
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


### theme
- Type: `String`
- Default: `light`

编辑器代码块主题，目前支持`light`、`dark`、`oneDark`、`gitHub`四种代码块风格，可通过自定义theme并修改样式文件进行主题定制。

自定义theme时，预览区域的会增加一个为`markdown-theme-[theme]`的`class`。


### autoSave
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
### interval
- Type: `Number`
- Default: `10000`

自动保存间隔时间，单位：`mm`，默认10000mm，需要`autoSave = true`时才有效。

### exportFileName
- Type: `String`
- Default: `unnamed`

导出的md文件名称，默认unnamed.md。

### markedOptions
- Type: `Object`
- Default: `{}`

marked配置项,可以根据需求自定义。

```vue
<Markdown :markedOptions="{baseUrl:'http://***.oss-cn-shanghai.aliyuncs.com/'}"/>
```
### isPreview
- Type: `Boolean`
- Default: `false`

是否是预览模式，开启时可作为一个预览组件使用，与预览组件功能一致。

### copyCode
- Type: `Boolean`
- Default: `true`

是否支持复制代码块内的内容。

### copyBtnText
- Type: `String`
- Default: `复制代码`

复制代码按钮显示文字。


## 预览组件基本属性
### initialValue
- Type: `String/Number`
- Default: `''`

预览组件初始化内容，支持动态更新。

### theme
- Type: `String`
- Default: `light`

代码块主题,与编辑器编辑器代码块主题一致。

### markedOptions
- Type: `Object`
- Default: `{}`

marked配置项,与编辑器内该配置一致。

### copyCode
- Type: `Boolean`
- Default: `true`

是否支持复制代码块内的内容。


### copyBtnText
- Type: `String`
- Default: `复制代码`

复制代码按钮显示文字。
