<template>
  <a-card :bordered="false" v-bind="$props" v-on="$listeners" class="interval"
          :class="{'detailCard': detailCard}"
  >
    <div slot="title" class="titleSolt" v-if="name&&showTitle">{{name}}</div>
    <slot name="extraCard" slot="extra">
      <!-- <a-icon @click="handlecloseAndOpen" :type="icon" /> -->
    </slot>
    <slot></slot>
  </a-card>
</template>

<script>
export default {
  data () {
    return {
      show: true,
      icon: 'minus'
    }
  },
  props: {
    name: {
      type: String,
      default: "查询条件"
    },
    headStyle: {
      type: Object,
      default: () => {
        return {}
      }
    },
      showTitle: {
          type: Boolean,
          default: true
      },
      // 详情页面card
      detailCard: {
          type: Boolean,
          default: false
      },
    bodyStyle: {
      type: Object,
      default: () => {
        return {}
      }
    },
  },
  methods: {
    handlecloseAndOpen () {
      this.show = !this.show
      console.log(this.show)
      this.icon = (this.icon == 'minus') ? 'plus' : 'minus'
    }
  },

}
</script>
<style lang="scss">
.detailCard {
  .ant-card-head {
    padding: 0 10px;
    .ant-card-head-wrapper{
      .ant-card-head-title {
        padding: 10px 0;
      }
    }
  }
  .ant-card,.ant-card-body{
    border-bottom-right-radius: 3px;
    border-bottom-left-radius: 3px;
    padding: 10px;

  }
}
</style>

<style lang="less" scoped>
.interval {
  height: 100%;
  // border: 4px solid #f1f2f6;
}
.titleSolt {
  font-size: 20px;
  text-align: left;
  border-left: 5px solid #51c51a;
  padding-left: 15px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.detailCard {
  .titleSolt{
    border:0;
    line-height: 18px;
    padding-left: 0;
  }

}
</style>
