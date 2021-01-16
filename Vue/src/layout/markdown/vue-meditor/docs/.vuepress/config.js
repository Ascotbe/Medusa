module.exports = {
    base: process.env.docs_env === 'dev' ? '' : '/vue-markdown-docs/',
    title: 'vue-markdown',
    description: '一款使用marked和highlight.js开发的一款vue markdown编辑器,支持codemirror编辑器。',

    themeConfig: {
        nav: [
            {text: 'GitHub', link: 'https://github.com/zhaoxuhui1122/vue-markdown'}
        ],
        sidebar: [
            ['/', '介绍'],
            ['/demo', '示例'],
            ['/use', '起步'],
            {
                title: 'API',
                collapsable: false,
                children: [
                    ['/props', 'Props'],
                    ['/events', 'Event']
                ]
            }, {
                title: '二次开发',
                collapsable: false,
                children: [
                    ['/extend', '功能扩展'],
                    ['/optimize', '优化']
                ]
            }, {
                collapsable: false,
                children: [
                    ['/others', '其他']
                ]
            },
            ['/changelog', '更新日志'],
        ]
    }
}
