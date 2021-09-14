<template >
  <!-- :style="{width: `${btn_width}px`,height:`${btn_hight}px`}" -->

  <div
    class="btn"
    @mouseover="btn_hover = true"
    @mouseleave="btn_hover = false"
    style="background-color: rgba(223, 245, 255, 0)"
    :style="btnStyle"
    @click="ClickPromise()"
  >
    <span class="name">{{ title }}</span>
    <span class="lefttop"></span>
    <span class="rightbottom"></span>
  </div>
</template>
<script>
export default {
  props: {
    title: {
      default: () => "",
      type: String,
    },
    btn_width: {
      default: () => 146,
      type: Number,
    },
    btn_hight: {
      default: () => 36,
      type: Number,
    },
    //点击后所触发的方法
    ClickPromise: {
      default: () => {
        console.log("click");
      },
      type: [Function],
    },
  },

  name: "Mybtn",
  data() {
    return {
      btn_hover: false,
    };
  },
  computed: {
    btnStyle() {
      // console.log(this.btn_width)
      return {
        width: `${this.btn_width}px`,
        height: `${this.btn_hight}px`,
        "line-height": `${this.btn_hight}px`,
      };
    },
  },
  // watch:
  methods: {},
};
</script>
<style lang="scss">
.btn + .btn {
  margin-left: 10px;
}
.btn {
  background: rgb(0, 0, 0);
  // width: 120px;
  // height: 30px;
  text-align: center;
  margin: 0 30px 30px 0;
  font-size: 10px;
  // line-height: 30px;
  box-sizing: border-box;
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
  display: inline-block;
  .name {
    // transition-delay: 0s;
    -moz-user-select: none;
    -o-user-select: none;
    -khtml-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
}
.btn.on {
  border: 1px solid rgba(223, 245, 255, 1);
}
.btn {
  opacity: 1 !important;
}
.btn {
  transition: opacity 0.5s;
  border: 1px solid rgb(69, 52, 69);
}
.btn .name {
  color: rgba(0, 0, 0, 1);
}
.btn {
  margin-left: 8px;
  position: relative;
  width: 146px;
  height: 36px;
  margin-top: 4px;
  margin-bottom: 4px;
  transition: all 0.6s ease-in-out; /*W3C标准*/
}
.btn.on:after {
  opacity: 0.5;
}
.btn:after {
  border: 1px solid rgba(52, 64, 69, 1);
}
.btn:after {
  content: "";
  position: absolute;
  height: 44px;
  width: 154px;
  opacity: 0;
  top: -5px;
  left: -5px;
}
.btn .lefttop:after,
.btn .lefttop:before {
  top: -1px;
  left: -1px;
  background: rgb(0, 195, 255);
}
.btn .rightbottom:after,
.btn .rightbottom:before {
  bottom: -1px;
  right: -1px;
}
.btn.on {
  background: rgba(223, 245, 255, 1);
} //颜色
.btn .rightbottom:after,
.btn .rightbottom:before {
  background: rgb(0, 255, 21);
}
.btn .lefttop:before,
.btn .rightbottom:before {
  content: "";
  height: 7px;
  width: 1px;
  position: absolute;
  display: block;
  transition: all 0.4s ease-in-out; /*W3C标准*/
}
.btn .lefttop:after,
.btn .rightbottom:after {
  content: "";
  display: block;
  height: 1px;
  width: 7px;
  position: absolute;
  transition: all 0.4s ease-in-out; /*W3C标准*/
}
.btn:focus,
.btn:hover {
  color: #409eff;
  border-color: #f80808;
  background-color: #ff9100;
}
.btn:hover .lefttop:after,
.btn:hover .lefttop:before {
  top: -6px;
  left: -6px;
}
.btn:hover .rightbottom:after,
.btn:hover .rightbottom:before {
  bottom: -6px;
  right: -6px;
}
</style>