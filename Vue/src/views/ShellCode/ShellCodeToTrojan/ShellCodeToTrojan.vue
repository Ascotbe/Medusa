<template>
  <a-row
    type="flex"
    style="height:100%"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :xs="24" :lg="8">
      <Card :name="''" :bodyStyle="bodyStyle">
        <a-form
          :form="form"
          :labelCol="{xs:8,lg:6}"
          :wrapper-col="{xs:{span: 15, offset: 1},lg:{span: 17, offset: 1}}"
        >
          <a-form-item label="项目名称">
            <a-input
              clearable
              v-decorator="['shellcode_name',{ rules: [{ required: true, message: 'ShellcodeName Cannot be empty' }] }]">
            </a-input>
          </a-form-item>
          <a-form-item label="插件名称">
            <a-select
              :options="pluginOptions"
              v-decorator="['plugin',{ rules: [{ required: true, message: 'Plugin Cannot be empty' }] }]"></a-select>
          </a-form-item>
          <a-form-item label="生成类型">
            <a-select
              :options="shellCodeTypeOptions"
              v-decorator="[
            'shellcode_type',
            { rules: [{ required: true, message: 'ShellCodeType Cannot be empty' }] }
          ]"
            ></a-select>
          </a-form-item>
          <a-form-item label="生成位数">
            <a-select
              :options="ShellCodeArchitectureOptions"
              v-decorator="[
            'shellcode_architecture',
            { rules: [{ required: true, message: 'ShellCodeArchitecture Cannot be empty' }] }
          ]"
            ></a-select>
          </a-form-item>
          <a-form-item label="自启动函数">
            <a-select
              allowClear
              :options="autoOptions"
              v-decorator="[
            'auto_start_function'
          ]"
            ></a-select>
          </a-form-item>
          <a-form-item label="反沙箱函数">
            <a-select
              allowClear
              :options="sandboxOptions"
              v-decorator="[
            'anti_sandbox_function'
          ]"
            ></a-select>
          </a-form-item>
          <a-form-item label="Shell Code">
            <a-input
              placeholder="这里填写shellcode，目前只支持\x86\x64格式..."
              :type="`textarea`"
              :autoSize="{minRows: 4}"
              v-decorator="[
            'shellcode',
            { rules: [{ required: true, message: 'Shell Code Cannot be empty' },{validator:(rule, value, callback)=>this.handleShellCodePin(rule, value, callback)}] }
          ]"
            ></a-input>
            <!-- <a-input
              placeholder="这里填写shellcode"
              :autosize="true"
              :type="`textarea`"
              v-decorator="[
            'shellcode',
            { rules: [{ required: true, message: 'Shell Code Cannot be empty' },{pattern:/\\[A-Za-z0-9]{3}\b/g,message:'需要符合/XXX/XXX/XXX...格式'}] }
          ]"
            ></a-input>-->
          </a-form-item>
          <a-form-item>
            <a-button @click="handleShellCodeToTrojan" type="primary">免杀生成</a-button>
          </a-form-item>
        </a-form>
      </Card>
    </a-col>
    <a-col :xs="24" :lg="16">
      <Card :name="''" :bodyStyle="bodyStyle">
        <Tables
          :columns="columns"
          :tableData="data"
          :rowKey="`trojan_id`"
          :scrollTable="{x:1000,y:400}"
          :total="total"
          @change="handleChange"
          :showTotalDIY="handleShowTotal"
        >
          <template slot="btn">
            <a-button @click="handleTrojan(current)" type="primary" size='small' style="margin-left: 5px;">刷新</a-button>
          </template>
        </Tables>
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/Tables.vue'
import { mapGetters } from 'vuex'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
export default {
  components: {
    Card,
    Tables,
  },
  mixins: [OverallMixins],
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  data () {
    return {
      form: this.$form.createForm(this, { name: 'form' }),
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      pluginOptions: [],//插件名称
      autoOptions: [],//自启动函数
      sandboxOptions: [],//反沙箱函数
      shellCodeTypeOptions: [//生成类型
        {
          label: 'MetasploitFramework',
          value: '1'
        },
        {
          label: 'CobaltStrike',
          value: '2'
        },
      ],
      ShellCodeArchitectureOptions: [//生成位数
        {
          label: 'x86',
          value: 'x86'
        },
        {
          label: 'x64',
          value: 'x64'
        },
      ],
      columns: [
        {
          title: "项目名称",
          dataIndex: "shellcode_name",
          ellipsis: true,
          width: 200
        },
        {
          title: "类型",
          dataIndex: "shellcode_type",
          customRender: (text, record, index) => {
            return <a-tag color={text == '1' ? 'cyan' : 'blue'}> {text == '1' ? 'MSF' : 'CS'} </a-tag>
          }
        },
        {
          title: "类型",
          dataIndex: "shellcode_architecture",
          customRender: (text, record, index) => text == 'x86' ? <span style="color:rgb(255 190 8)"> {text} </span> : <a> {text} </a>
        },
        {
          title: "状态",
          dataIndex: "compilation_status",
          customRender: (text, record, index) => {
            const flag = text == 0 ? '未完成' : text == 1 ? '完成' : '错误'
            return [<a-icon type={text == 0 ? "loading" : text == 1 ? "check-circle" : "close-circle"} style={text == 0 ? { 'color': '#00adff', 'margin-right': '2px' } : text == 1 ? { 'color': '#54c741', 'margin-right': '2px' } : { 'color': '#e0b22e', 'margin-right': '2px' }} />, <a style={text == 0 ? { 'color': '#00adff' } : text == 1 ? { 'color': '#54c741' } : { 'color': '#e0b22e' }} >{flag}</a>]
          }
        },
        {
          title: "创建时间",
          dataIndex: "creation_time",
          width: 180,
          customRender: (text, record, index) => { return this.moment(text, "X").format('YYYY-MM-DD H:mm:ss') }
        },
        // {
        //   title: "操作",
        //   dataIndex: "action",
        //   align: 'center',
        //   customRender: (text, record, index) => {
        //     return <a-button type="link" v-on:click={() => this.handleEXE(record)} >下载</a-button>
        //   }
        // },
      ],
      data: [],
      current: 1,
      total: 0,

    }
  },
  mounted () {
    const _this = this
    _this.handleShellCode()
    _this.handleTrojan(_this.current)
  },
  methods: {
    //select 字典获取
    handleShellCode () {
      const _this = this
      const params = {
        token: _this.token
      }
      // const plugins = _this.$api.get_trojan_plugins(params)
      // const auto = _this.$api.get_auto_start(params)
      // const sandbox = _this.$api.get_anti_sandbox(params)
      _this.$api.get_trojan_plugins(params).then(res => {
        if (res.code == '200') {
          let pluginsOptions = []
          for (let item in res.message) {
            pluginsOptions.push({ label: res.message[item], value: item })
          }
          _this.pluginOptions = pluginsOptions
        }
      })
      // Promise.all([plugins, auto, sandbox]).then(res => {
      //   res.map((items, i) => {
      //     if (items.code == '200') {
      //       switch (i) {
      //         case 0:
      //           const pluginsOptions = []
      //           for (const item in items.message) {
      //             pluginsOptions.push({ label: items.message[item], value: item })
      //           }
      //           _this.pluginOptions = pluginsOptions
      //           break;
      //         case 1:
      //           const autoOptions = []
      //           items.message.map(item => {
      //             autoOptions.push({ label: item, value: item })
      //           })
      //           _this.autoOptions = autoOptions
      //           break;
      //         case 2:
      //           const sandboxOptions = []
      //           items.message.map(item => {
      //             sandboxOptions.push({ label: item, value: item })
      //           })
      //           _this.sandboxOptions = sandboxOptions
      //           break;
      //       }
      //     }
      //   })
      // })

    },
    //表格信息获取
    handleTrojan (page) {
      const _this = this
      const hide = _this.$message.loading('查询中...', 0)
      const queryParams = {
        token: _this.token,
        number_of_pages: page
      }
      const statisticalParams = {
        token: _this.token,
      }
      const query = _this.$api.trojan_data_query(queryParams)
      const statistical = _this.$api.trojan_data_statistical(statisticalParams)
      Promise.all([query, statistical])
        .then(res => {
          res.map((items, i) => {
            if (items.code == 200) {
              setTimeout(hide)
              if (i == 0) {
                _this.$message.success('查询完成', 0.3)
                _this.data = items.message
              }
              else _this.total = items.message
            }
            else {
              setTimeout(hide)
              _this.$message.error(items.message)
            }
          })
        })
        .catch((err) => {
          setTimeout(hide)
          _this.$message.error(err)
        })
    },
    //ShellCode格式校验
    handleShellCodePin (rule, value, callback) {
      const text = value ? value : ''
      let arr = text.match(/\\[A-Za-z0-9]{3}\b/g) == null ? [] : text.match(/\\[A-Za-z0-9]{3}\b/g)
      if (text.length % 4 == 0 && arr.length * 4 == text.length) callback()
      else callback('目前只支持\\x86\\x64格式...')
    },
    //生成免杀
    handleShellCodeToTrojan () {
      const _this = this
      _this.form.validateFields((err, values) => {
        if (err) _this.$message.warn('表单信息填写有误或者必填项未填')
        else {
          let params = {
            token: _this.token,
            ...values
          }
          params.anti_sandbox_function = params.anti_sandbox_function ? params.anti_sandbox_function : ''
          params.auto_start_function = params.auto_start_function ? params.auto_start_function : ''
          _this.$api.shellcode_to_trojan(params).then((res) => {
            if (res.code == 200) {
              _this.$message.success(res.message)
              _this.handleTrojan(_this.current)
            }
            else {
              _this.$message.error(res.message)
            }
          })
        }
      })
    },
    //分页change
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleQueryScriptProject()
    },
    //下载
    handleEXE (record) {
      const _this = this
      if (record.compilation_status != 1) {
        _this.$message.warn('状态错误，无法下载')
        return
      }
      _this.$store.dispatch("ShellCodeStore/setTrojanId", record.trojan_id);
      _this.$store.dispatch("ShellCodeStore/setTrojanGenerateFileName", record.trojan_generate_file_name);
      // const params = {
      //   token: _this.token,
      //   trojan_id: record.trojan_id,
      //   trojan_generate_file_name: record.trojan_generate_file_name
      // }
      _this.$api.trojan_file_download_verification()
        .then((res) => {
          const link = window.URL.createObjectURL(new Blob([res]))
          let download = document.createElement('a')
          download.download = record.trojan_generate_file_name
          download.href = link
          download.click()
        })
    },
    handleShowTotal (Dom, total, range) {
      const _this = this
      const Btn = <div style="display: flex;align-items: center;">
        {Dom}
        <a-button v-on:click={() => { _this.handleTrojan(_this.current) }} type="primary">刷新</a-button>
      </div>
      return [Btn]
    }
  },
}
</script>

<style>
</style>