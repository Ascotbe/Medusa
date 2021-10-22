<template>
  <!-- 进入等待 -->
  <!-- <div
    class="windows98_loding"
    :style="{background:`url(${this.window_loding}) no-repeat`,'background-size': '100% 100%'}"
    v-if="loding"
  ></div>-->
  <!-- <div class="windows98" @contextmenu.prevent="handleMouseClick" @click="handleContextMenu"> -->
  <div class="windows98">
    <!-- 桌面 -->
    <div class="windows98_desktop" ref="desktop">
      <div
        v-for="(item, i) in desketop"
        class="windows98_desktop_file"
        :key="i"
        @click="handleGoUrl(item.url)"
      >
        <img :src="item.img" alt />
        <div>{{ item.name }}</div>
      </div>
    </div>
    <!-- 开始菜单栏 -->
    <div class="windows98_menu_curtain" v-if="startActive" @click="handleCurtain">
      <div class="windows98_menu_model" ref="menuModel">
        <div class="windows98_menu_model_logo">
          <div class="windows98_menu_model_logo_font">Windows98</div>
        </div>
        <div class="windows98_menu_model_options">
          <div class="windows98_menu_model_options_list">
            <div
              v-for="(item,i) in desketop"
              class="windows98_menu_model_options_list_item"
              :key="i"
              @click="handleGoUrl(item.url)"
              :class="item.key==hover?'windows98_hover':''"
              @mouseover="handleMouseover(item.key)"
              @mouseleave="handleMouseleave"
            >
              <img :src="item.img" alt />
              <div style="padding-left:10px">{{ item.name }}</div>
            </div>
          </div>
          <div class="windows98_menu_model_options_operation">
            <hr style="width: 90%" />
            <div
              class="windows98_menu_model_options_operation_item"
              v-for="(item,i) in operation"
              :key="i"
              :class="item.key==hover?'windows98_hover':''"
              @mouseover="handleMouseover(item.key)"
              @mouseleave="handleMouseleave"
              @click="handleOperation(item.key)"
            >
              <img :src="item.img" alt />
              <div style="padding-left:10px">{{ item.name }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 桌面底部菜单栏 -->
    <div class="windows98_taskbar">
      <button
        class="windows98_taskbar_start"
        :class="startActive?'windows98_taskbar_start_active':''"
        @click="()=> this.startActive=!this.startActive"
      >
        <img :src="windows_start" height="100%" />
        <span>Start</span>
      </button>
      <div class="windows98_taskbar_menu">
        <button
          class="windows98_taskbar_menu_button"
          :class="menuActive?'windows98_taskbar_menu_button_active':''"
          @click="()=>{
            this.menuActive=!this.menuActive
            if(this.menuActive) this.formVisble=true
            else this.formVisble=false
          }"
        >{{ task }}</button>
        <button
          v-show="errVisble"
          class="windows98_taskbar_menu_button windows98_taskbar_menu_button_active"
          style="margin-left:5px"
        >{{ err.title }}</button>
      </div>
      <div class="windows98_taskbar_end">
        <span class>P19e0n Team</span>
      </div>
    </div>
    <!-- 鼠标右击菜单 -->
    <div
      class="windows98_contextmenu"
      ref="contextMenu"
      :style="contextMenuStyle"
      v-if="contextMenu"
    >
      <div
        v-for="(item) in contextMenuListNow"
        :key="item.key"
        :class="item.key==hover?'windows98_hover':''"
        @mouseover="handleMouseover(item.key)"
        @mouseleave="handleMouseleave"
        style="padding:0 5px 0 5px"
      >
        <div class="windows98_contextmenu_item">
          <img :src="item.img" alt />
          <div style="padding-left:10px">{{ item.key }}</div>
        </div>
        <hr style="position: relative;top: 2px;" />
      </div>
    </div>
    <!-- 主要功能表单浮窗 -->
    <div class="windows98_form window" v-show="formVisble">
      <div class="title-bar">
        <div class="title-bar-text">{{task}}</div>
        <div class="title-bar-controls">
          <button
            aria-label="Minimize"
            @click="()=>{this.formVisble=false  
            this.menuActive= false
            }"
          ></button>
          <!-- <button aria-label="Close"></button> -->
        </div>
      </div>
      <div class="window-body">
        <slot></slot>
        <button style="margin-top:8px" @click="handleOk">Ok</button>
      </div>
    </div>
    <!-- err提示框 -->
    <div class="windows98_err window" v-show="errVisble">
      <div class="title-bar">
        <div class="title-bar-text">{{err.title}}</div>
        <div class="title-bar-controls">
          <button aria-label="Close" @click="()=>{ this.errVisble = false}"></button>
          <!-- <button aria-label="Close"></button> -->
        </div>
      </div>
      <div class="window-body">
        <p>{{err.message}}</p>
        <button @click="handleErrClose">Ok</button>
      </div>
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
      window_loding: require("@/assets/windows98/LODING.gif"),
      loding: true,
      desketop: [
        {
          img: require("@/assets/windows98/computer.png"),
          name: "My Computer",
          url: "https://github.com/Ascotbe/Medusa",
          key: 'MyComputer'
        },
        {
          img: require("@/assets/windows98/directory_closed_cool.png"),
          name: "Learning Materials",
          url: "http://medusa.ascotbe.com/Documentation/#/",
          key: 'LearningMaterials'
        },
        {
          img: require("@/assets/windows98/recycle_bin_file_directory.png"),
          name: "Recycle Bin",
          url: "/",
          key: 'RecycleBin'
        },
        {
          img: require("@/assets/windows98/html.png"),
          name: "Ascotbe的妙妙屋",
          url: "https://github.com/Ascotbe",
          key: 'Ascotbe'
        },
      ],
      operation: [
        // {
        //   img: require("@/assets/windows98/computer.png"),
        //   name: "User",
        //   key: 'User'
        // },
        {
          img: require("@/assets/windows98/computer.png"),
          name: "Shut Down",
          key: 'ShutDown'
        },
      ],
      startActive: false,
      menuActive: true,
      contextMenu: false,
      contextMenuStyle: {},
      contextMenuList: [//所有情况下的右击菜单
        {
          key: 'desktop',
          data: [
            {
              img: require("@/assets/windows98/directory_closed_cool.png"),
              name: '前往注册',
              key: 'Register'
            },
            {
              img: require("@/assets/windows98/directory_closed_cool.png"),
              name: '修改密码',
              key: 'Password'
            }
          ]
        }
      ],
      contextMenuListNow: [],//当前位置的右击菜单
      hover: '',//hover特效
      formVisble: true,//表单可视
      err: { //err提示框 内容
        title: 'ERR',
        message: 'There is a mistake'
      },
      errVisble: false,//err提示框可视

      // errTimeOut: ''//err自动隐藏的定时器
    };
  },
  methods: {
    handleGoUrl (url) {//跳转
      if (url == "/") {
      } else {
        window.location.href = url;
      }
    },
    handleOperation (key) {
      const _this = this
      _this.startActive = false
      if (key == 'ShutDown') {
        const Tips = {
          title: 'Tips',
          message: 'Whether Shut Down'
        }
        const callback = () => {
          _this.$router.push('/login')
        }
        _this.handleErrShow(Tips, callback)

      }
    },
    handleCurtain (e) {//幕布监听鼠标再菜单栏外
      const _this = this
      if (!_this.startActive) {
        return
      }
      if (!_this.$refs.menuModel.contains(e.target)) _this.handleMenuClose()
    },
    handleMenuClose () {//菜单栏关闭
      const _this = this
      _this.startActive = false
    },
    handleMouseClick (e) {//监听鼠标右键
      const _this = this
      _this.contextMenuList.map((item) => {
        for (const key in _this.$refs) {
          if (key == item.key && _this.$refs[key].contains(e.target)) _this.contextMenuListNow = item.data
        }
      })
      _this.contextMenu = true
      _this.contextMenuStyle = {
        top: `${e.y}px`,
        left: `${e.x}px`
      }

    },
    handleContextMenu (e) {//右击菜单监听鼠标再菜单栏外
      const _this = this
      if (!_this.$refs.contextMenu?.contains(e.target)) _this.handleContextMenuClose()
    },
    handleContextMenuClose () {//右击菜单栏关闭
      const _this = this
      _this.contextMenu = false
    },
    handleMouseover (key) {
      const _this = this
      _this.hover = key
    },
    handleMouseleave () {
      const _this = this
      _this.hover = -1
    },
    //显示错误框 传入报错信息
    //  errObject: { 
    //     title: 'ERR',
    //     message: 'There is a mistake'
    //   },
    handleErrShow (errObject, callback) {
      const _this = this
      _this.err = errObject
      _this.errVisble = true
      if (callback) _this.handleErrClose = callback
      else _this.handleErrClose = () => {
        _this.errVisble = false
      }
      // if (_this.errTimeOut) {
      //   clearTimeout(_this.errTimeOut)
      // }
      // else {
      //   _this.errTimeOut = setTimeout(() => {
      //     _this.errVisble = false
      //   }, 3000);
      // }
    },
    handleErrClose () {
      const _this = this
      // clearTimeout(_this.errTimeOut)
      _this.errVisble = false
    },
    handleOk () {
      const _this = this
      _this.$emit('Ok')
    },
  },
  // created () {
  //   const _this = this
  //   const time = setTimeout(() => {
  //     _this.loding = false
  //     clearTimeout(time)
  //   }, 1000);
  // }
};
</script>
<style src="../../../node_modules/98.css/dist/98.css" scoped></style>
<style lang="scss" scoped>
.windows98_loding {
  position: absolute;
  z-index: 101;
  width: 100%;
  height: 100%;
}
.windows98 {
  font-family: "Pixelated MS Sans Serif", Arial;
  display: -webkit-flex; /* Safari */
  display: flex;
  background-color: teal;
  height: 100%;
  min-height: 600px;
  overflow: auto;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
  flex-direction: column;
  justify-content: space-between;
  .windows98_desktop {
    flex-grow: 1;
    display: -webkit-flex; /* Safari */
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    .windows98_desktop_file {
      padding: 5px;
      min-width: 150px;
      color: #fff;
      cursor: pointer;
    }
  }
  .windows98_taskbar {
    height: 35px;
    padding: 4px;
    background-color: silver;
    display: -webkit-flex; /* Safari */
    display: flex;
    justify-content: space-between;
    .windows98_taskbar_start {
      cursor: pointer;
      height: 100%;
      padding: 2px 6px 3px;
      // background-color: silver;
      // border-top: 1px solid #fff;
      // border-left: 1px solid #fff;
      // border-right: 2px solid gray;
      // border-bottom: 2px solid gray;
      // box-shadow: inset 1px 1px #dfdfdf, 1px 0 #000, 0 1px #000, 1px 1px #000;
      min-width: 80px;
      line-height: 22px;
      font-size: 16px;
      font-weight: 800;
      color: #000;
    }
    .windows98_taskbar_start_active {
      box-shadow: inset -1px -1px #ffffff, inset 1px 1px #0a0a0a,
        inset -2px -2px #dfdfdf, inset 2px 2px #808080;
    }
    .windows98_taskbar_menu {
      display: -webkit-flex; /* Safari */
      display: flex;
      // justify-content: space-between;
      padding-left: 20px;
      padding-right: 20px;

      // justify-content: space-around;
      flex-grow: 1;
      .windows98_taskbar_menu_button {
        cursor: pointer;
        height: 100%;
        padding: 2px 6px 3px;
        // background-color: silver;
        // border-top: 1px solid #fff;
        // border-left: 1px solid #fff;
        // border-right: 2px solid gray;
        // border-bottom: 2px solid gray;
        // box-shadow: inset 1px 1px #dfdfdf, 1px 0 #000, 0 1px #000, 1px 1px #000;
        min-width: 180px;
        line-height: 22px;
        font-size: 16px;
        font-weight: 800;
        color: #000;
      }
      .windows98_taskbar_menu_button_active {
        box-shadow: inset -1px -1px #ffffff, inset 1px 1px #0a0a0a,
          inset -2px -2px #dfdfdf, inset 2px 2px #808080;
      }
    }
    .windows98_taskbar_end {
      height: 100%;
      padding: 2px 6px 3px;
      background-color: silver;
      border-top: 1px solid grey;
      border-left: 1px solid grey;
      border-right: 1px solid #fff;
      border-bottom: 1px solid #fff;
      box-shadow: inset -1px -1px #dfdfdf, inset 1px 1px grey;
      min-width: 160px;
      line-height: 22px;
      font-size: 16px;
      font-weight: 800;
      color: #000;
    }
  }
  .windows98_menu_curtain {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;

    .windows98_menu_model {
      position: absolute;
      bottom: 35px;
      left: 0;
      max-height: 500px;
      height: 50%;
      min-height: 353px;
      width: 250px;
      display: -webkit-flex; /* Safari */
      display: flex;
      justify-content: space-between;
      background: silver;
      box-shadow: inset -1px -1px #0a0a0a, inset 1px 1px #dfdfdf,
        inset -2px -2px grey, inset 2px 2px #fff;
      .windows98_menu_model_logo {
        width: 35px;
        height: 100%;
        padding-bottom: 10px;
        background: linear-gradient(0deg, navy, #1084d0);
        display: -webkit-flex; /* Safari */
        display: flex;
        flex-direction: row;
        align-items: flex-end;
        justify-content: flex-start;
        .windows98_menu_model_logo_font {
          transform: rotate(270deg);
          transform-origin: 12% 50%;
          font-size: 30px;
          color: #fff;
        }
      }
      .windows98_menu_model_options {
        height: 100%;
        width: 215px;
        display: -webkit-flex; /* Safari */
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        justify-content: space-between;
        align-items: flex-start;
        .windows98_menu_model_options_list {
          height: 100%;
          width: 215px;
          display: flex;
          flex-direction: column;
          flex-wrap: nowrap;
          align-items: flex-start;
          .windows98_menu_model_options_list_item {
            width: 100%;
            display: flex;
            padding-top: 10px;
            justify-content: flex-start;
            align-items: center;
            flex-direction: row;
            flex-wrap: nowrap;
            cursor: pointer;
            padding: 10px;
          }
        }
        .windows98_menu_model_options_operation {
          height: 100%;
          width: 215px;
          display: flex;
          flex-direction: column;
          flex-wrap: nowrap;
          align-items: flex-start;
          justify-content: flex-end;
          .windows98_menu_model_options_operation_item {
            width: 100%;
            display: flex;
            padding-top: 10px;
            justify-content: flex-start;
            align-items: center;
            flex-direction: row;
            flex-wrap: nowrap;
            cursor: pointer;
            padding: 10px;
          }
        }
      }
    }
  }
  .windows98_contextmenu {
    z-index: 99;
    width: 150px;
    height: 200px;
    position: absolute;
    background: silver;
    box-shadow: inset -1px -1px #ffffff, inset 1px 1px #0a0a0a,
      inset -2px -2px #dfdfdf, inset 2px 2px #808080;
    .windows98_contextmenu_item {
      padding: 5px 10px 0px 10px;
      display: -webkit-flex; /* Safari */
      display: flex;
      justify-content: flex-start;
      flex-direction: row;
      cursor: pointer;
      align-items: center;
    }
  }
  .windows98_form {
    width: 40%;
    min-width: 380px;
    max-width: 580px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .windows98_err {
    position: absolute;
    z-index: 100;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 14px;
  }

  .windows98_hover {
    background: linear-gradient(0deg, navy, #1084d0);
    color: #fff;
  }
}
</style>
