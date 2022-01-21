<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%"
    :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 4, sm: 8, md: 12, lg: 16 },
    ]"
  >
    <a-col span="24">
      <Card :name="``">
        <img :src="src" height="100px" />
        <a-col span="24" style="font-size:16px;">
          <!-- <a-icon type="smile" style="font-size: 18px;color: #E6A23C;" /> -->
          😃：{{DNSLOG}}
        </a-col>
        <a-col span="24">
          <Card :name="``" :bodyStyle="bodyStyle">
            <Tables
              :scrollTable="{ x: 1200, y: 500 }"
              :columns="columns"
              :tableData="data"
              :total="total"
              :rowKey="(record,index)=>index"
              @change="handleChange"
            />
          </Card>
        </a-col>
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/Tables.vue'
import { mapGetters } from "vuex";
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
export default {
  mixins: [OverallMixins],
  components: {
    Card,
    Tables
  },
  data () {
    return {
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      src: require('../../../assets/dnslog.gif'),
      columns: [
        {
          title: "DNS Query Record",
          dataIndex: "domain_name",
        },
        {
          title: "IP Address",
          dataIndex: "ip",
        },
        {
          title: "Created Time",
          dataIndex: "creation_time",
          customRender: (text, record, index) => {
            return text ? this.moment(text, "X").format('YYYY-MM-DD H:mm:ss') : ""
          },
        }
      ],
      data: [],
      total: 0,
      current: 1,
      //获取到的用户DNSLOG值
      DNSLOG: ''
    };
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
      userinfo: "UserStore/userinfo"
    })
  },
  created () {
    const _this = this
    _this.handleDNSLOG()
  },
  methods: {
    handleDNSLOG () {
      const _this = this
      const paramsGet = {
        key: _this.userinfo.key,
      };
      const paramsLog = {
        ...paramsGet,
        number_of_pages: _this.current,
      };
      const paramsStatistics = {
        token: _this.token,
      };
      const log = _this.$api.get_domain_name_system_log(paramsGet)
      const data = _this.$api.domain_name_system_log(paramsLog)
      const total = _this.$api.domain_name_system_log_statistics(paramsStatistics)
      Promise.all([data, total, log]).then((res) => {
        console.log(res)
        res.map((item, i) => {
          if (item.code == 200) {
            i == 0 ? _this.data = item.message : i == 1 ? _this.total = item.message : _this.DNSLOG = item.message
          }
          else _this.$message.warn(item.message)
        })
      })

    },
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleDNSLOG()
    }
  },
};
</script>

<style lang="scss" scoped>
</style>
