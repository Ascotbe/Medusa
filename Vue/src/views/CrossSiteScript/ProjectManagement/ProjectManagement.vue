<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%;min-height: 540px;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :span="24">
      <!-- <Card :name="'跨站脚本钓鱼项目列表'" :bodyStyle="bodyStyle"> -->
        <Tables
          :columns="columns"
          :tableData="data"
          :rowKey="`file_name`"
          :scrollTable="{x:1000,y:400}"
          :total="total"
          @change="handleChange"
        ></Tables>
      <!-- </Card> -->
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/Tables.vue'

import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
export default {
  mixins: [OverallMixins],
  data () {
    return {
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      columns: [
        {
          title: "项目名",
          dataIndex: "project_name",
          // align: 'center',
        },
        {
          title: "文件名",
          dataIndex: "file_name",
          // align: 'center',
        },
        {
          title: "创建时间",
          dataIndex: "creation_time",
          // align: 'center',
          customRender: (text, record, index) => { return this.moment(text, "X").format('YYYY-MM-DD H:mm:ss') }
        },
        {
          title: "容量",
          dataIndex: "capacity",
          // align: 'center',
          // scopedSlots: {
          //   customRender: "capacity",
          // },
          customRender: (text, record, index) => this.handleRenderCapacity(text, record, index)
        },
        {
          title: "操作",
          key: "action",
          // align: 'center',
          // scopedSlots: {
          //   customRender: "action",
          // },
          customRender: (text, record, index) => {
            return [
              <a v-on:click={() => {
                this.handleSerch(record)
              }}>查询</a>, <a-divider type="vertical" />, <a v-on:click={() => {
                this.handleDetails(record)
              }}>修改</a>, <a-divider type="vertical" />, <a v-on:click={() => {
                this.handleDelete(record)
              }}>删除</a>
            ]
          }
        },
      ],
      data: [],
      current: 1,
      total: 0
    }
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  components: { Card, Tables },
  mounted () {
    const _this = this
    _this.handleQueryScriptProject()
  },
  methods: {
    handleQueryScriptProject () {//查询表格信息
      const _this = this
      const params = {
        token: _this.token,
        number_of_pages: _this.current
      };
      _this.$api.query_script_project(params).then((res) => {
        if (res.code == 200) {
          const promise = res.message.map((item) => {
            const params = {
              token: _this.token,
              project_associated_file_name: item.file_name
            };
            return _this.$api.statistical_cross_site_script_project_data(params)
              .then((res) => {
                if (res.code == 200) {
                  item.capacity = res.message < 100 ? res.message : 100
                }
                else _this.$message.error(`项目名：${item.project_name}获取容量信息失败`)
              })
          })
          const promise2 = _this.$api.statistical_cross_site_script_project({ token: _this.token }).then((res) => {
            if (res.code == 200) _this.total = res.message
            else _this.$message.error(res.message)
          })
          Promise.all(promise, promise2).then(() => {
            _this.data = res.message
          })
        }
        else _this.$message.error(res.message);
      })
    },
    handleChange (pagination) {//分页change
      const _this = this
      _this.current = pagination.current
      _this.handleQueryScriptProject()
    },
    handleRenderCapacity (text, record, index) {//容量的渲染
      return <a-progress
        type="line"
        status="normal"
        strokeColor={{
          '0%': '#108ee9',
          '100%': '#87d068',
        }}
        percent={text}
      // format={(percent) => `${record.capacity} %`}
      >
      </a-progress>
    },
    handleSerch (record) {//查看项目详情
      const _this = this
      _this.$store.dispatch('CrossSiteScriptStore/setProjectAssociatedFileName', record.file_name)
      _this.$router.push("QueryProject")
    },
    handleDetails (record) {//进入项目修改页面
      const _this = this
      // _this.$store.dispatch('CrossSiteScriptStore/setProjectAssociatedFileName', record.file_name)
      _this.$router.push({path:"/layout/ModifyProject",query: {name: record.file_name}})
    },
    handleDelete (record) {//项目删除
      const _this = this
      const params = {
        token: _this.token,
        project_name: record.project_name
      };
      _this.$api.delete_cross_site_script_project(params).then((res) => {
        if (res.code == 200) {
          _this.$message.success("项目删除成功");
          _this.handleQueryScriptProject()
        } else {
          _this.$message.error(res.message);
        }
      });
    }
  }

}
</script>

<style>
</style>