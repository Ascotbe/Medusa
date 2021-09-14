<template>
  <a-row type="flex" :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]">
    <a-col :span="18">
      <Card :name="``" :bodyStyle="bodyStyle">
        <a-form :form="form" :label-col="{ span: 6 }" :wrapper-col="{ span: 18 }">
          <a-col :span="8">
            <a-form-item>
              <a-select
                placeholder="Filter by cvss v3 score"
                :options="options"
                allowClear
                v-decorator="[
              'severity',
            ]"
              ></a-select>
            </a-form-item>
          </a-col>
          <a-col :span="8">
            <a-form-item>
              <a-input
                placeholder="Search in CVEs"
                v-on:keyup.enter.native="handleNistQuery"
                v-decorator="[
              'key',
            ]"
              ></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="8">
            <a-button @click="handleReset" style="margin-right:15px">重置</a-button>
            <a-button type="primary" @click="handleNistQuery">Search</a-button>
          </a-col>
        </a-form>
      </Card>
    </a-col>

    <a-col :span="6">
      <Card :name="``" :bodyStyle="bodyStyle">
        <div class="myicon">
          <myicon :type="`icon-ziyuan1`" style="font-size:100px;" />
          <div class="total">
            <div :span="24">TOTAL:</div>
            <div :span="24" style="font-weight:800">{{total}}</div>
          </div>
        </div>
      </Card>
      <!-- <a-col :span="8" class="myicon"></a-col> -->
      <!-- <a-col :span="16"></a-col> -->
    </a-col>
    <a-col :span="24">
      <Card :name="``" :bodyStyle="bodyStyle">
        <Tables
          :columns="columns"
          :tableData="data"
          :total="total"
          :rowKey="`vulnerability_number`"
          :showExpandedRowKeys="true"
          @change="handleChange"
        ></Tables>
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/Tables.vue'
import { mapGetters } from "vuex";
import { Icon } from "ant-design-vue";
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1734998_iv1ouwpdggf.js",
});
export default {
  components: {
    Card,
    Tables,
    myicon: MyIcon,
  },
  data () {
    return {
      form: this.$form.createForm(this, { name: 'form' }),
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      columns: [
        {
          title: "漏洞编号",
          dataIndex: "vulnerability_number",
          key: "vulnerability_number",
          customRender: (text, record, index) => this.handleRenderVulnerabilityNumber(text, record, index)
        },
        {
          title: "CVSS v3 分数",
          dataIndex: "v3_base_score",
          key: "v3_base_score",
        },
        {
          title: "CVSS v3 分级",
          dataIndex: "v3_base_severity",
          key: "v3_base_severity",
          customRender: (text, record, index) => this.handleRenderTag(text, record, index)
        },
        {
          title: "CVSS v2 分数",
          dataIndex: "v2_base_score",
          key: "v2_base_score",
        },
        {
          title: "CVSS v2 分级",
          dataIndex: "v2_base_severity",
          key: "v2_base_severity",
          customRender: (text, record, index) => this.handleRenderTag(text, record, index)

        },
        {
          title: "最后更新时间",
          dataIndex: "last_up_date",
          key: "last_up_date",
        },
        {
          title: "开发商名称",
          dataIndex: "vendors",
          key: "vendors",
          width: 300,
          customRender: (text, record, index) => this.handleRenderVendorsAndProducts(text, record, index)

        },
        {
          title: "产品名称",
          dataIndex: "products",
          key: "products",
          width: 300,
          customRender: (text, record, index) => this.handleRenderVendorsAndProducts(text, record, index)
        },
      ],
      data: [],
      total: 0,
      current: 1,
      options: [//NONE、LOW、MEDIUM、HIGH、CRITICAL
        {
          value: "NONE",
          label: "NONE"
        },
        {
          value: "LOW",
          label: "LOW"
        },
        {
          value: "MEDIUM",
          label: "MEDIUM"
        },
        {
          value: "HIGH",
          label: "HIGH"
        },
        {
          value: "CRITICAL",
          label: "CRITICAL"
        },
      ]
    }
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  created () {
    const _this = this
    _this.handleNistQuery()
  },
  methods: {
    handleReset () {
      const _this = this
      _this.form.resetFields()
    },
    handleNistStatistics (severity, key) {
      const _this = this
      if (severity || key) {
        const params = {
          token: _this.token,
          number_of_pages: _this.current,
          severity: severity ? severity : "",
          key: key ? key : "",
        };
        _this.$api.nist_search_statistics(params).then((res) => {
          if (res.code == 200) {
            _this.total = res.message
          } else {
            _this.$message.error(res.message);
          }
        })
      }
      else {
        const params = {
          token: _this.token,
          number_of_pages: _this.current,
        };
        _this.$api.nist_statistics(params).then((res) => {
          if (res.code == 200) {
            _this.total = res.message
          } else {
            _this.$message.error(res.message);
          }
        })
      }
    },
    handleNistQuery () {
      const _this = this
      const form = _this.form.getFieldsValue()
      if (form.severity && !form.key) {
        _this.$message.warn('如药进行查询，请填写2个搜索哦条件')
        return
      }
      if (!form.severity && form.key) {
        _this.$message.warn('如药进行查询，请填写2个搜索哦条件')
        return
      }
      if (form.severity || form.key) {
        const params = {
          token: _this.token,
          number_of_pages: _this.current,
          severity: form.severity ? form.severity : "",
          key: form.key ? form.key : "",
        };
        _this.handleNistStatistics(form.severity, form.key)
        _this.$api.nist_search(params).then((res) => {
          if (res.code == 200) {
            _this.data = res.message
          } else {
            _this.$message.error(res.message);
          }
        })
      }
      else {
        const params = {
          token: _this.token,
          number_of_pages: _this.current,
        };
        _this.handleNistStatistics()
        _this.$api.nist_data_bulk_query(params).then((res) => {
          if (res.code == 200) {
            _this.data = res.message
          } else {
            _this.$message.error(res.message);
          }
        })
      }
    },
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleNistQuery()
    },
    handleRenderTag (text, record, index) {
      //NONE、LOW、MEDIUM、HIGH、CRITICAL
      let color = ''
      switch (text) {
        case 'NONE':
          color = "#00FF99"
          break;
        case 'LOW':
          color = "#00FF66"
          break;
        case 'MEDIUM':
          color = "#FF9900"
          break;
        case 'HIGH':
          color = "#FF6633"
          break;
        case 'CRITICAL':
          color = "#FF6666"
          break;
        // default:
        //   color = "#00FFCC"
        //   break;
      }
      return text ? <a-tag color={color}> {text} </a-tag > : ''
    },
    handleRenderVendorsAndProducts (text, record, index) {
      let arr = text ? eval('(' + text + ')') : []
      let dom = ''
      if (arr.length > 0) {
        dom = arr.map((item) => {
          return <a-tag color="green" v-on:click={() => {
            this.handleClickVendorsAndProducts(item)//暂时没用
          }}>{item}<br /></a-tag>
        })
      }
      return dom
    },
    handleClickVendorsAndProducts (item) {//暂时没用
      console.log(item)
    },
    handleRenderVulnerabilityNumber (text, record, index) {
      return <a-tag color="cyan" v-on:click={() => {
        this.handleClickVulnerabilityNumber(text)
      }}>{text}<br /></a-tag>
    },
    handleClickVulnerabilityNumber (item) {
      const _this = this
      _this.$store.commit('MonitorStore/setVulnerabilityCode', item)
      _this.$router.push('VulnerabilitiesMonitorDetailed')
    },
  }
}
</script>

<style lang="scss" scoped>
.myicon {
  text-align: left;
  .total {
    display: inline-block;
    padding-left: 15px;
  }
  // border-top: 3px solid #51c51a;
  // background: #51c51a;
}
</style>