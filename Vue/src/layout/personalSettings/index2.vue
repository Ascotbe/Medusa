<template>
  <div class="personalSettings">
    <a-row :gutter="[16, 64]">
      <a-col class="profile-left" :xs="{ span: 24 }" :lg="{ span: 11 }">
        <a-col class="profile-info" :xs="{ span: 24 }" :lg="{ span: 24 }">
          <a-avatar
            shape="square"
            class="profile-avatar"
            icon="user"
            :src="title"
            :loadError="handleLoadError"
            :size="180"
          />
          <div class="profile-name">{{ personalInformationList[0].nav }}</div>
          <div class="profile-email">{{ personalInformationList[2].nav }}</div>
          <a-col
            class="profile-operation"
            :xs="{ span: 14, offset: 5 }"
            :sm="{ span: 10, offset: 7 }"
            :md="{ span: 8, offset: 8 }"
            :lg="{ span: 14, offset: 5 }"
            :xl="{ span: 14, offset: 5 }"
            :xxl="{ span: 8, offset: 8 }"
          >
            <button
              type="button"
              class="ant-btn profile-operate ant-btn-primary"
              @click="handleUpdataPassword"
            >
              <span>修改密码</span>
            </button>
           
            <a-upload
              name="file"
              :customRequest="handleCustomRequest"
              @change="handle_Change"
              :file-list="fileList"
            >
              <a-button> <a-icon type="upload" /> 修改头像 </a-button>
            </a-upload>
          </a-col>
          <a-col :xs="{ span: 16, offset: 4 }" :lg="{ span: 16, offset: 4 }">
            <div class="profile-deadline"></div>
          </a-col>
        </a-col>
      </a-col>
      <a-col class="profile-right" :xs="{ span: 24 }" :lg="{ span: 10 }">
        <div class="profile-main">
          <a-col class="profile" :xs="{ span: 24 }" :lg="{ span: 24 }">
            <a-icon
              type="form"
              style="height: 40px; width: 40px; fontsize: 0.15rem; lineheight: 47px"
            />Profile
          </a-col>
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
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  name: "personalSettings2",
  
  data() {
    return {
      title: require("../../assets/avatar.png"),
      personalInformationList: [
        {
          title: "Username",
          type: "user",
          nav: "",
        },
        {
          title: "Nickname",
          type: "heart",
          nav: "",
        },
        {
          title: "Email",
          type: "mail",
          nav: "",
        },
        {
          title: "Mobile",
          type: "mobile",
          nav: "",
        },
        {
          title: "Verification",
          type: "unlock",
          nav: "",
        },
        {
          title: "Identifier",
          type: "rocket",
          nav: "",
        },
        {
          title: "API Token",
          type: "key",
          nav: "",
        },
        {
          title: "DNS Rebinding",
          type: "hourglass",
          nav: "",
        },
      ],
      fileList: [],
    };
  },
  computed: {
    getAvatar() {
      return this.$store.state.avatar;
    },
  },
  watch: {
    getAvatar: function (old, newd) {
      const config = require("../../../faceConfig");
      const imgURL = config.imgPath;
      this.title = imgURL + old;
    },
  },
  mounted() {
    this.handleSetPersonalInformationList();
  },
  methods: {
    handleSetPersonalInformationList() {
      const config = require("../../../faceConfig");
      const imgURL = config.imgPath;
      if (this.$store.state.userinfo.name != undefined) {
        let userinfo = this.$store.state.userinfo;
        console.log("获取vuex" + userinfo);
        this.title = imgURL + this.$store.state.avatar;
        this.personalInformationList = [
          {
            title: "Username",
            type: "user",
            nav: userinfo.name,
          },
          {
            title: "Nickname",
            type: "heart",
            nav: userinfo.show_name,
          },
          {
            title: "Email",
            type: "mail",
            nav: userinfo.email,
          },
          {
            title: "key",
            type: "key",
            nav: userinfo.key,
          },
        ];
      } else {
        console.log("请求后台");
        let params = {
          token: this.$store.state.storeToken,
        };
        this.$api.user_info(params).then((res) => {
          if (res.code == 200) {
            let user = res.message;
            this.title = imgURL + user.avatar;
            this.personalInformationList = [
              {
                title: "Username",
                type: "user",
                nav: user.show_name,
              },
              {
                title: "Nickname",
                type: "heart",
                nav: user.name,
              },
              {
                title: "Email",
                type: "mail",
                nav: user.email,
              },
              {
                title: "key",
                type: "key",
                nav: user.key,
              },
            ];
            let userinfo = {
              email: res.message.email,
              name: res.message.name,
              show_name: res.message.show_name,
              key: res.message.key,
            };
            this.$store.commit("userinfo", userinfo);
            let avatar = res.message.avatar;
            this.$store.commit("avatar", avatar);
          } else {
            this.$message.error("登录失败，请重新登录");
            this.$router.push("/");
          }
        });
      }
    },
    handleUpdataPassword(){
        this.$router.push('/setpassword')
    },
 
    handleBeforeUpload(file) {
      console.log(file);
      const isJpgOrPng =
        file.type === "image/jpeg" ||
        file.type === "image/jpg" ||
        file.type === "image/png";
      if (!isJpgOrPng) {
        this.$message.error("只能上传jpg/png格式的头像!");
      }
      console.log(file.size);
      const isLt10M = file.size / 1024 / 1024 < 10;
      const isLt10K = file.size / 1024 > 10;
      if (!isLt10M) {
        this.$message.error("图片不得大于10MB!");
      }
      if (!isLt10K) {
        this.$message.error("图片得大于10KB!");
        //  file.onError()
      }
      return isJpgOrPng && isLt10M && isLt10K;
    },
    handle_Change(info) {
      let fileList = [...info.fileList];
      this.fileList = fileList;
    },
    handleCustomRequest(file) {
      let params = new FormData();
      params.append("file", file.file);
      // await this.handleChange(file);
      console.log(file);
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
                this.$store.commit("avatar", res.message);
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
    handleLoadError() {
      console.log("error");
      const config = require("../../../faceConfig");
      const imgURL = config.imgPath;
      this.title = imgURL + "admin.jpg";
    },
  },
};
</script>

