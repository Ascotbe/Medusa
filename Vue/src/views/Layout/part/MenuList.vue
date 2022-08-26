<template>
  <a-menu
    class="menu"
    :class="collapsed?'shrinkState':''"
    mode="inline"
    theme="dark"
    v-model="selectedKeys"
    :defaultOpenKeys="defaultOpenKeys"
    v-bind="$props"
    v-on="$listeners"
    @click="handleGoTo"
  >
    <template v-for="(item) in menuList">
      <a-sub-menu :key="item.key" v-if="item.children &&item.show">
        <span slot="title">
          <MyIcon :type="item.iconType" />
          <span>{{ item.msg }}</span>
        </span>
        <template v-for="i in item.children">
          <a-menu-item :key="i.key" v-if="i.show">
            <span>{{ i.msg }}</span>
          </a-menu-item>
        </template>
      </a-sub-menu>
      <a-menu-item :key="item.key" v-if="!item.children && item.show">
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
      selectedKeys: ['dashboard'],
    }
  },
  props: {
    defaultOpenKeys: {
      type: Array,
      default: () => {
        return [];
      },
    },
    inlineCollapsed: {
      type: Boolean,
      default: () => false
    },
    inlineIndent: {
      type: Number,
      default: () => 24
    },
    collapsed: {
      type: Boolean,
      default: () => false
    }
  },
  computed: {
    ...mapGetters({
      StarSelectedKeys: "StateStore/starSelectedKeys",
    }),
  },
  mounted () {
    this.StarSelectedKeys != [] ? this.selectedKeys = this.StarSelectedKeys : ''
  },
  methods: {
    handleSetSelectedKeys (selectedKeys) {
      this.selectedKeys = selectedKeys
    },
    handleGoTo ({ item, key, keyPath }) {
      this.$router.push(key)
    }
  },
  watch: {
    collapsed: {
      handler: function (val) {
        //是否收缩菜单 false展开 true 收缩
        if (val) {

        }
      }
    }
  }

}
</script>

<style lang="scss" scoped>
.shrinkState {
  width: 40px;
  li {
    padding: 0 0 !important;
    text-align: center;
    ::v-deep .ant-menu-submenu-title {
      padding: 0 0 !important;
      text-align: center;
    }
  }
}

.menu {
  text-align: left;
  height: calc(100% - 120px);
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