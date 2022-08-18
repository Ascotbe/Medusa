/***
 * key 和路由表的key相同
 * iconType 图标
 * msg  目录名称
 * show  是否显示
 * children 子页面  不推荐个人界面与仪表盘设置为false
 */
const MenuConfig = () => {
  return [
    {
      key: "personalSettings",
      iconType: "icon-Serviceusers",
      msg: "个人界面",
      show: true,
    },
    {
      key: "dashboard",
      iconType: "icon-ziyuan",
      msg: "仪表盘",
      show: true,
    },
    {
      key: "ActiveScanning",
      iconType: "icon-saomiao1",
      msg: "主动扫描",
      show: false,
      children: [
        {
          key: "issueTasks",
          msg: "下发任务",
          show: true,
        },
        {
          key: "siteInformation",
          msg: "站点扫描",
          show: true,
        },
      ],
    },
    {
      key: "sub2",
      iconType: "icon-saomiao2",
      msg: "被动扫描",
      show: false,
      children: [],
    },
    {
      key: "Monitor",
      iconType: "icon-jiankong",
      msg: "监控页面",
      show: false,
      children: [
        {
          key: "GitHubMonitor",
          msg: "GitHub监控",
          show: true,
        },
        {
          key: "VulnerabilitiesMonitor",
          msg: "CVE监控",
          show: true,
        },
      ],
    },
    {
      key: "CrossSiteScript",
      iconType: "icon-heike",
      msg: "跨站脚本钓鱼",
      show: true,
      children: [
        {
          key: "CreateCrossSiteScript",
          msg: "创建项目",
          show: true,
        },
        {
          key: "ProjectManagement",
          msg: "项目管理",
          show: true,
        },
        {
          key: "TemplateManagement",
          msg: "模板管理",
          show: true,
        },
        {
          key: "PrivateTemplate",
          msg: "创建自定义模板",
          show: true,
        },
      ],
    },
    {
      key: "Combine",
      iconType: "icon-xietong",
      msg: "协同作战",
      show: false,
      children: [
        {
          key: "CreateCombine",
          msg: "创建/加入项目",
          show: true,
        },
        {
          key: "CombineList",
          msg: "项目列表",
          show: true,
        },
      ],
    },
    {
      key: "ShellCodeToTrojan",
      iconType: "icon-heike",
      msg: "免杀生成",
      show: false,
      // children: [
      //   {
      //     key: "ShellCodeToTrojan",
      //     msg: "免杀生成",
      //   },
      // ],
    },
    {
      key: "Toolbar",
      iconType: "icon-gongju",
      msg: "工具栏",
      show: false,
      children: [
        {
          key: "antivirusSoftwareCompared",
          msg: "杀毒软件进程查询接口",
          show: true,
        },
      ],
    },
    {
      key: "DNSLOG",
      iconType: "icon-DNSziyuan",
      msg: "DNSLOG",
      show: true,
      children: [
        {
          key: "DNS",
          msg: "DNS",
          show: true,
        },
        {
          key: "HTTP",
          msg: "HTTP",
          show: true,
        },
      ],
    },
    {
      key: "Mail",
      iconType: "icon-saomiao2",
      msg: "邮件",
      show: false,
      children: [
        {
          key: "SendMail",
          msg: "邮件发送",
          show: true,
        },
        {
          key: "MailList",
          msg: "邮件列表",
          show: true,
        },
      ],
    },
    {
      key: "About",
      iconType: "icon-Serviceusers",
      msg: "关于我们",
      show: false,
    },
  ]
}
module.exports = MenuConfig()