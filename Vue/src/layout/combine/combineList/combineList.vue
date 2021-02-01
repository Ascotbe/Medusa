<template>
  <div class="combineList">
    <a-row
      :gutter="[
        { xs: 8, sm: 16, md: 24, xs: 8 },
        { xs: 8, sm: 16, md: 24, lg: 32 },
      ]"
      class="combineList_bg"
    >
      <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
        <a-table
          :columns="columns"
          :data-source="data"
          :pagination="pagination"
          :scroll="{ x: 1600 }"
        >
          <span slot="action" slot-scope="text, record">
            <a
              @click="
                handleGetTableSerch(record.markdown_name, record.markdown_project_name)
              "
              >查询</a
            >
          </span>
        </a-table>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pagination: {
        //分页器配置
        defaultPageSize: 10,
      },
      columns: [
        {
          title: "项目名称",
          dataIndex: "markdown_project_name",
          key: "markdown_project_name",
          width: '20%',
        },
        {
          title: "项目是否所属自己",
          dataIndex: "markdown_project_owner",
          key: "markdown_project_owner",
          width: '10%',
        },
        {
          title: "项目邀请码",
          dataIndex: "markdown_project_invitation_code",
          key: "markdown_project_invitation_code",
          width: '40%',
        },
        {
          title: "创建时间",
          dataIndex: "creation_time",
          key: "creation_time",
          width: '20%',
        },
        {
          title: "操作",
          key: "action",
          fixed: "right",
          width: '10%',
          scopedSlots: {
            customRender: "action",
          },
        },
      ],
      data: [],
      FBdata: [], //data的副本
      file_nameList: [],
      Script_Project_Data: [], //每个data具体的内容
    };
  },
  mounted() {
    this.handleQuery_Markdown_Project();
  },
  methods: {
    handleQuery_Markdown_Project() {
      let params = {
        token: localStorage.getItem("storeToken"),
      };
      this.$api.query_markdown_project(params).then((res) => {
        if (res.code == 200) {
          this.data = [];
          res.message.map((item, i) => {
            let data = {
              key: i,
              markdown_project_name: item.markdown_project_name,
              markdown_name: item.markdown_name,
              creation_time: this.$qj.QjUnixTimes(item.creation_time),
              markdown_project_owner:
                item.markdown_project_owner == 0 ? "不属于" : "属于",
              markdown_project_invitation_code:
                item.markdown_project_owner == 1
                  ? item.markdown_project_invitation_code
                  : "您只是参与者，无法获取项目邀请码",
            };
            this.data.push(data);
          });
        } else {
          this.$message.error(res.message);
        }
      });
    },

    handleGetTableSerch(markdown_name, markdown_project_name) {
      this.$store.commit("markdown_name", markdown_name);
      this.$store.commit("markdown_project_name", markdown_project_name);
      this.$router.push("/layout/combinedList/markdownData");
    },
  },
};
</script>

<style lang="scss" scoped>
.combineList {
  margin: 0;
  padding: 20px;
  padding-top: 30px;
  height: 100%;

  .combineList_bg {
    min-height: 100%;
    background: #fff;
  }
}

.combineList /deep/.ant-table {
  height: 650px;
}
/*定义整体的宽度*/
.combineList /deep/.ant-table-body::-webkit-scrollbar {
  height: 3px;
}

/*定义滚动条轨道*/
.combineList /deep/.ant-table-body::-webkit-scrollbar-track {
  border-radius: 5px;
}

/*定义滑块*/
.combineList /deep/.ant-table-body::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background: rgba(0, 255, 42, 0.5);
}
</style>
