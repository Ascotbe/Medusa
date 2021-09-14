<template>
  <a-table
    :columns="columns"
    :data-source="tableData"
    :scroll="scrollTable"
    :pagination="pagination"
    :total="total"
    :rowKey="rowKey"
    @change="handleChange"
    :expandIcon="handleExpandIcon"
    :expandedRowKeys="expandedRowKeys"
  >
    <div slot="expandedRowRender" slot-scope="record">{{ record.vulnerability_description }}</div>
    <div slot="footer" style="text-align:left">
      总共
      <span style="color:#51c51a">{{total}}</span>条数据
    </div>
  </a-table>
</template>

<script>
export default {
  props: {
    columns: {
      type: Array,
      default: () => {
        return []
      }
    },
    tableData: {
      type: Array,
      default: () => {
        return []
      }
    },
    total: {
      type: Number,
      default: 0
    },
    rowKey: {
      type: String,
      default: 'key'
    },
    showExpandedRowKeys: {
      type: Boolean,
      default: false
    },
    scrollTable: {
      type: Object,
      default: () => {
        return { x: 1600, y: 400 }
      }
    }


  },
  data () {
    return {
      pagination: {
        position: 'bottom',
        defaultPageSize: 100,
        pageSizeOptions: ['100'],
        hideOnSinglePage: true,
        total: 0
      },
      expandedRowKeys: []
    }
  },
  methods: {
    handleChange (pagination, filters, sorter, { currentDataSource }) {
      this.$emit('change', pagination)
    },
    handleExpandIcon () {

    },
    handleExpandedRowKeys () {
      this.expandedRowKeys = this.tableData.map(item => item.vulnerability_number)
    }
  },
  watch: {
    total: {
      handler: function (now, old) {
        const _this = this
        _this.pagination.total = now
      },
      deep: true
    },
    tableData: {
      handler: function (now, old) {
        const _this = this
        if (_this.showExpandedRowKeys) _this.handleExpandedRowKeys()
        else _this.expandedRowKeys = []
      },
      deep: true
    }
  }
}
</script>

<style lang="scss" scoped>
/*定义整体的宽度*/
::v-deep .ant-table-body::-webkit-scrollbar {
  height: 5px;
  width: 5px;
}

/*定义滚动条轨道*/
::v-deep .ant-table-body::-webkit-scrollbar-track {
  border-radius: 2px;
}

/*定义滑块*/
::v-deep .ant-table-body::-webkit-scrollbar-thumb {
  border-radius: 2px;
  background: rgba(0, 255, 42, 0.5);
}
</style>