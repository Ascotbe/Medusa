<template>
  <a-card :bordered="false" v-bind="$props" v-on="$listeners">
    <div slot="title" class="titleSolt" v-if="name">{{name}}</div>
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

<style lang="less" scoped>
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
</style>