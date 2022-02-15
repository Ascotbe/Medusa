<template>
  <a-row
    type="flex"
    style="height:100%"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :xs="24" :lg="16">
      <a-col :xs="24">
        <Card :name="vulnerabilityCode" :bodyStyle="bodyStyle">
          <div style="text-align:left">
            <span style="font-size:24px; color:#51c51a">{{description.head}}</span>
            {{description.body}}
          </div>
          <a-tabs @activeKey="activeKey" style="text-align:left;">
            <a-tab-pane v-for="(item,i) in tabs" :key="i">
              <span slot="tab">
                {{item.name}}
                <a-tag
                  :color="handleColor(item.body.severity?item.body.severity:item.body.cvssV2?item.body.cvssV2.baseSeverity:item.body.cvssV3.baseSeverity)"
                >
                  {{item.body.cvssV2?item.body.cvssV2.baseScore:item.body.cvssV3.baseScore}}
                  {{item.body.severity?item.body.severity:item.body.cvssV2?item.body.cvssV2.baseSeverity:item.body.cvssV3.baseSeverity}}
                </a-tag>
              </span>
              <a-col :xs="24" :lg="8" class="inner">
                <a-col
                  :style="{background:handleColor(item.body.severity?item.body.severity:item.body.cvssV2?item.body.cvssV2.baseSeverity:item.body.cvssV3.baseSeverity) }"
                  class="innerFont"
                >
                  <span
                    style="font-size:32px"
                  >{{item.body.cvssV2?item.body.cvssV2.baseScore:item.body.cvssV3.baseScore}}</span>
                  <span>/10</span>
                  <div>
                    {{item.body.cvssV2?'cvssV2:':'cvssV3:'}}
                    {{item.body.severity?item.body.severity:item.body.cvssV2?item.body.cvssV2.baseSeverity:item.body.cvssV3.baseSeverity}}
                  </div>
                </a-col>
                <a-col>Vector :{{item.body.cvssV3?item.body.cvssV3.version:item.body.cvssV2.version}}</a-col>
                <a-col>Exploitability :{{item.body.exploitabilityScore?item.body.exploitabilityScore:''}}/Impact :{{item.body.impactScore?item.body.impactScore:''}}</a-col>
              </a-col>
              <a-col :xs="24" :lg="16">
                <a-col :xs="24" :lg="12" v-for="(value,key,index) in (item.cvssV)" :key="index">
                  <div class="cvssV">
                    <span>{{key}}</span>
                    <a-tag :color="handleColor(value)">
                      <span>{{value}}</span>
                    </a-tag>
                  </div>
                </a-col>
              </a-col>
            </a-tab-pane>
          </a-tabs>
        </Card>
      </a-col>
      <a-col :xs="24">
        <Card :name="'References'" :headStyle="bodyStyle">
          <!-- <a-icon slot="extraCard"  type="minus" /> -->
          <Tables
            :columns="columns"
            :tableData="data"
            :rowKey="`name`"
            :scrollTable="{x:1000,y:400}"
            :total="total"
          />
        </Card>
      </a-col>
      <a-col :xs="24">
        <Card :name="'Configurations'" :headStyle="bodyStyle">
          <Configurations :configurations="configurations" />
        </Card>
      </a-col>
    </a-col>
    <a-col :xs="24" :lg="8">
      <a-col :xs="24">
        <Card :name="'Information'" :bodyStyle="bodyStyle" style="textAlign:left">
          <a-col>Published :{{information.Published }}</a-col>
          <a-col>Updated :{{information.Updated }}</a-col>
          <a-divider />
          <a-col>
            <a-icon type="export" style="margin-right: 5px" />NVD link :
            <a :href="information.NVDLink">{{vulnerabilityCode}}</a>
          </a-col>
          <a-col>
            <a-icon type="export" style="margin-right: 5px" />Mitre link :
            <a :href="information.MitreLink">{{vulnerabilityCode}}</a>
          </a-col>
          <a-divider />
          <a-col>
            <a-icon type="unordered-list" style="margin-right: 5px" />JSON object :
            <a @click="()=>{this.informationVisible= true}">View</a>
          </a-col>
          <a-modal v-model="informationVisible" :footer="null" width="50%">
            <MarkdownPreview theme="oneDark" :initialValue="information.JSONObject" />
          </a-modal>
        </Card>
      </a-col>
      <a-col :xs="24">
        <Card :name="'Products Affected'" :bodyStyle="bodyStyle">
          <!-- <MarkdownPreview /> -->
          <a-col v-for="(items,i) in productsAffected" :key="i" style="text-align:left">
            <a-col style="font-weight: 800">{{items.name}}</a-col>
            <a-col v-for="(item,i) in items.body" :key="i">
              <a-icon type="tag" />
              {{item}}
            </a-col>
          </a-col>
        </Card>
      </a-col>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from "vuex";
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/Tables.vue'
import Configurations from './Configurations'
import { OverallMixins } from "@/js/Mixins/OverallMixins.js"
import { MarkdownPreview } from 'vue-meditor'
export default {
  mixins: [OverallMixins],
  components: {
    Card,
    Tables,
    Configurations,
    MarkdownPreview,
  },
  data () {
    return {
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      description: {
        head: '',
        body: ''
      },
      tabs: [],
      activeKey: 0,
      columns: [
        {
          title: "Link",
          dataIndex: "name",
          key: "name",
          customRender: (text, record, index) => this.handleRenderLink(text, record, index)
        },
        {
          title: "Resource",
          dataIndex: "tags",
          key: "tags",
          width: 300,
          customRender: (text, record, index) => this.handleRenderTags(text, record, index)
        },
      ],
      data: [],
      total: 0,
      configurations: [],
      information: {},
      informationVisible: false,
      productsAffected: []
    }
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
      vulnerabilityCode: "MonitorStore/vulnerabilityCode",
    }),
  },
  mounted () {
    const _this = this
    if (_this.vulnerabilityCode == '' || _this.vulnerabilityCode == undefined || _this.vulnerabilityCode == null) {
      _this.$message.warn('请重CVE监控跳转')
      _this.$router.push('VulnerabilitiesMonitor')
      return
    }
    const params = {
      token: _this.token,
      common_vulnerabilities_and_exposures: _this.vulnerabilityCode
    }
    _this.$api.nist_data_detailed_query(params).then((res) => {
      _this.handleDescription(res.message.cve.description.description_data[0].value)//头部信息
      _this.handleImpact(res.message.impact)//tab信息
      _this.handleReferences(res.message.cve.references.reference_data)//References表格信息
      _this.configurations = res.message.configurations.nodes
      _this.information = {
        Published: _this.moment(res.message.publishedDate).format('YYYY-MM-DD H:mm:ss'),
        Updated: _this.moment(res.message.lastModifiedDate).format('YYYY-MM-DD H:mm:ss'),
        NVDLink: `https://cve.mitre.org/cgi-bin/cvename.cgi?name=${_this.vulnerabilityCode}`,
        MitreLink: `https://nvd.nist.gov/vuln/detail/${_this.vulnerabilityCode}`,
        JSONObject: "```" + `\n ${JSON.stringify(res.message, undefined, 2)}\n` + " ```"
      }
      //Products Affected取值复杂 循环
      let productsAffected = _this.unique(_this.handleProductsAffected(res.message.configurations.nodes))
      let title = _this.unique(productsAffected.map((items) => {
        for (let i in items) {
          return { name: i, body: [] }
        }
      }))
      productsAffected.map((items) => {
        for (let i in items) {
          title.map(item => {
            if (i == item.name) {
              item.body.push(items[i])
            }
          })
        }
      })
      _this.productsAffected = title
    })
  },
  methods: {
    handleDescription (description) {
      const _this = this
      _this.description.head = description.substring(0, 1)
      _this.description.body = description.substring(1)
    },
    handleImpact (impact) {
      const _this = this
      if (impact == {} || impact == undefined) {

      }
      _this.tabs = []
      for (let i in impact) {
        let cvssV = {}
        for (let j in impact[i]) {
          if (j == 'cvssV3' || j == 'cvssV2') {
            for (let k in impact[i][j]) {
              if (_this.handleCvss(k)) cvssV[k] = impact[i][j][k]
            }
          }
        }
        let tab = {
          name: i,
          body: impact[i],
          cvssV: cvssV
          // ccvs:
        }
        _this.tabs.push(tab)
      }

    },
    handleReferences (references) {
      const _this = this
      _this.total = references.length
      _this.data = references
    },
    handleColor (val) {
      let color = ''
      switch (val) {
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
          color = "#d2d6de"
          break;
      }
      return color
    },
    handleCvss (val) {
      let flag = false
      switch (val) {
        case 'version':
          flag = false
          break;
        case 'vectorString':
          flag = false
          break;
        case 'baseScore':
          flag = false
          break;
        case 'baseSeverity':
          flag = false
          break;
        default:
          flag = true
          break;
      }
      return flag
    },
    handleRenderTags (text, record, index) {
      let dom = text.map((item) => {
        return <a-tag color="#777" >{item}<br /></a-tag>
      })
      return dom
    },
    handleRenderLink (text, record, index) {
      return <a v-on:click={() => {
        this.handleClickOpenUrl(record.url)//暂时没用
      }}>{text}</a>
    },
    handleClickOpenUrl (url) {
      window.open(url)
    },
    handleProductsAffected (productsAffected) {
      const _this = this
      let arr = []
      productsAffected.map((items) => {
        if (items.children.length > 0) {
          arr = arr.concat(_this.handleProductsAffected(items.children))
        }
        else {
          items.cpe_match.map(item => {
            let cpe_match = {}
            cpe_match[item.cpe23Uri.split(":")[3]] = item.cpe23Uri.split(":")[4]
            arr.push(cpe_match)
          })
        }
      })
      return arr
    },
    // ES6对象数组所有属性去重,筛选每个数组项的字符
    unique (arr) {
      const map = new Map()
      return arr.filter(item => !map.has(JSON.stringify(item)) && map.set(JSON.stringify(item), 1))
    }
  }

}
</script>
<style lang="scss" scoped>
.inner {
  text-align: left;
  color: #000;
  font-size: 18px;
  .innerFont {
    color: #fff;
  }
}
.cvssV {
  /* text-align: justify; */

  display: flex;
  justify-content: space-between;
  overflow: hidden;
  padding: 6px;
  border-color: #ddd;
  border: 1px solid;
  border-radius: 4px;
  background: #f5f5f5;
}
</style>