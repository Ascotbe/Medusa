<template>
  <a-row
    type="flex"
    justify="center"
    style="height:100%;"
    :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 4, sm: 8, md: 12, lg: 16 },
    ]"
  >
    <a-col :xs="24" :md="8" :xxl="6" style="height: 100%;overflow-y: auto;">
      <!-- <Card :name="``" :bodyStyle="bodyStyle"> -->
         <!-- :scrollTable="{ x: '100%', y: 700 }" -->
        <Tables
          :customRow="handleCustomRow"
         :scrollTable="{ x: '100%', y: '100%' }"
          :columns="columns"
          :tableData="data"
          :total="total"
          :rowKey="(record,index)=>index"
          @change="handleChange"
        />
      <!-- </Card> -->
    </a-col>
    <a-col :xs="24" :md="16" :xxl="18" style="height: 100%;">
      <!-- <Card :name="``" :bodyStyle="bodyStyle2"> -->
        <a-col :xs="24" :md="12" v-for="(value,key) in record" :key="key" style="padding-top: 0;padding-bottom: 0;height: 100%;">
          <!-- <a-col class="title">{{key}}</a-col> -->
          <a-col :xs="24" class="border" @click="handleCopy(value)" style="height: 100%;">
            <!-- <div class="copy">
              COPY
              <a-icon type="copy" />
            </div> -->
            <a-col style="display: flex;padding-left: 0;">
              <div style="flex: 1;font-size: 24px;text-align: left;">{{key}}</div>
              <div class="copy">
                COPY
              <a-icon type="copy" />
              </div>
            </a-col>
            <a-empty v-if="!value" :description="`未选择表格项`" />
            <!-- <MarkdownPreview
              class="pre"
              v-else
              theme="oneDark"
              :initialValue="'```' + `\n${value}\n` + '```'"
            /> -->
             <codemirror style="text-align: left;" v-else :value="value" :options="{mode: 'message/http',lineNumbers: false,theme:'default'}"></codemirror>
            <!-- <pre v-else class="pre" style="color: #666;font-size: 14px;">
              {{value}}
            </pre> -->
          </a-col>
        </a-col>
      <!-- </Card> -->
    </a-col>
  </a-row>
</template>

<script>
// import Card from '@/components/Card/Card.vue'
import Tables from '@/components/Tables/Tables.vue'
import { mapGetters } from "vuex";
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
// import { MarkdownPreview } from 'vue-meditor'

import { codemirror } from 'vue-codemirror'

// import base style
import 'codemirror/lib/codemirror.css'
// import 'codemirror/theme/base16-light.css'
import 'codemirror/mode/http/http.js'
export default {
  mixins: [OverallMixins],
  components: {
    // Card,
    Tables,
    // MarkdownPreview,
    codemirror
  },
  data () {
    return {
      bodyStyle: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px',
        display: 'flex',
        height: '100%'
      },
      bodyStyle2: {
        borderTop: '3px solid #51c51a',
        borderBottom: '0px',
        display: 'flex',
        flexWrap: 'wrap',
        height: '100%'
      },
      columns: [
        {
          title: "#",
          // align: 'center',
          width: 60,
          customRender: (text, record, index) => {
            return ++index
          },
        },
        {
          title: "TIME",
          dataIndex: "creation_time",
          // align: 'center',
          ellipsis: true,
          customRender: (text, record, index) => {
            return text ? this.moment(text, "X").format('YYYY-MM-DD H:mm:ss') : ""
          },
        }
      ],
      data: [],
      total: 0,
      current: 1,
      record: {
        request: false,
        response: false
      }
    };
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    })
  },
  created () {
    const _this = this
    _this.handleDNSLOG()
  },
  methods: {
    //分页查询
    handleDNSLOG () {
      const _this = this
      const params = {
        token: _this.token,
        number_of_pages: _this.current,
      };
      const data = _this.$api.http_domain_name_system_log(params)
      const total = _this.$api.http_domain_name_system_log_statistics(params)
      Promise.all([data, total]).then((res) => {
        res.map((item, i) => {
          if (item.code == 200) {
            i == 0 ? _this.data = item.message : _this.total = item.message
          }
          else _this.$message.warn(item.message)
        })
      })

    },
    //分页监听
    handleChange (pagination) {
      const _this = this
      _this.current = pagination.current
      _this.handleDNSLOG()
    },
    //回调分页
    handleShowTotal (Dom, total, range) {
      const page = <span style="display: flex;align-items: center;padding-left:3px;font-size:12px" v-show={total == 0 ? false : true}>共<span style="color:#51c51a;padding:0 3px 0 3px"><a-statistic value={total} valueStyle={{ color: '#51c51a' }} >
      </a-statistic></span>条</span>

      return page
    },
    // 点击表头行回调
    handleCustomRow (record, index) {
      const _this = this
      return {
        on: {
          click: () => {
            const { creation_time, ...obj } = record
            obj.request = _this.QJBase64Decode(obj.request)
            obj.response = _this.QJBase64Decode(obj.response)
            _this.record = {
              ...obj
            }
            console.log(_this.record)
          },
        }
      }
    },
    //复制
    handleCopy (value) {
      const _this = this
      if (value) {
        const input = document.createElement('input')
        input.value = value
        // 在body里面插入这个元素
        document.body.appendChild(input)
        input.select()
        document.execCommand("Copy")
        document.body.removeChild(input)
        _this.$message.success('复制成功')
      }
      else _this.$message.warn('没有数据无法复制')
    }
  },
};
</script>

<style lang="scss" scoped>
.title {
  text-align: left;
  font-size: 24px;
}
.border {
  // border: 1px solid #808080;
  border: 1px solid #fff;
  background: #fff;
  min-height: 500px;
  height: calc(100% - 56px);
  border-radius: 5px;
}
.copy {
  // position: relative;
  display: inline-block;
  padding: 0;
  margin: 0;
  height: 20px;
  width: 60px;
  line-height: 20px;
  margin-top: 8px;
  // top: -10px;
  // left: calc(50% - 30px);
  // transform: translateY(-50%);
  border: 1px solid #51c51a;
  border-radius: 5px;
  background: #51c51a;
  color: white;
  cursor: pointer;
  // transform: translateX(calc(100% - 40px));
}
.copy:active {
  background: #ffffff;
  color: #51c51a;
  border: 1px solid #51c51a;
  user-select: none;
}
.pre {
  width: 100%;
  all: initial; /*清除继承样式*/
  display: block; /*设置布局流，避免换行导致的错误布局*/
  white-space: pre-line; /*保留换行符，设置溢出换行*/
  // font-size: 12px; /*设置字号*/
  // white-space: pre-wrap; /* css-3 */
  // white-space: -moz-pre-wrap; /* Mozilla, since 1999 */
  // white-space: -pre-wrap; /* Opera 4-6 */
  // white-space: -o-pre-wrap; /* Opera 7 */
  overflow: auto;
  word-break: break-all;
  word-wrap: break-word;
  line-height: 30px;
}
</style>
