<template>
<div class="selectProject">
    <a-row :gutter="[
        { xs: 8, sm: 16, md: 24, lg: 32 },
        { xs: 24, sm: 32, md: 40, lg: 48 },
      ]" class="selectProject_bg">
        <a-col :xs="{ span: 24 }">
            <a-table :columns="columns" :data-source="data" :expand="expand" bordered>
                <a-tabs slot="expandedRowRender" slot-scope="record" :default-active-key="record.request_method" @change="callback">
                    <a-tab-pane :key="record.request_method" :tab="record.request_method">
                        <tablsTable :tableData="record.PAndG"></tablsTable>
                    </a-tab-pane>
                    <a-tab-pane key="Cookie" tab="Cookie">
                        <tablsTable :tableData="record.Cookie"></tablsTable>
                    </a-tab-pane>
                    <a-tab-pane key="HTTP" tab="HTTP请求信息">
                        <tablsTable :tableData="record.haeder"></tablsTable>
                    </a-tab-pane>
                    <a-tab-pane key="Other" tab="其他信息">
                        <a-descriptions :column="NumberColumn">
                            <a-descriptions-item v-for="(item, i) in record.Other" :key="i" :label="item.name">
                                {{ item.value }}
                            </a-descriptions-item>
                        </a-descriptions>
                    </a-tab-pane>
                </a-tabs>
            </a-table>
        </a-col>
    </a-row>
</div>
</template>

<script>
import tablsTable from "../../../../components/tablsTable.vue";
export default {
    components: {
        tablsTable,
    },
    data() {
        return {
            NumberColumn: 1,
            PAndG: "Get",
            data: [],
            columns: [{
                    title: "创建时间",
                    dataIndex: "creation_time",
                    key: "creation_time",
                },
                {
                    title: "数据包内容",
                    dataIndex: "data_pack",
                    key: "data_pack",
                    ellipsis: true,
                },
                {
                    title: "真实地址",
                    dataIndex: "ip",
                    key: "ip",
                },
                {
                    title: "请求方式",
                    dataIndex: "request_method",
                    key: "request_method",
                },
            ],
            PAndGData: [],
        };
    },
    mounted() {
        this.handleQuery_script_project_data();
    },
    methods: {
        handleQuery_script_project_data() {
            if (this.$store.state.project_associated_file_name != "null") {
                let params = {
                    project_associated_file_name: this.$store.state
                        .project_associated_file_name,
                    token: localStorage.getItem("storeToken"),
                };
                let data = {};

                this.$api.query_script_project_data(params).then((res) => {
                    console.log(res);
                    for (let i = 0; i < res.message.length; i++) {
                        let PAndGData = [];
                        let haederData = [];
                        let Cookie = [];
                        let Other = [{
                                name: "访问地址",
                                value: res.message[i].full_url,
                            },
                            {
                                name: "IP地址",
                                value: res.message[i].ip,
                            },
                            {
                                name: "协议",
                                value: res.message[i].request_method,
                            },
                        ];

                        let pand = eval(
                            "(" + this.$qj.QJBase64Decode(res.message[i].data_pack) + ")"
                        );
                        for (let i in pand) {
                            let pandlist = {
                                key: i,
                                name: i,
                                value: pand[i],
                            };
                            PAndGData.push(pandlist);
                        }

                        let header = eval(
                            "(" + this.$qj.QJBase64Decode(res.message[i].headers) + ")"
                        );

                        for (let i in header) {
                            if (i == "Connection") {
                                let Cookielist = {
                                    key: i,
                                    name: i,
                                    value: header[i],
                                };
                                Cookie.push(Cookielist);
                            }
                            if (i == "User-Agent") {
                                let Otherlist = {
                                    name: "客户端",
                                    value: header[i],
                                };
                                Other.push(Otherlist);
                            }
                            let headerlist = {
                                key: i,
                                name: i,
                                value: header[i],
                            };
                            haederData.push(headerlist);
                        }
                        console.log(Other);
                        let data_pack = "";
                        if (this.$qj.QJBase64Decode(res.message[i].data_pack) == "{}") {
                            data_pack = "null";
                        } else {
                            data_pack = this.$qj.QJBase64Decode(res.message[i].data_pack);
                        }
                        console.log(data_pack)
                        data = {
                            key: i,
                            creation_time: this.$qj.QjUnixTimes(res.message[i].creation_time),
                            data_pack: data_pack,
                            ip: res.message[i].ip,
                            request_method: res.message[i].request_method,
                            PAndG: PAndGData,
                            haeder: haederData,
                            Cookie: Cookie,
                            Other: Other,
                        };
                        this.data.push(data);
                        console.log(this.data);
                    }
                });
            } else {
                this.$message.warning("请从项目管理进入,跳转站点扫描中...");
                this.$router.push("/layout/projectManagement");
            }
        },
        callback(key) {
            console.log(key);
        },
        expand(expanded, record) {
            console.log(expanded, record);
        },
    },
};
</script>

<style lang="scss" scoped>
.selectProject {
    margin: 0;
    padding: 35px 20px 0 20px;
    height: 100%;

    .selectProject_bg {
        min-height: 100%;
        background: #fff;
    }
}
</style>
