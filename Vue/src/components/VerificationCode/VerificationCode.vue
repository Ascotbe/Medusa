<template>
  <img
    :src="verificationCodePath"
    @click="handleVerificationCode"
    width="100%"
    height="40px"
  />
</template>

<script>
export default {
  data() {
    return {
      verificationCodePath: "",
    };
  },
  mounted() {
    this.handleVerificationCode();
  },
  methods: {
    async handleVerificationCode() {
      this.verificationCodePath = await this.$api
        .get_verification_code()
        .then((res) => {
          return window.URL.createObjectURL(res);
        });
    },
  },
};
</script>

<style>
</style>