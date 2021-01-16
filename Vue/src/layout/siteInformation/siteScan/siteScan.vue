<template>
<a-row :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 4, sm: 8, md: 16, lg: 24 },
    ]" class="siteScan">
    <a-col :xs="{ span: 24 }">
        <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="safetyOverview-title">安全总览:</a-col>
        <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
            <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="safetyOverview-nav">
                <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="safetyOverview-nav-header">
                    <a-col :xs="{ span: 8 }" :lg="{ span: 4 }">richhc.com</a-col>
                    <a-col :xs="{ span: 16 }" :lg="{ span: 12 }">2020.03.12 16:15:06---1010.03.13 16:15:06</a-col>
                    <a-col :xs="{ span: 8 }" :lg="{ span: 3 }">得分: 100</a-col>
                    <a-col :xs="{ span: 8 }" :lg="{ span: 3 }">非周期任务</a-col>
                    <a-col :xs="{ span: 8 }" :lg="{ span: 2 }">导出报告</a-col>
                </a-col>
                <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="safetyOverview-nav-body">
                    <a-col :xs="{ span: 24 }" :lg="{ span: 8 }" class="safetyOverview-nav-body-risk">
                        <hisghtRisk></hisghtRisk>
                    </a-col>
                    <a-col :xs="{ span: 24 }" :lg="{ span: 8 }" class="safetyOverview-nav-body-risk">
                        <mediumRisk></mediumRisk>
                    </a-col>
                    <a-col :xs="{ span: 24 }" :lg="{ span: 8 }" class="safetyOverview-nav-body-risk">
                        <lowRisk></lowRisk>
                    </a-col>
                </a-col>
            </a-col>
        </a-col>
        <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
            <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="tabs">
                <a-tabs default-active-key="1" @change="handleCallback">
                    <a-tab-pane key="1" tab="端口信息">
                        <component :is="port_information"></component>
                    </a-tab-pane>
                    <a-tab-pane key="2" tab="子域名列表" force-render>
                        Content of Tab Pane 2
                    </a-tab-pane>
                </a-tabs>
            </a-col>
        </a-col>
        <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="vulnerabilityDetails_title">漏洞详情:
        </a-col>
        <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
            <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="vulnerabilityDetails_nav">
                <a-col :xs="{ span: 24 }" :lg="{ span: 24 }" class="vulnerabilityDetails_nav_lv">
                    威胁等级:
                    <a-checkbox-group @change="handleRiskOnChange" v-model="plainOptions">
                        <a-checkbox value="高危">高危</a-checkbox>
                        <a-checkbox value="中危">中危</a-checkbox>
                        <a-checkbox value="低危">低危</a-checkbox>
                    </a-checkbox-group>
                </a-col>
                <a-col :xs="{ span: 24 }" :sm="{ span: 10 }" :lg="{ span: 8 }" class="vulnerabilityDetails_nav_tag">
                    <a-col :xs="{ span: 8 }" :lg="{ span: 8 }" class="vulnerabilityDetails_nav_tag_hight">高危:{{ HightRisk }}</a-col>
                    <a-col :xs="{ span: 8 }" :lg="{ span: 8 }" class="vulnerabilityDetails_nav_tag_medium">中危:{{ MediumRisk }}</a-col>
                    <a-col :xs="{ span: 8 }" :lg="{ span: 8 }" class="vulnerabilityDetails_nav_tag_low">低危:{{ LowRisk }}</a-col>
                </a-col>
                <!--
                <a-col :xs="{ span: 24 }" :sm="{ span: 14 }" :lg="{ span: 12, offset: 4 }" class="vulnerabilityDetails_nav_tag">
                    <a-radio-group v-model="ScreenValue" @change="handleScreenOnChange">
                        <a-radio-button value="all"> 全部 </a-radio-button>
                        <a-radio-button value="repaired"> 待修复 </a-radio-button>
                        <a-radio-button value="fixed"> 已修复 </a-radio-button>
                        <a-radio-button value="Ignored"> 已忽略 </a-radio-button>
                    </a-radio-group>
                </a-col>
                -->
                <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
                    <a-table :columns="columns" :data-source="data" :pagination="pagination">
                        <span slot="action" slot-scope="text, record">
                            <a @click="handleGetTableSerch(record.key)">查询</a>
                        </span>
                    </a-table>
                </a-col>
            </a-col>
        </a-col>
    </a-col>
</a-row>
</template>

