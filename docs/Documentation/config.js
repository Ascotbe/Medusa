let config = {
    title: 'Medusa文档',
    home: 'Home.md',
    repo: 'Ascotbe/Medusa',
    nav: [
        {
            title: '简介', path: '/'
        },
        {
            title: '快速入门', path: '/QuickStart'
        },
		{
            title: '机器人模块', path: '/Bot'
        },
		{
            title: '插件编写', type: 'dropdown', items: [
				{   title: '3.7(当前版本)', path: '/PocVersion/3.7/PocWriting'
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
            title: 'API 描述', path: '/API'
        },
		{
            title: '插件列表', path: '/PluginDirectory'
        },
        {
            title: 'Web版本', type: 'dropdown', items: [
                {
                    title: '安装说明', path: '/WebVersionInstallation'
                }
            ]
        },
        {
            title: '更新日志', path: '/UpDataLog'
        },

        {
            title: '其它', type: 'dropdown', items: [
                {
                    title: '开发团队介绍', path: '/Team'
                },
                {
                    title: '问题列表', path: '/Bug'
                },
            ]
        }
    ],
    tocVisibleDepth: 2,
    plugins: []
};
