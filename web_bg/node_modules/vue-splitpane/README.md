# Vue Split Pane

Split-Pane component built with vue2.0, can be split vertically or horizontally.

## [Try the demo](http://panjiachen.github.io/split-pane/demo/index.html)

### How to use?
```bash
npm install vue-splitpane

#import
import splitPane from 'vue-splitpane'

# use as global component
Vue.component('split-pane', splitPane);
```

### Example

```html
   <split-pane v-on:resize="resize" :min-percent='20' :default-percent='30' split="vertical">
      <template slot="paneL">
        A
      </template>
      <template slot="paneR">
        B
      </template>
    </split-pane>
```

```html
  //nested
   <split-pane v-on:resize="resize" :min-percent='20' :default-percent='30' split="vertical">
      <template slot="paneL">
        A
      </template>
      <template slot="paneR">
        <split-pane split="horizontal">
          <template slot="paneL">
           B
          </template>
          <template slot="paneR">
            C
          </template>
        </split-pane>
      </template>
    </split-pane>
```

### Options
|    Property    |    Description   |   type   |	default	|
| -----------------  | ---------------- | :--------: | :----------: |
| split       | the split type |String [horizontal,vertical] |must choose one type |
| min-percent         | paneL max-min-percent  |Number | 10 |
| max-percent         | paneL max-percent  |Number | 10 |