<style lang="scss" scoped>
.personalSettings {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 20px;
  padding-top: 30px;
  background: #fff;
}

.ant-btn {
  font-size: 12px;
}

.profile-left,
.profile-right {
  padding: 5px 0;

  .profile-info {
    margin: 0 auto;
    text-align: center;

    .profile-avatar {
      display: inline-block;
      width: 80px;
      height: 80px;
      border-radius: 50%;
      overflow: hidden;
      border: 0;
      font-size: 0;
    }

    .profile-name {
      font-size: 22px;
      line-height: 50px;
      font-weight: 700;
      color: #000;
    }

    .profile-email {
      font-size: 18px;
      color: #888;
    }

    .profile-operation {
      display: -ms-flexbox;
      display: flex;
      -ms-flex-pack: justify;
      justify-content: space-between;
    }

    .profile-deadline {
      height: 54px;
      border-bottom: 4px solid #9ca4bf;
      padding: 0;
    }

    .profile-deadline::after {
      content: "";
      position: absolute;
      background: url("../../assets/giphy.gif") no-repeat;
      background-size: 100% 100%;
      width: 50px;
      height: 50px;
      top: 38px;
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
        top: 38px;
        transform: rotate(0deg);
      }

      28% {
        top: 0px;
        transform: rotate(360deg);
      }

      29% {
        top: 0px;
        transform: rotate(0);
      }

      31% {
        top: 38px;
        transform: rotate(0deg);
      }

      45% {
        left: calc(100% - 25px);
        transform: rotate(0deg);
        top: 38px;
      }

      50% {
        left: calc(100% - 25px);
        transform: rotate(180deg);
        top: 80px;
      }

      52% {
        left: calc(100% - 25px);
        transform: rotate(180deg);
        top: 80px;
      }

      95% {
        left: -25px;
        transform: rotate(180deg);
        top: 80px;
      }

      100% {
        left: -25px;
        transform: rotate(360deg);
        top: 38px;
      }
    }
  }
}

.profile-main {
  padding: 0.12rem 0.12rem;

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
}
</style>
