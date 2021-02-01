<template>
  <div class="createProject">
    <a-row
      :gutter="[
        { xs: 8, sm: 16, md: 24, xs: 8 },
        { xs: 8, sm: 16, md: 24, lg: 32 },
      ]"
      class="createProject_bg"
    >
      <a-col
        :xs="{ span: 24 }"
        :lg="{ span: 12 }"
        :xl="{ span: 12 }"
        :xxl="{ span: 12 }"
        class="createProject_bg"
      >
        <a-col :xs="{ span: 24 }" class="read">
          <!-- <a-list item-layout="horizontal" :data-source="ScriptTemplate" :column="[24]">
                    <a-list-item slot="renderItem" slot-scope="item">
                        <a-list-item-meta>
                            <span slot="title" class="read_font" @click="handleSet(item.template_data)">{{ item.template_name }}</span>
                            <myicon type="icon-js" slot="avatar" class="icon" />
                        </a-list-item-meta>
                    </a-list-item>
                </a-list>-->
          <a-form-model
            :model="showDataForm"
            :label-col="labelCol"
            :wrapper-col="wrapperCol"
            ref="showData"
          >
            <a-form-model-item label="选择的模板名" prop="title" :labelAlign="'left'">
              <a-input v-model="showDataForm.title" :disabled="true" />
            </a-form-model-item>
            <a-form-model-item label="模板内容" prop="data" :labelAlign="'left'">
              <codemirror
                v-model="showDataForm.data"
                :options="showDataFormOptions"
                class="code"
              ></codemirror>
            </a-form-model-item>
          </a-form-model>
        </a-col>
      </a-col>
      <a-col
        :xs="{ span: 24 }"
        :lg="{ span: 12 }"
        :xl="{ span: 12 }"
        :xxl="{ span: 12 }"
        class="createProject_bg"
      >
        <a-col :xs="{ span: 24 }" class="ruleForm">
          <a-col :xs="{ span: 24 }"> 填写项目基本信息 </a-col>
          <a-form-model
            :model="form"
            :label-col="labelCol"
            :wrapper-col="wrapperCol"
            :rules="rules"
            ref="ruleForm"
          >
            <a-form-model-item label="项目名" prop="projectName" :labelAlign="'left'">
              <a-input v-model="form.projectName" />
            </a-form-model-item>
            <a-form-model-item label="默认模板选择" prop="default" :labelAlign="'left'">
              <a-select
                :options="DefaultScriptTemplate"
                placeholder="选择模板"
                @dropdownVisibleChange="handleDropdownVisibleChange"
                @change="handleChange"
              >
              </a-select>
            </a-form-model-item>
            <a-form-model-item label="脚本数据" prop="script_data" :labelAlign="'left'">
              <codemirror
                ref="textarea"
                v-model="form.script_data"
                :options="cmOptions"
                class="code"
              ></codemirror>
            </a-form-model-item>

            <a-form-model-item :wrapper-col="{ span: 18, offset: 6 }">
              <a-button
                type="primary"
                @click="handleSetDefault"
                style="margin-right: 10px"
              >
                插入模板
              </a-button>
              <a-button type="primary" @click="handleOnSubmit"> 创建项目 </a-button>
            </a-form-model-item>
          </a-form-model>
        </a-col>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { Icon } from "ant-design-vue";
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1734998_apjce2fwnsu.js",
});
export default {
  components: {
    myicon: MyIcon,
  },
  data() {
    return {
      showDataFormOptions: {
        mode: "javascript",
        theme: "duotone-light",
        lineNumbers: true,
        line: true,
        lineWrapping: true, //自动换行
        readOnly: "nocursor", //只读
        matchBrackets: true,
      },
      cmOptions: {
        mode: "javascript",
        theme: "duotone-light",
        lineNumbers: true,
        lineWrapping: true, //自动换行
        line: true,
        //readOnly: "nocursor", //只读
        matchBrackets: true,
      },
      labelCol: {
        span: 20,
        offset: 2,
      },
      wrapperCol: {
        span: 20,
        offset: 2,
      },
      form: {
        projectName: "",
        script_data: "",
      },
      rules: {
        projectName: [
          {
            required: true,
            message: "项目名",
            whitespace: true,
          },
        ],
        script_data: [
          {
            required: true,
            message: "脚本数据",
            whitespace: true,
          },
        ],
      },
      showDataForm: {
        title: "您还未选择模板",
        data: "",
      },
      DefaultScriptTemplate: [],
      val: "",
      defaultVal: "",
    };
  },
  mounted() {},
  methods: {
    handleOnSubmit() {
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          let form = this.form;
          let params = {
            project_name: form.projectName,
            javascript_data: this.$qj.QJBase64Encode(form.script_data),
            token: localStorage.getItem("storeToken"),
          };
          this.$api.create_script_project(params).then((res) => {
            if (res.code == 200) {
              this.$message.success("项目创建成功，正在跳转...");
              this.$store.commit("project_associated_file_name", res.message);
              this.$router.push("/layout/projectManagement/projectDetails");
            } else {
              this.$message.error(res.message);
            }
          });
        } else {
          this.$message.error("请填写内容");
          return false;
        }
      });
    },
    handleChange(val) {
      this.DefaultScriptTemplate.map((item) => {
        if (item.value == val) {
          this.defaultVal = item.key;
          this.showDataForm.title = item.value;
          this.showDataForm.data = item.key;
        }
      });
    },
    handleDropdownVisibleChange(open) {
      let params = {
        token: localStorage.getItem("storeToken"),
      };
      this.$api.read_default_script_template(params).then((res) => {
        if (res.code == 200) {
          this.DefaultScriptTemplate = [];
          let options = {};
          let list = [];
          res.message.map((item) => {
            options = {
              value: item.file_name,
              label: item.file_name,
              key: this.$qj.QJBase64Decode(item.file_data),
            };
            list.push(options);
          });
          this.$api.read_script_template(params).then((res) => {
            if (res.code == 200) {
              res.message.map((item) => {
                options = {
                  value: item.template_name,
                  label: item.template_name,
                  key: this.$qj.QJBase64Decode(item.template_data),
                };
                list.push(options);
              });
              this.DefaultScriptTemplate = list;
            } else {
              this.$message.error(res.message);
            }
          });
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleSetDefault() {
      let val = this.defaultVal;
      let tc = this.$refs.textarea.codemirror.getCursor();
      let tc2 = {
        line: tc.line,
        ch: tc.ch,
      };
      this.$refs.textarea.codemirror.replaceRange(val, tc2);
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
  min-width: 300px;
  height: 100%;

  .createProject_bg {
    height: 850px;
    min-height: 100%;
  }
}

.read,
.ruleForm {
  background: #fff;
  height: 100%;
  border: 1px solid #ccc;
  font-size: 18px;

  .btn {
    display: -webkit-flex;
    /* Safari */
    display: flex;
    justify-content: space-around;
  }
}

.ruleForm /deep/ .ant-form-item-control {
  line-height: 20px;
}

.read /deep/ .ant-form-item-control {
  line-height: 20px;
}

.read /deep/.CodeMirror {
  height: 510px;
}
</style>
