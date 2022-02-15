const MenuConfig = () => {
  return [
    {
      key: "personalSettings",
      iconType: "icon-Serviceusers",
      msg: "个人界面",
    },
    {
      key: "dashboard",
      iconType: "icon-ziyuan",
      msg: "仪表盘",
    },
    {
      key: "ActiveScanning",
      iconType: "icon-saomiao1",
      msg: "主动扫描",
      children: [
        {
          key: "issueTasks",
          msg: "下发任务",
        },
        {
          key: "siteInformation",
          msg: "站点扫描",
        },
      ],
    },
    {
      key: "sub2",
      iconType: "icon-saomiao2",
      msg: "被动扫描",
      children: [],
    },
    {
      key: "Monitor",
      iconType: "icon-jiankong",
      msg: "监控页面",
      children: [
        {
          key: "GitHubMonitor",
          msg: "GitHub监控",
        },
        {
          key: "VulnerabilitiesMonitor",
          msg: "CVE监控",
        },
      ],
    },
    {
      key: "CrossSiteScript",
      iconType: "icon-heike",
      msg: "跨站脚本钓鱼",
      children: [
        {
          key: "CreateCrossSiteScript",
          msg: "创建项目",
        },
        {
          key: "ProjectManagement",
          msg: "项目管理",
        },
        {
          key: "TemplateManagement",
          msg: "模板管理",
        },
        {
          key: "PrivateTemplate",
          msg: "创建自定义模板",
        },
      ],
    },
    {
      key: "Combine",
      iconType: "icon-xietong",
      msg: "协同作战",
      children: [
        {
          key: "CreateCombine",
          msg: "创建/加入项目",
        },
        {
          key: "CombineList",
          msg: "项目列表",
        },
      ],
    },
    {
      key: "ShellCodeToTrojan",
      iconType: "icon-heike",
      msg: "免杀生成",
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
      children: [
        {
          key: "antivirusSoftwareCompared",
          msg: "杀毒软件进程查询接口",
        },
      ],
    },
    {
      key: "DNSLOG",
      iconType: "icon-DNSziyuan",
      msg: "DNSLOG",
      children: [
        {
          key: "DNS",
          msg: "DNS",
        },
        {
          key: "HTTP",
          msg: "HTTP",
        },
      ],
    },
    {
      key: "Mail",
      iconType: "icon-saomiao2",
      msg: "邮件",
      children: [
        {
          key: "SendMail",
          msg: "邮件发送",
        },
        {
          key: "MailList",
          msg: "邮件列表",
        },
      ],
    },
    {
      key: "About",
      iconType: "icon-Serviceusers",
      msg: "关于我们",
    },
  ]
}
module.exports = MenuConfig()