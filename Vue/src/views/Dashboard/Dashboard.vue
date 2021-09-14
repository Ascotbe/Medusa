<template>
  <a-row
    type="flex"
    justify="start"
    align="top"
    style="height:100%"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col
      :xs="{ span: 24 }"
      :md="{ span: 12 }"
      :lg="{ span: 6 }"
      v-for="(item, i) in syntheticalList"
      :key="i"
      style="min-width:158px;"
    >
      <a-col class="synthetical" :style="{ background: item.background }">
        <div style="padding: 10px 0 10px 0">{{ item.name }}</div>
        <myicon :type="item.type" class="myicon" />
        <span class="syntheticalVal">
          <span style="font-size:36px">{{ item.val }}</span>个
        </span>
      </a-col>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 12 }" class="Itemized">
      <a-col :xs="{ span: 24 }" class="Itemized-name">等级分布</a-col>
      <a-col :xs="{ span: 24 }" class="Itemized-nav">
        <Echarts :echartsData="lvEchartsData" :echartsDeploy="lvDeploy" />
      </a-col>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 12 }" class="Itemized">
      <a-col :xs="{ span: 24 }" class="Itemized-name">系统信息</a-col>
      <a-col :xs="{ span: 24 }" class="Itemized-nav">
        <SystemInforMation />
      </a-col>
    </a-col>
    <a-col :lg="{ span: 24 }" class="Itemized">
      <a-col :xs="{ span: 24 }" class="Itemized-name">
        <a-col :xs="{ span: 12}">漏洞分布</a-col>
        <a-col :xs="{ span: 12}">
          检索时间:
          <a-range-picker
            :default-value="defaultDate"
            @change="(moment, dateArr)=>{
            this.handleLeak(dateArr)
            }"
          />
        </a-col>
      </a-col>
      <a-col :xs="{ span: 24 }" class="Itemized-nav">
        <Echarts :echartsData="leakEchartsData" :echartsDeploy="leakDeploy" />
      </a-col>
    </a-col>
    <a-col :lg="{ span: 24 }" class="Itemized">
      <a-col :xs="{ span: 24 }" class="Itemized-name">
        <a-col :xs="{ span: 12}">GitHub监控</a-col>
        <a-col :xs="{ span: 12}">
          检索时间:
          <a-range-picker
            :default-value="defaultDate"
            @change="(moment, dateArr)=>{
            this.handleGitHub(dateArr)
            }"
          />
        </a-col>
      </a-col>
      <a-col :xs="{ span: 24 }" class="Itemized-nav">
        <Echarts :echartsData="gitHubEchartsData" :echartsDeploy="gitHubDeploy" />
      </a-col>
    </a-col>
    <a-col :lg="{ span: 24 }" class="Itemized">
      <a-col :xs="{ span: 24 }" class="Itemized-name">
        <a-col :xs="{ span: 12}">CPU监控</a-col>
      </a-col>
      <a-col :xs="{ span: 24 }" class="Itemized-nav">
        <Echarts :echartsData="cpuEchartsData" :echartsDeploy="cpuDeploy" />
      </a-col>
    </a-col>
    <a-col :lg="{ span: 24 }" class="Itemized">
      <a-col :xs="{ span: 24 }" class="Itemized-name">
        <a-col :xs="{ span: 12}">内存监控</a-col>
      </a-col>
      <a-col :xs="{ span: 24 }" class="Itemized-nav">
        <Echarts :echartsData="memoryEchartsData" :echartsDeploy="memoryDeploy" />
      </a-col>
    </a-col>
  </a-row>
</template>

<script>
import Echarts from "@/components/Echarts/Echarts.vue"
import SystemInforMation from "./part/SystemInforMation.vue"
import { OverallMixins } from "@/js/Mixins/OverallMixins.js"

