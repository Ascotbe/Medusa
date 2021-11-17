<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-form :form="form" :label-col="{ span: 24 }" :wrapper-col="{ span: 24 }">
      <a-col :xs="24" style="height:50%">
        <Card name="创建协同项目" :headStyle="bodyStyle">
          <a-col :xs="24">
            <a-form-item label="项目名称">
              <a-input
                placeholder="项目名称"
                v-decorator="[
              'markdown_project_name',
            ]"
              ></a-input>
            </a-form-item>
          </a-col>
          <a-col :xs="24">
            <a-button type="primary" @click="handleCombine('Create')">创建协同任务</a-button>
          </a-col>
        </Card>
      </a-col>
      <a-col :xs="24" style="height:50%">
        <Card name="加入协同项目" :headStyle="bodyStyle">
          <a-col :xs="24">
            <a-form-item label="项目邀请码">
              <a-input
                placeholder="项目邀请码"
                v-decorator="[
              'markdown_project_invitation_code',
            ]"
              ></a-input>
            </a-form-item>
          </a-col>
          <a-col :xs="24">
            <a-button type="primary" @click="handleCombine('Join')">加入协同项目</a-button>
          </a-col>
        </Card>
      </a-col>
    </a-form>
  </a-row>
</template>

<script>
import Card from '@/components/Card/Card.vue'
import { mapGetters } from "vuex";
export default {
  components: {
    Card,
  },
  data () {
    return {
      form: this.$form.createForm(this, { name: 'form' }),
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px'
      },
    }
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  methods: {
    handleCombine (flag) {
      const _this = this
      const form = _this.form.getFieldsValue()
      if (flag == 'Create') {
        const params = {
          token: this.token,
          markdown_project_name: form.markdown_project_name
        }
        _this.$api.create_markdown_project(params).then((res) => {
          if (res.code == 200) {
            _this.$message.success(res.message);
            _this.$router.push("./CombineList");
          } else {
            _this.$message.error(res.message);
          }
        })
      }
      else if (flag == 'Join') {
        const params = {
          token: this.token,
          markdown_project_invitation_code: form.markdown_project_invitation_code
        }
        this.$api.join_markdown_project(params).then((res) => {
          if (res.code == 200) {
            this.$message.success(res.message);
            this.$router.push("./CombineList");
          } else {
            this.$message.error(res.message);
          }
        });
      }
    },
  }
};
</script>

<style lang="scss" scoped>
</style>
