<template>
<a-table :columns="columns" :pagination="pagination" :data-source="tableData" bordered> </a-table>
</template>

<script>
export default {
    props: {
        tableData: {
            type: Array,
            default: () => {
                return [];
            },
        },
    },
    name: "tablsTable",
    data() {
        return {
            pagination: {
                //分页器配置
                defaultPageSize: 5,
            },
            columns: [{
                    title: "键",
                    dataIndex: "name",
                    key: "name",
                    width: "20%",
                    className: 'column-name',
                },
                {
                    title: "值",
                    dataIndex: "value",
                    key: "value",
                },
            ],
        };
    },
    mounted() {
        console.log(this.tableData)
    },
    watch: {
        tableData() {
            console.log(this.tableData)
        }
    }
};
</script>

<style lang="scss" scopet>
th.column-name,
td.column-name {
  text-align: center !important;
}
</style>
