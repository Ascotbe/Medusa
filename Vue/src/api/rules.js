import {
  get,
  post,
  postDownload
} from './request'
import {
  // 用户
  URL_POST_LOGIN,
  URL_POST_REGISTERED,
  URL_POST_GETINFO,
  URL_POST_UPDATE_PASSWORD,
  URL_POST_FORGET_PASSWORD,
  URL_POST_UPLOAD_AVATAR,
  URL_GET_VERIFICATION_CODE,

  //首页
  URL_POST_HOMEPAGE_DEFAULT_DATA,
  URL_POST_HOMEPAGE_GITHUB_MONITOR_DATA,
  URL_POST_HOMEPAGE_VULNERABILITY_DISTRIBUTIONT_DATA,
  URL_POST_HARDWARE_INITIALIZATION,
  URL_POST_HARDWARE_USAGE_QUERY,

  //工具库
  URL_POST_ANTIVIRUS_SOFTWARE_COMPARED,

  //cve监控
  URL_POST_GITHUB_MONITOR,
  URL_POST_GITHUB_MONITOR_SEARCH,
  URL_POST_NIST_DATA_BULK_QUERY,
  URL_POST_NIST_SEARCH,
  URL_POST_NIST_SEARCH_STATISTICS,
  URL_POST_NIST_STATISTICS,
  URL_POST_NIST_DATA_DETAILED_QUERY,



  URL_POST_SCANNING,
  URL_POST_LIST_QUERY,
  URL_POST_PORT_INFORMATION,
  URL_POST_INFOMATION_QUERY,
  URL_POST_MEDUSA_QUERY,
  URL_POST_GENERATE_WORD,
  URL_POST_DOWNLOAD_WORD,

  //XSS平台
  URL_POST_CREATE_SCRIPT_PROJECT,
  URL_POST_QUERY_SCRIPT_PROJECT,
  URL_POST_QUERY_SCRIPT_PROJECT_DATA,
  URL_POST_STATISTICAL_CROSS_SITE_SCRIPT_PROJECT_DATA,
  URL_POST_STATISTICAL_CROSS_SITE_SCRIPT_PROJECT,
  URL_POST_QUERY_SCRIPT_PROJECT_INFO,
  URL_POST_MODIFY_CROSS_SITE_SCRIPT_PROJECT,
  URL_POST_READ_SCRIPT_TEMPLATE,
  URL_POST_READ_DEFAULT_SCRIPT_TEMPLATE,
  URL_POST_SAVE_CROSS_SITE_SCRIPT_TEMPLATE,
  URL_POST_MODIFY_CROSS_SITE_SCRIPT_TEMPLATE,


  //协同作战
  URL_POST_CREATE_MARKDOWN_PROJECT,
  URL_POST_QUERY_MARKDOWN_PROJECT, // 查询协同作战项目
  URL_POST_QUERY_MARKDOWN_DATA, //用来查询Markdown文档数据
  URL_POST_SAVE_MARKDOWN_DATA,
  URL_POST_MARKDOWN_IMAGE_UPLOAD,
  URL_POST_MARKDOWN_DATA_COMPARISON,
  URL_POST_JOIN_MARKDOWN_PROJECT,
  URL_POST_MARKDOWN_PROJECT_STATISTICAL,

} from './url'
import store from '@/store'

