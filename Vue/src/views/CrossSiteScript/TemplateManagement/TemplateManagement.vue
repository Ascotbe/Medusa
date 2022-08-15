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
      <Card name>
        <a-tabs v-model="activeKey" @change="handleTemplate">
          <a-tab-pane :key="items.key" :tab="items.tab" v-for="items in tabs">
            <a-list item-layout="horizontal" :data-source="templateList">
              <a-list-item
                slot="renderItem"
                slot-scope="item"
                style="cursor: pointer;"
                @click="handleClick(items.key,item)"
                :class="{active: activeName === item.file_name}"
              >
                <a-list-item-meta>
                  <a
                    slot="title"
                    style="font-size: 16px;"
                  >{{items.key == 'public'?item.file_name :item.template_name}}</a>
                  <a-col
                    slot="description"
                    class="description"
                  >{{items.key == 'public'?item.file_data:item.template_data}}</a-col>
                  <MyIcon type="icon-js" slot="avatar" style="font-size: 24px;" />
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane>
        </a-tabs>
      </Card>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 16 }">
      <Card name>
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
              />-->
              <codemirror
                v-model="templateCode"
                :options="{mode: 'text/javascript',lineNumbers: true,theme:'base16-light'}"
              ></codemirror>
            </a-form-item>
          </a-col>
          <a-col :span="24" v-if="!disabled" style="display:flex;justify-content: center;">
            <a-button type="danger" style="margin-right:2px" @click="handleDelete">删除模板</a-button>
            <a-button type="primary" @click="handleSave">保存修改</a-button>
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
      activeName: '',
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
      tabs: [
        {
          key: "public",
          tab: "公共模板"
        },
        {
          key: "private",
          tab: "个人模板"
        },
      ],
      activeKey: 'public',
      templateList: [],
      templateForm: this.$form.createForm(this, { name: 'templateForm' }),
      templateCode: '',
      disabled: false,
    }
  },
  mounted () {
    this.handleTemplate("public")
    // this.$refs.MarkdownPro.split = false
  },
  methods: {
    handleTemplate (key) {//查询模板

      const params = {
        token: this.token,
      };
      this.templateList = []
      if (key == "public") {
        this.$api.read_default_script_template(params).then((res) => {
          if (res.code == 200) {
            res.message.map((item) => item.file_data = this.QJBase64Decode(item.file_data))
            this.templateList = res.message
          }
          else this.$message.error(res.message);
        })
      }
      else if (key == "private") {
        this.$api.read_script_template(params)
          .then((res) => {
            if (res.code == 200) {
              res.message.map((item) => item.template_data = this.QJBase64Decode(item.template_data))
              this.templateList = res.message
            }
            else this.$message.error(res.message);
          })
      }
    },
    handleClick (key, item) {//选中模板渲染
      this.activeName = item.file_name

      if (key == 'public') {
        this.disabled = true
        this.templateForm.setFieldsValue({ template_name: item.file_name })
        // this.templateCode = "```" + `\n${item.file_data}\n` + "```"
        this.templateCode = item.file_data
      }
      else {
        this.disabled = false
        this.templateForm.setFieldsValue({ template_name: item.template_name })
        this.$nextTick(() => {
          this.templateCode = item.template_data
          // this.$refs.MarkdownPro.split = false
        })
      }
    },
    handleSave () {//保存模板修改

      // if (this.templateCode.indexOf("```\n") != 0 || this.templateCode.indexOf("\n```") != this.templateCode.length - 4) {
      //   this.$message.warn('```\n您没有在添加代码\n```')
      //   return
      // }
      if (!this.templateForm.getFieldsValue().template_name) {
        this.$message.warn('请先选择模板')
        return
      }
      // const templateCode = this.templateCode.replace(/```\n/g, "").replace(/\n```/g, "")
      const params = {
        template_name: this.templateForm.getFieldsValue().template_name,
        template_data: this.templateCode,
        token: this.token
      };
      this.$api.modify_cross_site_script_template(params).then((res) => {
        if (res.code == 200) {
          this.$message.success("模板修改成功");
          this.handleTemplate("private");
        } else {
          this.$message.error(res.message);
        }
      });
    },
    handleDelete () {//删除模板

      if (!this.templateForm.getFieldsValue().template_name) {
        this.$message.warn('请先选择模板')
        return
      }
      const params = {
        template_name: this.templateForm.getFieldsValue().template_name,
        token: this.token
      };
      this.$api.delete_cross_site_script_template(params).then((res) => {
        if (res.code == 200) {
          this.$message.success("模板删除成功");
          this.templateForm.resetFields()
          this.handleTemplate("private");
        } else {
          this.$message.error(res.message);
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
