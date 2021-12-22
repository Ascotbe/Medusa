<template>
  <a-layout style="height:100%">
    <a-layout-sider width="170">
      <div style="height:60px">
        <img width="100%" height="100%" src="@/assets/logo.png" />
      </div>
      <MenuList ref="MenuList" />
    </a-layout-sider>
    <a-layout>
      <a-layout-header>
        <Header @change="handleGetSelectedKeys" />
      </a-layout-header>
      <a-layout-content class="views">
        <router-view></router-view>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>
import MenuList from './part/MenuList.vue'
import Header from './part/Header.vue'

export default {
  data () {
    return {
    }
  },
  components: {
    MenuList,
    Header
  },
  methods: {
    handleGetSelectedKeys (selectedKeys) {
      this.$refs.MenuList.handleSetSelectedKeys(selectedKeys)
    }
  }
}
</script>

<style lang="scss" scoped>
.views {
  border: 16px solid #f1f2f6;
  // height: calc(100% - 36px);
  padding: 10px;
  height: 100%;
  min-height: 540px;
  // background: #fff;
  overflow: auto;
  overflow-x: hidden;
}

/*定义整体的宽度*/
.views::-webkit-scrollbar {
  display: none;
}

/*定义滚动条轨道*/
.views::-webkit-scrollbar-track {
  display: none;
}

/*定义滑块*/
.views::-webkit-scrollbar-thumb {
  display: none;
}
</style>