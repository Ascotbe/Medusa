<template>
  <a-row
    :gutter="[
      { xs: 4, sm: 8, md: 12, lg: 16 },
      { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
    class="Layout"
  >
    <a-form :form="form" :layout="`vertical`" :wrapper-col="{ span: 14, offset: 4 }">
      <a-form-item>
        <img width="75%" :src="medusaUrl" />
      </a-form-item>
      <a-form-item>
        <a-input
          v-on:keyup.enter.native="handleLogin"
          v-decorator="[
            'userName',
            { rules: [{ required: true, message: '请输入user' }] }
          ]"
        >
          <a-icon slot="prefix" type="user" style="color: rgba(0, 0, 0, 0.25)" />
        </a-input>
      </a-form-item>
      <a-form-item>
        <a-input
          type="password"
          v-on:keyup.enter.native="handleLogin"
          v-decorator="[
            'passWord',
            {
              rules: [{ required: true, message: '请输入密码' }]
            }
          ]"
        >
          <a-icon slot="prefix" type="key" />
        </a-input>
      </a-form-item>
      <a-form-item>
        <a-col :xs="{ span: 15 }">
          <a-input
            v-on:keyup.enter.native="handleLogin"
            v-decorator="[
              'verificationCode',
              {
                rules: [{ required: true, message: '请输入验证码' }]
              }
            ]"
          ></a-input>
        </a-col>
        <a-col :xs="{ span: 8, offset: 1 }">
          <VerificationCode ref="verificationCode" />
        </a-col>
      </a-form-item>
      <a-form-item>
        <a-checkbox
          style="float: left"
          v-decorator="[
            'agreement',
            {
              valuePropName: 'checked',
              rules: [{ required: true, message: '请阅读相关协议' }]
            }
          ]"
          @change="handleChangeAgreement()"
        >
          <a style="color: #aaa">我已阅读并同意相关服务条款和使用协议</a>
        </a-checkbox>
      </a-form-item>
      <a-form-item>
        <a-col :sm="{ span: 24 }" :xl="{ span: 8 }">
          <MedusButton :title="`登录`" :btn_width="110" :btn_hight="40" :ClickPromise="handleLogin" />
        </a-col>
        <a-col :sm="{ span: 24 }" :xl="{ span: 8 }">
          <MedusButton
            :title="`注册`"
            :btn_width="110"
            :btn_hight="40"
            :ClickPromise="handleRegister"
          />
        </a-col>
        <a-col :sm="{ span: 24 }" :xl="{ span: 8 }">
          <MedusButton
            :title="`忘记密码`"
            :btn_width="110"
            :btn_hight="40"
            :ClickPromise="handleForget"
          />
        </a-col>
      </a-form-item>
    </a-form>

    <a-modal
      title="Medusa使用协议"
      :visible="visible"
      @ok="handleAgreementOk"
      @cancel="handleAgreementCancel"
    >
      <p>
        在原有的
        <a
          href="https://github.com/Ascotbe/Medusa/blob/master/LICENSE"
          style="color: #0366d6"
        >协议</a>中追加以下内容：
      </p>
      <ul>
        <li>本项目禁止进行未授权商业用途</li>
        <li>
          本项目仅面向
          <strong>合法授权</strong>的企业安全建设行为，在使用本项目进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。
        </li>
        <li>如您在使用本项目的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。</li>
        <li>
          在使用本项目前，请您
          <strong>务必审慎阅读、充分理解各条款内容</strong>，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。
          除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本项目。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
        </li>
      </ul>
    </a-modal>
  </a-row>
</template>

<script>
import MedusButton from '@/components/MedusButton/MedusButton.vue'
import VerificationCode from '@/components/VerificationCode/VerificationCode.vue'
import { mapGetters } from "vuex";
export default {
  data () {
    return {
      form: this.$form.createForm(this, { name: 'form' }),
      medusaUrl: require('@/assets/cover.png'),
      visible: false,
      verificationCodePath: ''
    }
  },
  components: {
    MedusButton,
    VerificationCode
  },
  computed: {
    ...mapGetters({
      verificationcodekey: "UserStore/verificationcodekey",
      token: "UserStore/token",
      userinfo: "UserStore/userinfo"
    }),
  },
  methods: {
    handleChangeAgreement () {
      this.visible = true
      this.$nextTick(() => {
        this.form.setFieldsValue({ agreement: false })
      })
    },
    handleAgreementOk () {
      this.visible = false
      this.form.setFieldsValue({ agreement: true })
    },
    handleAgreementCancel () {
      this.visible = false
      this.form.setFieldsValue({ agreement: false })
    },
    handleLogin () {
      this.form.validateFields((err, values) => {
        if (!err) {
          const params = {
            username: values.userName,
            passwd: values.passWord,
            verification_code_key: this.verificationcodekey,
            verification_code: values.verificationCode
          }
          this.$api.login(params).then((res) => {
            if (res.code == 200) {
              this.$message.success('登录成功,正在获取用户信息')
              this.$store.commit('UserStore/setToken', res.message)
              this.$store.dispatch('UserStore/setUserinfo', res.message)
              if (this.userinfo != {}) this.$router.push('./Layout')
            } else {
              this.$message.error(res.message)
              this.$refs.verificationCode.handleVerificationCode()
            }
          })
        } else {
          this.$message.warn('请输入完整信息')
        }
      })
    },
    handleForget () { },
    handleRegister () {
      this.$router.push('./Register')
    }
  }
}
</script>

<style lang="scss" scoped>
.Layout {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
