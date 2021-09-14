export const OverallMixins = {
  data () {
    return {
      Base64: require("js-base64").Base64,
      moment: require('moment')
    }
  },
  methods: {
    QJBase64Encode (e) {//加密
      return this.Base64.encode(e);
    },
    QJBase64Decode (e) {//解密
      return this.Base64.decode(e);
    },
    QJMemorySize (e) {//内存处理
      let val = (e / 1024 / 1024 / 1024).toFixed(4)
      return val;
    },

  },
}