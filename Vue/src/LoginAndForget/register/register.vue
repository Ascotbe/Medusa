<template>
  <windows98 :task="task">
    <a-row class="register" :class="registerSize">
      <a-col :xs="xs" :sm="sm" class="register_nav" :class="registerNavSize">
        <div class="window" :class="windowSize">
          <div class="title-bar">
            <div class="title-bar-text">注册</div>
            <div class="title-bar-controls">
              <button aria-label="Minimize" @click="handelMinimize"></button>
              <button aria-label="Maximize" @click="handelMaximize"></button>
              <button aria-label="Close" @click="handelClose"></button>
            </div>
          </div>
          <div class="window-body">
            <div class="field-row">
              <label for="text17" class="label">key:</label>
              <input id="text17" type="text" class="input" v-model="form.key" />
              <label for="text17" class="label labelEnd">{{ keyLabel }}</label>
            </div>
            <div class="field-row">
              <label for="text17" class="label">E-mail:</label>
              <input
                id="text17"
                type="text"
                class="input"
                v-model="form.email"
                v-on:input="handelChangeEmail"
              />
              <label for="text17" class="label labelEnd">{{ EmailLabel }}</label>
            </div>
            <div class="field-row">
              <label for="text17" class="label">Password:</label>
              <input
                id="text17"
                type="password"
                class="input"
                v-model="form.passwd"
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
              <label for="text17" class="label">Showname:</label>
              <input id="text17" type="text" class="input" v-model="form.showname" />
              <label for="text17" class="label labelEnd">{{ shownameLabel }}</label>
            </div>
            <div class="field-row">
              <label for="text17" class="label">Username:</label>
              <input id="text17" type="text" class="input" v-model="form.username" />
              <label for="text17" class="label labelEnd">{{ usernameLabel }}</label>
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
              <button class="registerBtn" @click="handelRegister">注册</button>
            </div>
          </div>
        </div>
      </a-col>
    </a-row>
  </windows98>
</template>

<script>
import windows98 from "../../components/windows98";
export default {
  name: "Register",
  components: {
    windows98,
  },
  data() {
    return {
      task:'Register User',
      xs: { span: 24, offset: 0 },
      sm: { span: 12, offset: 6 },
      form: {
        key: "",
        email: "",
        passwd: "",
        confirmPasswd: "",
        showname: "",
        username: "",
        verificationCode: "",
      },
      keyLabel: "请输入您的Key",
      shownameLabel: "请输入您的显示名",
      usernameLabel: "请输入您的用户名",
      EmailLabel: "",
      passwdLabel: "",
      registerSize: "registerMini",
      registerNavSize: "registerNavMini",
      windowSize: "windowMini",
      imgFilePath: "",
    };
  },
  beforeCreate() {
    this.form = this.$form.createForm(this, {
      name: "register",
    });
  },
  mounted() {
    this.handleCAPTCHA();
  },
  methods: {
    handelChangePassWord() {
      if (this.form.confirmPasswd != "" || this.form.passwd != "") {
        if (this.form.confirmPasswd == this.form.passwd) {
          console.log("两次密码一致");
          this.passwdLabel = "两次密码一致";
        } else {
          console.log("两次密码不一致");
          this.passwdLabel = "两次密码不一致";
        }
      } else {
        this.passwdLabel = "密码不能为空";
      }
    },
    handelChangeEmail() {
      let ruleEmail = /^[A-Za-zd0-9]+([-_.][A-Za-zd]+)*@([A-Za-zd]+[-.])+[A-Za-zd]{2,5}$/;
      if (this.form.email != "") {
        if (ruleEmail.test(this.form.email)) {
          this.EmailLabel = "邮箱格式正确";
        } else {
          this.EmailLabel = "邮箱格式错误";
        }
      } else {
        this.EmailLabel = "邮箱不能为空";
      }
    },
    handelMinimize() {
      this.registerSize = "registerMini";
      this.registerNavSize = "registerNavMini";
      this.windowSize = "windowMini";
      this.sm = { span: 12, offset: 6 };
    },
    handelMaximize() {
      this.registerSize = "registerMax";
      this.registerNavSize = "registerNavMax";
      this.windowSize = "windowMax";
      this.sm = { span: 24, offset: 0 };
    },
    handelClose() {
      this.$router.push("/");
    },
    async handleCAPTCHA() {
      //获取验证码.
      this.imgFilePath = await this.$qj.QJGETCAPTCHA();
    },
    handelRegister() {
      let form = this.form;
      if (
        form.verificationCode != "" &&
        form.key != "" &&
        form.email != "" &&
        form.passwd != "" &&
        form.confirmPasswd != "" &&
        form.showname != "" &&
        form.username != ""&&
        form.passwd  == form.confirmPasswd
      ) {
        let params = {
          key: form.key,
          show_name: form.showname,
          username: form.username,
          passwd: form.passwd,
          email: form.email,
          verification_code_key: this.$store.state.verificationcodekey,
          verification_code: form.verificationCode,
        };
        this.$api.registered(params).then((res) => {
          console.log(res);
          if (res.code == 200) {
            this.$message.success("注册成功");
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
<style src="../../../node_modules/98.css/dist/98.css" scoped></style>
<style lang="scss" scoped>
.register {
  height: 100%;
  // display: flex;

  .register_nav {
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
             font-size:18px;
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
          .registerBtn {
            margin: 0 auto;
          }
        }
      }
    }
  }
}
.registerMax {
  display: flex;
  .registerNavMax {
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
.registerMini {
  display: flex;
  .registerNavMini {
    // height: 410px;
    align-self: center;
    .windowMini {
    }
  }
}
</style>
