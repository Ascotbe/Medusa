<template>
  <a-layout style="height:100%">
    <a-layout-sider
      width="170"
      v-model="collapsed"
      collapsed-width="40"
      @mouseleave="handleMouseleave"
      @mouseenter="handleMouseenter"
    >
      <div style="height:60px">
        <img width="100%" height="100%" v-show="!collapsed" :src="Logo" />
        <img width="100%" height="100%" v-show="collapsed" :src="LogoM" />
      </div>
      <MenuList ref="MenuList" :collapsed="collapsed" />
      <div style="height:40px">
        <Header @change="handleGetSelectedKeys" :collapsed="collapsed" />
      </div>
    </a-layout-sider>
    <a-layout>
      <!-- <a-layout-header>
        <Header @change="handleGetSelectedKeys" />
      </a-layout-header>-->
      <a-layout-content class="views">
        <router-view></router-view>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>
import MenuList from './part/MenuList.vue'
import Header from './part/Header.vue'
import { mapGetters } from "vuex";
const Logo = require('@/assets/logo.png')
const LogoM = require('@/assets/M.png')

export default {
  data () {
    return {
      Logo,
      LogoM,
    }
  },
  components: {
    MenuList,
    Header
  },
  computed: {
    ...mapGetters({
      collapsed: "StateStore/collapsed",//是否收缩菜单
    }),
  },
  methods: {
    handleGetSelectedKeys (selectedKeys) {
      this.$refs.MenuList.handleSetSelectedKeys(selectedKeys)
    },
    //鼠标移出事件
    handleMouseleave () {
      this.$store.commit('StateStore/setCollapsed', true)
    },
    //鼠标移入事件
    handleMouseenter () {
      this.$store.commit('StateStore/setCollapsed', false)

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