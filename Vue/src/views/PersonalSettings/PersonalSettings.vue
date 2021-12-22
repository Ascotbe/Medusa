<template>
  <a-row type="flex" justify="center" style="height:100%" :gutter="[
     16,  16
    ]">
    <a-col :xs="24" :lg="12">
      <Card :name="''" class="layout">
        <a-avatar
          shape="circle"
          icon="user"
          :src="headerImg"
          :loadError="handleLoadError"
          :size="250"
        />
        <a-col :span="24">{{userinfo.name}}</a-col>
        <a-col :span="24">{{userinfo.email}}</a-col>
        <a-col
          :span="24"
          style="display: flex;
    justify-content:center;
    align-items: flex-end;"
        >
          <a-upload
            name="file"
            @change="handleHeaderPhoto"
            :customRequest="handleCustomRequest"
            :file-list="fileList"
          >
            <a-button>
              <a-icon type="upload" />修改头像
            </a-button>
          </a-upload>
          <a-button type="primary" @click="handleRevisePassWord" class="headPortrait">修改密码</a-button>
        </a-col>
        <a-col :xs="{span:24}" :lg="{offset:4,span:16}">
          <div class="profile-deadline"></div>
        </a-col>
      </Card>
    </a-col>
    <a-col :xs="24" :lg="12" style="text-align: left;">
      <Card :name="''" class="layout">
        <div class="profile">
          <a-icon
            type="form"
            style="height: 40px; width: 40px; fontsize: 0.15rem; lineheight: 47px"
          />Profile
        </div>
        <a-descriptions :column="1">
          <a-descriptions-item v-for="item in personalInformationList" :key="item.title">
            <template slot="label">
              <span class="personalInformationList">
                <a-icon :type="item.type" />
                {{item.title}}
              </span>
            </template>
            <span class="personalInformationList">{{ item.nav }}</span>
          </a-descriptions-item>
        </a-descriptions>
        <!-- <a-col
          class="personalInformationList"
          :md="{ span: 24 }"
          :lg="{ span: 24 }"
          v-for="item in personalInformationList"
          :key="item.title"
        >
          <a-col :md="{ span: 24 }" :lg="{ span: 8 }">
            <a-icon :type="item.type" />
            {{ item.title }}:
          </a-col>
          <a-col :md="{ span: 24 }" :lg="{ span: 16 }">{{ item.nav }}</a-col>
        </a-col>-->
      </Card>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from "vuex";
import Card from '@/components/Card/Card.vue'
const config = require("../../../faceConfig");
export default {
  data () {
    return {
      headerImg: '',
      fileList: [],
      personalInformationList: [
        {
          title: "Username",
          type: "user",
          store: "name",
          nav: "",
        },
        {
          title: "Nickname",
          type: "heart",
          store: "show_name",
          nav: ""
        },
        {
          title: "Email",
          type: "mail",
          store: "email",
          nav: ""
        },
        {
          title: "key",
          type: "key",
          store: "key",
          nav: ""
        },
      ],
    }
  },
  components: { Card },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
      userinfo: "UserStore/userinfo"
    })
  },
  mounted () {
    this.handleSetUsetInfo(this.userinfo)
  },
  methods: {
    handleLoadError () {
      const imgURL = config.imgPath;
      this.headerImg = imgURL + "admin.jpg";
    },
    handleHeaderPhoto (info) {
      let fileList = [...info.fileList];
      this.fileList = fileList;
    },
    handleBeforeUpload (file) {
      const isJpgOrPng =
        file.type === "image/jpeg" ||
        file.type === "image/jpg" ||
        file.type === "image/png";
      if (!isJpgOrPng) {
        this.$message.error("只能上传jpg/png/jpeg格式的头像!");
      }
      const isLt10M = file.size / 1024 / 1024 < 10;
      const isLt10K = file.size / 1024 > 10;
      if (!isLt10M) {
        this.$message.error("图片不得大于10MB!");
      }
      if (!isLt10K) {
        this.$message.error("图片得大于10KB!");
      }
      return isJpgOrPng && isLt10M && isLt10K;
    },
    handleCustomRequest (file) {
      let params = new FormData();
      params.append("file", file.file);
      let progress = {
        percent: 0,
      };
      const intervalId = setInterval(() => {
        if (progress.percent < 100) {
          progress.percent += 25;
          file.onProgress(progress);
        } else {
          clearInterval(intervalId);
          if (this.handleBeforeUpload(file.file)) {
            this.$api.upload_avatar(params).then((res) => {
              if (res.code == 200) {
                file.onSuccess();
                this.fileList = [];
                this.$message.success("头像上传成功");
                this.$store.dispatch("UserStore/setUserinfo", this.token)
              } else {
                this.$message.error(res.message);
                file.onError();
              }
            });
          } else {
            console.log("false");
            this.fileList = [];
          }
        }
      }, 100);
    },
    handleSetUsetInfo (now) {
      const imgURL = config.imgPath;
      this.headerImg = imgURL + now.avatar;
      this.personalInformationList.map((item) => {
        for (let key in now) {
          if (item.store == key) item.nav = now[key]
        }
      })
    },
    handleRevisePassWord () {
      const _this = this
      _this.$router.push('/RevisePassWord')
    }
  },
  watch: {
    userinfo: {
      handler: function (now, old) {
        this.handleSetUsetInfo(now)
      },
      deep: true
    }
  }
}
</script>
<style lang="scss" scoped>
.profile {
  height: 40px;
  width: 100%;
  border-left: 5px solid #1890ff;
  font-size: 24px;
  line-height: 48px;
}
.personalInformationList {
  // width: 100%;
  font-size: 20px;
  line-height: 80px;
  // white-space: nowrap;
  // overflow: hidden;
  // text-overflow: ellipsis;
  // line-height: unset;
  // display: flex;
}
.layout {
  font-size: 24px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.profile-deadline {
  height: 54px;
  border-bottom: 4px solid #9ca4bf;
  padding: 0;
}
.headPortrait {
  margin-left: 10px;
}

.profile-deadline::after {
  content: "";
  position: absolute;
  background: url("../../assets/giphy.gif") no-repeat;
  background-size: 100% 100%;
  width: 50px;
  height: 50px;
  top: 15px;
  left: -25px;
  animation: Mario 5s linear infinite;
  -moz-animation: Mario 5s linear infinite;
  /* Firefox */
  -webkit-animation: Mario 5s linear infinite;
  /* Safari 和 Chrome */
  -o-animation: Mario 5s linear infinite;
  /* Opera */
}

@keyframes Mario {
  0% {
    left: -25px;
  }

  25% {
    top: 15px;
    transform: rotate(0deg);
  }

  28% {
    top: -10px;
    transform: rotate(360deg);
  }

  29% {
    top: -10px;
    transform: rotate(0);
  }

  31% {
    top: 15px;
    transform: rotate(0deg);
  }

  45% {
    left: calc(100% - 25px);
    transform: rotate(0deg);
    top: 15px;
  }

  50% {
    left: calc(100% - 25px);
    transform: rotate(180deg);
    top: 55px;
  }

  52% {
    left: calc(100% - 25px);
    transform: rotate(180deg);
    top: 55px;
  }

  95% {
    left: -25px;
    transform: rotate(180deg);
    top: 55px;
  }

  100% {
    left: -25px;
    transform: rotate(360deg);
    top: 15px;
  }
}
</style> 