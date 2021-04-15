<template>
<div class="agreement">
    <test>
        <div slot="title">服务条款</div>
        <div slot="main">
            <p>
                在原有的<a href="https://github.com/Ascotbe/Medusa/blob/master/LICENSE" style="color: #0366d6">协议</a>中追加以下内容：
            </p>
            <ul style="margin:0">
                <li>本项目禁止进行未授权商业用途</li>
                <li>
                    本项目仅面向<strong>合法授权</strong>的企业安全建设行为，在使用本项目进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。
                </li>
                <li>
                    如您在使用本项目的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
                </li>
                <li>
                    在使用本项目前，请您<strong>务必审慎阅读、充分理解各条款内容</strong>，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。
                    除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本项目。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
                </li>
            </ul>
        </div>
    </test>
</div>
</template>

<script>
import test from "../../components/test.vue";
export default {
    name: "agreement",
    components: {
        test,
    },
};
</script>

<style lang="scss">
.agreement {
    width: 50%;
    min-width: 300px;
    margin: 0 auto;
}
</style>
