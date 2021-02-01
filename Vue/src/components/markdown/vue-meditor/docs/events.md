### on-ready
编辑器初始化完成时触发，返回值为`Object`，包含组件本身和`insertContent`方法。

### on-save
编辑器保存事件，自动保存或者手动保存时触发，支持`ctrl+s`或`command+s`触发保存，返回值类型为`Object`，包含当前输入值`value`和选择的代码块主题`theme`。


### on-paste-image [已废除,可改用on-upload-image]	

监听编辑器粘贴图片事件，在编辑区域内手动粘贴图片时触发，可用于支持粘贴插入图片文件，返回`file`文件，上传文件后可结合`on-ready`事件内返回的`insertContent`插入图片。

### on-copy 
复制代码块内容，触发时返回当前代码块的text，copyCode开启时才有效。

### on-upload-image

图片上传事件，用户自定义上传图片，复制粘贴图片截图、文件和点开菜单栏上传按钮时式触发，返回`file`文件，上传文件后可结合`on-ready`事件内返回的`insertContent`插入图片。
