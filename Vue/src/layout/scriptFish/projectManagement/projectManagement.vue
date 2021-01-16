<template>
<div class="projectManagement">
    <a-row :gutter="[
        { xs: 8, sm: 16, md: 24, xs: 8 },
        { xs: 8, sm: 16, md: 24, lg: 32 },
      ]" class="projectManagement_bg">
        <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
            <a-table :columns="columns" :data-source="data" :pagination="pagination" @change="handleChangePage">
                <span slot="capacity" slot-scope="text, record">
                    <a-progress type="line" :status="record.status" :stroke-color="record.color" :percent="record.capacity" :format="(percent) => `${record.capacity} %`">
                    </a-progress>
                </span>
                <span slot="action" slot-scope="text, record">
                    <a @click="handleGetTableSerch(record.key)">查询</a>
                    <a-divider type="vertical" />
                    <a @click="handleGetDetails(record.key)">修改</a>
                </span>
            </a-table>
        </a-col>
    </a-row>
</div>
</template>

<script>
export default {
    data() {
        return {
            pagination: {
                //分页器配置
                defaultPageSize: 10,
            },
            columns: [{
                    title: "项目名",
                    dataIndex: "project_name",
                    key: "project_name",
                },
                {
                    title: "文件名",
                    dataIndex: "file_name",
                    key: "file_name",
                },
                {
                    title: "创建时间",
                    dataIndex: "creation_time",
                    key: "creation_time",
                },
                {
                    title: "容量",
                    dataIndex: "capacity",
                    key: "capacity",
                    scopedSlots: {
                        customRender: "capacity",
                    },
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
            file_nameList: [],
            Script_Project_Data: [], //每个data具体的内容
        };
    },
    mounted() {
        this.handleQuery_Script_Project();
    },
    methods: {
        handleQuery_Script_Project() {
            let params = {
                token: localStorage.getItem("storeToken"),
            };
            this.$api.query_script_project(params).then((res) => {
                console.log(res);
                switch (res.code) {
                    case 200:
                        res.message.map((item) => {
                            let data = {
                                key: item.file_name,
                                project_name: item.project_name,
                                file_name: item.file_name,
                                creation_time: this.$qj.QjUnixTimes(item.creation_time),
                                capacity: 0,
                                status: "normal",
                                color: {
                                    "0%": "#108ee9",
                                    "100%": "#87d068",
                                },
                            };
                            this.FBdata.push(data);
                        });
                        this.data = this.FBdata;
                        let pagination = {
                            current: 1,
                            defaultPageSize: this.pagination.defaultPageSize,
                        };
                        let currentDataSource = this.data;
                        this.handleChangePage(pagination, 0, 0, {
                            currentDataSource,
                        });
                        break;

                    case 403:
                        this.$message.error(res.message);
                        break;
                    case 169:
                        this.$message.error(res.message);
                        break;
                    case 500:
                        this.$message.error(res.message);
                        break;
                }
            });
        },
        handleQuery_Script_Project_Data() {
            this.file_nameList.map((i) => {
                let params = {
                    project_associated_file_name: i.file_name,
                    token: localStorage.getItem("storeToken"),
                };

                this.$api.query_script_project_data(params).then((res) => {
                    console.log(res);
                    switch (res.code) {
                        case 200:
                            this.FBdata.map((item) => {
                                if (item.key == i.file_name) {
                                    if (res.message.length > 100) {
                                        item.status = "exception";
                                        item.color = {
                                            "0%": "#f15a22",
                                            "100%": "#aa2116",
                                        };
                                    }
                                    if ((res.message == "null")) {
                                        console.log("res.message==null")
                                        item.capacity = 0;
                                    } else {
                                        item.capacity = res.message.length;
                                    }
                                }
                            });
                            this.data = this.FBdata;
                            console.log(this.data);
                            break;

                        case 403:
                            this.$message.error(res.message);
                            break;
                        case 404:
                            this.$message.error(res.message);
                            break;
                        case 169:
                            this.$message.error(res.message);
                            break;
                        case 500:
                            this.$message.error(res.message);
                            break;
                    }
                });
            });
        },
        handleChangePage(pagination, filters, sorter, {
            currentDataSource
        }) {
            console.log({
                currentDataSource,
            });
            let allLength = currentDataSource.length; //总长度
            let current = pagination.current; //单前页数
            let defaultPageSize = pagination.defaultPageSize; //每页多少数据行
            let pageSize = Math.ceil(allLength / defaultPageSize); //最后一页页码 或者一共页数
            let data = [];
            this.file_nameList = [];
            // console.log(pageSize);
            if (current == pageSize) {
                let val = (pageSize - 1) * defaultPageSize; // 单前页的有多少行数据
                for (let i = val; i < allLength; i++) {
                    console.log(i);
                    data = {
                        file_name: currentDataSource[i].file_name,
                    };
                    this.file_nameList.push(data);
                }
            } else {
                let val = (current - 1) * defaultPageSize;
                for (let i = val; i < val + defaultPageSize; i++) {
                    console.log(i);
                    data = {
                        file_name: currentDataSource[i].file_name,
                    };
                    this.file_nameList.push(data);
                }
            }
            this.handleQuery_Script_Project_Data();
        },

        handleGetTableSerch(key) {
            this.$store.commit("project_associated_file_name", key);
            this.$router.push("/layout/projectManagement/selectProject");
        },
        handleGetDetails(key) {
            this.$store.commit("project_associated_file_name", key);
            this.$router.push("/layout/projectManagement/projectDetails");
        }
    },
};
</script>

<style lang="scss" scoped>
.projectManagement {
    margin: 0;
    padding: 20px;
    padding-top: 30px;
    height: 100%;

    .projectManagement_bg {
        min-height: 100%;
        background: #fff;
    }
}

.projectManagement /deep/.ant-table {
    height: 650px;
}
</style>