import { Icon } from "ant-design-vue";
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1734998_iv1ouwpdggf.js",
});
import { mapGetters } from "vuex";
export default {
  mixins: [OverallMixins],
  components: {
    Echarts,
    SystemInforMation,
    myicon: MyIcon,
  },
  data () {
    return {
      syntheticalList: [
        {
          name: "目标网站",
          type: "icon-Vector",
          background: "rgba(153,217,234,1)",
          id: "number_of_websites",
          val: 0,
        },
        {
          name: "端口发现",
          type: "icon-duankousaomiao",
          background: "rgba(105,160,251,1)",
          id: "number_of_port",
          val: 0,
        },
        {
          name: "代理扫描",
          type: "icon-saomiao",
          background: "rgba(107,133,252,1)",
          id: "number_of_agent_tasks",
          val: 0,
        },
        {
          name: "发现漏洞",
          type: "icon-loudongyujing",
          background: "rgba(101,206,165,1)",
          id: "number_of_vulnerabilities",
          val: 0,
        },
      ],
      lvEchartsData: [], //等级分布 的 数据 
      lvDeploy: {  //等级分布 的 参数
        seriesType: 'bar',
        xType: "category",
        yType: "value",
        // titleText: "等级分布",
        xData: ["低危", "中危", "高危"],
        seriesItemStyle: [
          {
            color: function (params) {
              // build a color map as your need.
              let colorList = [
                "rgb(254, 67, 101)",
                "rgb(250, 218, 141)",
                "rgb(137, 190, 178)",
              ];
              return colorList[params.dataIndex];
            },
          }
        ]
      },
      gitHubEchartsData: [], //githu监控 的 数据
      gitHubDeploy: { //githu监控 的参数
        seriesName: ["gitHub"],
        seriesType: 'line',
        xType: "category",
        yType: "value",
        seriesItemStyle: [

        ]
      },
      leakEchartsData: [],//漏洞分布 的 数据
      leakDeploy: {//漏洞分布 的 参数
        seriesName: ["leak"],
        seriesType: 'line',
        xType: "category",
        yType: "value",
        seriesItemStyle: [

        ]
      },
      cpuEchartsData: [],//cpu的 数据
      cpuDeploy: {//cpu 的 参数
        seriesName: ["核心", "cpu0", "cpu1", "cpu2", "cpu3", "cpu4", "cpu5", "cpu6", "cpu7", "cpu8", "cpu9", "cpu10", "cpu11", "cpu12", "cpu13", "cpu14", "cpu15"],
        seriesType: 'line',
        xType: "category",
        yType: "value",
      },
      memoryEchartsData: [],//内存监控的数据
      memoryDeploy: { //内存监控的参数
        seriesName: ["已使用", "未使用", "使用百分比"],
        seriesType: 'line',
        xType: "category",
        yType: "value",
      },
      defaultDate: []

    }
  },
  created () {
    this.handleDefaultDate()
    this.handleHomePage()
    this.handleHardware()
  },
  mounted () {
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    }),
  },
  methods: {
    handleHomePage () { // 基本数据请求
      const _this = this
      const params = {
        token: _this.token,
      };
      _this.$api.homepage_data(params).then((res) => {
        if ((res.code = 200)) {
          _this.syntheticalList.map((item) => {
            for (let key in res.message) {
              if (item.id = res.message[key]) {
                item.val = res.message[key]
              }
            }
          })
          _this.lvEchartsData = [
            [
              res.message.low_risk_number, res.message.mid_risk_number, res.message.high_risk_number
            ]
          ]
        } else {
          _this.$message.error(res.message);
        }
      });
    },
    handleDefaultDate () { // 获取 默认时间
      const _this = this
      _this.defaultDate = [_this.moment().subtract(30, 'days'), _this.moment()]
      _this.handleGitHub(_this.defaultDate)
      _this.handleLeak(_this.defaultDate)
    },
    handleGitHub (dateArr) { //获取github监控数据
      const _this = this
      const params = {
        token: _this.token,
        start_time: _this.moment(dateArr[0]).unix(),
        end_time: _this.moment(dateArr[1]).unix(),
      }
      _this.$api.homepage_github_monitor_data(params)
        .then(async (res) => {
          if (res.code != 200) {
            this.$message.error(res.message)
            _this.gitHubEchartsData = [_this.handleFillArray(dateArr[0], dateArr[1], [])]
            return
          }
          let Arr = []
          let old = ''
          let now = ''
          let itemVal = 0
          await res.message.map((item, i) => {
            now = _this.moment(item[0], "X").format('YYYY-MM-DD')
            if (i == 0) old = now
            if (now == old) {
              if (i == res.message.length - 1) {
                itemVal += item[1]
                Arr.push([now, itemVal])
              }
              else {
                itemVal += item[1]
              }
            }
            else {
              if (i == res.message.length - 1) {
                Arr.push([old, itemVal])
                itemVal = 0
                itemVal += item[1]
                Arr.push([now, itemVal])
              }
              else {
                Arr.push([old, itemVal])
                itemVal = 0
                itemVal += item[1]
              }
            }
            old = now
            // Arr.push()

          })
          _this.gitHubEchartsData = [_this.handleFillArray(dateArr[0], dateArr[1], Arr)]
        })
        .catch((err) => {
          _this.gitHubEchartsData = [_this.handleFillArray(dateArr[0], dateArr[1], [])]
        })
    },
    handleLeak (dateArr) { //获取漏洞分布数据
      const _this = this
      const params = {
        token: _this.token,
        start_time: _this.moment(dateArr[0]).unix(),
        end_time: _this.moment(dateArr[1]).unix(),
      }
      _this.$api.homepage_vulnerability_distributiont_data(params)
        .then(async (res) => {
          if (res.code != 200) {
            this.$message.error(res.message)
            _this.leakEchartsData = [_this.handleFillArray(dateArr[0], dateArr[1], [])]
            return
          }
          let Arr = []
          let old = ''
          let now = ''
          let itemVal = 0
          await res.message.map((item, i) => {
            now = _this.moment(item[0], "X").format('YYYY-MM-DD')
            if (i == 0) old = now
            if (now == old) {
              if (i == res.message.length - 1) {
                itemVal += item[1]
                Arr.push([now, itemVal])
              }
              else {
                itemVal += item[1]
              }
            }
            else {
              if (i == res.message.length - 1) {
                Arr.push([old, itemVal])
                itemVal = 0
                itemVal += item[1]
                Arr.push([now, itemVal])
              }
              else {
                Arr.push([old, itemVal])
                itemVal = 0
                itemVal += item[1]
              }
            }
            old = now
          })
          _this.leakEchartsData = [_this.handleFillArray(dateArr[0], dateArr[1], Arr)]
        })
        .catch((err) => {
          _this.leakEchartsData = [_this.handleFillArray(dateArr[0], dateArr[1], [])]
        })
    },
    handleFillArray (startDate, endDate, Array) { //填充echarts所需要的数组
      const _this = this
      let daysList = [];
      const start = _this.moment(startDate)
      const end = _this.moment(endDate)
      const day = end.diff(start, "days");
      for (let i = 0; i < day; i++) {
        let flag = 0
        Array.map((item) => {
          if (item[0] == start.format("YYYY-MM-DD")) {
            flag = item[1]
          }
        })
        daysList.push([start.format("YYYY-MM-DD"), flag]);
        start.add(1, "days").format("YYYY-MM-DD")
      }
      return daysList;
    },
    handleHardware () { // cup 内存 使用查询
      const _this = this
      let params = {
        token: _this.token,
      };
      _this.$api.hardware_usage_query(params).then((res) => {
        let thread = [] // 线程
        let core = []// 核心
        let memory = []
        let memory_used = [] //内存使用
        let memory_free = []// 空闲的内存
        let memory_percent = []// 内存使用率
        thread.length = res.message[0].per_core_central_processing_unit_usage_rate.length
        for (let i = 0; i < thread.length; i++) {
          thread[i] = []
        }
        for (let i = 0; i < res.message.length; i++) {
          // cpu 核心 和 线程 格式调整
          core.push([_this.moment(res.message[i].creation_time, "X").format('H:mm:ss'), res.message[i].central_processing_unit_usage_rate])
          for (let j = 0; j < thread.length; j++) {
            thread[j].push([_this.moment(res.message[i].creation_time, "X").format('H:mm:ss'), res.message[i].per_core_central_processing_unit_usage_rate[j]])
          }
          // 内存使用 未使用内存 内存使用率 格式调整
          memory_used.push([_this.moment(res.message[i].creation_time, "X").format('H:mm:ss'), _this.QJMemorySize(res.message[i].memory_used)])
          memory_free.push([_this.moment(res.message[i].creation_time, "X").format('H:mm:ss'), _this.QJMemorySize(res.message[i].memory_free)])
          memory_percent.push([_this.moment(res.message[i].creation_time, "X").format('H:mm:ss'), res.message[i].memory_percent])
        }
        thread.unshift(core)
        _this.cpuEchartsData = thread
        memory = [memory_used, memory_free, memory_percent]
        _this.memoryEchartsData = memory
      });
    },

  }
}
</script>

