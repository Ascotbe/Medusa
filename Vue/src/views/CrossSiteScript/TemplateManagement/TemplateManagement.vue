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
    <a-col :xs="{ span: 24 }" :lg="{ span: 8 }">
      <Card :name="`模板库`" :bodyStyle="bodyStyle">
        <a-tabs defaultActiveKey="public" @change="handleTemplate">
          <a-tab-pane :key="items.key" :tab="items.tab" v-for="items in tabs"></a-tab-pane>
        </a-tabs>
      </Card>
    </a-col>
    <a-col :xs="{ span: 24 }" :lg="{ span: 16 }">
      <Card :name="`模板详情`" :bodyStyle="bodyStyle"></Card>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'
import { MarkdownPro, MarkdownPreview } from 'vue-meditor'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
import { Icon } from "ant-design-vue";
const faceConfig = require("../../../../faceConfig");
const MyIcon = Icon.createFromIconfontCN({
  scriptUrl: faceConfig.scriptUrl,
});

export default {
  mixins: [OverallMixins],
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  components: { Card, MarkdownPreview, MarkdownPro },
  data () {
    return {
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
      templateList: []
    }
  },
  methods: {
    handleTemplate (key) {
      const _this = this
      const params = {
        token: _this.token,
      };
      if (key == "public") {
        _this.$api.read_default_script_template(params).then((res) => {
          if (res.code == 200) _this.templateList = res.message
          else _this.$message.error(res.message);
        })
      }
      else if (key == "private") {
        _this.$api.read_script_template(params).then((res) => {
          if (res.code == 200) _this.templateList = res.message
          else _this.$message.error(res.message);
        })
      }
    },
  }
}
</script>

<style>
</style>