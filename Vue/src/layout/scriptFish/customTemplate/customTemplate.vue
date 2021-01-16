<template>
<div class="customTemplate">
    <a-row :gutter="[
        { xs: 8, sm: 16, md: 24, xs: 8 },
        { xs: 8, sm: 16, md: 24, lg: 32 },
      ]" class="customTemplate_bg">
        <a-col :xs="{ span: 20, offset: 2 }" :lg="{ span: 14, offset: 5 }" :xl="{ span: 12, offset: 6 }" :xxl="{ span: 12, offset: 6 }">
            <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol" :rules="rules" ref="ruleForm">
                <a-form-model-item label="模板名称" prop="template_name">
                    <a-input v-model="form.template_name" />
                </a-form-model-item>
                <a-form-model-item label="模板脚本" prop="template_data">
                    <codemirror ref="myCm" v-model="form.template_data" :options="cmOptions" class="code"></codemirror>
                </a-form-model-item>
                <a-form-model-item :wrapper-col="{ span: 6, offset: 9 }">
                    <a-button type="primary" @click="handleOnSubmit">
                        创建模板
                    </a-button>
                </a-form-model-item>
            </a-form-model>
        </a-col>
    </a-row>
</div>
</template>

<script>
export default {
    data() {
        return {
            labelCol: {
                span: 24,
            },
            wrapperCol: {
                span: 24,
            },
            cmOptions: {
                tabSize: 4,
                styleActiveLine: true,
                theme: "duotone-light",
                lineNumbers: true,
                line: true,
                lineWrapping: true, //自动换行
                mode: "text/javascript",
                // readOnly: 'nocursor' //只读
            },
            form: {
                template_name: "",
                template_data: "",
            },
            rules: {
                template_name: [{
                    required: true,
                    message: "请输入自定义模板名称",
                    whitespace: true,
                }, ],

                template_data: [{
                    required: true,
                    message: "自定义脚本输入js脚本",
                    whitespace: true,
                }, ],
            },
        };
    },
    mounted() {},
    methods: {
        handleOnSubmit() {
            this.$refs.ruleForm.validate((valid) => {
                console.log("1");
                if (valid) {
                    let form = this.form;
                    let params = {
                        template_name: form.template_name,
                        template_data: form.template_data,
                        token: localStorage.getItem("storeToken"),
                    };
                    this.$api.save_cross_site_script_template(params).then((res) => {
                        switch (res.code) {
                            case 200:
                                console.log(res);
                                this.$message.success('模板创建成功');
                                break;
                            case 169:
                                this.$message.error(res.message);
                                break;
                            case 401:
                                this.$message.error(res.message);
                                break;
                            case 403:
                                this.$message.error(res.message);
                                break;
                            case 500:
                                this.$message.error(res.message);
                                break;
                        }
                    });
                } else {
                    this.$message.error("请填写内容");
                    return false;
                }
            });
        },
    },
};
</script>

<style lang="scss" scoped>
.customTemplate {
    margin: 0;
    padding: 20px;
    padding-top: 30px;
    height: 100%;
    .customTemplate_bg {
        background: #fff;
         min-height: 100%;
    }
    .customTemplate_bg /deep/ .CodeMirror {
        height: 550px;
    }

    .customTemplate_bg /deep/ .ant-form-item-control {
        line-height: 20px;
    }
}
</style>
