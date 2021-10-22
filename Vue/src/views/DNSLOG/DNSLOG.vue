<template>
  <a-row
    type="flex"
    justify="center"
    align="top"
    style="height:100%"
    :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 4, sm: 8, md: 12, lg: 16 },
    ]"
  >
    <a-col span="20">
      <img :src="src" height="200px" />
    </a-col>
    <a-col span="20">
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
      src: require('../../assets/dnslog.gif'),
      columns: [
        {
          title: "DNS Query Record",
          dataIndex: "domain_name",
          align: 'center',
          width: '30%',
        },
        {
          title: "IP Address",
          dataIndex: "ip",
          align: 'center',
          width: '45%',

        },
        {
          title: "Created Time",
          dataIndex: "creation_time",
          align: 'center',
          width: '35%',
          customRender: (text, record, index) => {
            return text ? this.moment(text, "X").format('YYYY-MM-DD H:mm:ss') : ""
          },
        }
      ],
      data: [],
      total: 0,
      current: 1
    };
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  created () {
    const _this = this
    _this.handleDNSLOG()
  },
  methods: {
    handleDNSLOG () {
      const _this = this
      const params = {
        token: _this.token,
        number_of_pages: _this.current,
      };
      const data = _this.$api.domain_name_system_log(params)
      // .then((res) => {
      //   if (res.code == 200) {
      //     _this.data = res.message
      //   } else {
      //     _this.$message.error(res.message);
      //   }
      // });
      const total = _this.$api.domain_name_system_log_statistics(params)
      Promise.all([data, total]).then((res) => {
        console.log(res)
        res.map((item, i) => {
          if (item.code == 200) {
            i == 0 ? _this.data = item.message : _this.total = item.message
            console.log(_this.data, _this.total)
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
