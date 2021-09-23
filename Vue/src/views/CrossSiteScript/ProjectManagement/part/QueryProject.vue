<template>
  <a-row
    type="flex"
    justify="center"
    align="top"
    style="height:100%;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :span="24">
      <Card :name="'项目详情'" :bodyStyle="bodyStyle">
        <Tables
          :columns="columns"
          :tableData="data"
          :scrollTable="{x:1000,y:700}"
          :total="total"
          :rowKey="(record,index)=>index"
          @change="handleChange"
          ref="tables"
          :ExpandedRowRenderCallback="handleCallback"
          :ExpandIconCallback="handleExpandIcon"
        ></Tables>
      </Card>
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
  computed: {
    ...mapGetters({
      token: "UserStore/token",
      projectAssociatedFileName: "CrossSiteScriptStore/projectAssociatedFileName"
    })
  },
  components: { Card, Tables },
  data () {
    return {
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      columns: [
        {
          title: "创建时间",
          dataIndex: "creation_time",
          customRender: (text, record, index) => { return this.moment(text, "X").format('YYYY-MM-DD H:mm:ss') }
        },
        {
          title: "数据包内容",
          dataIndex: "data_pack",
          ellipsis: true,
          customRender: (text, record, index) => { return this.QJBase64Decode(text) }
        },
        {
          title: "真实地址",
          dataIndex: "ip",
        }
      ],
      data: [],
      total: 0,
      current: 1
    }
  },
  mounted () {
    const _this = this
    if (_this.projectAssociatedFileName == '' || _this.projectAssociatedFileName == undefined || _this.projectAssociatedFileName == null) {
      _this.$message.warn('请从项目管理进入')
      _this.$router.push('ProjectManagement')
      return
    }
    _this.handleQueryScriptProjectData()
  },
  methods: {
    handleQueryScriptProjectData () {
      const _this = this
      const currentParams = {
        project_associated_file_name: _this.projectAssociatedFileName,
        token: _this.token,
      };
      const dataParams = {
        project_associated_file_name: _this.projectAssociatedFileName,
        token: _this.token,
        number_of_pages: _this.current
      };
      _this.$api.statistical_cross_site_script_project_data(currentParams).then((res) => {
        if (res.code == 200) _this.total = res.message
        else _this.$message.error(res.message)
      })
      _this.$api.query_script_project_data(dataParams).then((res) => {
        if (res.code == 200) {
          res.message.map((item) => {
            item.headerData = []
            item.requestData = []
            item.Cookie = []
            item.Other = [
              {
                key: "访问地址",
                value: item.full_url,
              },
              {
                key: "IP地址",
                value: item.ip,
              },
              {
                key: "协议",
                value: item.request_method,
              },
            ];
            const requestData = eval('(' + this.QJBase64Decode(item.data_pack) + ')')
            for (let key in requestData) {
              item.requestData.push({ "key": key, "value": requestData[key] })
            }
            const headerData = eval('(' + this.QJBase64Decode(item.headers) + ')')
            for (let key in headerData) {
              if (key == 'Connection') item.Cookie.push({ "key": key, "value": headerData[key] })
              if (key == 'User-Agent') item.Other.push({ "key": '客户端', "value": headerData[key] })
              item.headerData.push({ "key": key, "value": headerData[key] })
            }
          })
          this.data = res.message
        }
        else _this.$message.error(res.message)
      })

    },
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleQueryScriptProjectData()
    },
    handleExpandIcon (props) {
      if (props.expanded) {
        return <a style="color: 'black',margin-right:0px" onClick={e => {
          props.onExpand(props.record, e);
        }}><a-icon type="caret-down" /></a>
      } else {
        return <a style="color: 'black' ,margin-right:0px" onClick={e => {
          props.onExpand(props.record, e);
        }}><a-icon type="caret-right" /></a>
      }
      x
    },
    handleCallback (record) {
      const tabs = [record.request_method, 'Cookie', 'HTTP请求信息', '其他信息']
      const columns = [
        {
          title: "键",
          dataIndex: "key",
          width: 300
        },
        {
          title: "值",
          dataIndex: "value",
        },
      ]
      return (<a-tabs >
        {
          tabs.map(item => {
            return (<a-tab-pane key={item} tab={item}>
              {
                <Tables columns={columns} tableData={item == record.request_method ? record.requestData : item == 'Cookie' ? record.Cookie : item == 'HTTP请求信息' ? record.headerData : record.Other} rowKey={`key`}></Tables>
              }
            </a-tab-pane>)
          })
        }
      </a-tabs>)
    }
  },
}
</script>

<style>
</style>