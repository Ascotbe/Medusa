<template>
  <div class="createProject">
    <a-row
      :gutter="[
        { xs: 8, sm: 8, md: 8, xs: 8 },
        { xs: 8, sm: 16, md: 24, lg: 32 },
      ]"
      class="createProject_bg"
    >
      <a-col
        :xs="{ span: 24 }"
        :lg="{ span: 8 }"
        :xl="{ span: 8 }"
        :xxl="{ span: 6 }"
        class="createProject_bg_bg"
      >
        <a-col :xs="{ span: 24 }" class="read">
          <Tabbten
            @handelSetActiveL="handelSetActiveL"
            @handelSetActiveR="handelSetActiveR"
          ></Tabbten>
          <a-list
            item-layout="horizontal"
            class="read_horizontal"
            :data-source="DefaultScriptTemplate"
            :column="[24]"
          >
            <a-list-item slot="renderItem" slot-scope="item">
              <!-- <a slot="actions" @click="handleReadOnly(item)">修改模板</a>-->
              <a-list-item-meta>
                <span slot="title" class="read_font" @click="handleSelectData(item)">{{
                  item.template_name
                }}</span>
                <myicon type="icon-js" slot="avatar" class="icon" />
              </a-list-item-meta>
            </a-list-item>
          </a-list>
          <!--       <a-col :xs="{ span: 24 }" class="read_border">
                </a-col>-->
        </a-col>
      </a-col>
      <a-col
        :xs="{ span: 24 }"
        :lg="{ span: 16 }"
        :xl="{ span: 16 }"
        :xxl="{ span: 18 }"
        class="createProject_bg_bg"
      >
        <a-col :xs="{ span: 24 }" class="ruleForm">
          <a-form-model
            :model="form"
            :label-col="labelCol"
            :wrapper-col="wrapperCol"
            ref="ruleForm"
          >
            <a-form-model-item
              label="模板名称"
              prop="template_name"
              :labelAlign="'left'"
              class="form_model_item"
            >
              <a-input v-model="form.template_name" :disabled="true" />
            </a-form-model-item>
            <a-form-model-item
              label="模板内容"
              prop="template_data"
              :labelAlign="'left'"
              class="form_model_item"
            >
              <codemirror
                ref="myCm"
                v-model="form.template_data"
                :options="cmOptions"
                class="code"
              ></codemirror>
            </a-form-model-item>
            <a-form-model-item
              class="item_btn form_model_item"
              :wrapper-col="{ span: 24 }"
            >
              <a-button type="primary" @click="handleOnSubmit" :disabled="Display">
                保存修改
              </a-button>
            </a-form-model-item>
          </a-form-model>
          <div class="zhizhu">
            <img
              :src="zhizhu"
              height="300px"
              alt=""
              class="zhizhu_img"
              ref="zhizhu"
              :class="inAnimation ? 'zhizhu_animation' : ''"
              @animationend="inAnimation = false"
              @click="handleShaking"
            />
          </div>
        </a-col>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { Icon } from "ant-design-vue";
import Tabbten from "../../../components/Tabbten.vue";
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1734998_apjce2fwnsu.js",
});

