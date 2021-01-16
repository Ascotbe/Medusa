<template>
  <windows98 :task="task">
    <a-row class="updataPassword" :class="updataPasswordSize">
      <a-col :xs="xs" :sm="sm" class="updataPassword_nav" :class="updataPasswordNavSize">
        <div class="window" :class="windowSize">
          <div class="title-bar">
            <div class="title-bar-text">更新密码</div>
            <div class="title-bar-controls">
              <button aria-label="Minimize" @click="handelMinimize"></button>
              <button aria-label="Maximize" @click="handelMaximize"></button>
              <button aria-label="Close" @click="handelClose"></button>
            </div>
          </div>
          <div class="window-body">
            <div class="field-row">
              <label for="text17" class="label">Old password:</label>
              <input id="text17" type="password" class="input" v-model="form.old_pw" />
              <label for="text17" class="label labelEnd">{{ oldPassword }}</label>
            </div>
            <div class="field-row">
              <label for="text17" class="label">New Password:</label>
              <input
                id="text17"
                type="password"
                class="input"
                v-model="form.new_pw"
                v-on:input="handelChangePassWord"
              />
              <label for="text17" class="label labelEnd">{{ passwdLabel }}</label>
            </div>

            <div class="field-row">
              <label for="text17" class="label">Confirm PassWord:</label>
              <input
                id="text17"
                type="password"
                class="input"
                v-model="form.confirmPasswd"
                v-on:input="handelChangePassWord"
              />
              <label for="text17" class="label labelEnd">{{ passwdLabel }}</label>
            </div>
            <div class="field-row">
              <label for="text17" class="label">验证码:</label>
              <input
                id="text17"
                type="text"
                class="input"
                v-model="form.verificationCode"
              />
              <img
                width="100%"
                height="40px"
                :src="imgFilePath"
                @click="handleCAPTCHA"
                class="label labelEnd img"
              />
            </div>
            <div class="field-row">
              <button class="updataPasswordBtn" @click="handelupdataPassword">
                更新密码
              </button>
            </div>
          </div>
        </div>
      </a-col>
    </a-row>
  </windows98>
</template>

<script>
import windows98 from "../../../components/windows98";
export default {
  name: "setpassword",
  components: {
    windows98,
  },
  data() {
    return {
      // confirmDirty: false,
      task: "Updata Password",
      xs: { span: 24, offset: 0 },
      sm: { span: 12, offset: 6 },
      form: {
        old_pw: "",
        new_pw: "",
        confirmPasswd: "",
        verificationCode: "",
      },
      oldPassword: "请输入您的旧密码",
      passwdLabel: "",
      updataPasswordSize: "updataPasswordMini",
      updataPasswordNavSize: "updataPasswordNavMini",
      windowSize: "windowMini",
      imgFilePath: "",
    };
  },
  mounted() {
    this.handleCAPTCHA();
    this.handleGetUserinfo();
  },
  methods: {
    async handleCAPTCHA() {
      //获取验证码.
      this.imgFilePath = await this.$qj.QJGETCAPTCHA();
    },
    handleGetUserinfo() {
      if (
        this.$store.state.userinfo.name == null ||
        this.$store.state.userinfo.name == undefined
      ) {
        console.log(this.$store.state.userinfo);
        this.$message.error("未获取到您的用户信息请重新进入该界面");
        this.$router.push("/layout/personalSettings");
      }
    },
    handelChangePassWord() {
      if (this.form.confirmPasswd != "" || this.form.new_pw != "") {
        if (this.form.confirmPasswd == this.form.new_pw) {
          this.passwdLabel = "两次密码一致";
        } else {
          this.passwdLabel = "两次密码不一致";
        }
      } else {
        this.passwdLabel = "密码不能为空";
      }
    },
    handelMinimize() {
      this.updataPasswordSize = "updataPasswordMini";
      this.updataPasswordNavSize = "updataPasswordNavMini";
      this.windowSize = "windowMini";
      this.sm = { span: 12, offset: 6 };
    },
    handelMaximize() {
      this.updataPasswordSize = "updataPasswordMax";
      this.updataPasswordNavSize = "updataPasswordNavMax";
      this.windowSize = "windowMax";
      this.sm = { span: 24, offset: 0 };
    },
    handelClose() {
      this.$router.push("/layout/personalSettings");
    },
    handelupdataPassword() {
      let form = this.form;
      if (
        form.verificationCode != "" &&
        form.old_pw != "" &&
        form.new_pw != "" &&
        form.confirmPasswd != "" &&
        form.new_pw == form.confirmPasswd
      ) {
        let params = {
          username: this.$store.state.userinfo.name,
          old_passwd: form.old_pw,
          new_passwd: form.new_pw,
          verification_code_key: this.$store.state.verificationcodekey,
          verification_code: form.verificationCode,
        };
        this.$api.update_password(params).then((res) => {
          if (res.code == 200) {
            this.$message.success("密码修改成功，请重新登录");
            localStorage.setItem("storeToken", "");
            this.$store.commit("close");
            this.$router.push("/");
          } else if (res.code == 503) {
            this.$message.error("验证码错误");
            this.handleCAPTCHA();
          } else {
            this.$message.error("服务器卡住了，请稍后再试");
            this.handleCAPTCHA();
          }
        });
      } else {
        this.$message.warning("请填写完整");
      }
    },
  },
};
</script>
<style src="../../../../node_modules/98.css/dist/98.css" scoped></style>
<style lang="scss" scoped>
.updataPassword {
  height: 100%;
  .updataPassword_nav {
    min-width: 320px;
    // position: absolute;
    z-index: 15;
    // transition: all 1s;
    // height: 100%;
    // align-self: center;
    .window {
      .title-bar {
        width: 100%;
        align-self: flex-start;
      }
      .window-body {
        width: 100%;
        margin: 0;
        .field-row {
          margin: 20px auto 20px auto;
          width: 80%;
          min-width: 300px;
          .label {
            font-size: 18px;
            width: 25%;
            min-width: 95px;
            max-width: 190px;
          }
          .labelEnd {
            font-size: 12px;
            max-width: 100px;
            // color: rgb(0, 255, 0);
          }
          .img {
            cursor: pointer;
          }
          .input {
            font-size: 18px;
            height: 25px;
            width: 75%;
            min-width: 110px;
          }
          .updataPasswordBtn {
            margin: 0 auto;
          }
        }
      }
    }
  }
}
.updataPasswordMax {
  display: flex;
  .updataPasswordNavMax {
    height: 100%;
    // align-self: center;
    .windowMax {
      height: 100%;
      display: -webkit-flex; /* Safari */
      display: flex;
      // flex-direction:column;
      align-items: flex-start;
      // justify-content: center; // 垂直居中
      flex-wrap: wrap;
    }
  }
}
.updataPasswordMini {
  display: flex;
  .updataPasswordNavMini {
    // height: 410px;
    align-self: center;
    .windowMini {
    }
  }
}
</style>
