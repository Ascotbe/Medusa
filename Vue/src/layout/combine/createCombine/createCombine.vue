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
        <a-divider>创建协同项目</a-divider>
        <a-form-model
          :model="formCreate"
          :label-col="labelCol"
          :wrapper-col="wrapperCol"
          :rules="rulesCreate"
          ref="ruleFormCreate"
        >
          <a-form-model-item label="项目名称" prop="markdown_project_name">
            <a-input v-model="formCreate.markdown_project_name" />
          </a-form-model-item>
          <a-form-model-item :wrapper-col="{ span: 4, offset: 10 }">
            <a-button type="primary" @click="handleOnSubmitCreate">
              创建协同任务
            </a-button>
          </a-form-model-item>
        </a-form-model>
        <a-form-model
          :model="formJoin"
          :label-col="labelCol"
          :wrapper-col="wrapperCol"
          :rules="rulesJoin"
          ref="ruleFormJoin"
        >
          <a-divider>加入协同项目</a-divider>
          <a-form-model-item label="项目邀请码" prop="markdown_project_invitation_code">
            <a-input v-model="formJoin.markdown_project_invitation_code" />
          </a-form-model-item>
          <a-form-model-item :wrapper-col="{ span: 4, offset: 10 }">
            <a-button type="primary" @click="handleOnSubmitJoin"> 加入协同项目 </a-button>
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
      formCreate: {
        markdown_project_name: "",
      },
      formJoin: {
        markdown_project_invitation_code: "",
      },
      rulesCreate: {
        markdown_project_name: [
          {
            required: true,
            message: "请输入项目名称",
            whitespace: true,
          },
        ],
      },
      rulesJoin: {
        markdown_project_invitation_code: [
          {
            required: true,
            message: "请输入项目邀请码",
            whitespace: true,
          },
        ],
      },
    };
  },
  mounted() {},
  methods: {
    handleOnSubmitCreate() {
      this.$refs.ruleFormCreate.validate((valid) => {
        if (valid) {
          let form = this.formCreate;
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
    handleOnSubmitJoin() {
      this.$refs.ruleFormJoin.validate((valid) => {
        if (valid) {
          let form = this.formJoin;
          let params = {
            markdown_project_invitation_code: form.markdown_project_invitation_code,
            token: localStorage.getItem("storeToken"),
          };
          this.$api.join_markdown_project(params).then((res) => {
            if (res.code == 200) {
              console.log(res)
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
