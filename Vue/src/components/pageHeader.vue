<template>
  <div class="pageHeader">
    <div class="backIcon">
      <img src="../assets/退回.svg" class="icon" alt="" />
    </div>
    <div class="title"></div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.pageHeader {
  padding: 8px;
  border: 1px solid #ccc;
  .backIcon {
    display: inline-block;

    .icon {
      cursor: pointer;
    }
   
  }

  .title {
    display: inline-block;
    padding-right: 12px;
    color: rgba(0, 0, 0, 0.85);
    font-weight: 600;
    font-size: 20px;
    line-height: 32px;
  }
}
</style>
