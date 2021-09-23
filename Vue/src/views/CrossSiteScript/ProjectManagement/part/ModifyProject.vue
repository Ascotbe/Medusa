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
    <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
      <Card :name="'项目代码'" :bodyStyle="bodyStyle">
        <template slot="extraCard">
          <a-button type="primary" @click="handleSave">确认保存</a-button>
        </template>
        <MarkdownPro
          v-model="projectCode"
          ref="Markdown"
          theme="oneDark"
          :autoSave="false"
          :toolbars="toolbars"
        />
      </Card>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 24 }">
      <Card :name="'将如下代码植入怀疑出现xss的地方'" :bodyStyle="bodyStyle">
        <MarkdownPreview theme="oneDark" :initialValue="markdownData.the_first_use" />
      </Card>
      <Card :name="'再或者以你任何想要的方式插入'" :bodyStyle="bodyStyle">
        <MarkdownPreview theme="oneDark" :initialValue="markdownData.exploit_path" />
      </Card>
      <Card :name="'极限代码~！'" :bodyStyle="bodyStyle">
        <MarkdownPreview theme="oneDark" :initialValue="markdownData.the_second_use" />
      </Card>
      <Card :name="'图片插件'" :bodyStyle="bodyStyle">
        <MarkdownPreview theme="oneDark" :initialValue="markdownData.the_third_use" />
      </Card>
      <Card :name="'编码poc'" :bodyStyle="bodyStyle">
        <MarkdownPreview theme="oneDark" :initialValue="markdownData.coding_exploit" />
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import { MarkdownPro, MarkdownPreview } from 'vue-meditor'
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
export default {
  mixins: [OverallMixins],
  computed: {
    ...mapGetters({
      token: "UserStore/token",
      projectAssociatedFileName: "CrossSiteScriptStore/projectAssociatedFileName"
    })
  },
  components: { Card, MarkdownPro, MarkdownPreview },
  data () {
    return {
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
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
      },
      projectCode: '```\n请在这内部添加代码\n```',
      markdownData: {}
    }
  },
  mounted () {
    const _this = this
    if (_this.projectAssociatedFileName == '' || _this.projectAssociatedFileName == undefined || _this.projectAssociatedFileName == null) {
      _this.$message.warn('请从项目管理进入')
      _this.$router.push('ProjectManagement')
      return
    }
    _this.handleQueeryProjectInfo()
  },
  methods: {
    handleQueeryProjectInfo () {
      const _this = this
      const params = {
        token: _this.token,
        project_associated_file_name: _this.projectAssociatedFileName,
      };
      _this.$api.query_script_project_info(params).then((res) => {
        if (res.code = 200) {
          for (const key in res.message) {
            if (key == 'project_associated_file_data') _this.projectCode = "```" + `\n${_this.QJBase64Decode(res.message[key])}\n` + "```"
            else res.message[key] = "```" + `\n${res.message[key]}\n` + "```"
          }
          _this.markdownData = { ...res.message }
        }
        else _this.$message.warn(res.message)
      })
    },
    handleSave () {
      const _this = this
      if (_this.projectCode.indexOf("```\n") != 0 || _this.projectCode.indexOf("\n```") != _this.projectCode.length - 4) {
        _this.$message.warn('```\n您没有在添加代码\n```')
        return
      }
      const projectCode = _this.projectCode.replace(/```\n/g, "").replace(/\n```/g, "")
      console.log(projectCode)
      const params = {
        token: _this.token,
        project_associated_file_name: _this.projectAssociatedFileName,
        project_associated_file_data: _this.QJBase64Encode(projectCode),
      };
      this.$api.modify_cross_site_script_project(params).then((res) => {
        if (res.code) {
          _this.$message.success(res.message)
          _this.handleQueeryProjectInfo()
        }
        else _this.$message.success(res.message)
      })
    }
  }
}
</script>

<style>
</style>