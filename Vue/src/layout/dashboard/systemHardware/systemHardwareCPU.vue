<template>
  <div ref="systemHardwareCPU" class="systemHardware"></div>
</template>

<script>
export default {
  name: "systemHardwareCPU",
  props: {
    CPUData: {
      // 中央处理器使用率
      type: Array,
      default: [],
    },
    CoreData: {
      //每个核心使用率
      type: Array,
      default: [],
    },
  },
  data() {
    return {
      systemHardwareEcharts: {},
      //   xais: [],
      //   value: [],
      // CPUData: [], // 中央处理器使用率
      // CoreData: [], //每个核心使用率
      // series: [], //echarts的series
      // colorList: [
      //     "rgb(255, 0, 0)",
      //     "rgb(251, 255, 0)",
      //     "rgb(145, 255, 0)",
      //     "rgb(0, 255, 115)",
      //     "rgb(0, 255, 242)",
      //     "rgb(0, 153, 255)",
      //     "rgb(0, 60, 255)",
      //     " rgb(89, 0, 255)",
      //     "rgb(204, 0, 255)",
      //     "rgb(255, 0, 242)",
      //     ' rgb(255, 0, 119)',
      //     ' rgb(255, 208, 0)',
      //     'rgb(179, 255, 0)',
      //     'rgb(0, 217, 255)',
      //     'rgb(184, 229, 235)',
      //     'rgb(220, 184, 235)'

      // ], //调色盘
    };
  },
  created() {},
  mounted() {},
  methods: {
    fnsystemHardwareEcharts() {
      //   console.log(this.parameter);
      // 基于准备好的dom，初始化echarts实例
      this.systemHardwareEcharts = this.$echarts.init(this.$refs.systemHardwareCPU);
      this.systemHardwareEcharts.setOption({
        tooltip: {
          show: true,
          trigger: "axis",
          axisPointer: {
            type: "line",
          },
          // formatter: function (params) {
          //     console.log(params)
          //     let a = params[0].seriesName+':'+params[0].data[0]+"<br />"+ params[0].data[1]+
          //     return params[0].data[0] + "<br />" + "监控数:" + params[0].data[1];
          // },
          backgroundColor: "rgba(111, 111, 111, 1)",
          borderWidth: 1,
          borderColor: "#ccc",
          padding: 10,
          textStyle: {
            color: "#fff",
          },
        },
        dataZoom: [
          {
            type: "inside",
            show: true,
            start: 80,
            end: 100,
          },
        ],
        xAxis: {
          type: "time",
          nameTextStyle: {
            color: "rgba(169,169,169,1)",
          },
          axisLine: {
            lineStyle: {
              color: "rgba(169,169,169,1)",
            },
          },
          axisLabel: {
            show: true,
            interval: 0,
            formatter: function (value, index) {
              // 格式化成月/日，只在第一个刻度显示年份
              let date = new Date(value);
              let texts = [date.getHours(), date.getMinutes(), date.getSeconds()];
              return texts.join(":");
            },
          },
          splitLine: {
            show: false,
          },
          // maxInterval: 3600 * 24 * 1000,
          boundaryGap: [0, 0],
        },
        yAxis: [
          {
            name: "使用率",
            type: "value",
            splitNumber: 5,
            minInterval: 25,
            max: 100,
            axisLabel: {
              show: true,
              color: "rgba(169,169,169,1)",
              formatter: "{value} %",
            },
            axisLine: {
              lineStyle: {
                color: "rgb(255, 145, 0)",
              },
            },
            splitLine: {
              lineStyle: {
                // 使用深浅的间隔色
                type: "dashed",
                color: ["rgba(169,169,169,0.5)"],
              },
            },
            label: {
              show: false,
            },
            emphasis: {
              label: {
                show: false,
              },
            },
          },
        ],
        grid: {
          top: "30%",
          height: "60%",
        },
        legend: {
          show: true,
        },
        series: this.handleSetSeries(),
      });
      window.addEventListener("resize", () => {
        this.systemHardwareEcharts.resize();
      });
    },
    handleSetSeries() {
      let series = [
        {
          name: "中央处理器使用率",
          type: "line",
          showSymbol: false,
          symbol: "circle",
          smooth: true,
          hoverAnimation: true,
          itemStyle: {
            color: "rgba(255, 145, 0,0.8)",
          },
          emphasis: {
            label: {
              show: false,
            },
          },
          yAxisIndex: 0,
          data: this.CPUData,
        },
      ];
      let a = this.getLenght();
      let CoreData = this.CoreData;
      let list = new Array(a);
      for (let i = 0; i < list.length; i++) {
        list[i] = new Array();
      }
      for (let i = 0; i < CoreData.length; i++) {
        for (let j = 0; j < CoreData[i].length; j++) {
          list[j].push(CoreData[i][j]);
        }
        i;
      }
      let option = {};
      for (let i = 0; i < list.length; i++) {
        option = {
          name: "线程" + i,
          type: "line",
          showSymbol: false,
          symbol: "circle",
          smooth: true,
          hoverAnimation: true,
          // itemStyle: {
          //     color: "rgb(0, 255, 242)",
          // },
          emphasis: {
            label: {
              show: false,
            },
          },
          yAxisIndex: 0,
          data: list[i],
        };
        series.push(option);
      }
      return series;
    },
    getLenght() {
      return this.CoreData[0].length;
    },
  },
  computed: {
    systemHardwareCPU_Collapsed() {
      return this.$store.state.collapsed;
    },
  },
  watch: {
    CPUData() {
      this.fnsystemHardwareEcharts();
    },
    systemHardwareCPU_Collapsed() {
      let _this = this;
      this.$nextTick(function () {
        setTimeout(function () {
          _this.systemHardwareEcharts.resize();
        }, 500);
      });
    },
  },
};
</script>

<style>
.systemHardware {
  width: 100%;
  height: 100%;
}
</style>
