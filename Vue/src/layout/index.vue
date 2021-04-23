<template>
  <keep-alive>
    <a-config-provider :locale="locale">
      <a-layout class="layout">
        <a-layout-sider
          class="layout_sider"
          v-model="collapsed"
          :trigger="null"
          collapsible
          breakpoint="lg"
          collapsed-width="0"
          ref="layout_sider"
        >
          <div class="logo">
            <img width="100%" height="100%" src="../assets/logo.png" />
          </div>
          <a-menu
            theme="dark"
            mode="inline"
            :selectedKeys="activeIndex"
            :default-open-keys="defaultOpenKeys"
          >
            <template v-for="item in menuList">
              <a-menu-item :key="item.key" @click="handleGoChange" v-if="!item.children">
                <myicon :type="item.iconType" />
                <span>{{ item.msg }}</span>
              </a-menu-item>
              <sub-menu
                v-else
                :key="item.key"
                :menu-info="item"
                :handleGoChange="handleGoChange"
              />
            </template>
          </a-menu>
          <!--
                <div class="footer">
                    Medusa
                    <br>
                    Copyright 2019-2020 P19e0n团队出品
                </div>
               -->
        </a-layout-sider>
        <a-layout>
          <a-layout-header class="layout_header">
            <a-icon
              class="trigger"
              :type="collapsed ? 'menu-unfold' : 'menu-fold'"
              @click="handleCollapsed"
            />
            <div class="control">
              <a-dropdown class="user">
                <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
                  <a-avatar :src="headerImg" :loadError="handleLoadError" />
                  <span class="user_name">{{ username }}</span>
                </a>
                <a-menu slot="overlay" @click="handleMenuClick">
                  <a-menu-item key="user">
                    <a-icon type="setting" />个人中心
                  </a-menu-item>
                  <a-menu-item key="logOut">
                    <a-icon type="poweroff" />退出登录
                  </a-menu-item>
                </a-menu>
              </a-dropdown>
              <div class="language">
                <a-button @click="handelSetLanguage"> {{ language }} </a-button>
              </div>
            </div>
          </a-layout-header>

          <a-layout-content>
            <router-view></router-view>
          </a-layout-content>
        </a-layout>
      </a-layout>
    </a-config-provider>
  </keep-alive>
</template>

<script>
import { Icon } from "ant-design-vue";
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1734998_x30axu5phw.js",
});
import zhCN from "ant-design-vue/lib/locale-provider/zh_CN";
import enUS from "ant-design-vue/lib/locale-provider/en_US";
import SubMenu from "./SubMenu";

