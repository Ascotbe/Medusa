/*
 * @Author: your name
 * @Date: 2020-12-22 20:02:53
 * @LastEditTime: 2021-04-15 01:49:42
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /undefined/Users/ascotbe/code/Medusa/docs/Documentation/config.js
 */
let config = {
    title: 'Medusa文档',
    home: 'Home.md',
    repo: 'Ascotbe/Medusa',
    nav: [
        {
            title: '简介', path: '/'
        },
        {
            title: '快速入门', type: 'dropdown', items: [
                {
                    title: 'Web安装说明', path: '/QuickStart/WebVersionInstallation'
                },
                {
                    title: 'Bash使用说明', path: '/QuickStart/BashVersion'
                }
            ]
        },
		{
            title: '插件编写', type: 'dropdown', items: [
                {   title: '3.9(当前版本)', path: '/PocVersion/3.9/PocWriting'
            },
                {   title: '3.8', path: '/PocVersion/3.8/PocWriting'
            },
				{   title: '3.7', path: '/PocVersion/3.7/PocWriting'
                },
                {   title: '3.6', path: '/PocVersion/3.6/PocWriting'
            },
                {   title: '3.5', path: '/PocVersion/3.5/PocWriting'
                },
				{   title: '3.4', path: '/PocVersion/3.4/PocWriting'
                },
				{   title: '3.3', path: '/PocVersion/3.3/PocWriting'
                },
				{   title: '3.2', path: '/PocVersion/3.2/PocWriting'
                },
				{   title: '3.1', path: '/PocVersion/3.1/PocWriting'
                },
				{   title: '3.0', path: '/PocVersion/3.0/PocWriting'
                },
			    {   title: '2.9', path: '/PocVersion/2.9/PocWriting'
                },
                {
                    title: '2.8', path: '/PocVersion/2.8/PocWriting'
                },
				{
                    title: '2.7', path: '/PocVersion/2.7/PocWriting'
                },
            ]
        },
        {
            title: '功能详情', path: '/FunctionDetails'
        },
        {
            title: '接口描述', type: 'dropdown', items: [
                {
                    title: '用户', path: '/API/User'
                },
                {
                    title: '首页', path: '/API/Home'
                },
                {
                    title: '工具库', path: '/API/Tools'
                },
                {
                    title: 'APP收集', path: '/API/ApplicationCollection'
                },
                {
                    title: 'CVE监控', path: '/API/CommonVulnerabilitiesAndExposures'
                },
                {
                    title: 'XSS平台', path: '/API/CrossSiteScript'
                },
                {
                    title: '协同作战', path: '/API/Markdown'
                },
                {
                    title: '监控相关', path: '/API/Monitoring'
                },
                {
                    title: '主动扫描', path: '/API/ActiveScanning'
                },
                {
                    title: '被动扫描', path: '/API/PassiveScanning'
                },
                {
                    title: '验证码', path: '/API/VerificationCode'
                },
                {
                    title: 'DNSLOG', path: '/API/DomainNameSystemLog'
                },
                {
                    title: '免杀生成', path: '/API/AntiAntiVirus'
                },
            ]
        },
		{
            title: '插件列表', path: '/PluginDirectory'
        },
        {
            title: '更新日志', path: '/UpDataLog'
        },
        {
            title: '赞助列表', path: '/Reward'
        }
    ],
    tocVisibleDepth: 10,
    plugins: []
};
