<template>
  <div class="windows98">
    <div class="windows98_background"></div>
    <div class="windows98_main">
      <slot></slot>
    </div>
    <div class="windows98_desktop">
      <div
        class="windows98_desktop_list"
        v-for="(item, i) in desketop"
        :key="i"
        @click="handleGoUrl(item.url)"
      >
        <div class="windows98_desktop_list_icon">
          <img :src="item.img" alt />
        </div>
        <div class="windows98_desktop_list_name">{{ item.name }}</div>
      </div>
    </div>
    <div class="windows98_start">
      <a class="windows98_start_win">
        <img :src="windows_start" height="100%" />
        <span>Start</span>
      </a>
      <span class="windows98_start_task">{{ task }}</span>
      <span class="windows98_start_team">P19e0n团队出品</span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    task: {
      type: String,
      default: "Change Password",
    },
  },
  data () {
    return {
      windows_start: require("@/assets/windows98/windows.png"),
      desketop: [
        {
          img: require("@/assets/windows98/computer.png"),
          name: "我的电脑",
          url: "https://github.com/Ascotbe/Medusa",
        },
        {
          img: require("@/assets/windows98/directory_closed_cool.png"),
          name: "学习资料",
          url: "http://medusa.ascotbe.com/Documentation/#/",
        },
        {
          img: require("@/assets/windows98/recycle_bin_file_directory.png"),
          name: "回收站",
          url: "/",
        },
        {
          img: require("@/assets/windows98/html.png"),
          name: "Ascotbe的妙妙屋",
          url: "https://github.com/Ascotbe",
        },
      ],
    };
  },
  methods: {
    handleGoUrl (url) {
      if (url == "/") {
      } else {
        window.location.href = url;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.windows98 {
  height: 100%;
  .windows98_background {
    width: 100%;
    height: 100%;
    position: absolute;
    background-color: teal;
  }
  .windows98_desktop {
    width: 150px;
    position: absolute;
    z-index: 10;
    left: 0;
    top: 20px;
    .windows98_desktop_list {
      min-width: 50px;
      padding: 8px;
    }
    .windows98_desktop_list_icon {
      text-align: center;
      cursor: pointer;
    }
    .windows98_desktop_list_name {
      cursor: pointer;
      text-align: center;
      color: #fff;
      font-size: 16px;
    }
  }
  .windows98_main {
    position: relative;
    height: 100%;
  }
  .windows98_start {
    display: block;
    padding: 2px;
    width: 100%;
    height: 35px;
    position: fixed;
    z-index: 10;
    bottom: 0px;
    left: 0;
    right: 0;
    background-color: silver;
    border-top: 1px solid #f4f4f4;
    border-bottom: 1px solid #4e4e4e;
    .windows98_start_win {
      float: left;
      height: 100%;
      padding: 2px 6px 3px;
      background-color: silver;
      border-top: 1px solid #fff;
      border-left: 1px solid #fff;
      border-right: 1px solid gray;
      border-bottom: 1px solid gray;
      box-shadow: inset 1px 1px #dfdfdf, 1px 0 #000, 0 1px #000, 1px 1px #000;
      min-width: 59px;
      line-height: 22px;
      font-size: 16px;
      font-weight: 800;
      color: #000;
    }
    .windows98_start_task {
      text-align: center;
      margin-left: 20px;
      height: 100%;
      line-height: 22px;
      min-width: 110px;
      float: left;
      padding: 2px 6px 3px;
      border-top: 1px solid #000;
      border-left: 1px solid #000;
      vertical-align: middle;
      border-right: 1px solid rgb(212, 212, 212);
      border-bottom: 1px solid rgb(212, 212, 212);
      font-family: Arial;
      font-weight: 400;
      color: #000;
      box-shadow: inset 1px 1px grey;
    }
    .windows98_start_team {
      float: right;
      height: 100%;
      line-height: 22px;
      text-align: right;
      padding: 2px 6px 3px;
      border-top: 1px solid gray;
      border-left: 1px solid gray;
      border-right: 1px solid rgb(212, 212, 212);
      border-bottom: 1px solid rgb(212, 212, 212);
      font-weight: 400;
      color: #000;
    }
  }
}
</style>
