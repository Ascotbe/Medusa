<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%;min-height: 540px;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :xs="{ span: 24 }" :lg="{ span: 8 }">
      <Card name="">
        <!-- <a-tabs v-model="activeKey" @change="handleTemplate">
          <a-tab-pane :key="items.key" :tab="items.tab" v-for="items in tabs"> -->
            <a-list item-layout="horizontal" :data-source="templateList" v-for="items in tabs" :key="items.key">
              <a-list-item slot="renderItem" slot-scope="item" style="cursor: pointer;" @click="handleClick(items.key,item)" :class="{active: activeName === item.file_name}">
                <a-list-item-meta>
                  <a
                    slot="title"
                    style="font-size: 16px;"
                  >{{items.key == 'public'?item.file_name :item.template_name}}</a>
                  <!-- <a-col
                    slot="description"
                    class="description"
                  >{{items.key == 'public'?item.file_data:item.template_data}}</a-col>-->
                  <MyIcon type="icon-js" slot="avatar" style="font-size: 24px;" />
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          <!-- </a-tab-pane>
        </a-tabs> -->
      </Card>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 16 }">
      <Card name="">
        <!-- <template slot="extraCard" v-if="!disabled">
          <a-button type="danger" style="margin-right:2px" @click="handleDelete">删除模板</a-button>
          <a-button type="primary" @click="handleSave">保存修改</a-button>
        </template> -->
        <a-form
          :form="templateForm"
          :layout="`vertical`"
          :label-col="{ span: 24 }"
          :wrapper-col="{ span: 24 }"
        >
          <a-col :span="24">
            <a-form-item label="模板名称:">
              <a-input
                disabled
                v-decorator="[
              'template_name',
              { rules: [{ required: true, message: '请输入模板名称' }] }
            ]"
              ></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="24">
            <a-form-item label="模板内容:">
              <!-- <MarkdownPreview v-if="disabled" theme="oneDark" :initialValue="templateCode" />
              <MarkdownPro
                v-model="templateCode"
                ref="MarkdownPro"
                theme="oneDark"
                :autoSave="false"
                :toolbars="toolbars"
                v-else
              /> -->
               <codemirror v-model="templateCode" :options="{mode: 'text/javascript',lineNumbers: true,theme:'base16-light'}"></codemirror>
            </a-form-item>
          </a-col>
        </a-form>
      </Card>
      <!-- <Card :name="`模板内容`" :bodyStyle="bodyStyle"></Card> -->
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
// import { MarkdownPro, MarkdownPreview } from 'vue-meditor'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
import { Icon } from "ant-design-vue";
const faceConfig = require("../../../../faceConfig");
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: faceConfig.scriptUrl,
});

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
  // components: { MyIcon, Card, MarkdownPreview, MarkdownPro },
  components: { MyIcon, Card, codemirror },
  data () {
    return {
      activeName:'',
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      tabs: [
        {
          key: "public",
          tab: "公共模板"
        },
        // {
        //   key: "private",
        //   tab: "个人模板"
        // },
      ],
      activeKey: 'public',
      templateList: [],
      templateForm: this.$form.createForm(this, { name: 'templateForm' }),
      templateCode: '',
      disabled: false,
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
    }
  },
  mounted () {
    const _this = this
    _this.handleTemplate("public")
    // _this.$refs.MarkdownPro.split = false
  },
  methods: {
    handleTemplate (key) {//查询模板
      const _this = this
      const params = {
        token: _this.token,
      };
      _this.templateList = []
      if (key == "public") {
        _this.$api.read_default_script_template(params).then((res) => {
          if (res.code == 200) {
            res.message.map((item) => item.file_data = _this.QJBase64Decode(item.file_data))
            _this.templateList = res.message
          }
          else _this.$message.error(res.message);
        })
      }
      else if (key == "private") {
        _this.$api.read_script_template(params)
          .then((res) => {
            if (res.code == 200) {
              res.message.map((item) => item.template_data = _this.QJBase64Decode(item.template_data))
              _this.templateList = res.message
            }
            else _this.$message.error(res.message);
          })
      }
    },
    handleClick (key, item) {//选中模板渲染
      this.activeName = item.file_name
      const _this = this
      if (key == 'public') {
        _this.disabled = true
        _this.templateForm.setFieldsValue({ template_name: item.file_name })
        // _this.templateCode = "```" + `\n${item.file_data}\n` + "```"
        _this.templateCode = item.file_data
      }
      else {
        _this.disabled = false
        _this.templateForm.setFieldsValue({ template_name: item.template_name })
        _this.$nextTick(() => {
          _this.templateCode = item.template_data
          // _this.$refs.MarkdownPro.split = false
        })
      }
    },
    handleSave () {//保存模板修改
      const _this = this
      // if (_this.templateCode.indexOf("```\n") != 0 || _this.templateCode.indexOf("\n```") != _this.templateCode.length - 4) {
      //   _this.$message.warn('```\n您没有在添加代码\n```')
      //   return
      // }
      if (!_this.templateForm.getFieldsValue().template_name) {
        _this.$message.warn('请先选择模板')
        return
      }
      // const templateCode = _this.templateCode.replace(/```\n/g, "").replace(/\n```/g, "")
      const params = {
        template_name: _this.templateForm.getFieldsValue().template_name,
        template_data: _this.templateCode,
        token: _this.token
      };
      _this.$api.modify_cross_site_script_template(params).then((res) => {
        if (res.code == 200) {
          _this.$message.success("模板修改成功");
          _this.handleTemplate("private");
        } else {
          _this.$message.error(res.message);
        }
      });
    },
    handleDelete () {//删除模板
      const _this = this
      if (!_this.templateForm.getFieldsValue().template_name) {
        _this.$message.warn('请先选择模板')
        return
      }
      const params = {
        template_name: _this.templateForm.getFieldsValue().template_name,
        token: _this.token
      };
      _this.$api.delete_cross_site_script_template(params).then((res) => {
        if (res.code == 200) {
          _this.$message.success("模板删除成功");
          _this.templateForm.resetFields()
          _this.handleTemplate("private");
        } else {
          _this.$message.error(res.message);
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.description {
  min-width: 75px;
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.active a {
  color: #51c51a;
}
</style>