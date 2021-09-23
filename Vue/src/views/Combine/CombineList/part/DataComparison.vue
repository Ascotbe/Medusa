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
    <a-col :span="24">
      <Card name="Markdown文档数据对比">
        <template slot="extraCard">
          <a-button @click="handleSave" type="primary">确认保存</a-button>
          <a-button @click="handleCancel">取消退回</a-button>
        </template>
        <a-col :span="24" v-html="comparisonData.old"></a-col>
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from 'vuex'
import Card from '@/components/Card/Card.vue'

export default {
  computed: {
    ...mapGetters({
      markdown_name: "CombineStore/markdown_name",
      token: "UserStore/token",
      comparisonData: "CombineStore/comparisonData",
    })
  },
  components: { Card },
  mounted () {
    const _this = this
    if (_this.markdown_name == '' || _this.markdown_name == undefined || _this.markdown_name == null || _this.comparisonData == {} || _this.comparisonData == undefined || _this.comparisonData == null) {
      _this.$message.warn('项目列表进入')
      _this.$router.push('CombineList')
      return
    }
  },
  methods: {
    handleSave () {
      const _this = this
      const params = {
        token: _this.token,
        markdown_name: _this.markdown_name,
        markdown_data: _this.comparisonData.new,
      };
      _this.$api.save_markdown_data(params).then((res) => {
        if (res.code == 200) {
          _this.$message.success("保存成功..");
          _this.$store.dispatch("CombineStore/setComparisonData", {});
          _this.$router.go(-1);
        } else {
          _this.$message.error(res.message);
        }
      });
    },
    handleCancel () {
      const _this = this
      _this.$store.dispatch("CombineStore/setComparisonData", {});
      _this.$router.go(-1);
    }
  }


}
</script>

<style>
</style>