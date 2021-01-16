<template>
  <div class="login">
    <a-row
      :gutter="[
        { xs: 8, sm: 16, md: 24, xs: 8 },
        { xs: 4, sm: 6, md: 8, lg: 10 },
      ]"
      class="login_nav"
    >
      <a-form-model
        :model="form"
        :label-col="labelCol"
        :wrapper-col="wrapperCol"
        :rules="rules"
        ref="ruleForm"
      >
        <a-form-model-item>
          <img width="100%" height="100%" src="./cover.png" />
        </a-form-model-item>
        <a-form-model-item prop="userName">
          <a-input v-model="form.userName" placeholder="UserName">
            <a-icon slot="prefix" type="user" style="color: rgba(0, 0, 0, 0.25)" />
          </a-input>
        </a-form-model-item>
        <a-form-model-item prop="passWord">
          <a-input v-model="form.passWord" placeholder="PassWord" type="password">
            <a-icon slot="prefix" type="lock" style="color: rgba(0, 0, 0, 0.25)" />
          </a-input>
        </a-form-model-item>
        <a-form-model-item prop="verificationCode">
          <a-col :xs="{ span: 15 }">
            <a-input v-model="form.verificationCode" placeholder="请输入验证码">
            </a-input>
          </a-col>
          <a-col :xs="{ span: 8, offset: 1 }">
            <img
              width="100%"
              height="40px"
              :src="imgFilePath"
              @click="handleCAPTCHA"
              class="img"
            />
          </a-col>
        </a-form-model-item>
        <a-form-model-item prop="clause">
          <a-checkbox :disabled="checkboxDisabled" :checked="form.clause">
            <a
              @click="
                () => {
                  this.visible = true;
                }
              "
              style="color: #aaa"
              >我已阅读并同意相关服务条款和使用协议</a
            >
          </a-checkbox>
          <a-modal
            title="Medusa使用协议"
            :visible="visible"
            @ok="handleOk"
            @cancel="handleCancel"
          >
            <p>
              在原有的<a
                href="https://github.com/Ascotbe/Medusa/blob/master/LICENSE"
                style="color: #0366d6"
                >协议</a
              >中追加以下内容：
            </p>
            <ul>
              <li>本项目禁止进行未授权商业用途</li>
              <li>
                本项目仅面向<strong>合法授权</strong>的企业安全建设行为，在使用本项目进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。
              </li>
              <li>
                如您在使用本项目的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
              </li>
              <li>
                在使用本项目前，请您<strong>务必审慎阅读、充分理解各条款内容</strong>，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。
                除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本项目。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
              </li>
            </ul>
          </a-modal>
        </a-form-model-item>

        <a-form-model-item>
          <a-col :xs="{ span: 24 }" :sm="{ span: 8 }" class="col_mybtn">
            <Mybtn
              :title="loginbtn"
              :btn_width="110"
              :btn_hight="40"
              :ClickPromise="handleLogin"
            />
          </a-col>
          <a-col :xs="{ span: 24 }" :sm="{ span: 8 }" class="col_mybtn">
            <Mybtn
              :title="regbtn"
              :btn_width="110"
              :btn_hight="40"
              :ClickPromise="handleRegister"
            />
          </a-col>
          <a-col :xs="{ span: 24 }" :sm="{ span: 8 }" class="col_mybtn">
            <Mybtn
              :btn_width="110"
              :btn_hight="40"
              :title="forget"
              :ClickPromise="handleForget"
            />
          </a-col>
        </a-form-model-item>
      </a-form-model>
    </a-row>
  </div>
</template>

<script>
import Mybtn from "../../components/Mybtn.vue";
export default {
  data() {
    // let validatorClause = (rule, value, callback) => {
    //   //验证条款效验
    //   if (value) {
    //     callback();
    //   }
    //   callback("请认真阅读并同意Medusa服务条款");
    // };
    return {
      loginbtn: "登陆",
      regbtn: "注册",
      forget: "忘记密码",
      checkboxDisabled: true,
      visible: false,
      form: {
        userName: "",
        passWord: "",
        clause: false, //条款
        verificationCode: "", //验证码
      },
      imgFilePath: "", //二进制图片验证码数据
      rules: {
        userName: [
          {
            required: true,
            message: "请输入用户名",
            whitespace: true,
          },
        ],
        passWord: [
          {
            required: true,
            message: "请输入密码",
            whitespace: true,
          },
        ],
        verificationCode: [
          {
            trigger: "blur",
            required: true,
            message: "请输入验证码",
            whitespace: true,
          },
        ],
        clause: [
          {
            validator: this.validatorClause,
          },
        ],
      },
      labelCol: {
        span: 6,
      },
      wrapperCol: {
        xxl: { span: 6, offset: 9 },
        xl: { span: 8, offset: 8 },
        md: { span: 12, offset: 6 },
        sm: { span: 16, offset: 4 },
        xs: { span: 20, offset: 2 },
      },
    };
  },
  components: {
    Mybtn,
  },
  mounted() {
    this.handleCAPTCHA();
  },
  methods: {
    handleForget() {
      this.$router.push("/Forget");
    },
    async handleCAPTCHA() {
      //获取验证码.
        this.imgFilePath = await this.$qj.QJGETCAPTCHA()
    
    },
    validatorClause(rule, value, callback) {
      //验证条款效验
      if (value) {
        callback();
      }
      callback("请认真阅读并同意Medusa服务条款");
    },
    handleOk() {
      this.form.clause = true;
      this.visible = false;
    },
    handleCancel() {
      this.form.clause = false;
      this.checkboxDisabled = true;
      this.visible = false;
    },
    handleLogin() {
      // this.$refs.form.onSubmit();
      // this.$router.push('/layout');
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          let form = this.form;
          let params = {
            username: form.userName,
            passwd: form.passWord,
            verification_code_key: this.$store.state.verificationcodekey,
            verification_code: form.verificationCode,
          };
          console.log(params);
          this.$api.login(params).then((res) => {
            if (res.code == 200) {
              this.$message.success("登录成功,正在获取用户信息");
              this.$store.commit("tokenLogin", res.message);
              let token = {
                token: res.message,
              };
              console.log("1");
              this.$api.user_info(token).then((res) => {
                if (res.code == 200) {
                  this.$message.success("欢迎" + res.message.show_name);
                  let userinfo = {
                    email: res.message.email,
                    name: res.message.name,
                    show_name: res.message.show_name,
                    key: res.message.key,
                  };
                  this.$store.commit("userinfo", userinfo);
                  let avatar = res.message.avatar;
                  this.$store.commit("avatar", avatar);
                  this.$router.push("/layout");
                } else {
                  this.$message.error("您的信息好像获取不到，请稍后再试");
                }
              });
            } else {
              this.$message.error(res.message);
              this.handleCAPTCHA();
            }
          });
        } else {
          this.$message.error("请填写内容");
          return false;
        }
      });
    },
    handleRegister() {
      this.$router.push("/register");
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  height: 100%;
  display: flex;
  .login_nav {
    align-self: center;
  }
}
.img {
  cursor: pointer;
}
</style>
