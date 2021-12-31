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
            title: '安装说明', path: '/Installation'
        },
		{
            title: '插件编写',  path: '/PocVersion/PocWriting'
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
                // {
                //     title: '主动扫描', path: '/API/ActiveScanning'
                // },
                // {
                //     title: '被动扫描', path: '/API/PassiveScanning'
                // },
                {
                    title: '验证码', path: '/API/VerificationCode'
                },
                {
                    title: 'DNSLOG', path: '/API/DomainNameSystemLog'
                },
                {
                    title: '免杀生成', path: '/API/TrojanOrVirus'
                },
                {
                    title: '邮件发送相关', path: '/API/Email'
                },
                {
                    title: '配置信息', path: '/API/Information'
                },
                {
                    title: '文件接收', path: '/API/FileAcquisition'
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
