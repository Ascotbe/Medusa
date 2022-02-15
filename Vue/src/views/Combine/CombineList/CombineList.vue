<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :span="24">
      <Card name="项目列表">
        <Tables
          :columns="columns"
          :tableData="data"
          :total="total"
          :rowKey="`markdown_project_invitation_code`"
          @change="handleChange"
        />
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
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
export default {
  components: {
    Card,
    Tables,
  },
  mixins: [OverallMixins],
  data () {
    return {
      columns: [
        {
          title: "项目名称",
          dataIndex: "markdown_project_name",
          key: "markdown_project_name",
          width: '15%',
          // align: 'center',
          ellipsis: true
        },
        {
          title: "项目是否所属自己",
          dataIndex: "markdown_project_owner",
          key: "markdown_project_owner",
          // align: 'center',
          customRender: (text, record, index) => {
            return text == 0 ? "不属于" : "属于"
          }
        },
        {
          title: "项目邀请码",
          dataIndex: "markdown_project_invitation_code",
          key: "markdown_project_invitation_code",
          width: '40%',
          // align: 'center',
          customRender: (text, record, index) => {
            return record.markdown_project_owner == 1 ? text : "您只是参与者，无法获取项目邀请码"
          },
          ellipsis: true
        },
        {
          title: "创建时间",
          dataIndex: "creation_time",
          key: "creation_time",
          // align: 'center',
          customRender: (text, record, index) => {
            return text ? this.moment(text, "X").format('YYYY-MM-DD H:mm:ss') : ""
          },
          ellipsis: true

        },
        {
          title: "操作",
          key: "action",
          // align: 'center',
          // fixed: "right",
          customRender: (text, record, index) => {
            return <a-tag v-on:click={() => {
              this.$store.dispatch("CombineStore/setMarkdown_name", record.markdown_name)
              this.$store.dispatch("CombineStore/setMarkdown_project_name", record.markdown_project_name)
              this.$router.push("MarkdownData")
            }} >查看</a-tag>
          }
        },
      ],
      data: [],
      total: 0,
      current: 1
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
        token: _this.token,
        number_of_pages: _this.current
      };
      this.$api.query_markdown_project(params)
        .then((res) => {
          if (res.code = 200) {
            _this.data = res.message
            const params = {
              token: _this.token,
            };
            return _this.$api.markdown_project_statistical(params)
          }
          else _this.$message.error(res.message)
        })
        .then((res) => {
          if (res.code = 200) _this.total = res.message
          else _this.$message.error(res.message)
        })
    },

    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleCombine()
    }
  }
}
</script>

<style>
</style>