<style lang="scss" scoped>
.synthetical {
  margin-top: 25px;
  padding: 10px;
  border-radius: 5px;
  font-size: 20px;
  text-align: left;
  font-weight: 800;
  color: aliceblue;
  .myicon {
    display: inline-block;
    border: 1px solid #88888870;
    border-radius: 50% 50%;
    box-shadow: 0px 2px 5px #6b6b6b inset;
    overflow: hidden;
    padding: 10px;
    font-size: 40px;
  }
  .syntheticalVal {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
}
.Itemized-name {
  min-width: 85px;
  padding: 10px;
  color: rgba(113, 113, 113, 1);
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  text-align: left;
  background: #fff;
  margin-right: 30px;
  font-size: 20px;
  border-bottom: 1px solid rgb(238, 238, 238);
}

.Itemized-nav {
  padding: 10px;
  color: rgba(169, 169, 169, 1);
  height: 1.7rem;
  // min-width: 288px;
  min-height: 250px;
  // border-top-right-radius: 5px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  border-bottom: 1px solid rgb(238, 238, 238);
  text-align: left;
  background: #fff;
  font-size: 16px;
}
.Itemized:hover .Itemized-name,
.Itemized:hover .Itemized-nav {
  border-top: 1px solid rgb(238, 238, 238);
  border-left: 1px solid rgb(238, 238, 238);
  box-shadow: 10px 10px 5px #888888;
  /*设置阴影,可以自定义参数*/
  -webkit-box-shadow: 10px 10px 5px #888888;
  -o-box-shadow: 10px 10px 5px #888888;
  -moz-box-shadow: 10px 10px 5px #888888;
}
</style>