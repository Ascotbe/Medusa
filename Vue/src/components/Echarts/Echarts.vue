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
      },
      setInterval: {},//定时器
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
    /**
     * series的样式配置
     * echartsSeries={
     *  name:[],
     *  itemStyle:[],
     *  areaStyle:[]
     * }
     */
    echartsSeries: {
      type: Object,
      default: () => {
        return {}
      }
    },
    /**
     * x轴
     * xAxis={
     *  type:'',
     *  data:[]
     * }
     */
    xAxis: {
      type: Object,
      default: () => {
        return {}
      }
    },
    /**
       * y轴
       * yAxis={
       *  type:''
       * }
       */
    yAxis: {
      type: Array,
      default: () => {
        return []
      }
    },
    //图形类型
    //bar line
    type: {
      type: String,
      default: () => {
        return 'bar'
      }
    },
    //开启切换过度动画
    universalTransition: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    // handleSetOption (Model) {
    //   const _this = this
    //   const modelData = Model == 'simple' ? [] : _this.echartsDeploy.seriesName
    //   _this.Echarts.setOption(
    //     {
    //       title: {
    //         text: _this.echartsDeploy.titleText
    //       },
    //       tooltip: {
    //         trigger: 'axis',
    //         axisPointer: {            // 坐标轴指示器，坐标轴触发有效
    //           type: 'cross'        // 默认为直线，可选为：'line' | 'shadow |cross'
    //         }
    //       },
    //       legend: {
    //         data: modelData
    //       },
    //       xAxis: {
    //         type: _this.echartsDeploy.xType,
    //         data: _this.echartsDeploy.xData ? _this.echartsDeploy.xData : '',
    //         axisTick: {
    //           alignWithLabel: false
    //         }
    //       },
    //       yAxis: [
    //         {
    //           type: _this.echartsDeploy.yType,
    //           minInterval: 1
    //         }
    //       ],
    //       series: _this.series
    //     }
    //   )
    //   _this.$nextTick(() => {
    //     _this.Echarts.resize();
    //   })
    // },
    // handleSetSeries (data) {
    //   const _this = this

    //   _this.series = [
    //     {
    //       type: _this.echartsDeploy.seriesType,
    //       smooth: _this.echartsDeploy.seriesType == "line" ? true : false,
    //       showSymbol: _this.echartsDeploy.seriesType == "line" ? false : true,
    //       data: data,
    //       itemStyle: _this.echartsDeploy.seriesItemStyle ? _this.echartsDeploy.seriesItemStyle[0] : '',
    //       areaStyle: _this.echartsDeploy.seriesAreaStyle ? _this.echartsDeploy.seriesAreaStyle[0] : '',
    //       barMinHeight: _this.echartsDeploy.seriesType == "bar" ? 5 : undefined,//柱状图最小值
    //       barMaxWidth: _this.echartsDeploy.seriesType == "bar" ? '35%' : undefined,//柱状图最小值
    //     }
    //   ]
    //   _this.handleSetOption('simple') //简单 单个数组组成series
    // },
    // async handleSetSerieses (data) { //多个data
    //   const _this = this
    //   _this.echartsDeploy.seriesName.length = data.length
    //   await data.map((item, i) => {
    //     let mnue = {
    //       name: _this.echartsDeploy.seriesName[i],
    //       type: _this.echartsDeploy.seriesType,
    //       smooth: _this.echartsDeploy.seriesType == "line" ? true : false,
    //       showSymbol: _this.echartsDeploy.seriesType == "line" ? false : true,
    //       data: item,
    //       itemStyle: _this.echartsSeries.seriesItemStyle ? _this.echartsSeries.seriesItemStyle[i] : '',
    //       areaStyle: _this.echartsSeries.seriesAreaStyle ? _this.echartsSeries.seriesAreaStyle[i] : this.areaStyle,
    //     }
    //     _this.series.push(mnue)
    //     return mnue
    //   })
    //   _this.handleSetOption('complex')//复杂 多个数组组成series
    // },


    //构造x轴
    handleXAxis () {
      const _this = this
      const xAxis = {
        show: true,
        type: _this.xAxis.type,
        axisTick: {
          alignWithLabel: false
        }
      }
      return xAxis
    },
    //构造y轴
    handleYAxis () {
      const _this = this
      if (_this.yAxis.length == 1) {
        const yAxis = {
          type: _this.yAxis[0].type,
          splitNumber: _this.yAxis[0]?.splitNumber ? _this.yAxis[0].splitNumber : '',
          minInterval: _this.yAxis[0]?.minInterval ? _this.yAxis[0].minInterval : '',
          max: _this.yAxis[0]?.max ? _this.yAxis[0].max : '',
          axisLabel: _this.yAxis[0]?.axisLabel ? _this.yAxis[0].axisLabel : {}
        }
        return yAxis
      }
      else if (_this.yAxis.length == 2) {
        const yAxis = _this.yAxis.map((item, i) => {
          const menu = {
            name: item.name,
            type: item.type,
            splitNumber: item.splitNumber ? item.splitNumber : '',
            minInterval: item.minInterval ? item.minInterval : '',
            interval: item.interval || '',
            max: item.max ? item.max : '',
            axisLabel: item.axisLabel ? item.axisLabel : {}
          }
          return menu
        })
        return yAxis
      }
    },
    //构造tooltip
    handleTooltip () {
      const tooltip = {
        trigger: 'axis',
        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
          type: 'cross'        // 默认为直线，可选为：'line' | 'shadow |cross'
        }
      }
      return tooltip
    },
    //构造legend
    //flag 是否渲染多个 true 多个 false 单个
    handleLegend (flag) {
      const _this = this
      const legend = {
        data: !flag ? [] : _this.echartsSeries.name
      }
      return legend
    },
    //构造bar
    handleBar (flag, data, universalTransition) {
      const _this = this
      //flag 是否渲染多个
      //echartsSeries series配置项
      if (!flag) {//渲染一个
        const series = [
          {
            name: _this.echartsSeries.name ? _this.echartsSeries.name[0] : '',
            type: 'bar',
            itemStyle: _this.echartsSeries.itemStyle ? _this.echartsSeries.itemStyle[0] : '',
            areaStyle: _this.echartsSeries.areaStyle ? _this.echartsSeries.areaStyle[0] : '',
            smooth: false,
            showSymbol: true,
            barMinHeight: 5,//柱状图最小值
            barMaxWidth: '35%',//柱状图最小值
            universalTransition: universalTransition,
            id: universalTransition ? _this.echartsSeries.name ? _this.echartsSeries.name[0] : 'medusa' : 'medusa',
          }
        ]
        return series
      }
      else {//渲染多个

      }

    },
    //构造line
    handleLine (flag, data, universalTransition) {
      const _this = this
      //flag 是否渲染多个 true 多个 false 单个
      //echartsSeries series配置项
      if (!flag) {//渲染一个
        const series = [
          {
            name: _this.echartsSeries.name ? _this.echartsSeries.name[0] : '',
            type: 'line',
            itemStyle: _this.echartsSeries.itemStyle ? _this.echartsSeries.itemStyle[0] : '',
            areaStyle: _this.echartsSeries.areaStyle ? _this.echartsSeries.areaStyle[0] : '',
            smooth: true,
            showSymbol: false,
            universalTransition: universalTransition,
            id: universalTransition ? _this.echartsSeries.name ? _this.echartsSeries.name[0] : 'medusa' : 'medusa',
          }
        ]
        return series
      }
      else {//渲染多个
        const series = data.map((item, i) => {
          const mnue = {
            name: _this.echartsSeries.name ? _this.echartsSeries.name[i] : '',
            yAxisIndex: _this.echartsSeries.yAxisIndex ? _this.echartsSeries.yAxisIndex[i] : 0,
            type: 'line',
            smooth: true,
            showSymbol: false,
            itemStyle: _this.echartsSeries.itemStyle ? _this.echartsSeries.itemStyle[i] : '',
            areaStyle: _this.echartsSeries.areaStyle ? _this.echartsSeries.areaStyle[i] : this.areaStyle,
            universalTransition: universalTransition,
            id: universalTransition ? _this.echartsSeries.name ? _this.echartsSeries.name[i] : `medusa${i}` : `medusa${i}`,
            datasetIndex: `${i}`
          }
          return mnue
        })
        return series
      }
    },
    //构造pie
    handlePie (flag, data, universalTransition) {
      const _this = this
      //flag 是否渲染多个 true 多个 false 单个
      //echartsSeries series配置项
      if (!flag) {//渲染一个
        const series = [
          {
            name: _this.echartsSeries.name ? _this.echartsSeries.name[0] : '',
            type: 'pie',
            itemStyle: _this.echartsSeries.itemStyle ? _this.echartsSeries.itemStyle[0] : {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            areaStyle: _this.echartsSeries.areaStyle ? _this.echartsSeries.areaStyle[0] : '',
            radius: ['40%', '70%'],
            universalTransition: universalTransition,
            id: universalTransition ? _this.echartsSeries.name ? _this.echartsSeries.name[0] : 'medusa' : 'medusa',
          }
        ]
        return series
      }
      else {//渲染多个
        const span = parseInt(80 / data.length)
        const series = data.map((item, i) => {
          let star = 20
          const mnue = {
            name: _this.echartsSeries.name ? _this.echartsSeries.name[i] : '',
            type: 'pie',
            itemStyle: _this.echartsDeploy.itemStyle ? _this.echartsDeploy.itemStyle[i] : {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            areaStyle: _this.echartsDeploy.areaStyle ? _this.echartsDeploy.areaStyle[i] : this.areaStyle,
            radius: [`${star + (i - 1) * span}%`, `${star + i * span}%`],
            universalTransition: universalTransition,
            id: universalTransition ? _this.echartsSeries.name ? _this.echartsSeries.name[i] : `medusa${i}` : `medusa${i}`,
            datasetIndex: `${i}`
          }
          return mnue
        })
        return series
      }
    },
    //构造scatter
    handleScatter (flag, data, universalTransition) {
      const _this = this
      //flag 是否渲染多个 true 多个 false 单个
      //echartsSeries series配置项
      if (!flag) {//渲染一个
        const series = [
          {
            name: _this.echartsSeries.name ? _this.echartsSeries.name[0] : '',
            yAxisIndex: _this.echartsSeries.yAxisIndex ? _this.echartsSeries.yAxisIndex[i] : 0,
            type: 'scatter',
            // itemStyle: _this.echartsSeries.itemStyle ? _this.echartsSeries.itemStyle[0] : '',
            // areaStyle: _this.echartsSeries.areaStyle ? _this.echartsSeries.areaStyle[0] : '',
            smooth: true,
            showSymbol: false,
            universalTransition: universalTransition,
            id: universalTransition ? _this.echartsSeries.name ? _this.echartsSeries.name[0] : 'medusa' : 'medusa',
          }
        ]
        return series
      }
      else {//渲染多个
        const series = data.map((item, i) => {
          const mnue = {
            name: _this.echartsSeries.name ? _this.echartsSeries.name[i] : '',
            yAxisIndex: _this.echartsSeries.yAxisIndex ? _this.echartsSeries.yAxisIndex[i] : 0,
            type: 'scatter',
            smooth: true,
            itemStyle: {
              normal: {
                opacity: 0.4
              }
            },
            showSymbol: false,
            universalTransition: universalTransition,
            id: universalTransition ? _this.echartsSeries.name ? _this.echartsSeries.name[i] : `medusa${i}` : `medusa${i}`,
            datasetIndex: `${i}`
          }
          return mnue
        })
        return series
      }
    },

    //构造Option
    //type 渲染什么类型 bar line
    //flag 是否渲染多个 true 多个 false 单个
    //data series的data数据
    //universalTransition 开启过度动画
    handleOption (type, flag, data, universalTransition) {
      const _this = this
      if (!universalTransition) {
        const series = type == 'bar' ? _this.handleBar(flag, data) : type == 'line' ? _this.handleLine(flag, data) : _this.handlePie(flag, data)
        _this.Echarts.setOption(
          {
            tooltip: _this.handleTooltip(),
            dataset: _this.handleDataset(flag, data),
            legend: _this.handleLegend(flag),
            xAxis: _this.handleXAxis(),
            yAxis: _this.handleYAxis(),
            series: series
          }
        )
      }
      else {
        //bar
        const optionA = {
          tooltip: _this.handleTooltip(),
          legend: _this.handleLegend(flag),
          xAxis: _this.handleXAxis(),
          yAxis: _this.handleYAxis(),
          dataset: _this.handleDataset(flag, data),
          series: _this.handleBar(flag, data, universalTransition)
        }
        //pie
        const optionB = {
          xAxis: {
            axisLine: {
              show: false
            }
          },
          yAxis: _this.handleYAxis(),
          legend: _this.handleLegend(flag),
          tooltip: _this.handleTooltip(),
          dataset: _this.handleDataset(flag, data),
          series: _this.handlePie(flag, data, universalTransition)
        }
        //line
        const optionC = {
          tooltip: _this.handleTooltip(),
          xAxis: _this.handleXAxis(),
          yAxis: _this.handleYAxis(),
          legend: _this.handleLegend(flag),
          dataset: _this.handleDataset(flag, data),
          series: _this.handleLine(flag, data, universalTransition)
        }
        //scatter
        const optionD = {
          tooltip: _this.handleTooltip(),
          xAxis: _this.handleXAxis(),
          yAxis: _this.handleYAxis(),
          legend: _this.handleLegend(flag),
          dataset: _this.handleDataset(flag, data),
          series: _this.handleScatter(flag, data, universalTransition)
        }
        if (type === 'bar') {
          let option = optionA
          _this.Echarts.setOption(option)
          _this.setInterval = setInterval(() => {
            // option = option === optionA ? optionB : option === optionB ? optionC : optionA;
            option = option === optionA ? optionB : optionA;
            // 使用 notMerge 的形式可以移除坐标轴
            _this.Echarts.setOption(option)
          }, 5000);
        }
        else if (type === 'line') {
          let option = optionC
          _this.Echarts.setOption(option)
          _this.setInterval = setInterval(() => {
            // option = option === optionA ? optionB : option === optionB ? optionC : optionA;
            option = option === optionC ? optionD : optionC;
            // 使用 notMerge 的形式可以移除坐标轴
            _this.Echarts.setOption(option)
          }, 5000);
        }
      }
      _this.$nextTick(() => {
        _this.Echarts.resize();
      })
    },
    //构造数据集
    //flag 是否渲染多个 true 多个 false 单个
    //data series的data数据
    handleDataset (flag, data) {
      if (!flag) {
        const dataset = [
          {
            sourceHeader: false,
            source: data
          }
        ]
        return dataset
      }
      else {
        const dataset = data.map((item, i) => {
          return {
            source: item
          }
        })

        console.log(dataset)
        return dataset
      }

    }
  },
  watch: {
    echartsData: {
      handler: function (now, old) {
        const _this = this
        clearInterval(_this.setInterval)
        if (now.length == 1) {
          // _this.handleSetSeries(now[0])
          _this.handleOption(_this.type, false, now[0], this.universalTransition)
        }
        else {
          // _this.handleSetSerieses(now)
          _this.handleOption(_this.type, true, now, this.universalTransition)
        }
      }
    }
  }

}
</script>

<style>
</style>