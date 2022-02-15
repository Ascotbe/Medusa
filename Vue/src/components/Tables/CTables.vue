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
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      pagination: {
        current: 1,
        showQuickJumper: true,
        position: 'bottom',
        defaultPageSize: 100,
        pageSizeOptions: ['100'],
        hideOnSinglePage: false,
        showTotal: total => (<span><a-button type='link' icon='reload' v-on:click={this.reloadData}></a-button>共<span style="color:#51c51a;padding: 0 6px;">{total}</span>条</span>),
        // size: "small",
        total: 0
      },
      expandedRowKeys: []
    }
  },
  methods: {
    reloadData() {
      this.$emit('change', {...this.pagination,current: this.pagination.current || 1,pageSize: this.pagination.pageSize || this.pagination.defaultPageSize})
    },
    handleChange (pagination, filters, sorter, { currentDataSource }) {
      this.pagination.current = pagination.current
      this.pagination.pageSize = pagination.pageSize
      this.$emit('change', pagination)
    },
    handleExpandedRowRender (record, index, indent, expanded) {
      const _this = this
      const callback = _this.ExpandedRowRenderCallback(record)
      return callback
    },
    handleFooter (currentPageData) {//废弃
      const _this = this
      return <div style="text-align:left" v-show={_this.total == 0 ? false : true}>总共<span style="color:#51c51a">{_this.total}</span>条数据</div>
    },
    handleExpandedRowKeys () {//全部展开
      const _this = this
      _this.$nextTick(() => {
        _this.expandedRowKeys = _this.tableData.map((item, i) => (typeof (_this.rowKey) === 'function') ? i : item[_this.rowKey])
      })
    },
    handleExpandIcon (props) {
      const _this = this
      const callback = _this.ExpandIconCallback(props)
      return callback
    },
    handleCustomRow (record, index) {
      const _this = this
      const callback = _this.customRow(record, index)
      if (callback) {
        return callback
      }
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
  },
  render (h) {
    let propsOptions = {
          loading: this.loading,
          columns: this.columns,
          dataSource: this.tableData,
          scroll: this.scrollTable,
          pagination: this.showPagination ? false : this.pagination,
          total: this.total,
          rowKey: this.rowKey,
          size: this.size,
          showHeader: this.showHeader,
          customRow: (record, index) => this.handleCustomRow(record, index)
        }
    let onOptions  = {
          change: (pagination, filters, sorter, { currentDataSource }) => this.handleChange(pagination, filters, sorter, { currentDataSource })
        }
    //正常表格
    if (this.expandedRowKeys.length == 0 && !this.rowSelection) {
      return h('a-table', {
        props: {
          ...propsOptions
        },
        on: {
          ...onOptions
        }
      })
    }else if (this.rowSelection) {//选项表格
      return h('a-table', {
        props: {
         ...propsOptions,
          rowSelection: this.rowSelection
        },
        on: {
          ...onOptions
        }
      })
    }else { //展开表格
      return h('a-table', {
        props: {
          ...propsOptions,
          expandedRowKeys: this.expandedRowKeys,
          // footer: (currentPageData) => _this.handleFooter(currentPageData),
          expandedRowRender: (record, index, indent, expanded) => this.handleExpandedRowRender(record, index, indent, expanded),
          expandIcon: (props) => this.handleExpandIcon(props),
        },
        on: {
          ...onOptions,
          expandedRowsChange: expandedRowKeys => {
            this.expandedRowKeys = expandedRowKeys
          }
        }
      })
    }
  }
}
</script>