<template>
  <div class="dataComparison">
    <a-row
      :gutter="[
        { xs: 8, sm: 16, md: 24, xs: 8 },
        { xs: 8, sm: 16, md: 24, lg: 32 },
      ]"
      class="dataComparison_bg"
    >
      <a-page-header
        @back="handleCancel"
        style="border: 1px solid rgb(235, 237, 240)"
        :title="title"
      >
        <template slot="extra">
          <a-button @click="handleSave" type="primary"> 确认保存 </a-button>
          <a-button @click="handleCancel"> 取消退回 </a-button>
        </template>
      </a-page-header>
      <a-col :xs="{ span: 24 }" v-html="markdownData"> </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "新旧数据对比",
      markdownData: "",
    };
  },
  mounted() {
    this.handleGetMarkdownData();
  },
  methods: {
    handleGetMarkdownData() {
      if (
        this.$store.state.markdown_data_comparison != "" &&
        this.$store.state.markdown_data != ""
      ) {
        this.markdownData = this.$store.state.markdown_data_comparison;
      } else {
        this.$message.warning("请从协同项目详情页面进入，正在为您跳转到项目列表页..");
        this.$router.push("/layout/combinedList/markdownData");
      }
    },
    handleSave() {
      let params = {
        token: localStorage.getItem("storeToken"),
        markdown_name: this.$store.state.markdown_name,
        markdown_data: this.$store.state.markdown_data,
      };
      this.$api.save_markdown_data(params).then((res) => {
        if (res.code == 200) {
          this.$message.success("保存成功..");
          this.$store.commit("markdown_data", "");
          this.$store.commit("markdown_data_comparison", "");
          this.$router.go(-1);
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleCancel() {
      this.$store.commit("markdown_data", "");
      this.$store.commit("markdown_data_comparison", "");
      this.$router.go(-1);
    },
  },
};
</script>

<style lang="scss" scoped>
.dataComparison {
  margin: 0;
  padding: 20px;
  padding-top: 30px;
  height: 100%;

  .dataComparison_bg {
    min-height: 100%;
    background: #fff;
  }
}
</style>
