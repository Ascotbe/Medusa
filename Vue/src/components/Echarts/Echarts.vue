<template>
  <div ref="Echarts" style="width: 100%;height: 100%;"></div>
</template>

<script>
export default {
  data () {
    return {
      Echarts: {},
      series: [],
      areaStyle: {
        opacity: 0
      }
    }
  },
  mounted () {
    const _this = this
    _this.$nextTick(() => {
      _this.Echarts = _this.$echarts.init(_this.$refs.Echarts);
      window.addEventListener("resize", () => {
        _this.Echarts.resize();
      });
    })
  },
  props: {
    echartsDeploy: {
      type: Object,
      default: () => {
        return {
          seriesName: ["测试1"],
          seriesType: "line",
          xType: "category",
          yType: "value",
          titleText: "测试标题",
          itemStyle: [],
        }
      }
    },
    echartsData: {//series的data
      type: Array,
      default: () => {
        return []
      }
    },
  },
  methods: {
    handleSetOption (Model) {
      const _this = this
      const modelData = Model == 'simple' ? [] : _this.echartsDeploy.seriesName
      _this.Echarts.setOption(
        {
          title: {
            text: _this.echartsDeploy.titleText
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
              type: 'cross'        // 默认为直线，可选为：'line' | 'shadow |cross'
            }
          },
          legend: {
            data: modelData
          },
          xAxis: {
            type: _this.echartsDeploy.xType,
            data: _this.echartsDeploy.xData ? _this.echartsDeploy.xData : '',

            axisTick: {
              alignWithLabel: false
            }
          },
          yAxis: [
            {
              type: _this.echartsDeploy.yType,
              minInterval: 1
            }
          ],
          series: _this.series
        }
      )
      _this.$nextTick(() => {
        _this.Echarts.resize();
      })
    },
    handleSetSeries (data) {
      const _this = this

      _this.series = [
        {
          type: _this.echartsDeploy.seriesType,
          smooth: _this.echartsDeploy.seriesType == "line" ? true : false,
          showSymbol: _this.echartsDeploy.seriesType == "line" ? false : true,
          data: data,
          itemStyle: _this.echartsDeploy.seriesItemStyle ? _this.echartsDeploy.seriesItemStyle[0] : '',
          areaStyle: _this.echartsDeploy.seriesAreaStyle ? _this.echartsDeploy.seriesAreaStyle[0] : ''
        }
      ]
      _this.handleSetOption('simple') //简单 单个数组组成series
    },
    async handleSetSerieses (data) { //多个data
      const _this = this
      _this.echartsDeploy.seriesName.length = data.length
      await data.map((item, i) => {
        let mnue = {
          name: _this.echartsDeploy.seriesName[i],
          type: _this.echartsDeploy.seriesType,
          smooth: _this.echartsDeploy.seriesType == "line" ? true : false,
          showSymbol: _this.echartsDeploy.seriesType == "line" ? false : true,
          data: item,
          itemStyle: _this.echartsDeploy.seriesItemStyle ? _this.echartsDeploy.seriesItemStyle[i] : '',
          areaStyle: _this.echartsDeploy.seriesAreaStyle ? _this.echartsDeploy.seriesAreaStyle[i] : this.areaStyle,
        }
        _this.series.push(mnue)
        return mnue
      })
      _this.handleSetOption('complex')//复杂 多个数组组成series
    }
  },
  watch: {
    echartsData: {
      handler: function (now, old) {
        if (now.length == 1) {
          this.handleSetSeries(now[0])
        }
        else {
          this.handleSetSerieses(now)
        }
      }
    }
  }

}
</script>

<style>
</style>