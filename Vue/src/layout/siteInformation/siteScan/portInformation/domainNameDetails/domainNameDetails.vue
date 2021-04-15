<template>
<div class="domainNameDetails">
    <a-row style="margin:0" :gutter="[{ xs: 16, sm: 24, md: 32, lg: 40 },{xs: 16, sm: 24, md: 32, lg: 40 }]">
        <a-col :xs="{ span: 24}" :lg="{ span: 24}">
            <a-col :xs="{ span: 24}" :lg="{ span: 24}" class="domainNameDetails-search">
                <a-form-model :model="form" layout="inline" style="margin-left: 30px;">
                    <a-form-model-item label="添加目标" style="margin-left: 30px;">
                        <a-input v-model="form.url" placeholder="请输入目标网站地址（多个域名请使用XXX扫描）" />
                    </a-form-model-item>
                    <a-form-model-item>
                        <a-button style="margin-left: 30px;">提交</a-button>
                        <a-button style="margin-left: 30px;">XXXX扫描</a-button>
                    </a-form-model-item>
                    <a-form-model-item label="添加时间" style="margin-left: 30px;">
                        <a-date-picker @change="onChange" />
                    </a-form-model-item>
                    <a-form-model-item style="margin-left: 30px;">
                        <a-input-search placeholder="请输入搜索内容" enter-button @search="onSearch" />
                    </a-form-model-item>
                    <a-form-model-item>
                        <a-button style="margin-left: 30px;">中断任务</a-button>
                        <a-button style="margin-left: 30px;">导出报告</a-button>
                        <a-button style="margin-left: 30px;">删除任务</a-button>
                    </a-form-model-item>
                </a-form-model>
            </a-col>
            <a-col :xs="{ span: 24}" :lg="{ span: 24}" class="domainNameDetails-table">
                <a-table :row-selection="rowSelection" :columns="columns" :data-source="dataSearch" :pagination="pagination" :rowClassName="getrowClassName" :customHeaderRow="getcustomHeaderRow" :customRow="customRow">
                    <a slot="url" slot-scope="text">{{ text }}</a>

                    <span slot="action">
                        <a>中断任务</a>
                        <a-divider type="vertical" />
                        <a>查看报告</a>
                        <a-divider type="vertical" />
                        <a>删除任务</a>
                    </span>
                </a-table>
            </a-col>
        </a-col>
    </a-row>
</div>
</template>

<script>
const columns = [{
        title: '目标网站',
        dataIndex: 'url',
        ellipsis: true,
    },
    {
        title: '状态',
        dataIndex: 'state',
        ellipsis: true,
    },
    {
        title: '任务周期',
        dataIndex: 'taskCycle',
        ellipsis: true,
    },
    {
        title: '得分',
        dataIndex: 'grade',
        ellipsis: true,
    },
    {
        title: '创建时间',
        dataIndex: 'creationTime',
        ellipsis: true,
    },
    {
        title: '操作',
        dataIndex: 'operation',
        scopedSlots: {
            customRender: 'action'
        },
    },
];
const data = [{
        key: '1',
        url: 'baidu.com',
        state: 32,
        taskCycle: 'New York No. 1 Lake Park',
        grade: 32,
        creationTime: '2020-09-01',
    },
    {
        key: '2',
        url: 'ascotbe.com',
        state: 32,
        taskCycle: 'New York No. 1 Lake Park',
        grade: 32,
        creationTime: '2020-09-02',
    },
    {
        key: '3',
        url: 'John Brown',
        state: 32,
        taskCycle: 'New York No. 1 Lake Park',
        grade: 32,
        creationTime: '2020-09-01',
    },
    {
        key: '4',
        url: 'John Brown',
        state: 32,
        taskCycle: 'New York No. 1 Lake Park',
        grade: 32,
        creationTime: '2020-09-04',
    },
];
export default {
    name: 'domainNameDetails',
    data() {
        return {
            form: {
                url: '',
            },
            columns,
            data,
            dataSearch: [],
            rowSelection: {

            },
            pagination: {
                pageSize: 2
            },
            searchKey: '',
            changeKey: ''
        }
    },
    mounted() {
        this.dataSearch = this.data
    },
    methods: {
        onChange(date, dateString) { //假联查
            let Change = []
            this.changeKey = dateString
            console.log(this.changeKey);
            for (let i = 0; i < this.data.length; i++) {
                if (this.changeKey != '') {
                    if (this.data[i].creationTime == this.changeKey && this.data[i].url.indexOf(this.searchKey) != -1) {
                        Change.push(this.data[i])
                    }
                } else {
                    if (this.data[i].url.indexOf(this.searchKey) != -1) {
                        Change.push(this.data[i])
                    }
                }

            }
            this.dataSearch = Change
        },
        onSearch(value, event) { //假联查
            let Search = []
            this.searchKey = value
            console.log(this.searchKey);
            for (let i = 0; i < this.data.length; i++) {
                if (this.changeKey != '') {
                    if (this.data[i].url.indexOf(this.searchKey) != -1 && this.data[i].creationTime == this.changeKey) {
                        Search.push(this.data[i])
                    }
                } else {
                    if (this.data[i].url.indexOf(this.searchKey) != -1) {
                        Search.push(this.data[i])
                    }
                }
            }
            this.dataSearch = Search
        },
        getrowClassName(record, index) {
            console.log(record, index)
            let className = "light-row";
            if (index % 2 === 1) className = "dark-row";
            return className;

        },
        getcustomHeaderRow(column, index) {
            console.log(column, index)
            let className1 = ".ant-table-wrapper/deep/.ant-table-thead>tr>th";
            for (let i = 0; i < column.length; i++) {
                column[i].className = className1
            }

        },
        customRow(record) {
            return {
                on: {
                    mouseenter: (event) => {
                        console.log(event);
                    }
                }
            }
        }
    },
}
</script>

<style lang="scss">
.domainNameDetails {
    background: rgb(88, 119, 151);

    .domainNameDetails-search {
        margin-top: 50px;
        font-size: 14px;

        .ant-form /deep/.ant-form-item-label>label {
            color: #fff;
        }

        .ant-form /deep/.ant-btn {
            background: rgba(32, 181, 155, 1);
            color: #fff;
        }

        .ant-form /deep/.ant-input {
            background-color: rgba(42, 74, 105, 1);
            color: #fff;
        }
    }

    .domainNameDetails-table {}
}

.light-row {
    background: rgba(42, 74, 105, 1);
    color: #fff;
}

.dark-row {
    background: rgba(46, 64, 81, 1);
    color: #fff;
}

.hover-row {
    color: #000;
}

.ant-table-wrapper/deep/.ant-table-thead>tr>th {
    background: rgba(46, 64, 81, 1);
    color: #fff;
}

.ant-table-wrapper/deep/.ant-table-tbody>tr:hover:not(.ant-table-expanded-row):not(.ant-table-row-selected)>td {
    background: rgb(190, 190, 190);
    color: rgb(34, 34, 34);
}

.ant-table-wrapper/deep/.ant-table-tbody>tr.ant-table-row-selected td {
    background: rgb(255, 255, 255);
    color: rgb(34, 34, 34);
}
</style>
