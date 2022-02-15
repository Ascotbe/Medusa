<template>
  <!-- <a-row class="attachment" > -->
    <a-form :form="form">
      <a-col :xs='24' :lg='12'>
      <a-form-item label="附件" >
        <a-select
          :labelInValue="true"
          v-decorator="[
        'attachment',
        { rules: [{ required: false, message: 'attachment Cannot be empty' }] }]"
          :mode="`multiple`"
          :dropdownRender="handleDropdownRender"
          @focus="handleFocus"
          @deselect="handleDeselect"
          :getPopupContainer="triggerNode => triggerNode.parentNode"
        ></a-select>

        <!-- <a-upload
            name="file"
            @change="handleHeaderPhoto"
            :customRequest="handleCustomRequest"
            :file-list="fileList"
          >
            <a-button>
              <a-icon type="upload" />修改头像
            </a-button>
        </a-upload>-->
        <!-- <a-input
          v-decorator="[
            'attachment',
            { rules: [{ required: true, message: 'attachment Cannot be empty' }] }
          ]"
          
        ></a-input>-->
      </a-form-item>
      </a-col>
       <a-col :xs='24' :lg='12'>
      <a-form-item label="附件上传">
        <a-upload-dragger
          name="file"
          :multiple="false"
          :customRequest="handleCustomRequest"
          @change="handleAttachment"
        >
          <p class="ant-upload-drag-icon">
            <a-icon type="inbox" />
          </p>
          <p class="ant-upload-text">Click or drag file to this area to upload</p>
        </a-upload-dragger>
      </a-form-item>
       </a-col>
    </a-form>
  <!-- </a-row> -->
</template>

<script>
import Tables from '@/components/Tables/Tables.vue'
import { mapGetters } from 'vuex'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'

