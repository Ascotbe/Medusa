mediumRisk
<template>
<div id="mediumRisk" class="mediumRisk"></div>
</template>

<script>
export default {
    name: 'mediumRisk',
    data() {
        return {
            mediumRisk: {},
            highlight: "#FF8000", //#03b7c9
        };
    },
    mounted() {
        let _this = this;
        _this.fnDrawLine();
        window.onresize = () => {
            _this.mediumRisk.resize();
        };
    },
    methods: {
        fnDrawLine() {
            // 基于准备好的dom，初始化echarts实例
            this.mediumRisk = this.$echarts.init(
                document.getElementById("mediumRisk")
            );
            this.mediumRisk.setOption({
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
                        name: "中危",
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
                            formatter: ["{value} ", "{name|" + "中危" + "}"].join("\n"),
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
                this.mediumRisk.resize();
            });
        },
    },
};
</script>

<style>
.mediumRisk {
    width: 100%;
    height: 100%;
}
</style>
