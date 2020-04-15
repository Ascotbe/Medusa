# HTML webpack plugin interop

When using [html-webpack-plugin](https://github.com/jantimon/html-webpack-plugin) along with sprite-loader in extract mode it is possible 
to inline sprite content directly to the page. All extracted sprites stored in `htmlWebpackPlugin.files.sprites` template variable. 
It's an object where key is a sprite filename and value - file contents (`Object<filename:string, content:string>`). 

### [Demo](build/index.html)

### Template example

```ejs
...
<body>

<% if (htmlWebpackPlugin.files.sprites) { %>
  <% for (var spriteFileName in htmlWebpackPlugin.files.sprites) { %>
    <%= htmlWebpackPlugin.files.sprites[spriteFileName] %>
  <% } %>
<% } %>

</body>
...
```
