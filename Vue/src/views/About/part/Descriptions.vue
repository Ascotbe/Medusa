<script>
export default {
  props: {
    aboutInfo: {
      type: Object,
      default: () => {
        return {}
      }
    }
  },
  data () {
    return {
      visible: {
        1: false,
        2: false,
        3: false
      },

    }
  },
  methods: {
    handleSwitch (key) {
      const attribute = {}
      switch (key) {
        case 'version':
          attribute.label = '当前版本'
          attribute.tag = true
          break
        case 'latest_version':
          attribute.label = '最新版本'
          attribute.urlName = 'GitHub Releases '
          break
        case 'official_documentation':
          attribute.label = '官方文档'
          attribute.urlName = 'Medusa'
          break
        case 'registration_function_status':
          attribute.label = '注册功能状态'
          break
        case 'forgot_password_function_status':
          attribute.label = '忘记密码状态'
          break
        case 'cross_site_script_uses_domain_names':
          attribute.label = 'XSS域名配置'
          attribute.visibleId = 1
          break
        case 'domain_name_system_address':
          attribute.label = 'DNSLOG域名配置'
          attribute.visibleId = 2
          break
        case 'local_mail_host':
          attribute.label = '自建邮件服务'
          attribute.visibleId = 3
          break
      }
      return attribute
    }
  },
  render: function (h) {
    const _this = this
    const descriptions = []
    for (const key in _this.aboutInfo) {
      const objectList = {}
      objectList = {}
      objectList.key = key
      objectList.label = _this.handleSwitch(key).label
      objectList.tag = _this.handleSwitch(key).tag
      objectList.urlName = _this.handleSwitch(key).urlName
      objectList.visibleId = _this.handleSwitch(key).visibleId
      objectList.value = _this.aboutInfo[key]
      descriptions.push(objectList)
    }
    return h('a-descriptions',
      {
        props: {
          column: { sm: 1 }
        },
        style: {
          'font-size': '24px',
          'padding-left': '10%'
        }
      },
      descriptions.map((item, i) => {
        return h('a-descriptions-item',
          {
            props: {
              label: item.label,
              layout: "horizontal"
            },
          },
          [
            item.tag ? [h('a-tag',
              {
                props: {
                  color: 'green'
                }
              },
              item.value
            )] : item.urlName ? [h('a',
              {
                on: {
                  click: () => window.open(item.value)
                }
              },
              item.urlName
            )] : item.value.value ?
              [
                h('a-tag',
                  {
                    props: {
                      color: item.value.state ? 'red' : 'green'
                    },
                  },
                  item.value.state ? '已修改' : '未修改'
                ),
                _this.visible[item.visibleId] ? h('a',
                  {
                    style: { 'padding-right': '5px' }
                  },
                  item.value.value
                ) : '',
                h('a-icon',
                  {
                    props: {
                      type: _this.visible[item.visibleId] ? 'eye' : 'eye-invisible'
                    },
                    on: {
                      click: () => _this.visible[item.visibleId] = !_this.visible[item.visibleId]
                    }
                  },
                )
              ] : [h('a-tag',
                {
                  props: {
                    color: item.value ? 'green' : 'red'
                  }
                },
                item.value ? '开启' : '关闭'
              )]

          ]
        )
      })
    )
  },
}
</script>

<style lang="less" scoped>
/deep/ .ant-descriptions-row > td {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  padding: 10px;
  font-size: 40px;
  // background: rgba(0, 0, 0, 0);
}
</style>