<template>
  <a-row
    type="flex"
    justify="center"
    align="top"
    style="height:100%;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :xs="{ span: 24 }" :lg="{ span: 12 }">
      <Card :name="`项目基本信息`" :bodyStyle="bodyStyle">
        <a-form
          :form="XSSForm"
          :layout="`vertical`"
          :label-col="{ span: 6 }"
          :wrapper-col="{ span: 18 }"
        >
          <a-col :span="16">
            <a-form-item label="项目名:">
              <a-input
                v-decorator="[
              'projectName',
              { rules: [{ required: true, message: '请输入项目名' }] }
            ]"
              ></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="16">
            <a-form-item label="默认模板选择:">
              <a-select
                v-decorator="[
              'template',
            ]"
                :options="templateOption"
                @change="handleTemplateChange"
              ></a-select>
            </a-form-item>
          </a-col>
        </a-form>
      </Card>
      <Card :name="`模板内容`" :bodyStyle="bodyStyle">
        <MarkdownPreview theme="oneDark" :initialValue="markdownData" />
      </Card>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 12 }">
      <Card :name="`脚本数据(请输入代码)`" :bodyStyle="bodyStyle">
        <template slot="extraCard">
          <a-button @click="handleInsert">插入模板</a-button>
          <a-button @click="handleCreate" type="primary">创建项目</a-button>
          <!-- <a-col :xs="24" :lg="12"></a-col> -->
        </template>
        <MarkdownPro
          v-model="scriptData"
          ref="MarkdownPro"
          theme="oneDark"
          :autoSave="false"
          :toolbars="toolbars"
        />
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
import { MarkdownPro, MarkdownPreview } from 'vue-meditor'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
export default {
  mixins: [OverallMixins],
  data () {
    return {
      markdownData: '',//模板展示数据
      templateData: '',//模板实际插入数据
      scriptData: '',//脚本数据
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
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      XSSForm: this.$form.createForm(this, { name: 'XSSForm' }),
      templateOption: []
    }
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  components: { Card, MarkdownPreview, MarkdownPro },
  mounted () {
    const _this = this
    _this.markdownData = "```" + `\n${string}\n` + "```"
    _this.templateData = string
    _this.$refs.MarkdownPro.split = false
    _this.handleTemplateOption()
  },
  methods: {
    handleTemplateOption () {//查询模板信息
      const _this = this
      const params = {
        token: _this.token,
      };
      _this.templateOption = []
      _this.$api.read_default_script_template(params).then((res) => {
        if (res.code == 200) {
          res.message.map((item) => {
            const option = {
              value: item.file_data,
              label: item.file_name
            }
            _this.templateOption.push(option)
          })
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleTemplateChange (value) {//选择模板的回调
      const _this = this
      _this.markdownData = "```" + `\n${_this.QJBase64Decode(value)}\n` + "```"
      _this.templateData = _this.QJBase64Decode(value)
    },
    handleInsert () {//插入模板
      const _this = this
      _this.$refs.MarkdownPro.insertContent(_this.templateData)
    },
    handleCreate () {//创建项目
      const _this = this
      _this.XSSForm.validateFields((err, values) => {
        if (!err) {
          // if (_this.scriptData.indexOf("```\n") != 0 || _this.scriptData.indexOf("\n```") != _this.scriptData.length - 4) {
          //   _this.$message.warn('```\n您没有在添加代码\n```')
          //   return
          // }
          // const javascript_data = _this.scriptData.replace(/```\n/g, "").replace(/\n```/g, "")
          const params = {
            project_name: values.projectName,
            javascript_data: _this.QJBase64Encode(_this.scriptData),
            token: _this.token,
          }
          _this.$api.create_script_project(params).then((res) => {
            if (res.code == 200) _this.$message.success('项目创建成功')
            else _this.$message.warn(res.message)
          })
        }
        else _this.$message.warn('请输入项目名')
      })
    }
  }
}
const string = [
  ` ███▄ ▄███▓▓█████ ▓█████▄  █    ██   ██████  ▄▄▄      
▓██▒▀█▀ ██▒▓█   ▀ ▒██▀ ██▌ ██  ▓██▒▒██    ▒ ▒████▄    
▓██    ▓██░▒███   ░██   █▌▓██  ▒██░░ ▓██▄   ▒██  ▀█▄  
▒██    ▒██ ▒▓█  ▄ ░▓█▄   ▌▓▓█  ░██░  ▒   ██▒░██▄▄▄▄██ 
▒██▒   ░██▒░▒████▒░▒████▓ ▒▒█████▓ ▒██████▒▒ ▓█   ▓██▒
░ ▒░   ░  ░░░ ▒░ ░ ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░
░  ░      ░ ░ ░  ░ ░ ▒  ▒ ░░▒░ ░ ░ ░ ░▒  ░ ░  ▒   ▒▒ ░
░      ░      ░    ░ ░  ░  ░░░ ░ ░ ░  ░  ░    ░   ▒   
       ░      ░  ░   ░       ░           ░        ░  ░`
].join('\n')
</script>

<style>
</style>