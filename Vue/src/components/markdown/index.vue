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
    <Markdown v-model="value" @on-save="handleOnSave" :autoSave="true"/>
  </div>
</template>

<script>
import Markdown from "./vue-meditor";

export default {
  name: "markdown",
  components: {
    Markdown,
  },
  data() {
    return {
      value: "", //用户输入值
      // toolbars:{
      //   save:true,
      //theme:gitHub
      // }
    };
  },
  methods: {
    handleOnSave({value,theme}) {
      console.log(value,theme);
    },
  },
};
</script>
