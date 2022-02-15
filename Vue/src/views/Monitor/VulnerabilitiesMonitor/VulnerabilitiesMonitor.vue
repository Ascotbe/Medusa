<template>
  <a-row
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
  <a-col :span='24'>
    <div style="text-align: left; font-size: 18px;">
      Vulnerabilities (CVE)
    </div>
   </a-col>
    <a-col :span='24'>
      <a-col :xs="24" :lg="18" style="background: #fff;">
        <a-form  class="search-form" :form="form">
          <a-col :xs="24" :lg="8">
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
          <a-col :xs="24" :lg="8">
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
          <a-col :xs="24" :lg="8">
            <a-form-item>
              <div style="text-align:left;">
                <a-button @click="handleReset" style="margin-right:4px">重置</a-button>
                <a-button type="primary" @click="handleNistQuery">查询</a-button>
              </div>
            </a-form-item>
          </a-col>
        </a-form>
      </a-col>
      <a-col :xs='0' :lg='1'></a-col>
      <a-col :xs="24" :lg="5" style="display: flex;background: #fff;">
        <div style="display: flex;">
          <div style="height: 56px; font-size: 50px; line-height: 56px; width: 80px; text-align: center;">
            <a-icon type="safety-certificate" />
          </div>
          <div class="total" style="text-align: left;">
            <div style="font-size: 14px; line-height: 2;">TOTAL:</div>
            <div style="font-size: 18px; line-height: 1;font-weight: 800;">{{total}}</div>
          </div>
        </div>
      </a-col>
    </a-col>

    <a-col :span="24" >
      <Card name="">
        <Tables
          :loading='loading'
          :columns="columns"
          :tableData="data"
          :total="total"
          :rowKey="`vulnerability_number`"
          :showExpandedRowKeys="true"
          @change="handleChange"
          :ExpandedRowRenderCallback="handleCallback"
        ></Tables>
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/CTables.vue'
import { mapGetters } from "vuex";
import { Icon } from "ant-design-vue";
const faceConfig = require("../../../../faceConfig");
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: faceConfig.scriptUrl,
});

export default {
  components: {
    Card,
    Tables,
    MyIcon,
  },
  data () {
    return {
      loading: true,
      form: this.$form.createForm(this, { name: 'form' }),
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      columns: [
        {
          title: "CVE",
          dataIndex: "vulnerability_number",
          key: "vulnerability_number",
          customRender: (text, record, index) => this.handleRenderVulnerabilityNumber(text, record, index)
        },
        {
          title: "vendors",
          dataIndex: "vendors",
          key: "vendors",
          width: 300,
          customRender: (text, record, index) => this.handleRenderVendorsAndProducts(text, record, index)

        },
        {
          title: "Products",
          dataIndex: "products",
          key: "products",
          width: 300,
          customRender: (text, record, index) => this.handleRenderVendorsAndProducts(text, record, index)
        },
        {
          title: "Updated",
          dataIndex: "last_up_date",
          key: "last_up_date",
           width: 120,
        },
        // {
        //   title: "CVSS v3 分数",
        //   dataIndex: "v3_base_score",
        //   key: "v3_base_score",
        // },
        {
          title: "CVSS v2",
          dataIndex: "v2_base_severity",
          key: "v2_base_severity",
          width: 120,
          customRender: (text, record, index) => this.handleRenderTag(text, record, index,'v2')

        },
        {
          title: "CVSS v3",
          dataIndex: "v3_base_severity",
          key: "v3_base_severity",
          width: 120,
          customRender: (text, record, index) => this.handleRenderTag(text, record, index)
        },
        // {
        //   title: "CVSS v2 分数",
        //   dataIndex: "v2_base_score",
        //   key: "v2_base_score",
        // },
       
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
      this.loading = true
      const _this = this
      const form = _this.form.getFieldsValue()
      if (form.severity && !form.key) {
        _this.$message.warn('如要进行查询，请填写2个搜索条件')
        return
      }
      if (!form.severity && form.key) {
        _this.$message.warn('如要进行查询，请填写2个搜索条件')
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
        }).finally(() => {
          this.loading = false
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
        }).finally(() => {
          this.loading = false
        })
      }
    },
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleNistQuery()
    },
    handleRenderTag (text, record, index,type) {
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
        default:
          color = "#909399"
          break;
      }
      return text ? <a-tag color={color}>{type === 'v2'?record.v2_base_score:record.v3_base_score}{text} </a-tag > : <a-tag color={color}>N/A</a-tag>
    },
    handleRenderVendorsAndProducts (text, record, index) {
      let arr = text ? eval('(' + text + ')') : []
      let dom = ''
      if (arr.length > 0) {
        arr = Array.from(new Set(arr))
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
    handleCallback (record) {//回写展开项内容
      return record.vulnerability_description
    }
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
.search-form .ant-form-item {
  margin-bottom: 0;
}
</style>