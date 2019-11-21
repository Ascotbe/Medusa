let config = {
    title: 'MedusaScan 文档',
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
            title: '插件编写', path: '/PocWriting'
        },
        {
            title: '功能详情', path: '/FunctionDetails'
        },
        {
            title: 'API', type: 'dropdown', items: [
                {
                    title: 'API 描述', path: '/API'
                }
            ]
        },
        {
            title: 'Web版本', type: 'dropdown', items: [
                {
                    title: '使用介绍', path: '/WebVersion'
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
                    title: 'FAQ', path: '/FAQ'
                }
            ]
        }
    ],
    tocVisibleDepth: 2,
    plugins: []
};
