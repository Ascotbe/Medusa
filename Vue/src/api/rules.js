import {
    get,
    post,
    postDownload
} from '../utils/request'
import {

    URL_POST_LOGIN,
    URL_POST_REGISTERED,
    URL_GET_VERIFICATION_CODE,
    URL_POST_FORGET_PASSWORD,
    URL_POST_SCANNING,
    URL_POST_LIST_QUERY,
    URL_POST_PORT_INFORMATION,
    URL_POST_INFOMATION_QUERY,
    URL_POST_MEDUSA_QUERY,
    URL_POST_GENERATE_WORD,
    URL_POST_DOWNLOAD_WORD,
    URL_POST_GETINFO,
    URL_POST_UPDATE_PASSWORD,
    URL_POST_HOMEPAGE_DEFAULT_DATA,
    URL_POST_HOMEPAGE_VULNERABILITY_DISTRIBUTIONT_DATA,
    URL_POST_UPLOAD_AVATAR,
    URL_POST_GITHUB_MONITOR,
    URL_POST_HOMEPAGE_GITHUB_MONITOR_DATA,

    URL_POST_CREATE_SCRIPT_PROJECT,
    URL_POST_QUERY_SCRIPT_PROJECT,
    URL_POST_QUERY_SCRIPT_PROJECT_DATA,
    URL_POST_QUERY_SCRIPT_PROJECT_INFO,
    URL_POST_MODIFY_CROSS_SITE_SCRIPT_PROJECT,
    URL_POST_READ_SCRIPT_TEMPLATE,
    URL_POST_READ_DEFAULT_SCRIPT_TEMPLATE,
    URL_POST_SAVE_CROSS_SITE_SCRIPT_TEMPLATE,
    URL_POST_MODIFY_CROSS_SITE_SCRIPT_TEMPLATE,
    URL_POST_HARDWARE_INITIALIZATION,// 获取当前机器基础信息
    URL_POST_HARDWARE_USAGE_QUERY,// 获取当前机器CPU和内存使用率
    URL_POST_CREATE_MARKDOWN_PROJECT,
    URL_POST_QUERY_MARKDOWN_PROJECT,// 查询协同作战项目
    URL_POST_QUERY_MARKDOWN_DATA,//用来查询Markdown文档数据
    URL_POST_SAVE_MARKDOWN_DATA,
    URL_POST_MARKDOWN_IMAGE_UPLOAD,
    URL_POST_MARKDOWN_DATA_COMPARISON,
    URL_POST_JOIN_MARKDOWN_PROJECT,
    URL_POST_DOMAIN_NAME_SYSTEM_LOG,//DNSLOG查询
    URL_POST_DOMAIN_NAME_SYSTEM_LOG_STATISTICS,////DNSLOG统计
    URL_POST_NIST_DATA_BULK_QUERY,//CVE监控首页精简数据查询
    URL_POST_NIST_DATA_DETAILED_QUERY,//获取单个详细的CVE编号
    URL_POST_NIST_STATISTICS,//获取CVE编号数据个数
    URL_POST_NIST_SEVERITY_FILTER,//严重性等级筛选
    URL_POST_NIST_VENDORS_FILTER,//厂商名称筛选查询
    URL_POST_NIST_PRODUCTS_FILTER,//产品名称筛选查询

} from './url'
import store from '../Vuex'

