<template>
  <a-row
    type="flex"
    justify="center"
    align="top"
    style="height:100%"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :span="24">
      <Card name="项目列表">
        <Tables :columns="columns" :tableData="data" :rowKey="`markdown_project_invitation_code`" />
      </Card>
    </a-col>

    <!-- <a-table
       
        :data-source="data"
        :pagination="pagination"
        :scroll="{ x: 1600 }"
      >
        <span slot="action" slot-scope="text, record">
          <a
            @click="
                handleGetTableSerch(record.markdown_name, record.markdown_project_name)
              "
          >查询</a>
        </span>
    </a-table>-->
  </a-row>
</template>

<script>
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/Tables.vue'
import { mapGetters } from 'vuex'
export default {
  components: {
    Card,
    Tables,
  },
  data () {
    return {
      columns: [
        {
          title: "项目名称",
          dataIndex: "markdown_project_name",
          key: "markdown_project_name",
          width: '15%',
          // ellipsis: true
        },
        {
          title: "项目是否所属自己",
          dataIndex: "markdown_project_owner",
          key: "markdown_project_owner",
        },
        {
          title: "项目邀请码",
          dataIndex: "markdown_project_invitation_code",
          key: "markdown_project_invitation_code",
          width: '40%',
          // ellipsis: true
        },
        {
          title: "创建时间",
          dataIndex: "creation_time",
          key: "creation_time",
          // ellipsis: true
        },
        {
          title: "操作",
          key: "action",
          fixed: "right",
          customRender: (text, record, index) => {
            return <a-tag  >查看</a-tag>
          }
        },
      ],
      data: []
    }
  },
  mounted () {
    const _this = this
    _this.handleCombine();
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  methods: {
    handleCombine () {
      const _this = this
      const params = {
        token: _this.token
      };
      this.$api.query_markdown_project(params).then((res) => {
        _this.data = res.message
      })
    }
  }
}
</script>

<style>
</style>