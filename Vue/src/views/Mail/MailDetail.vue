<template>
    <a-card class="mail-detail">
        <a-form  layout='horizontal' labelAlign='left'>
            <a-form-item label='发件人'>{{info.sender}}</a-form-item>
            <a-form-item label='时间'>{{info.creation_time?moment(info.creation_time,'X').format('YYYY-MM-DD H:mm:ss'):''}}</a-form-item>
            <a-form-item label='收件人'>{{info.mail_status}}</a-form-item>
            <a-form-item label='附件'>{{info.count?(info.count+'个附件'):'无'}}</a-form-item>
        </a-form>
        <a-divider />
        <div v-html="info.mail_message"></div>
    </a-card>
</template>
<script>
import { OverallMixins } from '@/js/Mixins/OverallMixins.js'
import { mapGetters } from "vuex";
export default {
    mixins: [OverallMixins],
    data () {
        return {
            info: {}
        }
    },
    computed: {
        ...mapGetters({
            token: "UserStore/token",
        })
    },
    methods: {

    },
    mounted() {
        if(this.$route.query.id) {
            this.$api.mail_detail_query({token: this.token,email_id: this.$route.query.id}).then(res => {
                if (res.code == 200) { 
                    let data = res.message[0] || {}
                  this.info = {
                      ...data,
                      sender: this.QJBase64Decode(data.sender),
                      mail_message: this.QJBase64Decode(data.mail_message),
                      count: Object.keys(JSON.parse(data.attachment)).length,
                      mail_status: Object.keys(JSON.parse(data.mail_status)).join(';')
                  }
                }else {
                     this.$message.warn(res.message)
                }
            
            })
        }
    }
}
</script>
<style scoped>
.mail-detail >>> .ant-form-item {
    margin-bottom: 0;
    text-align: left;
}
.mail-detail >>> .ant-form-item-label {
    width: 55px;
    text-align-last: justify;
}
.mail-detail >>> .ant-form-item-label label {
    color: #999;
    /* display: inline-block; */
    
}
.mail-detail >>> .ant-form-item-control-wrapper {
    display: inline-block;
}
</style>