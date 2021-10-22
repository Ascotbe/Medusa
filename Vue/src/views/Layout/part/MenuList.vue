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
      menuList: [
        {
          key: "personalSettings",
          iconType: "icon-Serviceusers",
          msg: "个人界面",
        },
        {
          key: "dashboard",
          iconType: "icon-ziyuan",
          msg: "仪表盘",
        },
        {
          key: "DNSLOG",
          iconType: "icon-DNSziyuan",
          msg: "DNSLOG",
        },
        {
          key: "ActiveScanning",
          iconType: "icon-saomiao1",
          msg: "主动扫描",
          children: [
            {
              key: "issueTasks",
              msg: "下发任务",
            },
            {
              key: "siteInformation",
              msg: "站点扫描",
            },
          ],
        },
        {
          key: "sub2",
          iconType: "icon-saomiao2",
          msg: "被动扫描",
          children: [],
        },
        {
          key: "Monitor",
          iconType: "icon-jiankong",
          msg: "监控页面",
          children: [
            {
              key: "GitHubMonitor",
              msg: "GitHub监控",
            },
            {
              key: "VulnerabilitiesMonitor",
              msg: "CVE监控",
            },
          ],
        },
        {
          key: "CrossSiteScript",
          iconType: "icon-heike",
          msg: "跨站脚本钓鱼",
          children: [
            {
              key: "CreateCrossSiteScript",
              msg: "创建项目",
            },
            {
              key: "ProjectManagement",
              msg: "项目管理",
            },
            {
              key: "TemplateManagement",
              msg: "模板管理",
            },
            {
              key: "PrivateTemplate",
              msg: "创建自定义模板",
            },
          ],
        },
        {
          key: "Combine",
          iconType: "icon-xietong",
          msg: "协同作战",
          children: [
            {
              key: "CreateCombine",
              msg: "创建/加入项目",
            },
            {
              key: "CombineList",
              msg: "项目列表",
            },
          ],
        },
        {
          key: "ShellCode",
          iconType: "icon-heike",
          msg: "Shell Code",
          children: [
            {
              key: "ShellCodeToTrojan",
              msg: "免杀生成",
            },
          ],
        },
        {
          key: "Toolbar",
          iconType: "icon-gongju",
          msg: "工具栏",
          children: [
            {
              key: "antivirusSoftwareCompared",
              msg: "杀毒软件进程查询接口",
            },
          ],
        },
        {
          key: "About",
          iconType: "icon-Serviceusers",
          msg: "关于",
        },
      ],
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
    // defaultSelectedKeys: {
    //   type: Array,
    //   default: () => {
    //     return ['personalSettings'];
    //   },
    // },
    // selectedKeys: {
    //   type: Array,
    //   default: () => {
    //     return ['personalSettings'];
    //   },
    // }
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
  // render: function (h) {
  //   return h(
  //     'a-menu',   // 标签名称
  //     {
  //       props: {
  //         theme: "dark",
  //         mode: 'inline',
  //         // selectedKeys: this.activeIndex,
  //         defaultSelectedKeys: this.defaultSelectedKeys
  //       },
  //     },
  //     this.menuList.map((item) => {
  //       // return item.children ?
  //       //   <a-sub-menu key={item.key}>
  //       //     <span>{item.msg}</span>
  //       //   </a-sub-menu> :
  //       //   <a-menu-item key={item.key}>
  //       //     <span>{item.msg}</span>
  //       //   </a-menu-item>
  //       if (item.children) {
  //         return h('a-sub-menu',
  //           {
  //             props: {
  //               title: item.msg,
  //               key: item.key
  //             },
  //           },
  //           item.children.map((itemChildren) => {
  //             console.log('itemChildren', itemChildren)
  //             return h('a-menu-item',
  //               {
  //                 domProps: {
  //                   key: itemChildren.key
  //                 },
  //               },
  //               itemChildren.msg)
  //           })
  //         )
  //       }
  //       else {
  //         console.log('item', item)
  //         return h('a-menu-item',
  //           {
  //             props: {
  //               key: item.key
  //             },
  //           },
  //           item.msg)
  //       }
  //     })
  //   )
  // },
}
</script>

<style lang="scss" scoped>
.menu {
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