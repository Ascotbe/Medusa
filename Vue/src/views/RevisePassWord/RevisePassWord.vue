<template>
  <Win98 ref="win98" @Ok="handleRegister" :task="`Revise PassWord`">
    <a-row
      type="flex"
      justify="center"
      align="top"
      style="height:100%"
      :gutter="[
     16, { xs: 4, sm: 8, md: 12, lg: 16 }
    ]"
    >
      <a-col :span="24">
        <a-form :form="form" :labelCol="{xs:8,lg:6}" :wrapper-col="{ span: 14,offset:1 }">
          <a-form-item label="UserName">
            <a-input
              disabled
              v-decorator="[
            'username',
            { rules: [{ required: true, message: 'UserName Cannot be empty' }] }
          ]"
            >
              <a-icon slot="prefix" type="user" style="color: rgba(0, 0, 0, 0.25)" />
            </a-input>
          </a-form-item>

          <a-form-item label="OldPassWord">
            <a-input
              type="password"
              v-decorator="[
            'old_passwd',
            { rules: [{ required: true, message: 'OldPassWord Cannot be empty' }] }
          ]"
            >
              <a-icon slot="prefix" type="unlock" style="color: rgba(0, 0, 0, 0.25)" />
            </a-input>
          </a-form-item>
          <a-form-item label="NewPassWord">
            <a-input
              type="password"
              v-decorator="[
            'new_passwd',
            {rules: [{ required: true, message: 'NewPassWord Cannot be empty' },{validator:(rule, value, callback)=>this.handlePassWord(rule, value, callback)}] }
          ]"
            >
              <a-icon slot="prefix" type="unlock" style="color: rgba(0, 0, 0, 0.25)" />
            </a-input>
          </a-form-item>
          <a-form-item label="ConfirmPassWord">
            <a-input
              type="password"
              v-decorator="[
            'confirmpasswd',
            { rules: [{ required: true, message: 'ConfirmPassWord  Cannot be empty' },{validator:(rule, value, callback)=>this.handlePassWord(rule, value, callback)}] }
          ]"
            >
              <a-icon slot="prefix" type="unlock" style="color: rgba(0, 0, 0, 0.25)" />
            </a-input>
          </a-form-item>
          <a-form-item label="VerificationCode" :wrapper-col="{ span: 14,offset:1 }">
            <a-col :span="12">
              <a-input
                v-decorator="[
            'verificationCode',
            { rules: [{ required: true, message: 'VerificationCode  Cannot be empty' }] }
          ]"
              ></a-input>
            </a-col>
            <a-col :span="10" :offset="2">
              <VerificationCode ref="verificationCode" style="height: 30px;" />
            </a-col>
          </a-form-item>
        </a-form>
      </a-col>
    </a-row>
  </Win98>
</template>

<script>
import Win98 from "@/components/Win98/Win98.vue"
import { mapGetters } from "vuex";
import VerificationCode from '@/components/VerificationCode/VerificationCode.vue'
export default {
  data () {
    return {
      form: this.$form.createForm(this, { name: 'form' }),
      checkPasswd: false,
      checkConfirmPasswd: false
    }
  },
  components: {
    Win98,
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
    handleRegister () {
      const _this = this
      _this.form.validateFields((err, values) => {
        if (!err) {
          const params = {
            username: values.username,
            old_passwd: values.old_passwd,
            new_passwd: values.new_passwd,
            verification_code_key: _this.verificationcodekey,
            verification_code: values.verificationCode,
          }
          _this.$api.update_password(params).then((res) => {
            if (res.code == 200) {
              _this.$store.commit('UserStore/setToken', '')
              const success = {
                title: 'Success',
                message: 'register has success:需要重新登录,是否跳转到登录页?'
              }
              const callback = () => {
                this.$router.push("/login");
              }
              _this.$refs.win98.handleErrShow(success, callback)
            } else {
              const err = {
                title: 'Err',
                message: `register has failed:${res.message}`
              }
              _this.$refs.win98.handleErrShow(err)
              _this.$refs.verificationCode.handleVerificationCode()
            }
          });
        }
        else {
          const warn = {
            title: 'Warn',
            message: 'Please complete all form items'
          }
          _this.$refs.win98.handleErrShow(warn)
        }
      })
    },
    handlePassWord (rule, value, callback) {
      const _this = this
      const form = _this.form.getFieldsValue()
      if (value == undefined) {
        callback('Is Null')
      }
      else {
        if (rule.field == 'new_passwd') {
          if (value == form.confirmpasswd) {
            _this.checkPasswd = true
            if (_this.checkConfirmPasswd && _this.checkPasswd) {
              _this.checkConfirmPasswd = false
              _this.checkPasswd = false
            }
            else {
              _this.form.validateFields(["confirmpasswd"])
            }
            callback()
          }
          else {
            _this.checkPasswd = false
            callback('The two passwords are inconsistent')
          }
        }
        else if (rule.field == 'confirmpasswd') {
          if (value == form.new_passwd) {
            _this.checkConfirmPasswd = true
            if (_this.checkConfirmPasswd && _this.checkPasswd) {
              _this.checkConfirmPasswd = false
              _this.checkPasswd = false
            }
            else {
              _this.form.validateFields(["new_passwd"])
            }
            callback()
          }
          else {
            _this.checkConfirmPasswd = false
            callback('The two passwords are inconsistent')
          }
        }
      }

    }
  },
  mounted () {
    const _this = this
    _this.form.setFieldsValue({ username: _this.userinfo.name })
  }

}
</script>

<style>
</style>