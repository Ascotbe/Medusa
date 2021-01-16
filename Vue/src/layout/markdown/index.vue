<!--
 * @Description: mrakdown
 * @Author: zk-chen
 * @Date: 2021-01-01 12:43:36
 * @LastEditTime: 2021-01-02 00:00:41
 * @LastEditors: zk-chen
 * @FilePath: /Vue/src/layout/markdown/index.vue
-->
<template>
  <div class="markdown">
    <div>{{ value }}</div>

    <Markdown v-model="value" @on-save="handleOnSave" />
  </div>
</template>

<script>
import Markdown from './vue-meditor'

export default {
  name: 'markdown',
  components: {
    Markdown
  },
  data() {
    return {
      value: '' //用户输入值
    }
  },
  methods: {
    handleOnSave(value) {
      console.log(value)
    }
  }
}
</script>
