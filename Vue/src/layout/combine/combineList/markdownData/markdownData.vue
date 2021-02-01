<template>
  <div class="markdown">
    <a-row
      :gutter="[
        { xs: 0, sm: 0, md: 0, xs: 0 },
        { xs: 0, sm: 0, md: 8, lg: 8 },
      ]"
      class="markdown_bg"
    >
      <a-page-header
        @back="() => $router.go(-1)"
        style="border: 1px solid rgb(235, 237, 240)"
        :title="title"
      >
        <a-col :xs="{ span: 24 }" class="header_text">
          <a-col :xs="{ span: 24 }" :sm="{ span: 12 }" :md="{ span: 8 }">
            创建时间:{{ MarkdownData.creation_time }}
          </a-col>
          <a-col :xs="{ span: 24 }" :sm="{ span: 12 }" :md="{ span: 8 }">
            最后修改时间:{{ MarkdownData.update_time }}
          </a-col>
        </a-col>
      </a-page-header>
      <Markdown
        v-model="MarkdownData.markdown_data"
        ref="Markdown"
        @on-save="handleOnSave"
        @on-upload-image="handleOnUpladImage"
        :autoSave="false"
        :height="750"
        :theme="theme"
        :toolbars="toolbars"
      />
    </a-row>
  </div>
</template>

<script>
import Markdown from "../../../../components/markdown/vue-meditor";
export default {
  components: {
    Markdown,
  },
  data() {
    return {
      MarkdownData: {
        markdown_name: "",
        markdown_data: "",
        creation_time: "",
        update_time: "",
      },
      value: "", //用户输入值
      title: "项目:",
      toolbars: {
        save: true,
        uploadImage: true,
      },
      theme: "oneDark",
    };
  },
  mounted() {
    this.handleQuery_Markdown_Data();
  },
  methods: {
    handleQuery_Markdown_Data() {
      if (
        this.$store.state.markdown_name != "" &&
        this.$store.state.markdown_project_name != ""
      ) {
        this.title = "项目:" + this.$store.state.markdown_project_name;
        let params = {
          token: localStorage.getItem("storeToken"),
          markdown_name: this.$store.state.markdown_name,
        };
        this.$api.query_markdown_data(params).then((res) => {
          if (res.code == 200) {
            if (res.message != "") {
              let data = {
                markdown_name: res.message[0].markdown_name,

                markdown_data: this.$qj.QJBase64Decode(res.message[0].markdown_data),
                creation_time: this.$qj.QjUnixTimes(res.message[0].creation_time),
                update_time: this.$qj.QjUnixTimes(res.message[0].update_time),
              };
              this.MarkdownData = data;
            } else {
              this.$message.success("您是个新项目还没有数据哦！");
            }
          } else {
            this.$message.error(res.message);
          }
        });
      } else {
        this.$message.warning("您应该从协同作战的项目列表进入该页，正为您跳转...");
        this.$router.push("/layout/combinedList");
      }
    },
    handleOnSave(value) {
      let params = {
        token: localStorage.getItem("storeToken"),
        markdown_name: this.$store.state.markdown_name,
        new_markdown_data: value.value,
      };
      this.$api.markdown_data_comparison(params).then((res) => {
        if (res.code == 200) {
          this.$store.commit("markdown_data", value.value);
          this.$store.commit("markdown_data_comparison", res.message);
          this.$router.push("/layout/combinedList/markdownData/dataComparison");
        } else {
          this.$message.success(res.message);
        }
      });
    },
    handleOnUpladImage(file) {
      if (this.handleBeforeUpload(file) == true) {
        let params = new FormData();
        params.append("file", file);
        this.$api.markdown_image_upload(params).then((res) => {
          console.log(res);
          const config = require("../../../../../faceConfig");
          const imgURL = config.imgPath;
          let resUrl = imgURL + res.message;
          // this.MarkdownData.markdown_data = this.MarkdownData.markdown_data + resUrl;
          this.$refs.Markdown.insertContent(`![image](${resUrl})`);
        });
      }
    },
    handleBeforeUpload(file) {
      const isLt10K = file.size / 1024 > 1;
      if (!isLt10K) {
        this.$message.error("图片得大于1KB!");
        return false;
        //  file.onError()
      } else {
        return true;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.markdown {
  margin: 0;
  // padding: 20px;
  // padding-top: 30px;
  height: 100%;
  padding-left: 5px;
  padding-right: 5px;
  .markdown_bg {
    min-height: 100%;
    // background: #fff;
    .header_text {
      text-align: left;
      font-size: 16px;
    }
  }
}
</style>
