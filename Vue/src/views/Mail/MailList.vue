<template>
    <transition name="show" mode="out-in">
      <div>
    <!-- <Card name="" :key="visable" :bodyStyle="bodyStyle">
        <template slot="extraCard">
        <a-button
            @click="visable?handleSearchPage():handleClose()"
            type="primary"
        >{{visable?'刷新':'返回'}}</a-button>
        </template> -->
        <Tables
          :loading='loading'
          :columns="columns"
          :tableData="data"
          :rowKey="(record,index)=>index"
          :scrollTable="{x:1000,y:400}"
          :total="total"
          @change="handleChange" />
        <!-- <Card :name="`邮件内容`" v-show="!visable" :bodyStyle="bodyStyle">
        <MarkdownPreview theme="oneDark" :initialValue="mailMessageShow" />
        </Card> -->
        <!-- <MarkdownPreview v-show="!visable" theme="oneDark" :initialValue="mailMessageShow" /> -->
    <!-- </Card> -->
    </div>
    </transition>
</template>

<script>
// import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/CTables.vue'
import { mapGetters } from 'vuex'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
// import { MarkdownPreview } from 'vue-meditor'

export default {
  mixins: [OverallMixins],
  components: {
    // Card,
    Tables,
    // MarkdownPreview
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token"
    })
  },
  data () {
    return {
      form: this.$form.createForm(this, { name: 'form' }),
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px',
        textAlign: 'left'
      },
      //邮件服务器 options
      thirdPartyOptions: [
        {
          label: '本地',
          value: '0'
        },
        {
          label: '第三方',
          value: '1'
        },
      ],
      total: 0,
      current: 1,
      columns: [
        {
          title: "邮件标题",
          dataIndex: "mail_title",
          ellipsis: true,
          width: 150,
          // align: 'center',
          customRender: (text) => this.QJBase64Decode(text)
        },
        // {
        //   title: "内容",
        //   dataIndex: "mail_message",
        //   ellipsis: true,
        //   width: 500,
        //   align: 'center',
        //   customRender: (text) => this.QJBase64Decode(text)
        // },
        // {
        //   title: "附件",
        //   dataIndex: "attachment",
        //   ellipsis: true,
        //   width: 120,
        //   align: 'center'
        // },
        {
          title: "发送人",
          dataIndex: "sender",
          ellipsis: true,
          width: 120,
          // align: 'center',
          customRender: (text) => this.QJBase64Decode(text)
        },
        // {
        //   title: "发送服务器",
        //   dataIndex: "forged_address",
        //   ellipsis: true,
        //   width: 150,
        //   // align: 'center',
        //   customRender: (text) => this.QJBase64Decode(text)

        // },
        // {
        //   title: "目标邮件发送的状态",
        //   dataIndex: "mail_status",
        //   ellipsis: true,
        //   width: 150,
        //   align: 'center'
        // },
        {
          title: "任务状态",
          dataIndex: "compilation_status",
          ellipsis: true,
          width: 150,
          // align: 'center',
          customRender: (text) => text == 1 ? <a-tag color="green">已完成</a-tag> : <a-tag color="blue">未完成</a-tag>

        },
        {
          title: '操作',
          dataIndex: "action",
          ellipsis: true,
          // align: 'center',
          width: 150,
          customRender: (text, record) => {
            const actions = <a onClick={
              () => {
                const _this = this
                _this.handleShow(record)
              }
            }>详情</a>
            return actions
          }
        }
      ],
      data: [],
      //邮件内容
      mailMessage: '',
      //不显示功能
      toolbars: {
        importmd: false,
        exportmd: false,
        fullscreen: false,
        theme: false,
        split: false,
        strong: false,
        overline: false,
        italic: false,
        h1: false,
        h2: false,
        h3: false,
        h4: false,
        h5: false,
        h6: false,
        hr: false,
        quote: false,
        ul: false,
        ol: false,
        pl: false,
        link: false,
        image: false,
        table: false,
        checked: false,
        notChecked: false,
        code: false,
        preview: false
      },
      //详情展示 true 为隐藏 false 展示
      visable: true,
      //详情内容表格
      columnsDetails: [
        {
          title: "邮件标题",
          dataIndex: "title",
          ellipsis: true,
          width: 150,
        //   align: 'center',
          customRender: (text) => this.QJBase64Decode(text)
        },
        {
          title: "附件",
          dataIndex: "attachment",
          ellipsis: true,
          width: 120,
        //   align: 'center',
          customRender: (text) => {
            const pattern = /\'/g
            const string = text.replace(pattern, '"')
            const addressee = JSON.parse(string)
            const dom = []
            for (const key in addressee) {
              dom.push(<a-tag color="green">{key}</a-tag>)
            }
            return dom
          }
        },
        {
          title: "收件人",
          dataIndex: "addressee",
          ellipsis: true,
          width: 150,
        //   align: 'center'
        },
        {
          title: "完成状态",
          dataIndex: "status",
          ellipsis: true,
          width: 150,
        //   align: 'center',
          customRender: (text) => text == 1 ? '成功' : text == 0 ? '失败' : ''
        },
      ],
      dataDetails: [

      ],
      totalDetails: 0,
      //邮件发送内容回显
      mailMessageShow: '',
      loading: false
    }
  },
  created () {
    const _this = this
    _this.handleSearchPage()
  },
  mounted () {
    // const _this = this
    // _this.$refs.MarkdownPro.split = false
  },
  methods: {
    //发送邮件
    handleSendFishingMail () {
      const _this = this
      this.form.validateFields((err, values) => {
        if (!err && _this.mailMessage != '') {
          const params = {
            token: _this.token,
            ...values,
            ..._this.$refs.attachment.handleGetFieldsValue(),
            mail_message: _this.mailMessage
          }
          _this.$api.send_fishing_mail(params).then(res => {
            if (res.code == 200) {
              this.$message.success(res.message)
              _this.handleSearchPage()
            }
            else this.$message.warn(res.message)
          })
        }
        else this.$message.warn('请输入必填项')
      })
    },
    //分页查询表格数据
    handleSearchPage () {
      const _this = this
      // const hide = _this.$message.loading('查询中...', 0)
      const params = {
        token: _this.token,
        number_of_pages: _this.current
      }
      this.loading = true
      _this.$api.malicious_mail_query(params)
        .then(res => {
          if (res.code == 200) {
            _this.data = res.message
            const total = {
              token: _this.token,
            }
            return _this.$api.statistics_malicious_email(total)
          }
          else {
            _this.$message.warn(res.message)
            _this.data = []
            _this.total = 0
          }
        })
        .finally(() => {
          this.loading = false
          // setTimeout(hide)
          // _this.$message.success('查询结束')
        })
        .then(res => {
          if (res?.code == 200) _this.total = res.message
          else {
            _this.$message.warn('分页统计数据查询失败')
            _this.total = 0
          }
        })
    },
    //分页change
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      this.handleSearchPage()
    },
    //返回列表页
    handleClose () {
      const _this = this
      _this.visable = true
    },
    //展示详情页
    handleShow (record) {
        this.$router.push({path:'/layout/MailDetail',query: {id: record.email_id}})
        return false

      const _this = this
      _this.visable = false
      const mailStatus = JSON.parse(record.mail_status)
      const data = []
      const menu = {}
      for (let key in mailStatus) {
        menu.addressee = key
        menu.status = mailStatus[key]
        menu.attachment = record.attachment
        menu.title = record.mail_title
        data.push(menu)
      }
      _this.dataDetails = data
      _this.mailMessageShow = "```" + `\n${this.QJBase64Decode(record.mail_message)}\n` + "```"
      // menu.title = record.mail_message

    }
  },
}

</script>

<style lang="scss" scoped>
.show-enter-active,
.show-leave-active {
  transition: all 0.5s;
}
.show-enter,
.show-leave-to {
  margin-left: 100px;
  // opacity: 0;
}
.show-enter-to,
.show-leave {
  margin-left: 0px;
  // opacity: 1;
}
</style>