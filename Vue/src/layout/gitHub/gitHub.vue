<template>
  <a-row
    :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 8, sm: 16, md: 24, lg: 32 },
    ]"
    class="github"
  >
    <a-col class="github_bg" :xs="{ span: 24 }">
      <a-col :xs="{ span: 12 }" :lg="{ offset: 14, span: 4 }">
        <a-select
          style="width: 100%"
          :options="options"
          placeholder="选择搜索字段"
          @change="handleChange"
        >
        </a-select>
      </a-col>
      <a-col :xs="{ span: 12 }" :lg="{ span: 6 }">
        <a-input-search placeholder="搜索内容" enter-button @search="handleOnSearch" />
      </a-col>
      <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
        <a-table :columns="columns" :data-source="data" :scroll="{ x: 1600 }"> </a-table>
      </a-col>
    </a-col>
  </a-row>
</template>

<script>
export default {
  name: "gitHub",
  data() {
    return {
      columns: [
        {
          title: "GitHub编号",
          dataIndex: "github_id",
          key: "github_id",
          fixed: "left",
        },
        {
          title: "项目名称",
          dataIndex: "name",
          key: "name",
        },
        {
          title: "项目地址",
          dataIndex: "html_url",
          key: "html_url",
        },
        {
          title: "项目创建时间",
          dataIndex: "created_at",
          key: "created_at",
        },
        {
          title: "项目更新时间",
          dataIndex: "updated_at",
          key: "updated_at",
        },
        {
          title: "最新上传时间",
          dataIndex: "pushed_at",
          key: "pushed_at",
        },
        {
          title: "Fork",
          dataIndex: "forks_count",
          key: "forks_count",
        },
        {
          title: "Star",
          dataIndex: "watchers_count",
          key: "watchers_count",
        },
      ],
      data: [],
      FBdata: [], //data的副本
      options: [],
      optionValue: "",
    };
  },
  mounted() {
    this.columns.map((item) => {
      let itemlist = {
        value: item.dataIndex,
        label: item.title,
      };
      this.options.push(itemlist);
    });
    this.handlegithub_moitor();
  },
  methods: {
    handlegithub_moitor() {
      let params = {
        token: localStorage.getItem("storeToken"),
      };

      this.$api.github_monitor(params).then((res) => {
        if (res.code == 200) {
          res.message.map((item) => {
            let data = {
              key: item.github_id,
              github_id: item.github_id,
              name: item.name,
              html_url: item.html_url,
              created_at: item.created_at,
              updated_at: item.updated_at,
              pushed_at: item.pushed_at,
              forks_count: item.forks_count,
              watchers_count: item.watchers_count,
            };
            this.FBdata.push(data);
          });
          this.data = this.FBdata;
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleOnSearch(val) {
      let item = this.optionValue;
      if (item != "") {
        // for (let i = 0; i < this.FBdata.length; i++) {
        //     console.log(this.FBdata[i][item])
        // }
        this.data = [];
        this.FBdata.map((i) => {
          if (i[item].indexOf(val) != -1) {
            let data = {
              key: i.github_id,
              github_id: i.github_id,
              name: i.name,
              html_url: i.html_url,
              created_at: i.created_at,
              updated_at: i.updated_at,
              pushed_at: i.pushed_at,
              forks_count: i.forks_count,
              watchers_count: i.watchers_count,
            };
            this.data.push(data);
          }
        });
      } else {
        this.$message.error("请先选择要搜索的字段");
      }
    },
    handleChange(val) {
      this.optionValue = val;
    },
  },
};
</script>

<style lang="scss" scoped>
.github {
  margin: 0;
  padding: 20px;
  padding-top: 30px;
  height: 100%;
  min-height: auto;
  .github_bg {
    background: #fff;
    min-height: 100%;
  }
  /*定义整体的宽度*/
  .github_bg /deep/.ant-table-body::-webkit-scrollbar {
    height: 3px;
  }

  /*定义滚动条轨道*/
  .github_bg /deep/.ant-table-body::-webkit-scrollbar-track {
    border-radius: 5px;
  }

  /*定义滑块*/
  .github_bg /deep/.ant-table-body::-webkit-scrollbar-thumb {
    border-radius: 5px;
    background: rgba(0, 255, 42, 0.5);
  }
}
</style>
