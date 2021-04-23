// 此文件暴露接口地址
export const URL_POST_REGISTERED = `/registered/` // 注册
export const URL_POST_LOGIN = `/login/` // 登陆
export const URL_GET_VERIFICATION_CODE = `/get_verification_code/` // 获取验证码

export const URL_POST_FORGET_PASSWORD = `/forget_password/`// 忘记密码
export const URL_POST_SCANNING = `/vulnerability_scanning/` // 扫描任务下发接口
export const URL_POST_LIST_QUERY = `/active_scan_list_query/` // 主动扫描目标列表查询接口
export const URL_POST_PORT_INFORMATION =`actively_scan_port_information/`//主动扫描端口查询
export const URL_POST_INFOMATION_QUERY = `/scan_information_query/` // 主动扫描目标漏洞列表查询接口
export const URL_POST_MEDUSA_QUERY = `/medusa_query/` //主动扫描目标单个漏洞详细内容查询接口
export const URL_POST_GENERATE_WORD = `/generate_word/` // 扫描报告生成接口
export const URL_POST_DOWNLOAD_WORD = `/download_word/` // 扫描报告下载接口

export const URL_POST_GETINFO = `/user_info/`// 获取用户个人信息
export const URL_POST_UPDATE_PASSWORD = `/update_password/`// 更新密码
export const URL_POST_HOMEPAGE_DEFAULT_DATA = `/homepage_default_data/`// 首页信息查询接口
export const URL_POST_HOMEPAGE_VULNERABILITY_DISTRIBUTIONT_DATA = `/homepage_vulnerability_distributiont_data/`// 首页信息查询接口
export const URL_POST_HOMEPAGE_GITHUB_MONITOR_DATA = `/homepage_github_monitor_data/`// 首页GitHub监控信息

export const URL_POST_UPLOAD_AVATAR = `/upload_avatar/`// 上传头像接口
export const URL_POST_GITHUB_MONITOR = `/github_monitor/`// GitHub监控接口

export const URL_POST_CREATE_SCRIPT_PROJECT = `/create_cross_site_script_project/`// 创建跨站脚本钓鱼项目
export const URL_POST_QUERY_SCRIPT_PROJECT = `/query_cross_site_script_project/`// 查询跨站脚本钓鱼项目
export const URL_POST_QUERY_SCRIPT_PROJECT_DATA = `/query_cross_site_script_project_data/`// 查询跨站脚本钓鱼项目中数据
export const URL_POST_QUERY_SCRIPT_PROJECT_INFO = `/query_cross_site_script_project_info/`// 查询跨站脚本钓鱼项目中详细信息

export const URL_POST_MODIFY_CROSS_SITE_SCRIPT_PROJECT = `/modify_cross_site_script_project/`// 修改跨站脚本钓鱼项目中详细信息


export const URL_POST_READ_SCRIPT_TEMPLATE = `/read_cross_site_script_template/`// 读取用户自定义跨站脚本模板数据
export const URL_POST_READ_DEFAULT_SCRIPT_TEMPLATE = `/read_default_cross_site_script_template/`// 读取默认跨站脚本模板数据
export const URL_POST_SAVE_CROSS_SITE_SCRIPT_TEMPLATE = `/save_cross_site_script_template/`// 保存用户自定义跨站脚本模板数据
export const URL_POST_MODIFY_CROSS_SITE_SCRIPT_TEMPLATE = `/modify_cross_site_script_template/`// 修改用户自定义跨站脚本模板数据

export const URL_POST_HARDWARE_INITIALIZATION = `/system_hardware_initialization/`// 获取当前机器基础信息
export const URL_POST_HARDWARE_USAGE_QUERY = `/system_hardware_usage_query/`// 获取当前机器CPU和内存使用率




export const URL_POST_CREATE_MARKDOWN_PROJECT = `/create_markdown_project/`// 创建协同作战项目
export const URL_POST_QUERY_MARKDOWN_PROJECT = `/query_markdown_project/`// 查询协同作战项目
export const URL_POST_QUERY_MARKDOWN_DATA = `/query_markdown_data/`//用来查询Markdown文档数据
export const URL_POST_SAVE_MARKDOWN_DATA = `/save_markdown_data/`//保存Markdown文档数据
export const URL_POST_MARKDOWN_IMAGE_UPLOAD = `/markdown_image_upload/`//上传Markdown图片
export const URL_POST_MARKDOWN_DATA_COMPARISON = `/markdown_data_comparison/`//Markdown文档数据对比
export const URL_POST_JOIN_MARKDOWN_PROJECT = `/join_markdown_project/`//加入协同作战项目
export const URL_POST_DOMAIN_NAME_SYSTEM_LOG = `/domain_name_system_log/`//DNSLOG数据查询
export const URL_POST_DOMAIN_NAME_SYSTEM_LOG_STATISTICS = `/domain_name_system_log_statistics/`//DNSLOG数据查询个数统计
export const URL_POST_NIST_DATA_BULK_QUERY = `/nist_data_bulk_query/`//CVE监控首页精简数据查询
export const URL_POST_NIST_DATA_DETAILED_QUERY = `/nist_data_detailed_query/`//获取单个详细的CVE编号
export const URL_POST_NIST_STATISTICS = `/nist_statistics/`//获取CVE编号数据个数
export const URL_POST_NIST_SEVERITY_FILTER = `/nist_severity_filter/`//严重性等级筛选
export const URL_POST_NIST_VENDORS_FILTER = `/nist_vendors_filter/`//厂商名称筛选查询
export const URL_POST_NIST_PRODUCTS_FILTER = `/nist_products_filter/`//产品名称筛选查询


// /api/vulnerability_scanning/
// /api/active_scan_list_query/
// /api/registered/
// /api/login/
// /api/scan_information_query/
// /api/medusa_query/
// /api/generate_word/
// /api/download_word/
