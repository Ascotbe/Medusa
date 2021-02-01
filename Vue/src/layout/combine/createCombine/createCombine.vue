<template>
  <a-row
    :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 8, sm: 16, md: 24, lg: 32 },
    ]"
    class="createCombine"
  >
    <a-col :xs="{ span: 24 }" class="createCombine_bg">
      <a-col
        :xs="{ span: 20, offset: 2 }"
        :lg="{ span: 14, offset: 5 }"
        :xl="{ span: 12, offset: 6 }"
        :xxl="{ span: 10, offset: 7 }"
      >
        <a-form-model
          :model="form"
          :label-col="labelCol"
          :wrapper-col="wrapperCol"
          :rules="rules"
          ref="ruleForm"
        >
          <a-form-model-item label="项目名称" prop="markdown_project_name">
            <a-input v-model="form.markdown_project_name" />
          </a-form-model-item>
          <a-form-model-item :wrapper-col="{ span: 6, offset: 9 }">
            <a-button type="primary" @click="handleOnSubmit"> 创建协同任务 </a-button>
          </a-form-model-item>
        </a-form-model>
      </a-col>
    </a-col>
  </a-row>
</template>

<script>
import { Layout } from "ant-design-vue";
export default {
  data() {
    return {
      labelCol: {
        span: 6,
      },
      wrapperCol: {
        span: 14,
      },
      form: {
        markdown_project_name: "",
      },
      rules: {
        markdown_project_name: [
          {
            required: true,
            message: "请输入项目名称",
            whitespace: true,
          },
        ],
      },
    };
  },
  mounted() {},
  methods: {
    handleOnSubmit() {
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          let form = this.form;
          let params = {
            markdown_project_name: form.markdown_project_name,
            token: localStorage.getItem("storeToken"),
          };
          this.$api.create_markdown_project(params).then((res) => {
            if (res.code == 200) {
              this.$message.success(res.message);
              this.$router.push("./combinedList");
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
  },
};
</script>

<style lang="scss" scoped>
.createCombine {
  margin: 0;
  padding: 20px;
  padding-top: 30px;
  height: 100%;
  min-height: auto;

  .createCombine_bg {
    background: #fff;
    min-height: 100%;
  }
}
</style>
