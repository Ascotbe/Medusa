<template>
<a-row :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 8, sm: 16, md: 24, lg: 32 },
    ]" style="background: #fff">
    <!--<a-col :xs="{ span: 12 }" :lg="{ offset: 14, span: 4 }">
            <a-select style="width: 100%" :options="options" placeholder="选择搜索字段" @change="handleChange">
            </a-select>
        </a-col>
        <a-col :xs="{ span: 12 }" :lg="{ span: 6 }">
            <a-input-search placeholder="搜索内容" enter-button @search="handleOnSearch" />
        </a-col>-->
    <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
        <a-table :columns="columns" :data-source="data" :pagination="pagination"> </a-table>
    </a-col>
</a-row>
</template>

<script>
export default {
    name: "portInformation",
    data() {
        return {
            pagination: {
                //分页器配置
                defaultPageSize: 5,
            },
            columns: [{
                    title: "创建时间",
                    dataIndex: "creation_time",
                    key: "creation_time",
                },
                {
                    title: "目标",
                    dataIndex: "domain",
                    key: "domain",
                },
                {
                    title: "IP",
                    dataIndex: "ip",
                    key: "ip",
                },
                {
                    title: "端口",
                    dataIndex: "port",
                    key: "port",
                },
            ],
            data: [],
            FBdata: [], //data的副本
        };
    },
    mounted() {
        this.handlePort_information();
    },
    methods: {
        handlePort_information() {
            let params = {
                token: localStorage.getItem("storeToken"),
                active_scan_id: this.$store.state.active_scan_id,
                // active_scan_id: "Soryu Asuka Langley",
            };
            this.$api.port_information(params).then((res) => {
                console.log(res);
                switch (res.code) {
                    case 200:
                        res.message.map((item) => {

                        });
                        for (let i = 0; i < res.message.length; i++) {
                            let data = {
                                key: i,
                                creation_time: this.$qj.QjUnixTimes(res.message[i].creation_time),
                                domain: res.message[i].domain,
                                ip: res.message[i].ip,
                                port: res.message[i].port,
                            };
                            this.FBdata.push(data);

                        }
                        this.data = this.FBdata;
                        console.log(this.data)
                        break;
                    case 404:
                        this.$message.error(res.message);
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
    },
};
</script>

<style lang="scss">
.portInformation-nav-header {
    font-size: 0.09rem;
    text-align: center;
}

.portInformation-nav-body {
    font-size: 0.07rem;
    text-align: center;
    height: 140px;

    .portInformation-nav-body-for {
        height: 20%;
    }

    .portInformation-nav-body-for:hover .portInformation-nav-body-for-hover {
        background: #2a4a69;
    }
}

.pagination {
    color: floralwhite !important;

    .ant-pagination-prev,
    .ant-pagination-next,
    .ant-pagination-item a {
        font-size: 0.07rem;
        color: floralwhite !important;
    }

    .ant-pagination-item-active a {
        font-size: 0.07rem;
        color: #1890ff !important;
    }
}
</style>
