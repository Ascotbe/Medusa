<template>
  <div ref="systemHardwareMemory" class="systemHardware"></div>
</template>

<script>
export default {
  name: "systemHardwareMemory",
  props: {
    parameter: {
      type: Array,
      default: [],
    },
  },
  data() {
    return {
      systemHardwareEcharts: {},
      //   xais: [],
      //   value: [],
      memoryFreeData: [], //内存未使用量
      memoryPercentData: [], // 内存利用率
      memoryUsedData: [], //内存使用量
      memoryAll: 0,
    };
  },
  mounted() {},
  methods: {
    fnsystemHardwareEcharts() {
      //   console.log(this.parameter);
      // 基于准备好的dom，初始化echarts实例
      this.systemHardwareEcharts = this.$echarts.init(this.$refs.systemHardwareMemory);
      let _this = this;
      this.memoryAll =
        parseFloat(this.memoryFreeData[0][1]) + parseFloat(this.memoryUsedData[0][1]);
      // console.log(this.memoryAll);
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
            name: "内存占用率",
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
          {
            name: "未使用",
            type: "value",
            splitNumber: 5,
            minInterval: 1,
            axisLabel: {
              show: true,
              color: "rgba(169,169,169,1)",
              formatter: "{value} Gb",
            },
            axisLine: {
              lineStyle: {
                color: "rgb(51, 255, 0)",
              },
            },
            max: Math.ceil(this.memoryAll),
            splitLine: {
              lineStyle: {
                // 使用深浅的间隔色
                type: "dashed",
                color: ["rgba(169,169,169,0.5)"],
              },
            },
            position: "right",
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
          top: "20%",
          height: "70%",
        },
        legend: {
          data: ["内存占用率", "内存未使用"],
        },
        series: [
          {
            name: "内存占用率",
            type: "line",
            showSymbol: false,
            symbol: "circle",
            smooth: true,
            hoverAnimation: true,
            itemStyle: {
              color: "rgba(255, 145, 0,0.8)",
            },
            lineStyle: {
              shadowBlur: 10,
              shadowColor: "#000",
            },
            emphasis: {
              label: {
                show: false,
              },
            },
            yAxisIndex: 0,
            data: this.memoryPercentData,
          },
          {
            name: "内存未使用",
            type: "line",
            showSymbol: false,
            symbol: "circle",
            smooth: true,
            hoverAnimation: true,
            itemStyle: {
              color: "rgba(51, 255,0,0.8)",
            },
            lineStyle: {
              shadowBlur: 10,
              shadowColor: "#000",
            },
            emphasis: {
              label: {
                show: false,
              },
            },
            yAxisIndex: 1,
            data: this.memoryFreeData,
          },
        ],
      });
      window.addEventListener("resize", () => {
        this.systemHardwareEcharts.resize();
      });
    },
  },
  computed: {
    systemHardwareMemory_Collapsed() {
      return this.$store.state.collapsed;
    },
  },
  watch: {
    parameter() {
      let _this = this;
      _this.data = [];
      _this.parameter.map((item) => {
        _this.memoryFreeData.push([item.creation_time, item.memory_free]);
        _this.memoryPercentData.push([item.creation_time, item.memory_percent]);
        _this.memoryUsedData.push([item.creation_time, item.memory_used]);
      });

      _this.fnsystemHardwareEcharts();
    },
    systemHardwareMemory_Collapsed() {
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
  color: rgb(141, 141, 141);
}
</style>
