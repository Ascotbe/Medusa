<template>
  <div class="rank_Distribution" ref="rank_Distribution"></div>
</template>

<script>
export default {
  name: "rank_Distribution",
  props: ["myEcharts"],
  data() {
    return {
      myChart: {},
    };
  },
  mounted() {
   
  },
  computed: {
    rank_Distribution_Collapsed() {
      return this.$store.state.collapsed;
    },
  },
  methods: {
    fnDrawLine() {
      // 基于准备好的dom，初始化echarts实例
      this.myChart = this.$echarts.init(this.$refs.rank_Distribution);
      this.myChart.setOption({
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c}",
          textStyle: {
            fontSize: 16,
            color: "#fff",
          },
        },
        grid: {
          left: "3%",
          right: "3%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "category",
            data: ["高危", "中危", "低危"],

            nameTextStyle: {
              color: "rgba(169,169,169,1)",
            },
            axisLine: {
              lineStyle: {
                color: "rgba(169,169,169,1)",
              },
            },
          },
        ],
        yAxis: [
          {
            type: "value",
            splitNumber: 4,

            axisLabel: {
              show: true,
              color: "rgba(169,169,169,1)",
            },
            axisLine: {
              lineStyle: {
                color: "rgba(169,169,169,1)",
              },
            },

            splitLine: {
              lineStyle: {
                // 使用深浅的间隔色
                type: "dashed",
                color: ["rgba(169,169,169,0.5)"],
              },
            },
          },
        ],
        series: [
          {
            name: "等级分布",
            type: "bar",
            itemStyle: {
              color: function (params) {
                // build a color map as your need.
                let colorList = [
                  "rgb(254, 67, 101)",
                  "rgb(250, 218, 141)",
                  "rgb(137, 190, 178)",
                ];
                return colorList[params.dataIndex];
              },
            },
            barMaxWidth: "20%",
            barMinHeight: 5,
            data: [
              {
                value: this.myEcharts.high_risk_number,
              },
              {
                value: this.myEcharts.mid_risk_number,
              },
              {
                value: this.myEcharts.low_risk_number,
              },
            ],
            // roseType:'radius',
            // minAngle:'33',
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
            label: {
              show: true,
              fontFamily: "黑体",
              fontSize: 16,
              color: function (params) {
                // build a color map as your need.
                let colorList = [
                  "rgb(254, 67, 101)",
                  "rgb(244, 208, 0)",
                  "rgb(69, 137, 148)",
                ];
                return colorList[params.dataIndex];
              },
              // backgroundColor: "#fff",
              position: "top",
            },
          },
        ],
      });
      window.addEventListener("resize", () => {
        this.myChart.resize();
      });
    },
  },
  watch: {
    myEcharts() {
      this.myEcharts = this.myEcharts;
      this.fnDrawLine();
    },
    rank_Distribution_Collapsed() {
      let _this = this;
      this.$nextTick(function () {
        setTimeout(function () {
          _this.myChart.resize();
        }, 500);
      });
    },
  },
};
</script>

<style>
.rank_Distribution {
  width: 100%;
  height: 100%;
}
</style>
