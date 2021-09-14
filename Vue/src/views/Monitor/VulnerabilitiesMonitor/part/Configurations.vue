<script>
export default {
  props: {
    configurations: {
      type: Array,
      default: () => {
        return []
      }
    }
  },
  data () {
    return {
      blogTitle: '1'
    }
  },
  methods: {
    handleCreateConfigurations (configurations, h, flag) {//flag 为是否回调过
      const _this = this
      return configurations.map((items, i) => {
        return h('a-row', {
          props: {
            gutter: [
              16, { xs: 4, sm: 8, md: 12, lg: 16 }
            ],
            type: "flex",
            justify: "space-around",
          },
        },
          [
            flag == false ? h('a-col', {
              props: {
                xs: 24
              },
              style: {
                textAlign: 'left',
              },
            }, `Configurations${i + 1}`) : '',
            items.cpe_match.length == 1 ? '' :
              h('a-col', {
                props: {
                  xs: 2
                },
                style: {
                  padding: 0,
                  background: '#ddd',
                  borderTop: '2px solid #fff',
                  borderLeft: '5px solid #fff',
                  borderBottom: '2px solid #fff',
                  display: 'flex',
                  alignContent: 'center',
                  alignItems: 'center',
                  flexDirection: 'row',
                  justifyContent: 'space-evenly',
                },
              }, items.operator)
            ,

            h('a-col', {
              props: {
                xs: items.cpe_match.length == 1 ? 24 : 22
              },
              style: {
              }
            },
              items.children.length > 0 ? _this.handleCreateConfigurations(items.children, h, true) : items.cpe_match.map((item) => {
                return h('a-col', {
                  props: {
                    xs: 24
                  },
                  style: {
                    textAlign: 'left',
                    border: '1px solid #ddd'
                  },
                }, item.cpe23Uri)
              })
            ),
            flag == false ? h('a-divider', {
              props: {
                xs: 24
              },

            }) : '',
          ]
        )

      })
    }
  },
  render: function (h) {
    const _this = this
    return h('div', {
      props: {
        // gutter: [
        //   16, { xs: 4, sm: 8, md: 12, lg: 16 }
        // ],
        // type: "flex",
        // justify: "space-around",
        // align: "middle"
      },
    },
      _this.handleCreateConfigurations(this.configurations, h, false)
      // _this.configurations.map(items => {
      //   if (items.children.length > 0) {
      //     return
      //   }
      //   else {
      //     items.cpe_match.map((item) => {
      //       return h('span', {},
      //         item.cpe23Uri
      //       )
      //     })
      //   }
      // })
    )

  }
}
</script>

<style>
.a {
  border: solid;
  text-align: left;
}
</style>