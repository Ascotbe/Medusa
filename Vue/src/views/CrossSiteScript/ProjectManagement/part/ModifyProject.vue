<template>
  <div style="text-align: left;">
    <a-form>
      <a-form-item label='项目代码'>
        <codemirror  v-model='projectCode' :options="{mode: 'text/javascript',lineNumbers: true,theme:'base16-light'}"></codemirror>
      </a-form-item>
      <a-form-item label='将如下代码植入怀疑出现xss的地方' class="code">
        <codemirror v-model='markdownData.the_first_use' :options="{mode: 'text/javascript',lineNumbers: false,theme:'base16-light'}"></codemirror>
      </a-form-item>
       <a-form-item label='再或者以你任何想要的方式插入' class="code">
        <codemirror v-model='markdownData.exploit_path' :options="{mode: 'text/javascript',lineNumbers: false,theme:'base16-light'}"></codemirror>
      </a-form-item>
       <a-form-item label='极限代码~！：' class="code">
        <codemirror v-model='markdownData.the_second_use' :options="{mode: 'text/javascript',lineNumbers: false,theme:'base16-light'}"></codemirror>
      </a-form-item>
      <a-form-item label='图片插件' class="code">
        <codemirror v-model='markdownData.the_third_use' :options="{mode: 'text/javascript',lineNumbers: false,theme:'base16-light'}"></codemirror>
      </a-form-item>
      <a-form-item label='编码poc' class="code">
        <codemirror v-model='markdownData.coding_exploit' :options="{mode: 'text/javascript',lineNumbers: false,theme:'base16-light'}"></codemirror>
      </a-form-item>
      <a-form-item style="text-align: center;">
        <a-button type='primary' @click="reset">重置</a-button>
        <a-button type='primary' style="margin-left: 10px;" @click="handleSave">保存修改</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
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
  components: { codemirror },
  data () {
    return {
      projectCode: '',
      projectCodeOrigin: '',
      markdownData: {},
      markdownDataOrigin: {},
      projectAssociatedFileName:''
    }
  },
  mounted () {
    this.projectAssociatedFileName = this.$route.query.name
    if (this.projectAssociatedFileName == '' || this.projectAssociatedFileName == undefined || this.projectAssociatedFileName == null) {
      this.$message.warn('请从项目管理进入')
      this.$router.push('ProjectManagement')
    }else {
      this.handleQueeryProjectInfo()
    }
  },
  methods: {
    handleQueeryProjectInfo () {
      const _this = this
      const params = {
        token: _this.token,
        project_associated_file_name: _this.projectAssociatedFileName,
      };
      _this.$api.query_script_project_info(params).then((res) => {
        if (res.code == 200) {
          for (const key in res.message) {
            if (key == 'project_associated_file_data') {
              _this.projectCode = _this.QJBase64Decode(res.message[key])
              _this.projectCodeOrigin = _this.QJBase64Decode(res.message[key])
            }
            // else res.message[key] = "```" + `\n${res.message[key]}\n` + "```"
          }
          _this.markdownData = { ...res.message }
          _this.markdownDataOrigin = { ...res.message }
        }
        else _this.$message.warn(res.message)
      })
    },
    reset() {
      this.markdownData = { ...this.markdownDataOrigin }
      this.projectCode = this.projectCodeOrigin
    },
    handleSave () {
      const _this = this
      // if (_this.projectCode.indexOf("```\n") != 0 || _this.projectCode.indexOf("\n```") != _this.projectCode.length - 4) {
      //   _this.$message.warn('```\n您没有在添加代码\n```')
      //   return
      // }
      // const projectCode = _this.projectCode.replace(/```\n/g, "").replace(/\n```/g, "")
      const params = {
        token: _this.token,
        project_associated_file_name: _this.projectAssociatedFileName,
        project_associated_file_data: _this.QJBase64Encode(_this.projectCode),
      };
      this.$api.modify_cross_site_script_project(params).then((res) => {
        if (res.code) {
          _this.$message.success(res.message)
          _this.handleQueeryProjectInfo()
        }else _this.$message.success(res.message)
      })
    }
  }
}
</script>

<style>
.code  .CodeMirror {
  height: auto !important;
  max-height: 300px;
}
</style>