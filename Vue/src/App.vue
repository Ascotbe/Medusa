<template>
  <div id="app">
    <router-view />
  </div>
</template>

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