export default {
  mixins: [OverallMixins],
  components: {
    Tables,
  },
  data () {
    return {
      form: this.$form.createForm(this, { name: 'form' }),
      // modalForm: this.$form.createForm(this, { name: 'modalForm' }),
      visable: false,
      columns: [
        {
          dataIndex: "file_name",
          ellipsis: true,
          // align: 'center',
          customRender: (text) => this.QJBase64Decode(text)
        },
      ],
      selectedRows: [],//选中的表格具体数据
      rowSelection: {
        selectedRowKeys: [],//选中的表格key值
        onChange: (selectedRowKeys, selectedRows) => {//表格选中回调
          const _this = this
          _this.rowSelection.selectedRowKeys = selectedRowKeys
          _this.selectedRows = selectedRows
          // const tag = selectedRows.map(item => {
          //   const tag = <a-tag color="cyan">{item.file_name}</a-tag>
          //   return tag
          // })
          const tag = selectedRows.map((item, i) => {
            return {
              label: <a-tag color="cyan">{_this.QJBase64Decode(item.file_name)}</a-tag>,
              key: item.document_real_name
            }
          })
          _this.form.setFieldsValue({ attachment: tag })
        },
      },
      data: [],
      pageNo: 1,//页码
      fileList: []
      // selectAllTitle: '全选'//按钮名字
    }
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    }),
    selectAllTitle () {
      if (this.data.length == this.rowSelection.selectedRowKeys.length) {
        return 'delete'
      }
      else return 'plus'
    }
  },
  methods: {
    //获取焦点回调
    handleFocus () {
      const _this = this
      // _this.visable = true
      _this.handleSearchPage(1)
      // _this.$nextTick(() => {
      //   _this.$refs.input.focus()
      // })
    },
    //关闭浮框
    handleClose () {
      this.visable = false
    },
    //分页查询
    handleSearchPage (pageNo) {
      const _this = this
      const params = {
        token: _this.token,
        number_of_pages: pageNo
      }
      _this.$api.email_attachment_query(params)
        .then((res) => {
          if (res.code == 200) {
            _this.data = res.message
          }
          else {
            _this.$message.warn(res.message)
            _this.data = []

          }
        })
    },
    //全选\反选
    handleSelectAll () {
      const _this = this
      const [list, record] = [[], []]
      let tag = []
      if (_this.data.length != _this.rowSelection.selectedRowKeys.length) {
        tag = _this.data.map((item, i) => {
          list.push(item.document_real_name)
          record.push(item)
          return {
            label: <a-tag color="cyan">{_this.QJBase64Decode(item.file_name)}</a-tag>,
            key: item.document_real_name
          }
        })
      }
      _this.rowSelection.selectedRowKeys = list
      _this.selectedRows = record
      _this.form.setFieldsValue({ attachment: tag })
    },
    handleDropdownRender (menuNode) {
      // const menu = menuNode
      // <a-form form={_this.modalForm} labelCol={{ span: 0 }} wrapper-col={{ lg: { span: 24, offset: 0 } }}>
      //       <a-form-item>
      //         <a-input decorator="['attachment']" ref="input">
      //           <a-icon slot="addonAfter" type="close" onClick={_this.handleClose} />
      //         </a-input>
      //       </a-form-item>
      //     </a-form>
      const _this = this

      return (
        <div onMousedown={(e) => {
          e.preventDefault()
        }}>
          <a-row gutter={[0, 0]} class="modal" ref="modal">
            <a-col
              style="box-shadow: 0 2px 8px rgb(0 0 0 / 15%);"
              xs={{ span: 24, offset: 0 }}
              lg={{ span: 24, offset: 0 }}
              class="modal_input"
            >
              <Tables
                showTotalDIY={(Dom, total, range) => _this.handleShowTotal(Dom, total, range)}
                scrollTable={{ x: '100%', y: 250 }}
                rowSelection={_this.rowSelection}
                columns={_this.columns}
                tableData={_this.data}
                showHeader={false}
                rowKey={(record, index) => record.document_real_name}
                size="small"
              />
            </a-col>
          </a-row >
        </div>
      )
    },
    //回调分页
    handleShowTotal (Dom, total, range) {
      const _this = this
      const page = <span style="display: flex;align-items: center;padding-left:3px;font-size:12px" v-show={total == 0 ? false : true}>共<span style="color:#51c51a;padding:0 3px 0 3px"><a-statistic value={total} valueStyle={{ color: '#51c51a' }} >
      </a-statistic></span>条</span>
      const btn = <div style="display: flex;align-items: center;height: 100%;">
        <a-button type="primary" size="small" v-on:click={() => { _this.handleSelectAll() }} icon={_this.selectAllTitle}></a-button>
        {page}
      </div>
      return btn
    },
    //文本框删除时回调
    handleDeselect (value, option) {
      const _this = this
      _this.rowSelection.selectedRowKeys.map((item, i) => {
        if (item == value.key) {
          _this.rowSelection.selectedRowKeys.splice(i, 1)
          _this.selectedRows.splice(i, 1)
          return
        }
      })
      // console.log(_this.rowSelection.selectedRowKeys, _this.selectedRows)
    },
    //返回选定的值
    handleGetFieldsValue () {
      const _this = this
      const Obj = {}
      _this.selectedRows.map(item => {
        const file_name = _this.QJBase64Decode(item.file_name)
        Obj[file_name] = item.document_real_name
      })
      // this.$emit('change', returnArr)

      return { attachment: Obj }
    },
    //给父组件的校验方法 返回true 或者 false
    handleValidateFields () {
      let flag = false
      this.form.validateFields((err) => {
        if (!err) {
          flag = true
        }
      })
      return flag
    },
    //通过覆盖默认的上传行为，可以自定义自己的上传实现
    handleCustomRequest (file) {
      const _this = this
      const params = new FormData();
      params.append("file", file.file);
      const progress = {
        percent: 0,
      };
      const intervalId = setInterval(() => {
        if (progress.percent < 100) {
          progress.percent += 25;
          file.onProgress(progress);
        } else {
          clearInterval(intervalId);
          _this.$api.upload_mail_attachment(params)
            .then(res => {
              if (res.code == 200) {
                file.onSuccess();
                _this.fileList = [];
                _this.$message.success("附件上传成功");
              } else {
                _this.$message.error(res.message);
                file.onError();
                _this.fileList = [];

              }
            })
            .catch(err => {
              file.onError();
              _this.fileList = [];
            })

        }
      }, 100);
    },
    //文件状态改变的回调，返回为：
    // {
    //   file: { /* ... */ },
    //   fileList: [ /* ... */ ],
    //   event: { /* ... */ },
    // }
    handleAttachment (info) {
      let fileList = [...info.fileList];
      this.fileList = fileList;
    },

  }
}
</script>

<style lang="less" scoped>
.attachment {
  display: inline-block;
  width: 100%;
}
// .modal {
//   position: relative;
//   /* width: 100%; */
//   top: -64px;
//   background: rgba(0, 0, 0, 0);
// }
// .modal_input {
//   // border: 1px solid #e8e8e8;
//   font-size: 14px;
//   // line-height: 1.5;
//   // text-align: left;
//   list-style: none;
//   background-color: #fff;
//   background-clip: padding-box;
//   border: 1px solid #fff;
//   border-radius: 4px;
//   outline: none;
//   // box-shadow: 0 2px 8px rgb(0 0 0 / 15%);
// }
.modal {
  width: 100%;
  height: 100%;
}
.modal_input {
  // border: 1px solid #e8e8e8;
  font-size: 14px;
  // line-height: 1.5;
  // text-align: left;
  list-style: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #fff;
  border-radius: 4px;
  outline: none;
  // box-shadow: 0 2px 8px rgb(0 0 0 / 15%);
}
.modal /deep/ .ant-input {
  border: 0;
  border-bottom: 1px solid #d9d9d9;
}

.modal /deep/ .ant-input-group-addon {
  border: 0;
  border-bottom: 1px solid #d9d9d9;
}
</style>