const api = {
  // 登陆接口
  async login (params) {
    let response = await post(URL_POST_LOGIN, params, {
      headers: {}
    })
    return response
  },
  // 注册接口
  async registered (params) {
    let response = await post(URL_POST_REGISTERED, params, {
      headers: {}
    })
    return response
  },
  // 获取验证码
  async get_verification_code (params) {
    let response = await get(URL_GET_VERIFICATION_CODE, params, {
      headers: {},
      responseType: 'blob',
    })
    return response
  },

  // 忘记密码
  async forget_password (params) {
    let response = await post(URL_POST_FORGET_PASSWORD, params, {
      headers: {}
    })
    return response
  },
  // 扫描任务下发接口
  async scanning (params) {
    let response = await post(URL_POST_SCANNING, params, {
      headers: {}
    })
    return response
  },
  //列表接口
  async list_query (params) {
    let response = await post(URL_POST_LIST_QUERY, params, {
      headers: {}
    })
    return response
  },
  //主动扫描端口查询
  async port_information (params) {
    let response = await post(URL_POST_PORT_INFORMATION, params, {
      headers: {}
    })
    return response
  },

  //主动扫描目标漏洞列表查询接口
  async imfomation_query (params) {
    let response = await post(URL_POST_INFOMATION_QUERY, params, {
      headers: {}
    })
    return response
  },
  //主动扫描目标单个漏洞详细内容查询接口
  async medusa_query (params) {
    let response = await post(URL_POST_MEDUSA_QUERY, params, {
      headers: {}
    })
    return response
  },
  //获取用户个人信息
  async user_info (params) {
    let response = await post(URL_POST_GETINFO, params, {
      headers: {

      }
    })
    return response
  },
  //更新密码
  async update_password (params) {
    let response = await post(URL_POST_UPDATE_PASSWORD, params, {
      headers: {}
    })
    return response
  },
  //首页内容
  async homepage_data (params) {
    let response = await post(URL_POST_HOMEPAGE_DEFAULT_DATA, params, {
      headers: {}
    })
    return response
  },
  //首页漏洞分布
  async homepage_vulnerability_distributiont_data (params) {
    let response = await post(URL_POST_HOMEPAGE_VULNERABILITY_DISTRIBUTIONT_DATA, params, {
      headers: {}
    })
    return response
  },
  // 首页GitHub监控信息
  async homepage_github_monitor_data (params) {
    let response = await post(URL_POST_HOMEPAGE_GITHUB_MONITOR_DATA, params, {
      headers: {}
    })
    return response
  },

  //上传头像
  async upload_avatar (params) {
    console.log(store.state.UserStore.token)
    let response = await post(URL_POST_UPLOAD_AVATAR, params, {
      headers: {
        token: store.state.UserStore.token
      }
    })
    return response
  },

  //github监控
  async github_monitor (params) {
    let response = await post(URL_POST_GITHUB_MONITOR, params, {
      headers: {

      }
    })
    return response
  },
  //github监控
  async github_monitor_search (params) {
    let response = await post(URL_POST_GITHUB_MONITOR_SEARCH, params, {
      headers: {

      }
    })
    return response
  },
  //创建钓鱼脚本项目
  async create_script_project (params) {
    let response = await post(URL_POST_CREATE_SCRIPT_PROJECT, params, {
      headers: {

      }
    })
    return response
  },
  //查询钓鱼脚本项目
  async query_script_project (params) {
    let response = await post(URL_POST_QUERY_SCRIPT_PROJECT, params, {
      headers: {

      }
    })
    return response
  },
  // 查询跨站脚本钓鱼项目中数据
  async query_script_project_data (params) {
    let response = await post(URL_POST_QUERY_SCRIPT_PROJECT_DATA, params, {
      headers: {

      }
    })
    return response
  },
  // 查询跨站脚本钓鱼项目中详细信息

  async query_script_project_info (params) {
    let response = await post(URL_POST_QUERY_SCRIPT_PROJECT_INFO, params, {
      headers: {

      }
    })
    return response
  },

  // 修改跨站脚本钓鱼项目中详细信息
  async modify_cross_site_script_project (params) {
    let response = await post(URL_POST_MODIFY_CROSS_SITE_SCRIPT_PROJECT, params, {
      headers: {

      }
    })
    return response
  },
  //读取用户自定义跨站脚本模板数据
  async read_script_template (params) {
    let response = await post(URL_POST_READ_SCRIPT_TEMPLATE, params, {
      headers: {

      }
    })
    return response
  },
  // 获取当前机器基础信息
  async hardware_initialization (params) {
    let response = await post(URL_POST_HARDWARE_INITIALIZATION, params, {
      headers: {}
    })
    return response
  },

  // 获取当前机器CPU和内存使用率
  async hardware_usage_query (params) {
    let response = await post(URL_POST_HARDWARE_USAGE_QUERY, params, {
      headers: {}
    })
    return response
  },



  //读取默认跨站脚本模板数据
  async read_default_script_template (params) {
    let response = await post(URL_POST_READ_DEFAULT_SCRIPT_TEMPLATE, params, {
      headers: {

      }
    })
    return response
  },

  // 保存用户自定义跨站脚本模板数据
  async save_cross_site_script_template (params) {
    let response = await post(URL_POST_SAVE_CROSS_SITE_SCRIPT_TEMPLATE, params, {
      headers: {

      }
    })
    return response
  },

  // 修改用户自定义跨站脚本模板数据
  async modify_cross_site_script_template (params) {
    let response = await post(URL_POST_MODIFY_CROSS_SITE_SCRIPT_TEMPLATE, params, {
      headers: {}
    })
    return response
  },


  // 创建协同作战项目
  async create_markdown_project (params) {
    let response = await post(URL_POST_CREATE_MARKDOWN_PROJECT, params, {
      headers: {}
    })
    return response
  },
  // 查询协同作战项目
  async query_markdown_project (params) {
    let response = await post(URL_POST_QUERY_MARKDOWN_PROJECT, params, {
      headers: {}
    })
    return response
  },
  // 用来查询Markdown文档数据
  async query_markdown_data (params) {
    let response = await post(URL_POST_QUERY_MARKDOWN_DATA, params, {
      headers: {}
    })
    return response
  },
  // 保存Markdown文档数据
  async save_markdown_data (params) {
    let response = await post(URL_POST_SAVE_MARKDOWN_DATA, params, {
      headers: {}
    })
    return response
  },
  // 上传Markdown图片
  async markdown_image_upload (params) {
    let response = await post(URL_POST_MARKDOWN_IMAGE_UPLOAD, params, {
      headers: {
        token: store.state.UserStore.token
      }
    })
    return response
  },
  // Markdown文档数据对比
  async markdown_data_comparison (params) {
    let response = await post(URL_POST_MARKDOWN_DATA_COMPARISON, params, {
      headers: {}
    })
    return response
  },
  // 加入协同作战项目
  async join_markdown_project (params) {
    let response = await post(URL_POST_JOIN_MARKDOWN_PROJECT, params, {
      headers: {}
    })
    return response
  },

  // 杀毒软件进程查询
  async antivirus_software_compared (params) {
    let response = await post(URL_POST_ANTIVIRUS_SOFTWARE_COMPARED, params, {
      headers: {}
    })
    return response
  },


  async generate_word (params) {
    let response = await post(URL_POST_GENERATE_WORD, params, {
      headers: {}
    })
    return response
  },
  async download_word (params) {
    let response = await postDownload(URL_POST_DOWNLOAD_WORD, params, {
      headers: {}
    })
    return response
  },
  async nist_data_bulk_query (params) {
    let response = await post(URL_POST_NIST_DATA_BULK_QUERY, params, {
      headers: {}
    })
    return response
  },
  async nist_statistics (params) {
    let response = await post(URL_POST_NIST_STATISTICS, params, {
      headers: {}
    })
    return response
  },
  async nist_search (params) {
    let response = await post(URL_POST_NIST_SEARCH, params, {
      headers: {}
    })
    return response
  },
  async nist_search_statistics (params) {
    let response = await post(URL_POST_NIST_SEARCH_STATISTICS, params, {
      headers: {}
    })
    return response
  },
  async nist_data_detailed_query (params) {
    let response = await post(URL_POST_NIST_DATA_DETAILED_QUERY, params, {
      headers: {}
    })
    return response
  },
  async markdown_project_statistical (params) {
    let response = await post(URL_POST_MARKDOWN_PROJECT_STATISTICAL, params, {
      headers: {}
    })
    return response
  },

  async statistical_cross_site_script_project_data (params) {
    let response = await post(URL_POST_STATISTICAL_CROSS_SITE_SCRIPT_PROJECT_DATA, params, {
      headers: {}
    })
    return response
  },
  async statistical_cross_site_script_project (params) {
    let response = await post(URL_POST_STATISTICAL_CROSS_SITE_SCRIPT_PROJECT, params, {
      headers: {}
    })
    return response
  },


}

export default api