<script>
import hisghtRisk from "./risk/hightRisk";
import mediumRisk from "./risk/mediumRisk";
import lowRisk from "./risk/lowRisk";
import port_information from "./portInformation/portInformation.vue";
export default {
    name: "siteScan",
    components: {
        hisghtRisk,
        mediumRisk,
        lowRisk,
        port_information,
    },
    data() {
        return {
            pagination: {
                //分页器配置
                defaultPageSize: 5,
            },
            ScreenValue: "all",
            port_information: "port_information",
            columns: [{
                    title: "目标URL",
                    dataIndex: "url",
                    key: "url",
                },
                {
                    title: "威胁等级",
                    dataIndex: "rank",
                    key: "rank",
                },
                {
                    title: "漏洞名称",
                    dataIndex: "name",
                    key: "name",
                },
                {
                    title: "操作",
                    key: "action",
                    scopedSlots: {
                        customRender: "action",
                    },
                },
            ],
            data: [],
            FBdata: [], //data的副本
            plainOptions: ["高危", "中危", "低危"],
            HightRisk: 0, //高危数量
            MediumRisk: 0,
            LowRisk: 0,
        };
    },
    mounted() {
        this.handleGetImfomation_query();
    },
    methods: {
        handleGetImfomation_query() {
            console.log(this.$store.state.active_scan_id);
            if (this.$store.state.active_scan_id != "null") {
                let params = {
                    token: localStorage.getItem("storeToken"),
                    active_scan_id: this.$store.state.active_scan_id,
                };
                this.$api.imfomation_query(params).then((res) => {
                    console.log(res);
                    switch (res.code) {
                        case 200:
                            res.message.map((item) => {
                                let data = {
                                    key: item.scan_info_id,
                                    url: item.url,
                                    rank: item.rank,
                                    name: item.name,
                                };
                                this.FBdata.push(data);
                            });
                            this.FBdata.map((item) => {
                                switch (item.rank) {
                                    case "高危":
                                        this.HightRisk++;
                                        break;
                                    case "中危":
                                        this.MediumRisk++;
                                        break;
                                    case "低危":
                                        this.LowRisk++;
                                        break;
                                }
                            });
                            this.data = this.FBdata;

                            break;
                        case 404:
                            this.$message.error("数据库炸了BOOM~");
                            break;
                        case 403:
                            this.$message.error("小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧");
                            break;
                        case 169:
                            this.$message.error("莎酱被玩坏啦(>^ω^<)喵");
                            break;
                        case 500:
                            this.$message.error("请使用Post请求");
                            break;
                    }
                });
            } else {
                this.$message.warning("请从站点扫描进入,跳转站点扫描中...");
                this.$router.push("/layout/siteInformation");
            }
        },
        handleCallback(key) {
            console.log(key);
        },
        handleRiskOnChange(checkedValues) {
            console.log(checkedValues);
            let data = [];
            this.FBdata.map((item) => {
                checkedValues.map((i) => {
                    if (item.rank == i) {
                        data.push(item);
                    }
                });
            });
            this.data = data;
        },

        handleGetTableSerch(e) {
            this.$store.commit("scan_info_id", e);
            if (Math.round(Math.random() * 10) == 1) {
                this.$router.push(
                    "/layout/siteInformation/siteScan/vulnerabilityDetails2"
                );
            } else {
                this.$router.push(
                    "/layout/siteInformation/siteScan/vulnerabilityDetails"
                );
            }
        },
    },
};
</script>

<style lang="scss" scoped>
$background: #fff;
$color: #51c51a;

.siteScan {
    margin: 0;
    padding: 20px;
    padding-top: 0;

    // .safetyOverview-title {
    //     min-width: 60px;
    //     padding: 10px;
    //     color: $color;
    //     border-top-left-radius: 5px;
    //     border-top-right-radius: 5px;
    //     text-align: center;
    //     background: $background;
    //     margin-right: 20px;
    //     font-size: 16px;
    // }
    .safetyOverview-title,
    .vulnerabilityDetails_title {
        font-size: 18px;
        color: $color;
    }

    .safetyOverview-nav,
    .tabs,
    .vulnerabilityDetails_nav {
        min-width: 280px;
        padding: 10px;
        color: $color;
        border-radius: 15px;
        text-align: left;
        background: $background;
        font-size: 14px;

        .safetyOverview-nav-header {
            color: $color;
            font-size: 14px;
            border-bottom: 1px solid #ccc;
        }

        .portInformation-nav-header {
            font-size: 14px;
            text-align: center;
        }

        .safetyOverview-nav-body {
            background: $background;
            min-height: 210px;

            .safetyOverview-nav-body-risk {
                min-height: 190px;
                height: 1rem;
            }
        }

        .vulnerabilityDetails_nav_lv {
            border-bottom: 1px solid #ccc;
        }

        .vulnerabilityDetails_nav_tag {
            font-size: 16px;

            .vulnerabilityDetails_nav_tag_hight {
                color: #ff6347;
            }

            .vulnerabilityDetails_nav_tag_low {
                color: #03b7c9;
            }

            .vulnerabilityDetails_nav_tag_medium {
                color: #ff8000;
            }
        }
    }

    .safetyOverview-nav:hover,
    .tabs:hover,
    .vulnerabilityDetails_nav:hover {
        box-shadow: 10px 10px 5px #888888;
        /*设置阴影,可以自定义参数*/
        -webkit-box-shadow: 10px 10px 5px #888888;
        -o-box-shadow: 10px 10px 5px #888888;
        -moz-box-shadow: 10px 10px 5px #888888;
    }
}
</style>