export default {
  name: "layout",
  components: {
    myicon: MyIcon,
    "sub-menu": SubMenu,
  },
  data() {
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
          key: "sub1",
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
          key: "sub3",
          iconType: "icon-jiankong",
          msg: "监控页面",
          children: [
            {
              key: "nist_data_bulk_query",
              msg: "CVE监控",
            },
            {
              key: "gitHub",
              msg: "GitHub监控",
            },
          ],
        },
        {
          key: "sub4",
          iconType: "icon-heike",
          msg: "跨站脚本钓鱼",
          children: [
            {
              key: "createProject",
              msg: "创建项目",
            },
            {
              key: "projectManagement",
              msg: "项目管理",
            },
            {
              key: "publicTemplate",
              msg: "模板管理",
            },
            {
              key: "customTemplate",
              msg: "创建自定义模板",
            },
          ],
        },
        {
          key: "sub5",
          iconType: "icon-xietong",
          msg: "协同作战",
          children: [
            {
              key: "createCombine",
              msg: "创建/加入项目",
            },
            {
              key: "combinedList",
              msg: "项目列表",
            },
          ],
        },
        {
          key: "sub6",
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
          key: "domain_name_system_log",
          iconType: "icon-DNSziyuan",
          msg: "DNSLOG",
        },
        {
          key: "about_us",
          iconType: "icon-guanyuwomen1-02",
          msg: "关于我们",
        },
      ],
      top: 0.1,
      collapsed: false,
      contentBackground: {
        background: "rgba(242,242,242,1)",
        padding: "10px",
      },
      locale: zhCN,
      activeIndex: [],
      defaultOpenKeys: [],
      username: "",
      headerImg: "",
      language: "中文",
    };
  },
  created() {
    this.Refresh();
  },
  mounted() {
    this.handleGetuserinfo();
  },
  computed: {
    getAvatar() {
      return this.$store.state.avatar;
    },
  },
  methods: {
    handleCollapsed() {
      this.collapsed = !this.collapsed;
    },
    handleGoChange(e) {
      this.$router.push("/layout/" + e.key);
    },
    handleMenuClick(e) {
      switch (e.key) {
        case "user":
          this.$router.push("/layout/personalSettings");
          this.activeIndex = ["personalSettings"];
          break;
        case "logOut":
          this.$store.commit("close");
          localStorage.setItem("storeToken", "");
          this.$router.push("/");
          break;
      }
    },
    handelSetLanguage(e) {
      if (this.language == "中文") {
        this.language = "English";
        this.locale = enUS;
      } else if (this.language == "English") {
        this.language = "中文";
        this.locale = zhCN;
      }
    },

    handleGetuserinfo() {
      const config = require("../../faceConfig");
      const imgURL = config.imgPath;
      let params = {
        token: localStorage.getItem("storeToken"),
      };
      // console.log(params + "开始验证身份");
      this.$api.user_info(params).then((res) => {
        if (res.code == 200) {
          let userinfo = {
            email: res.message.email,
            name: res.message.name,
            show_name: res.message.show_name,
            key: res.message.key,
          };
          let avatar = res.message.avatar;
          this.$store.commit("avatar", avatar);
          this.headerImg = imgURL + res.message.avatar;
          (this.username = res.message.name), this.$store.commit("userinfo", userinfo);
        } else {
          this.$message.error("用户信息获取出现问题，请重新登录");
          this.$router.push("/");
        }
      });
    },
    Refresh() {
      this.activeIndex = [this.$route.meta.activeIndex];
      if (this.$route.meta.defaultOpenKeys) {
        this.defaultOpenKeys = [this.$route.meta.defaultOpenKeys];
      }
    },
    handleLoadError() {
      const config = require("../../faceConfig");
      const imgURL = config.imgPath;
      this.headerImg = imgURL + "admin.jpg";
    },
  },
  watch: {
    $route(to) {
      this.activeIndex = [to.name];
      this.Refresh();
      this.handleGetuserinfo();
    },
    getAvatar: function (old, newd) {
      const config = require("../../faceConfig");
      const imgURL = config.imgPath;
      this.headerImg = imgURL + old;
    },
    // collapsed: function(){
    //   this.$store.commit('collapsed',this.collapsed)
    // },
    collapsed: function () {
      this.$store.commit("collapsed", this.collapsed);
    },
  },
};
</script>

<style lang="scss" scoped>
.icon {
  font-size: 40px;
}

.layout {
  height: 100%;
  .layout_header {
    background: #fff;
    padding: 0;
    display: flex;
    justify-content: space-between;
    .control {
      display: flex;

      .user {
        color: #000;
        align-self: flex-start;
        padding-left: 15px;
        padding-right: 10px;

        .user_name {
          margin-left: 10px;
          font-size: 16px;
        }

        // .user_item {
        //     border-top: 1px solid rgb(2, 177, 247);
        //     background: rgba(236, 236, 236, 0.5);
        // }
      }

      .user:hover {
        background: rgba(236, 236, 236, 0.5);
      }

      .language {
        width: 80px;
        align-self: flex-end;
        margin-right: 0px;
        margin-left: 10px;
      }
    }
  }
}

// .layout_sider /deep/ .ant-layout-sider-children {
//     display: flex;

//     .footer {

//         align-self: flex-end;
//         color: #fff;
//     }
// }

.layout .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

.layout .trigger:hover {
  color: #1890ff;
}

.layout .logo {
  height: 60px;
  padding: 10px;
}

// .ant-menu>>>.ant-menu-item-selected,
// .ant-menu-submenu-popup>>>.ant-menu-item-selected {
//     background-color: rgb(114, 193, 65);
// }
</style>
