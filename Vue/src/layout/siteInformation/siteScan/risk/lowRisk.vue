<template>
<div id="lowRisk" class="lowRisk"></div>
</template>

<script>
export default {
    name: 'lowRisk',
    data() {
        return {
            lowRisk: {},
            highlight: "#03b7c9",
        };
    },
    mounted() {
        let _this = this;
        _this.fnDrawLine();
        window.onresize = () => {
            _this.lowRisk.resize();
        };
    },
    methods: {
        fnDrawLine() {
            // 基于准备好的dom，初始化echarts实例
            this.lowRisk = this.$echarts.init(document.getElementById("lowRisk"));
            this.lowRisk.setOption({
                series: [{
                        type: "gauge",
                        center: ["50%", "50%"],
                        radius: "65%", // 1行3个
                        splitNumber: 10,
                        min: 0,
                        max: 100,
                        startAngle: 225,
                        endAngle: -45,
                        axisLine: {
                            show: true,
                            lineStyle: {
                                width: 1,
                                shadowBlur: 0,
                                color: [
                                    [1, this.highlight]
                                ],
                            },
                        },
                        axisTick: {
                            show: true,
                            lineStyle: {
                                color: this.highlight,
                                width: 1,
                            },
                            length: -5,
                            splitNumber: 10,
                        },
                        splitLine: {
                            show: true,
                            length: -10,
                            lineStyle: {
                                color: this.highlight,
                            },
                        },
                        axisLabel: {
                            distance: -20,
                            textStyle: {
                                color: this.highlight,
                                fontSize: "14",
                                fontWeight: "bold",
                            },
                        },
                        pointer: {
                            show: 0,
                        },
                        detail: {
                            show: 0,
                        },
                    },
                    {
                        name: "低危",
                        type: "gauge",
                        center: ["50%", "50%"],
                        radius: "65%", // 1行3个
                        startAngle: 225,
                        endAngle: -45,
                        min: 0,
                        max: 100,
                        axisLine: {
                            show: true,
                            lineStyle: {
                                width: 16,
                                color: [
                                    [1, "rgba(255,255,255,.1)"]
                                ],
                            },
                        },
                        axisTick: {
                            show: 0,
                        },
                        splitLine: {
                            show: 0,
                        },
                        axisLabel: {
                            show: 0,
                        },
                        pointer: {
                            show: true,
                            length: "100%",
                        },
                        detail: {
                            show: true,
                            offsetCenter: [0, "100%"],
                            textStyle: {
                                fontSize: 20,
                                color: this.highlight,
                            },
                            formatter: ["{value} ", "{name|" + "低危" + "}"].join("\n"),
                            rich: {
                                name: {
                                    fontSize: 14,
                                    lineHeight: 30,
                                    color: this.highlight,
                                },
                            },
                        },
                        itemStyle: {
                            normal: {
                                color: this.highlight,
                            },
                        },
                        data: [{
                            value: "88",
                        }, ],
                    },
                ],
            });
            window.addEventListener("resize", () => {
                this.lowRisk.resize();
            });
        },
    },
};
</script>

<style>
.lowRisk {
    width: 100%;
    height: 100%;
}
</style>
