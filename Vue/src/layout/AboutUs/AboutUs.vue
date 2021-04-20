<template>
  <a-row class="about_us">
    <div class="about_us_background">
      <p style="padding:50px;"></p><!-- 对数据进行填充使图片下移 -->
    <img alt="" src="../../assets/Medusa.png" class="picture_in_the_picture" />
    <p align="center"  class="word_description">项目还在Alpha开发阶段，欢迎打赏~</p>

    <div class='payment_code'>
<p align="center" style="font-size:15px;"><img class='payment_code_center'  src='../../assets/Alipay.jpeg'>支付宝</p>
<p align="center" style="font-size:15px;"><img class='payment_code_center'  src='../../assets/WeChat.jpeg'>微信</p>

</div>
<a  href="http://medusa.ascotbe.com/Documentation/#/Reward"><p style="text-align: center;font-size:20px;color:rgb(0,0,0)"><img src="../../assets/AbuotUsReward.gif" width="70"> 赞助列表</p></a>

</div>

  </a-row>

</template>


<style lang="scss" scoped>
.about_us
{
  margin: 0;
  padding: 10px;
  padding-top: 10px;
  height: 100%;
  min-height: auto;
  .about_us_background
  {
    background: #fff;
    min-height: 100%;
  }

  .alignright
  {
    display: inline;
    float: right;
  }
  .text_aligncenter
  {
    text-align: center;

  }
  .picture_in_the_picture {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width:200px;
  }
  body {
  background-color: lightblue;
}

.payment_code{
  justify-content:center;
  //background:rgb(0, 0, 0);
  display:flex
}

.payment_code_center{
width:200px;
display:block;
align-items:center;
margin:0 20px
}
.word_description {
  padding:20px;
  font-size:40px;
  }

}
</style>
