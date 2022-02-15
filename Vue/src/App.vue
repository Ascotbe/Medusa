<template>
  <a-locale-provider :locale="zh_CN">
    <div id="app">
      <router-view />
    </div>
  </a-locale-provider>
</template>
<script>
import zh_CN from 'ant-design-vue/lib/locale-provider/zh_CN';
export default {
  data() {
    return {
      zh_CN
    }
  }
}
</script>


<style lang="scss">
/* 定义 */
@font-face {
  font-family: "Lato";
  src: url("./assets/font/Lato-Regular.ttf");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "NotoSans";
  src: url("./assets/font/NotoSans-Regular.ttf");
  font-weight: normal;
  font-style: normal;
}
#app {
  font-family: "Lato", "NotoSans";
  // font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  min-height: 604px;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
