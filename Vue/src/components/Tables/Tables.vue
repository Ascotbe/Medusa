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
      type: String | Function,
      default: 'key' | function () { }
    },
    showPagination: {//是否分页
      type: Boolean,
      default: false
    },
    showExpandedRowKeys: {//是否展开默认行
      type: Boolean,
      default: false
    },
    scrollTable: {
      type: Object,
      default: () => {
        return { x: 1600, y: 450 }
      }
    },
    ExpandedRowRenderCallback: {
      tyep: Function,
      default: () => {
        return function () { }
      }
    },
    ExpandIconCallback: {
      tyep: Function,
      default: () => {
        return function () { }
      }
    },
    showTotalDIY: {
      tyep: Function,
      default: () => {
        return function () { }
      }
    },
    size: {
      tyep: String,
      default: 'default'
    },
    rowSelection: {
      type: Object,
      default: () => {
        return undefined
      }
    },
    showHeader: {//显示表头
      type: Boolean,
      default: true
    },
    customRow: {
      tyep: Function,
      default: () => {
        return function () { }
      }
    }
  },
  data () {
    return {
      pagination: {
        showQuickJumper: true,
        position: 'bottom',
        defaultPageSize: 100,
        pageSizeOptions: ['100'],
        hideOnSinglePage: false,
        size: "small",
        showTotal: (total, range) => {
          const Dom = <span style="font-size:16px;line-height: 22px;" v-show={total == 0 ? false : true}><a-button type='link' icon='reload' v-on:click={this.reloadData}></a-button>共<span style="color:#51c51a;padding: 0 6px;">
            <span>{total}</span></span>条</span>
          const callback = this.showTotalDIY(Dom, total, range)
          if (callback) {
            return callback
          }
          else return Dom
        },
        // itemRender: (page, type, originalElement) => {
        //   console.log(page, type, originalElement)
        //   if (type === 'prev') {
        //     return <a>Previous</a>;
        //   } else if (type === 'next') {
        //     return <a>Next</a>;
        //   }
        //   return originalElement;
        // },
        total: 0
      },
      expandedRowKeys: []
    }
  },
  methods: {
    reloadData () {
      this.$emit('change', { ...this.pagination, current: this.pagination.current || 1, pageSize: this.pagination.pageSize || this.pagination.defaultPageSize })
    },
    handleChange (pagination, filters, sorter, { currentDataSource }) {
      this.$emit('change', pagination)
    },
    handleExpandedRowRender (record, index, indent, expanded) {
      const callback = this.ExpandedRowRenderCallback(record)
      return callback
    },
    handleFooter (currentPageData) {//废弃
      return <div style="text-align:left" v-show={this.total == 0 ? false : true}>总共<span style="color:#51c51a">{this.total}</span>条数据</div>
    },
    handleExpandedRowKeys () {//全部展开
      this.$nextTick(() => {
        this.expandedRowKeys = this.tableData.map((item, i) => (typeof (this.rowKey) === 'function') ? i : item[this.rowKey])
      })
    },
    handleExpandIcon (props) {
      const callback = this.ExpandIconCallback(props)
      return callback
    },
    handleCustomRow (record, index) {
      const callback = this.customRow(record, index)
      if (callback) {
        return callback
      }
    }
  },
  watch: {
    total: {
      handler: function (now, old) {
        this.pagination.total = now
      },
      deep: true
    },
    tableData: {
      handler: function (now, old) {
        if (this.showExpandedRowKeys) this.handleExpandedRowKeys()
        else this.expandedRowKeys = []
      },
      deep: true
    }
  },
  render: function (h) {
    const props = {
      columns: this.columns,
      dataSource: this.tableData,
      scroll: this.scrollTable,
      total: this.total,
      rowKey: this.rowKey,
      size: this.size,
      showHeader: this.showHeader,
      customRow: (record, index) => this.handleCustomRow(record, index),
      pagination: this.showPagination ? false : this.pagination,
    }
    const on = {
      change: (pagination, filters, sorter, { currentDataSource }) => this.handleChange(pagination, filters, sorter, { currentDataSource }),
    }
    //正常表格
    if (this.expandedRowKeys.length == 0 && !this.rowSelection) {
      return h('a-table', {
        props: props,
        on: on
      })
    }
    //选项表格
    else if (this.rowSelection) {
      return h('a-table', {
        props: {
          ...props,
          rowSelection: this.rowSelection,
        },
        on: on
      })
    }
    //展开表格
    else {
      return h('a-table', {
        props: {
          ...props,
          expandedRowKeys: this.expandedRowKeys,
          // footer: (currentPageData) => this.handleFooter(currentPageData),
          expandedRowRender: (record, index, indent, expanded) => this.handleExpandedRowRender(record, index, indent, expanded),
          expandIcon: (props) => this.handleExpandIcon(props),

        },
        on: {
          ...on,
          expandedRowsChange: (expandedRowKeys) => {
            this.expandedRowKeys = expandedRowKeys
          }
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
// ::v-deep .ant-table {
//   minheight: ;
// }
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