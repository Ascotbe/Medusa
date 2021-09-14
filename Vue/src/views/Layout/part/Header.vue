<template>
  <!-- <a-icon class="trigger" :type="collapsed ? 'menu-unfold' : 'menu-fold'" @click="handleCollapsed" /> -->
  <a-dropdown class="dropdown">
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
</template>

<script>
import { mapGetters } from "vuex";
const config = require("../../../../faceConfig");
export default {
  data () {
    return {
      headerImg: '',
      username: 'USER'
    }
  },
  mounted () {
  },
  computed: {
    ...mapGetters({
      userinfo: "UserStore/userinfo"
    })
  },
  mounted () {
    this.handleSetUsetInfo(this.userinfo)
  },
  methods: {
    handleMenuClick (e) {
      switch (e.key) {
        case "user":
          this.$router.push("/layout/personalSettings");
          this.$emit('change', ["personalSettings"])
          break;
        case "logOut":
          this.$store.commit('UserStore/setToken', '')
          this.$router.push("/login");
          break;
      }
    },
    handleLoadError () {
      const imgURL = config.imgPath;
      this.headerImg = imgURL + "admin.jpg";
    },
    handleSetUsetInfo (now) {
      const imgURL = config.imgPath;
      this.headerImg = imgURL + now.avatar;
      this.username = now.name
    }
  },
  watch: {
    userinfo: {
      handler: function (now, old) {
        this.handleSetUsetInfo(now)
      },
      deep: true
    }
  }
}
</script>

<style lang="scss" scoped>
.dropdown {
  position: absolute;
  right: 60px;
  .user_name {
    color: aliceblue;
    padding: 10px;
  }
}
</style>