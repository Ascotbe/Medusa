<template>
  <a-result status="404" title="404" sub-title="未找到该页面">
    <template #extra>
      <a-button type="primary" @click="handleBack">返回</a-button>
    </template>
  </a-result>
</template>

<script>
export default {
  methods: {
    handleBack () {
      this.$router.push({ path: '/layout' })
    }
  },
}
</script>

<style>
</style>