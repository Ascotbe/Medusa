import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    storeToken: localStorage.getItem('storeToken')?localStorage.getItem('storeToken'):'',
    userinfo:{},
    avatar:'',
    active_scan_id:'null',//主动扫描目标单个漏洞详细内容查询key
    scan_info_id:'null',//主动扫描目标单个漏洞详细内容查询接口
    project_associated_file_name:'null',//查询跨站脚本钓鱼项目中生成的特殊文件名
    verificationcodekey:'',//验证码的key
    collapsed:false//layout的侧边栏变化
  },
  mutations: {
    close(state){
      state.storeToken ='',
      state.userinfo={}
    },
    tokenLogin(state,usertoken){
      state.storeToken=usertoken
      localStorage.setItem('storeToken',state.storeToken)
      console.log(state.storeToken)
    },
    userinfo(state,userinfo){
      state.userinfo=userinfo
      console.log(state.userinfo)
    },
    avatar(state,avatar){
      state.avatar = avatar
      console.log(state.avatar)
    },
    active_scan_id(state,active_scan_id){
      state.active_scan_id = active_scan_id
    },
    scan_info_id(state,scan_info_id){
      state.scan_info_id=scan_info_id
    },
    project_associated_file_name(state,project_associated_file_name){
      state.project_associated_file_name=project_associated_file_name
    },
    verificationcodekey(state,verificationcodekey){
      state.verificationcodekey=verificationcodekey
    },
    collapsed(state,collapsed){
      state.collapsed=collapsed
    }
  },
  actions: {
  },
  modules: {
  }
})
