<template>
  <div>
    <a-form :form="form">
      <a-row :gutter="[16,{ xs:0, md:10}]">
        <a-col :xs='24' :md="7" :lg='4'>
          <a-form-item label="">
            <a-input
              placeholder="搜索项目名称"
              v-on:keyup.enter.native="handleSearch"
              v-decorator="[
          'name',
        ]"
            ></a-input>
          </a-form-item>
        </a-col>
        <a-col :xs='24' :md="7" :lg='4'>
          <a-form-item label="">
            <a-input
              placeholder="搜索GitHubId"
              v-on:keyup.enter.native="handleSearch"
              v-decorator="[
          'github_id',
        ]"
            ></a-input>
          </a-form-item>
        </a-col>
        <a-col :xs='24' :md="7" :lg='4'>
          <a-form-item label="">
            <a-input
              placeholder="搜索项目连接"
              v-on:keyup.enter.native="handleSearch"
              v-decorator="[
          'html_url',
        ]"
            ></a-input>
          </a-form-item>
        </a-col>
        <a-col :xs='24' :md='3' :lg='2' style="text-align: left;">
          <a-form-item>
            <a-button type="primary" @click="handleSearch">查询</a-button>
          </a-form-item>
        </a-col>
      </a-row>
    </a-form>
   
      <Card name="">
        <Tables
          :loading='loading'
          :columns="columns"
          :tableData="data"
          :total="total"
          :rowKey="`github_id`"
          @change="handleChange"
        />
      </Card>
   
 </div>
</template>

<script>
import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/CTables.vue'
import { mapGetters } from "vuex";

export default {
  name: "GitHubMonitor",
  components: {
    Card,
    Tables
  },
  data () {
    return {
      loading: false,
      columns,
      form: this.$form.createForm(this, { name: 'form' }),
      data: [],
      total: 0,
      current: 1
    };
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  created () {
    const _this = this
    _this.handleGitHubMoitor()
  },
  methods: {
    handleSearch () {
      const _this = this
      _this.handleGitHubMoitor()
    },
    handleGitHubMoitor () {
      const _this = this
      const form = _this.form.getFieldsValue()
      const params = {
        token: _this.token,
        number_of_pages: _this.current,
        name: form.name ? form.name : '',
        github_id: form.github_id ? form.github_id : '',
        html_url: form.html_url ? form.html_url : '',
      };
      this.loading = true
      _this.$api.github_monitor_search(params).then((res) => {
        if (res.code == 200) {
          _this.data = res.message.data
          _this.total = res.message.amount
        } else {
          _this.$message.error(res.message);
        }
      }).then(() => {
        this.loading = false
      })
    },
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleGitHubMoitor()
    }
  },
};
const columns = [
  {
    title: "GitHub编号",
    dataIndex: "github_id",
    key: "github_id",
    fixed: "left",
  },
  {
    title: "项目名称",
    dataIndex: "name",
    width: 200,
    key: "name",
  },
  {
    title: "项目地址",
    dataIndex: "html_url",
    width: 350,
    key: "html_url",
  },
  {
    title: "项目创建时间",
    dataIndex: "created_at",
    key: "created_at",
    width: 250,
  },
  {
    title: "项目更新时间",
    dataIndex: "updated_at",
    key: "updated_at",
  },
  {
    title: "最新上传时间",
    dataIndex: "pushed_at",
    key: "pushed_at",
  },
  {
    title: "Fork",
    dataIndex: "forks_count",
    key: "forks_count",
  },
  {
    title: "Star",
    dataIndex: "watchers_count",
    key: "watchers_count",
  },
]
</script>

<style lang="scss" scoped>
</style>
