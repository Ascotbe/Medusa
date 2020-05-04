<template>
  <el-card style="margin-bottom:20px;">
    <div slot="header" class="clearfix">
      <span>About me</span>
    </div>

    <div class="user-profile">
      <div class="box-center">
       <pan-thumb width="100px" height="120px" image="http://www.wjlshare.xyz/wp-content/uploads/2020/04/F6701A7C13DFF3922B2B810A67994D02.jpg">
        </pan-thumb>
      </div>
      <div class="box-center">
        <div class="user-name text-center">Medusa</div>
        <div class="user-role text-center text-muted">{{ user.role | uppercaseFirst }}</div>
      </div>
    </div>

    <div class="user-bio">
      <div class="user-education user-bio-section">
        <div class="user-bio-section-header"><svg-icon icon-class="education" /><span>Introduce</span></div>
        <div class="user-bio-section-body">
          <div class="text-muted">
            请使用者遵守 中华人民共和国网络安全法,
          </div>
          <div class="text-muted">
            勿将Medusa项目用于非授权的测试,
          </div>
          <div class="text-muted">
            Medusa项目开发者不负任何连带法律责任。
          </div>
        </div>
      </div>

    <!-- <div class="user-skills user-bio-section">
        <div class="user-bio-section-header"><svg-icon icon-class="skill" /><span>登录日志</span></div>
           <div class="user-bio-section-body">
            <div class="progress-item" v-for="(item,index) of loginlog" :key="index" :timestamp="item.timestamp" placement="top" >
            <span>{{ item.title }}></span>
            </div>
            <div class="progress-item" v-for="(item,index) of loginlog" :key="index" :timestamp="item.timestamp" placement="top" >
            <span>{{ item.content }}></span>
            </div>
          </div>
      </div>
    </div> -->
    <div class="user-skills user-bio-section">
            <div class="user-bio-section-header"><svg-icon icon-class="skill" /><span>Skills</span></div>
            <div class="user-bio-section-body">
              <div class="progress-item">
                <span>Bash</span>
                <el-progress :percentage="70" />
              </div>
              <div class="progress-item">
                <span>Robot</span>
                <el-progress :percentage="18" />
              </div>
              <div class="progress-item">
                <span>Website</span>
                <el-progress :percentage="12" />
              </div>
              <div class="progress-item">
                <span>ESLint</span>
                <el-progress :percentage="100" status="success" />
              </div>
            </div>
          </div>
        </div>

  </el-card>
</template>

<script>
import PanThumb from '@/components/PanThumb'

export default {
  components: { PanThumb },
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          name: '',
          email: '',
          avatar: '',
          role: ''
        }
      }
    },
    data() {
      return {
        loginlog: [
          {
            timestamp: '2020/3/20',
            IP: '127.0.0.1',
            content: '福建省南平市'
          },
          {
            timestamp: '2020/3/21',
            IP: '127.0.0.1',
            content: '福建省南平市'
          },
          {
            timestamp: '2020/3/22',
            IP: '127.0.0.1',
            content: '福建省南平市'
          },
          {
            timestamp: '2020/3/23',
            IP: '127.0.0.1',
            content: '福建省南平市'
          }
        ]
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.box-center {
  margin: 0 auto;
  display: table;
}

.text-muted {
  color: #777;
}

.user-profile {
  .user-name {
    font-weight: bold;
  }

  .box-center {
    padding-top: 10px;
  }

  .user-role {
    padding-top: 10px;
    font-weight: 400;
    font-size: 14px;
  }

  .box-social {
    padding-top: 30px;

    .el-table {
      border-top: 1px solid #dfe6ec;
    }
  }

  .user-follow {
    padding-top: 20px;
  }
}

.user-bio {
  margin-top: 20px;
  color: #606266;

  span {
    padding-left: 4px;
  }

  .user-bio-section {
    font-size: 14px;
    padding: 15px 0;

    .user-bio-section-header {
      border-bottom: 1px solid #dfe6ec;
      padding-bottom: 10px;
      margin-bottom: 10px;
      font-weight: bold;
    }
  }
}
</style>
