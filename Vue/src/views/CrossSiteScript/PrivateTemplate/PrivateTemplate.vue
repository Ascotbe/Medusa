<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%;min-height: 540px;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
      <Card :name="`创建个人模板`" :bodyStyle="bodyStyle">
        <template slot="extraCard">
          <a-button type="primary" @click="handleSave">创建模板</a-button>
        </template>
        <a-form
          :form="templateForm"
          :layout="`vertical`"
          :label-col="{ span: 24 }"
          :wrapper-col="{ span: 24 }"
        >
          <a-col :span="24">
            <a-form-item label="模板名称:">
              <a-input
                v-decorator="[
              'template_name',
              { rules: [{ required: true, message: '请输入模板名称' }] }
            ]"
              ></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="24">
            <a-form-item label="模板内容:">
              <!-- <MarkdownPro
                v-model="templateCode"
                theme="oneDark"
                :autoSave="false"
                :toolbars="toolbars"
                ref="MarkdownPro"
              />-->
              <codemirror
                v-model="templateCode"
                :options="{mode: 'text/javascript',lineNumbers: true,theme:'base16-light'}"
              ></codemirror>
            </a-form-item>
          </a-col>
        </a-form>
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
// import { MarkdownPro } from 'vue-meditor'
import { codemirror } from 'vue-codemirror'

// import base style
import 'codemirror/lib/codemirror.css'
import 'codemirror/theme/base16-light.css'
import 'codemirror/mode/javascript/javascript.js'
export default {
  mixins: [OverallMixins],
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  // components: { Card, MarkdownPro },
  components: { Card, codemirror },
  data () {
    return {
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      templateForm: this.$form.createForm(this, { name: 'templateForm' }),
      templateCode: '',//脚本数据,
    }
  },
  mounted () {
    this.$refs.MarkdownPro.split = false
  },
  methods: {
    handleSave () {//创建模板
      // if (this.templateCode.indexOf("```\n") != 0 || this.templateCode.indexOf("\n```") != this.templateCode.length - 4) {
      //   this.$message.warn('```\n您没有在添加代码\n```')
      //   return
      // }
      if (!this.templateForm.getFieldsValue().template_name) {
        this.$message.warn('请先输入模板名')
        return
      }
      // const templateCode = this.templateCode.replace(/```\n/g, "").replace(/\n```/g, "")
      const params = {
        token: this.token,
        template_name: this.templateForm.getFieldsValue().template_name,
        template_data: this.templateCode,
      };
      this.$api.save_cross_site_script_template(params).then((res) => {
        if (res.code) {
          this.$message.success('创建成功')
          this.templateForm.resetFields()
        }
        else this.$message.success(res.message)
      })
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