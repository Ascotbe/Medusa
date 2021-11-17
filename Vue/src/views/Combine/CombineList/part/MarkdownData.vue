<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%;min-height: 540px;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :span="24">
      <Card :name="`项目:${markdown_project_name}`" :bodyStyle="bodyStyle">
        <template slot="extraCard">
          <div>
            创建时间:
            <span
              style="color: #51c51a"
            >{{moment(markdownInfo.creation_time,'X').format('YYYY-MM-DD H:mm:ss')}}</span>
          </div>
          <div>
            最后修改时间:
            <span
              style="color: #51c51a"
            >{{moment(markdownInfo.update_time,'X').format('YYYY-MM-DD H:mm:ss')}}</span>
          </div>
        </template>
        <MarkdownPro
          ref="Markdown"
          theme="oneDark"
          @on-save="handleOnSave"
          @on-upload-image="handleOnUpladImage"
          :autoSave="false"
          v-model="markdownData"
          :toolbars="toolbars"
        />
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
import { MarkdownPro } from 'vue-meditor'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
const config = require("../../../../../faceConfig");
export default {
  mixins: [OverallMixins],
  data () {
    return {
      markdownData: '',
      markdownInfo: {},
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      toolbars: {
        save: true,
        uploadImage: true,
      }
    }
  },
  computed: {
    ...mapGetters({
      markdown_name: "CombineStore/markdown_name",
      markdown_project_name: "CombineStore/markdown_project_name",
      token: "UserStore/token",
    })
  },
  components: { Card, MarkdownPro },
  mounted () {
    const _this = this
    if (_this.markdown_name == '' || _this.markdown_name == undefined || _this.markdown_name == null) {
      _this.$message.warn('项目列表进入')
      _this.$router.push('CombineList')
      return
    }
    _this.handleMarkdownData()
  },
  methods: {
    handleMarkdownData () {
      const _this = this
      const params = {
        token: _this.token,
        markdown_name: _this.markdown_name
      }
      _this.$api.query_markdown_data(params).then((res) => {
        _this.markdownInfo = { ...res.message[0] }
        _this.markdownData = _this.QJBase64Decode(_this.markdownInfo.markdown_data)
      })
    },
    handleOnSave (value) {
      const _this = this
      const params = {
        token: _this.token,
        markdown_name: _this.markdown_name,
        new_markdown_data: value.value,
      }
      _this.$api.markdown_data_comparison(params).then((res) => {
        if (res.code == 200) {
          const comparisonData = {
            new: value.value,
            old: res.message
          }
          _this.$store.dispatch("CombineStore/setComparisonData", comparisonData)
          _this.$router.push("DataComparison")
        } else {
          _this.$message.success(res.message);
        }
      })

    },
    handleOnUpladImage (file) {
      const _this = this
      if (_this.handleBeforeUpload(file) == true) {
        let params = new FormData();
        params.append("file", file);
        _this.$api.markdown_image_upload(params).then((res) => {
          const resUrl = `${config.imgPath}${res.message}`
          _this.$refs.Markdown.insertContent(`![image](${resUrl})`);
        });
      }
    },
    handleBeforeUpload (file) {
      const _this = this
      const isLt10K = file.size / 1024 > 1;
      if (!isLt10K) {
        _this.$message.error("图片得大于1KB!");
        return false;
      } else {
        return true;
      }
    },
  },
}
</script>

<style>
</style>