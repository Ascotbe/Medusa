<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%;min-height: 540px;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :xs="{ span: 24 }" :lg="{ span: 12 }">
      <Card name>
        <div style="font-size: 16px; color: #000;margin-bottom: 10px;">模板信息</div>
        <a-form layout="vertical">
          <a-form-item label="选择模板:">
            <a-select
              v-decorator="['template']"
              :options="templateOption"
              @change="handleTemplateChange"
            ></a-select>
          </a-form-item>
          <a-form-item label="模板内容:">
            <codemirror
              ref="codemirror_read_only"
              :value="templateData"
              :options="{mode: 'text/javascript',lineNumbers: true,theme:'base16-light',lineWrapping:'true'}"
            ></codemirror>
          </a-form-item>
        </a-form>
      </Card>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 12 }">
      <Card name>
        <div style="font-size: 16px; color: #000;margin-bottom: 10px;">填写基本信息</div>
        <a-form :form="XSSForm" layout="vertical">
          <a-form-item label="项目名：">
            <a-input v-decorator="['projectName',{ rules: [{ required: true, message: '请输入项目名'}]}]"></a-input>
          </a-form-item>
          <a-form-item label="脚本数据：">
            <codemirror
              ref="codemirror"
              v-decorator="['scriptData',{ rules: [{ required: true, message: '请输入脚本数据'}]}]"
              :options="{mode: 'text/javascript',lineNumbers: true,theme:'base16-light',lineWrapping:'true'}"
              @input="handleCodeMirrorChange"
            ></codemirror>
          </a-form-item>
        </a-form>
        <div style="text-align: center;margin-top: 20px;">
          <a-button @click="handleInsert" type="primary" ghost>插入模板</a-button>
          <a-button @click="handleCreate" type="primary" style="margin-left: 10px;">创建项目</a-button>
        </div>
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'

import { codemirror } from 'vue-codemirror'

// import base style
import 'codemirror/lib/codemirror.css'
import 'codemirror/theme/base16-light.css'
import 'codemirror/mode/javascript/javascript.js'
export default {
  mixins: [OverallMixins],
  data () {
    return {
      templateData: '',//模板实际插入数据
      XSSForm: this.$form.createForm(this, { name: 'XSSForm' }),
      templateOption: []
    }
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  components: { Card, codemirror },
  mounted () {
    this.handleTemplateOption()
    // console.log()

    this.$refs.codemirror_read_only.codemirror.setSize('auto', 600)
    this.$refs.codemirror.codemirror.setSize('auto', 600)
  },
  methods: {
    handleTemplateOption () {//查询模板信息
      const params = {
        token: this.token,
      };
      this.templateOption = []
      this.$api.read_default_script_template(params).then((res) => {
        if (res.code == 200) {
          res.message.map((item) => {
            const option = {
              value: item.file_data,
              label: item.file_name
            }
            this.templateOption.push(option)
          })
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleTemplateChange (value) {//选择模板的回调
      this.templateData = this.QJBase64Decode(value)
    },
    handleInsert () {//根据光标位置插入模板
      //replaceRange(replacement: string, from: {line, ch}, to: {line, ch}, ?origin: string)
      // console.log(this.$refs.codemirror.codemirror.replaceRange())
      const { sticky, ...cursor } = this.$refs.codemirror.codemirror.getCursor()
      this.$refs.codemirror.codemirror.replaceRange(this.templateData, cursor)
      // this.XSSForm.setFieldsValue({ scriptData: (this.XSSForm.getFieldValue('scriptData') || '') + this.templateData })
    },
    handleCreate () {//创建项目
      this.XSSForm.validateFields((err, values) => {
        if (!err) {
          const params = {
            project_name: values.projectName,
            javascript_data: this.QJBase64Encode(values.scriptData),
            token: this.token,
          }
          this.$api.create_script_project(params).then((res) => {
            if (res.code == 200) {
              this.$message.success('项目创建成功')
              let timer = setTimeout(() => {
                this.$router.push({ path: '/layout/ModifyProject', query: { name: res.message } })
                clearTimeout(timer)
              }, 500)
            } else {
              this.$message.warn(res.message)
            }
          })
        }
      })
    },
    //监听codemirror 内容改变 赋值给表单 scriptData对象
    handleCodeMirrorChange (newValue) {
      this.XSSForm.setFieldsValue({ scriptData: newValue })
    },

  }
}
</script>
<style lang="less" scoped>
/*定义整体的宽度*/
::v-deep .CodeMirror-hscrollbar::-webkit-scrollbar {
  height: 5px;
  width: 5px;
}

/*定义滚动条轨道*/
::v-deep .CodeMirror-hscrollbar::-webkit-scrollbar-track {
  border-radius: 2px;
}

/*定义滑块*/
::v-deep .CodeMirror-hscrollbar::-webkit-scrollbar-thumb {
  border-radius: 2px;
  background: rgba(0, 255, 42, 0.5);
}

/*定义整体的宽度*/
::v-deep .CodeMirror-vscrollbar::-webkit-scrollbar {
  height: 5px;
  width: 5px;
}

/*定义滚动条轨道*/
::v-deep .CodeMirror-vscrollbar::-webkit-scrollbar-track {
  border-radius: 2px;
}

/*定义滑块*/
::v-deep .CodeMirror-vscrollbar::-webkit-scrollbar-thumb {
  border-radius: 2px;
  background: rgba(0, 255, 42, 0.5);
}
</style>