<template>
  <a-row
    type="flex"
    justify="center"
    align="middle"
    style="height:100%"
    :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
  >
    <a-col :span="12">
      <a-avatar
        shape="circle"
        icon="user"
        :src="headerImg"
        :loadError="handleLoadError"
        :size="180"
      />
      <a-col :span="24">{{userinfo.name}}</a-col>
      <a-col :span="24">{{userinfo.email}}</a-col>
      <a-col :span="24">
        <a-button type="primary" style="margin-right:15px">修改密码</a-button>
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
      </a-col>
    </a-col>
    <a-col :span="12" style="text-align: left;">
      <div class="profile">
        <a-icon type="form" style="height: 40px; width: 40px; fontsize: 0.15rem; lineheight: 47px" />Profile
      </div>
      <a-col
        class="personalInformationList"
        :xs="{ span: 24 }"
        :lg="{ span: 24 }"
        v-for="item in personalInformationList"
        :key="item.title"
      >
        <span :xs="{ span: 16 }" :lg="{ span: 8 }">
          <a-icon :type="item.type" />
          {{ item.title }}:
        </span>
        <span :xs="{ span: 16 }" :lg="{ span: 12 }">{{ item.nav }}</span>
      </a-col>
    </a-col>
  </a-row>
</template>

<script>
import { mapGetters } from "vuex";
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
      ]
    }
  },
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
      console.log(isJpgOrPng);
      if (!isJpgOrPng) {
        this.$message.error("只能上传jpg/png/jpeg格式的头像!");
      }
      // console.log(file.size);
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
      console.log(params);
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
  height: 20px;
  width: 100%;
  font-size: 20px;
  line-height: 40px;
  margin-top: 20px;
  line-height: unset;
}
</style> 