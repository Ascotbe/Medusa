<template>
  <a-row
    type="flex"
    style="height:100%;text-align:left"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <Card
      class="about"
      :name="''"
      :bodyStyle="{
          'display': 'flex',
          'align-content': 'center',
          'align-items': 'center',
          'flex-direction': 'row',
          'justify-content': 'center',
          'flex-wrap': 'wrap'
        }"
    >
      <a-col :sm="24" :lg="8">
        <Descriptions :aboutInfo="aboutInfo" />
      </a-col>
      <a-col :sm="24" :lg="12">
        <img :src="AscotbeUrl" alt width="100%" style="padding-top:5%" />
      </a-col>
    </Card>

    <!-- <img :src="AscotbeUrl" alt height="100%" /> -->
  </a-row>
</template>

<script>
import Descriptions from './part/Descriptions.vue'
import Card from '@/components/Card/Card.vue'
import { mapGetters } from 'vuex'
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
export default {
  components: {
    Card,
    Descriptions
  },
  mixins: [OverallMixins],
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  data () {
    return {
      // bodyStyle: {
      //   borderTop: '3px solid #51c51a',
      //   borderBottom: '0px'
      // },
      aboutInfo: {},
      AscotbeUrl: require('../../assets/Ascotbe.png')
    }
  },
  mounted () {
    const _this = this
    _this.handleAbout()
  },
  methods: {
    handleAbout () {
      const _this = this
      const params = {
        token: _this.token
      }
      _this.$api.medusa_info(params).then((res) => {
        if (res.code == 200) {
          _this.aboutInfo = res.message
        }
        else _this.$message.error(res.message)
      })
    },
    handleLabel (key) {
      let label = key
      switch (key) {
        case 'version':
          label = '当前版本'
          break
        case 'latest_version':
          label = '最新版本'
          break
        case 'official_documentation':
          label = '官方文档'
          break
        case 'registration_function_status':
          label = '注册功能状态'
          break
        case 'forgot_password_function_status':
          label = '忘记密码状态'
          break
        case 'cross_site_script_uses_domain_names':
          label = 'XSS域名配置'
          break
        case 'domain_name_system_address':
          label = 'DNSLOG域名配置'
          break
        case 'local_mail_host':
          label = '自建邮件服务'
          break
      }
      return label
    }

  },
}
</script>

<style lang="less" scoped>
.ascotbe {
  background: url("../../assets/Ascotbe.png") no-repeat;
  background-size: auto 100%;
  background-position: top right;
}
.about {
  // display: flex;
  overflow-y: scroll;
}
/*定义整体的宽度*/
.about::-webkit-scrollbar {
  display: none;
}

/*定义滚动条轨道*/
.about::-webkit-scrollbar-track {
  display: none;
}

/*定义滑块*/
.about::-webkit-scrollbar-thumb {
  display: none;
}
/deep/ .ant-card {
  // background: rgba(0, 0, 0, 0);
}
// /deep/ .ant-card::before {
//   content: "";
//   width: calc(100% - 40px);
//   height: calc(100% - 40px);
//   position: absolute;
//   top: 20px;
//   left: 20px;
//   right: 0;
//   bottom: 0;
//   z-index: -1;
//   background: url("../../assets/Ascotbe.png") no-repeat;
//   background-position: left;
//   background-size: cover;
//   -webkit-filter: blur(5px);
//   -moz-filter: blur(5px);
//   -ms-filter: blur(5px);
//   -o-filter: blur(5px);
//   filter: blur(5px);
// }
// .ascotbe::before {
//   content: "";
//   // width: calc(100% - 40px);
//   // height: calc(100% - 40px);
//   // width: 100%;
//   height: 100%;
//   position: absolute;
//   top: 0;
//   right: 0;
//   bottom: 0;
//   z-index: 1;
//   background: url("../../assets/Ascotbe.png") no-repeat;
//   background-size: auto 100%;
// }
</style>