export default {
  components: {
    myicon: MyIcon,
    Tabbten,
  },
  data() {
    return {
      zhizhu: require("../../../assets/zhizhu.png"),
      inAnimation: false,
      labelCol: {
        span: 20,
        offset: 2,
      },
      wrapperCol: {
        span: 20,
        offset: 2,
      },
      form: {
        template_name: "",
        template_data: "",
      },
      DefaultScriptTemplate: [],
      DisplayState: false,
      Display: true,
      cmOptions: {
        mode: "javascript",
        theme: "duotone-light",
        lineNumbers: true,
        lineWrapping: true,
        line: true,
        readOnly: "nocursor", //只读 nocursor
        matchBrackets: true,
      },
    };
  },
  mounted() {
    this.handleReadDefaultScriptTemplate();
  },
  methods: {
    handleReadDefaultScriptTemplate() {
      let params = {
        token: localStorage.getItem("storeToken"),
      };
      this.$api.read_default_script_template(params).then((res) => {
        let DefaultScriptTemplate = [];
        if (res.code == 200) {
          res.message.map((item) => {
            let Template = {
              template_data: this.$qj.QJBase64Decode(item.file_data),
              template_name: item.file_name,
            };
            DefaultScriptTemplate.push(Template);
          });
          this.DefaultScriptTemplate = DefaultScriptTemplate;
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleSelectData(val) {
      if (this.DisplayState) {
        this.Display = false;
      } else {
        this.Display = true;
      }
      this.form = {
        template_name: val.template_name,
        template_data: val.template_data,
      };

      this.cmOptions.readOnly = false;
      this.handleShaking();
    },
    // handleReadOnly(val) { //修改
    //     this.form = {
    //         template_name: val.template_name,
    //         template_data: val.template_data,
    //     };
    //     this.cmOptions.readOnly = false
    //     this.handleShaking()
    // },
    handelSetActiveL() {
      this.DisplayState = false;
      this.handleReadDefaultScriptTemplate();
    },
    handelSetActiveR() {
      this.DisplayState = true;
      let params = {
        token: localStorage.getItem("storeToken"),
      };
      let list = [];
      this.$api.read_script_template(params).then((res) => {
        if (res.code == 200) {
          res.message.map((item) => {
            let options = {
              template_data: this.$qj.QJBase64Decode(item.template_data),
              template_name: item.template_name,
            };
            list.push(options);
          });
          this.DefaultScriptTemplate = list;
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleShaking() {
      let deg = Math.round(Math.random() * 45); //0-45随机数
      this.$refs.zhizhu.style.setProperty("--Deg", deg + "deg");
      this.$refs.zhizhu.style.setProperty("--Deg2", -deg + "deg");
      this.inAnimation = true;
    },
    handleOnSubmit() {
      let form = this.form;
      if (form.template_name != "") {
        let params = {
          template_name: form.template_name,
          template_data: form.template_data,
          token: localStorage.getItem("storeToken"),
        };
        this.$api.modify_cross_site_script_template(params).then((res) => {
          if (res.code == 200) {
            this.$message.success("模板修改成功");
            this.handelSetActiveR();
          } else {
            this.$message.error(res.message);
          }
        });
      } else {
        this.$message.error("请确定您选择了模板");
        return false;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
$color: #51c51a;

.icon {
  font-size: 30px;
}

.read_font {
  font-size: 20px;
}

.read_font:hover {
  color: $color;
  cursor: pointer;
}

.createProject {
  margin: 0;
  padding: 20px;
  padding-top: 20px;
  padding-bottom: 0;
  min-width: 300px;
  height: 100%;
  min-height: 850px;

  .createProject_bg {
    height: 100%;
    min-height: auto;
    .createProject_bg_bg {
      height: 100%;
    }
  }

  .zhizhu {
    text-align: center;
    padding: 0;

    .zhizhu_img {
      transform: rotate(0deg);
      transform-origin: center top;
      cursor: pointer;
    }

    .zhizhu_animation {
      --Deg: 30deg;
      --Deg2: -30deg;
      animation: Shaking 4s linear;
      -moz-animation: Shaking 4s linear;
      /* Firefox */
      -webkit-animation: Shaking 4s linear;
      /* Safari 和 Chrome */
      -o-animation: Shaking 4s linear;
      /* Opera */
    }

    @keyframes Shaking {
      0% {
        transform: rotate(0deg);
      }

      25% {
        transform: rotate(var(--Deg));
      }

      50% {
        transform: rotate(0deg);
      }

      75% {
        transform: rotate(var(--Deg2));
      }

      100% {
        transform: rotate(0deg);
      }
    }
  }

  .read,
  .ruleForm {
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 18px;
    height: 100%;

    .item_btn {
      margin-top: 20px;
      text-align: center;
    }
  }

  .ruleForm /deep/ .ant-form-item-control {
    line-height: 20px;
  }

  .ruleForm {
    // background: url("../../../assets/blackBack.jpg") no-repeat;
    // background-size: 100% 100%;
    background: #fff;

    .form_model_item {
      margin-bottom: 0;
    }
  }

  // .read /deep/.ant-list-split .ant-list-item {
  //     border-bottom: 1px solid rgb(148, 148, 148);
  // }

  .read {
    background: #fff;

    .read_horizontal {
      margin: 10px;
      border-top: 2px solid rgb(255, 238, 0);
    }
  }

  .read_border {
    width: 100%;
    height: 100%;
    border: 1px solid #fff;
    border-radius: 5px;
    overflow: auto;
    background: #fff;
  }

  /*定义整体的宽度*/
  .read_border::-webkit-scrollbar {
    width: 3px;
  }

  /*定义滚动条轨道*/
  .read_border::-webkit-scrollbar-track {
    border-radius: 5px;
  }

  /*定义滑块*/
  .read_border::-webkit-scrollbar-thumb {
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.5);
  }

  .read_border::after {
  }
}
</style>
