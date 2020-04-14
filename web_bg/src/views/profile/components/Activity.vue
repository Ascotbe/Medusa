<template>
  <div class="user-activity">
    <div class="property">
      <div class="property_indoor" >
        <span class="username text-muted" prop="Token">Token</span>
        <p>
          Token
        </p>
      </div>
    </div>
    <div class="property">
      <div class="property_indoor">
        <span class="username text-muted" prop="Email">Email</span>
      </div>
      <p>
        Email@qq.com
      </p>
    </div>
   <div class="property">
      <div class="property_indoor">
        <span class="username text-muted" prop="Time">注册时间</span>
      </div>
      <p>
        2020-04-04
      </p>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      Token: '',
      Email: '',
      Time: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.user-activity {
  .property_indoor {

    .username,
    .description {
      display: block;
      margin-left: 50px;
      padding: 2px 0;
    }

    .username{
      font-size: 16px;
      color: #000;
    }

    :after {
      clear: both;
    }

    .img-circle {
      border-radius: 50%;
      width: 40px;
      height: 40px;
      float: left;
    }

    span {
      font-weight: 500;
      font-size: 12px;
    }
  }

  .property {
    font-size: 14px;
    border-bottom: 1px solid #d2d6de;
    margin-bottom: 15px;
    padding-bottom: 15px;
    color: #666;

    .image {
      width: 100%;
      height: 100%;

    }

    .user-images {
      padding-top: 20px;
    }
  }

  .list-inline {
    padding-left: 0;
    margin-left: -5px;
    list-style: none;

    li {
      display: inline-block;
      padding-right: 5px;
      padding-left: 5px;
      font-size: 13px;
    }

    .link-black {

      &:hover,
      &:focus {
        color: #999;
      }
    }
  }

}

.box-center {
  margin: 0 auto;
  display: table;
}

.text-muted {
  color: #777;
}
</style>
