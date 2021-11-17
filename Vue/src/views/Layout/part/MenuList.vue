<template>
  <a-menu
    class="menu"
    mode="inline"
    theme="dark"
    v-model="selectedKeys"
    :defaultOpenKeys="defaultOpenKeys"
    v-bind="$props"
    v-on="$listeners"
    @click="handleGoTo"
  >
    <template v-for="(item) in menuList">
      <a-sub-menu :key="item.key" v-if="item.children">
        <span slot="title">
          <MyIcon :type="item.iconType" />
          <span>{{ item.msg }}</span>
        </span>
        <template v-for="i in item.children">
          <a-menu-item :key="i.key">
            <span>{{ i.msg }}</span>
          </a-menu-item>
        </template>
      </a-sub-menu>
      <a-menu-item :key="item.key" v-else>
        <MyIcon :type="item.iconType" />
        <span>{{ item.msg }}</span>
      </a-menu-item>
    </template>
  </a-menu>
</template>
<script>
import { Icon } from "ant-design-vue";
const faceConfig = require("../../../../faceConfig");
const menuList = require("../../../../MenuConfig");
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: faceConfig.scriptUrl,
});
import { mapGetters } from "vuex";
export default {
  components: {
    MyIcon,
  },
  data () {
    return {
      menuList,
      selectedKeys: ['dashboard']
    }
  },
  props: {
    defaultOpenKeys: {
      type: Array,
      default: () => {
        return [];
      },
    },
  },
  computed: {
    ...mapGetters({
      StarSelectedKeys: "StateStore/starSelectedKeys",
    }),
  },
  mounted () {
    const _this = this
    _this.StarSelectedKeys != [] ? _this.selectedKeys = _this.StarSelectedKeys : ''
  },
  methods: {
    handleSetSelectedKeys (selectedKeys) {
      const _this = this
      _this.selectedKeys = selectedKeys
    },
    handleGoTo ({ item, key, keyPath }) {
      const _this = this
      _this.$router.push(key)
    }
  },
}
</script>

<style lang="scss" scoped>
.menu {
  text-align: left;
  height: calc(100% - 60px);
  min-height: 540px;
  overflow-y: scroll;
}
/*定义整体的宽度*/
.menu::-webkit-scrollbar {
  display: none;
}

/*定义滚动条轨道*/
.menu::-webkit-scrollbar-track {
  display: none;
}

/*定义滑块*/
.menu::-webkit-scrollbar-thumb {
  display: none;
}
</style>