let api = {
    // 登陆接口
    async login(params) {
        let response = await post(URL_POST_LOGIN, params, {
            headers: {}
        })
        return response
    },
    // 注册接口
    async registered(params) {
        let response = await post(URL_POST_REGISTERED, params, {
            headers: {}
        })
        return response
    },
    // 获取验证码
    async get_verification_code(params) {
        let response = await get(URL_GET_VERIFICATION_CODE, params, {
            headers: {},
            responseType: 'blob',
        })
        return response
    },

    // 忘记密码
    async forget_password(params) {
        let response = await post(URL_POST_FORGET_PASSWORD, params, {
            headers: {}
        })
        return response
    },
    // 扫描任务下发接口
    async scanning(params) {
        let response = await post(URL_POST_SCANNING, params, {
            headers: {}
        })
        return response
    },
    //列表接口
    async list_query(params) {
        let response = await post(URL_POST_LIST_QUERY, params, {
            headers: {}
        })
        return response
    },
    //主动扫描端口查询
    async port_information(params) {
        let response = await post(URL_POST_PORT_INFORMATION, params, {
            headers: {}
        })
        return response
    },

    //主动扫描目标漏洞列表查询接口
    async imfomation_query(params) {
        let response = await post(URL_POST_INFOMATION_QUERY, params, {
            headers: {}
        })
        return response
    },
    //主动扫描目标单个漏洞详细内容查询接口
    async medusa_query(params) {
        let response = await post(URL_POST_MEDUSA_QUERY, params, {
            headers: {}
        })
        return response
    },
    //获取用户个人信息
    async user_info(params) {
        let response = await post(URL_POST_GETINFO, params, {
            headers: {

            }
        })
        return response
    },
    //更新密码
    async update_password(params) {
        let response = await post(URL_POST_UPDATE_PASSWORD, params, {
            headers: {}
        })
        return response
    },
    //首页内容
    async homepage_data(params) {
        let response = await post(URL_POST_HOMEPAGE_DEFAULT_DATA, params, {
            headers: {}
        })
        return response
    },
    //首页漏洞分布
    async homepage_vulnerability_distributiont_data(params) {
        let response = await post(URL_POST_HOMEPAGE_VULNERABILITY_DISTRIBUTIONT_DATA, params, {
            headers: {}
        })
        return response
    },
    // 首页GitHub监控信息
    async homepage_github_monitor_data(params) {
        let response = await post(URL_POST_HOMEPAGE_GITHUB_MONITOR_DATA, params, {
            headers: {}
        })
        return response
    },
    //上传头像
    async upload_avatar(params) {
        let response = await post(URL_POST_UPLOAD_AVATAR, params, {
            headers: {
                token: store.state.storeToken
            }
        })
        return response
    },

    //github监控
    async github_monitor(params) {
        let response = await post(URL_POST_GITHUB_MONITOR, params, {
            headers: {

            }
        })
        return response
    },
    //创建钓鱼脚本项目
    async create_script_project(params) {
        let response = await post(URL_POST_CREATE_SCRIPT_PROJECT, params, {
            headers: {

            }
        })
        return response
    },
    //查询钓鱼脚本项目
    async query_script_project(params) {
        let response = await post(URL_POST_QUERY_SCRIPT_PROJECT, params, {
            headers: {

            }
        })
        return response
    },
    // 查询跨站脚本钓鱼项目中数据
    async query_script_project_data(params) {
        let response = await post(URL_POST_QUERY_SCRIPT_PROJECT_DATA, params, {
            headers: {

            }
        })
        return response
    },
    // 查询跨站脚本钓鱼项目中详细信息

    async query_script_project_info(params) {
        let response = await post(URL_POST_QUERY_SCRIPT_PROJECT_INFO, params, {
            headers: {

            }
        })
        return response
    },

    // 修改跨站脚本钓鱼项目中详细信息
    async modify_cross_site_script_project(params) {
        let response = await post(URL_POST_MODIFY_CROSS_SITE_SCRIPT_PROJECT, params, {
            headers: {

            }
        })
        return response
    },
    //读取用户自定义跨站脚本模板数据
    async read_script_template(params) {
        let response = await post(URL_POST_READ_SCRIPT_TEMPLATE, params, {
            headers: {

            }
        })
        return response
    },
    // 获取当前机器基础信息
    async hardware_initialization(params) {
        let response = await post(URL_POST_HARDWARE_INITIALIZATION, params, {
            headers: {}
        })
        return response
    },

    // 获取当前机器CPU和内存使用率
    async hardware_usage_query(params) {
        let response = await post(URL_POST_HARDWARE_USAGE_QUERY, params, {
            headers: {}
        })
        return response
    },



    //读取默认跨站脚本模板数据
    async read_default_script_template(params) {
        let response = await post(URL_POST_READ_DEFAULT_SCRIPT_TEMPLATE, params, {
            headers: {

            }
        })
        return response
    },

    // 保存用户自定义跨站脚本模板数据
    async save_cross_site_script_template(params) {
        let response = await post(URL_POST_SAVE_CROSS_SITE_SCRIPT_TEMPLATE, params, {
            headers: {

            }
        })
        return response
    },

    // 修改用户自定义跨站脚本模板数据
    async modify_cross_site_script_template(params) {
        let response = await post(URL_POST_MODIFY_CROSS_SITE_SCRIPT_TEMPLATE, params, {
            headers: {
            }
        })
        return response
    },


    // 创建协同作战项目
    async create_markdown_project(params) {
        let response = await post(URL_POST_CREATE_MARKDOWN_PROJECT, params, {
            headers: {}
        })
        return response
    },
    // 查询协同作战项目
    async query_markdown_project(params) {
        let response = await post(URL_POST_QUERY_MARKDOWN_PROJECT, params, {
            headers: {}
        })
        return response
    },
    // 用来查询Markdown文档数据
    async query_markdown_data(params) {
        let response = await post(URL_POST_QUERY_MARKDOWN_DATA, params, {
            headers: {}
        })
        return response
    },
    // 保存Markdown文档数据
    async save_markdown_data(params) {
        let response = await post(URL_POST_SAVE_MARKDOWN_DATA, params, {
            headers: {}
        })
        return response
    },
    // 上传Markdown图片
    async markdown_image_upload(params) {
        let response = await post(URL_POST_MARKDOWN_IMAGE_UPLOAD, params, {
            headers: {
                token: store.state.storeToken
            }
        })
        return response
    },
    // Markdown文档数据对比
    async markdown_data_comparison(params) {
        let response = await post(URL_POST_MARKDOWN_DATA_COMPARISON, params, {
            headers: {
            }
        })
        return response
    },
    // 加入协同作战项目
    async join_markdown_project(params) {
        let response = await post(URL_POST_JOIN_MARKDOWN_PROJECT, params, {
            headers: {
            }
        })
        return response
    },
    // DNSLOG查询
    async domain_name_system_log(params) {
      let response = await post(URL_POST_DOMAIN_NAME_SYSTEM_LOG, params, {
          headers: {
          }
      })
      return response
    },


    // DNSLOG查询个数统计
    async domain_name_system_log_statistics(params) {
      let response = await post(URL_POST_DOMAIN_NAME_SYSTEM_LOG_STATISTICS, params, {
          headers: {
          }
      })
      return response
    },

    //CVE监控首页精简数据查询
    async nist_data_bulk_query(params) {
      let response = await post(URL_POST_NIST_DATA_BULK_QUERY, params, {
          headers: {
          }
      })
      return response
    },
    //获取单个详细的CVE编号
    async nist_data_detailed_query(params) {
      let response = await post(URL_POST_NIST_DATA_DETAILED_QUERY, params, {
          headers: {
          }
      })
      return response
    },
    //获取CVE编号数据个数
    async nist_statistics(params) {
      let response = await post(URL_POST_NIST_STATISTICS, params, {
          headers: {
          }
      })
      return response
    },
    //对于严重性等级筛选
    async nist_severity_filter(params) {
      let response = await post(URL_POST_NIST_SEVERITY_FILTER, params, {
          headers: {
          }
      })
      return response
    },
    //厂商名称筛选查询
    async nist_vendors_filter(params) {
      let response = await post(URL_POST_NIST_VENDORS_FILTER, params, {
          headers: {
          }
      })
      return response
    },
    //产品名称筛选查询
    async nist_vendors_filter(params) {
      let response = await post(URL_POST_NIST_PRODUCTS_FILTER, params, {
          headers: {
          }
      })
      return response
    },

    async generate_word(params) {
        let response = await post(URL_POST_GENERATE_WORD, params, {
            headers: {}
        })
        return response
    },
    async download_word(params) {
        let response = await postDownload(URL_POST_DOWNLOAD_WORD, params, {
            headers: {}
        })
        return response
    }
}

export default api
