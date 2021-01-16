<template>
<div class="projectDetails">
    <a-row :gutter="[
        { xs: 8, sm: 16, md: 24, xs: 8 },
        { xs: 8, sm: 16, md: 24, lg: 32 },
      ]" class="projectDetails_bg">
        <a-col :xs="{ span: 24 }">
            <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol" ref="ruleForm">
                <a-form-model-item label="项目代码" :labelAlign="'left'">
                    <codemirror ref="myCm" v-model="form.project_associated_file_data" :options="cmOptions" class="code"></codemirror>
                </a-form-model-item>

                <a-form-model-item label="将如下代码植入怀疑出现xss的地方" :labelAlign="'left'">
                    <a-input v-model="form.the_first_use" :disabled="disabled" :size="'large'" />
                </a-form-model-item>

                <a-form-model-item label="再或者以你任何想要的方式插入" :labelAlign="'left'">
                    <a-input v-model="form.exploit_path" :disabled="disabled" :size="'large'" />
                </a-form-model-item>

                <a-form-model-item label="极限代码~！" :labelAlign="'left'">
                    <a-input v-model="form.the_second_use" :disabled="disabled" :size="'large'" />
                </a-form-model-item>
                <a-form-model-item label="图片插件" :labelAlign="'left'">
                    <a-input v-model="form.the_third_use" :disabled="disabled" :size="'large'" />
                </a-form-model-item>

                <a-form-model-item label="编码poc" :labelAlign="'left'">
                    <a-input v-model="form.coding_exploit" :disabled="disabled" :size="'large'" type="textarea" :autoSize="true" />
                </a-form-model-item>

                <a-form-model-item class="item">
                    <a-button type="primary" @click="handleReset" class="item_btn">
                        重置
                    </a-button>
                    <a-button type="primary" @click="handleSave" class="item_btn">
                        保存修改
                    </a-button>
                </a-form-model-item>
            </a-form-model>
        </a-col>
    </a-row>
</div>
</template>

<script>
export default {
    name: "projectDetails",
    data() {
        return {
            labelCol: {
                span: 14,
                offset: 5,
            },
            wrapperCol: {
                span: 14,
                offset: 5,
            },
            disabled: true, //true禁用
            form: {
                project_associated_file_data: "", //项目代码
                the_first_use: "", //将如下代码植入怀疑出现xss的地方
                exploit_path: "", //再或者以你任何想要的方式插入
                the_second_use: "", //极限代码
                the_third_use: "", //图片插件
                coding_exploit: "", //编码poc
            },
            formRest: {
                project_associated_file_data: "", //项目代码
                // the_first_use: "", //将如下代码植入怀疑出现xss的地方
                // exploit_path: "", //再或者以你任何想要的方式插入
                // the_second_use: "", //极限代码
                // the_third_use: "", //图片插件
                // coding_exploit: "", //编码poc
            },
            cmOptions: {
                mode: "javascript",
                theme: "duotone-light",
                lineNumbers: true,
                lineWrapping: true, //自动换行
                line: true,
                // readOnly: "nocursor", //只读
                matchBrackets: true,
            },
        };
    },
    mounted() {
        this.handelModifyCrossSiteScriptProject();
    },
    methods: {
        handelModifyCrossSiteScriptProject() {
            if (this.$store.state.project_associated_file_name == "null") {
                this.$message.warning("请从项目管理进入,跳转站点扫描中...");
                this.$router.push("/layout/projectManagement");
            } else {
                let params = {
                    token: localStorage.getItem("storeToken"),
                    project_associated_file_name: this.$store.state
                        .project_associated_file_name,
                };
                this.$api.query_script_project_info(params).then((res) => {
                    console.log(res);
                    if (res.code == 200) {
                        let form = {
                            project_associated_file_data: this.$qj.QJBase64Decode(
                                res.message.project_associated_file_data
                            ), //项目代码
                            exploit_path: res.message.exploit_path, //再或者以你任何想要的方式插入
                            the_first_use: res.message.the_first_use, //将如下代码植入怀疑出现xss的地方
                            the_second_use: res.message.the_second_use, //极限代码
                            the_third_use: res.message.the_third_use, //图片插件
                            coding_exploit: res.message.coding_exploit, //编码poc
                        };
                        this.formRest = {
                            project_associated_file_data: this.$qj.QJBase64Decode(
                                res.message.project_associated_file_data
                            ), //项目代码
                            // exploit_path: res.message.exploit_path, //再或者以你任何想要的方式插入
                            // the_first_use: res.message.the_first_use, //将如下代码植入怀疑出现xss的地方
                            // the_second_use: res.message.the_second_use, //极限代码
                            // the_third_use: res.message.the_third_use, //图片插件
                            // coding_exploit: res.message.coding_exploit, //编码poc
                        };
                        this.form = form;
                    } else {
                        this.$message.error("请求似乎出了点小问题");
                    }
                });
            }
        },
        handleReset() {
            this.form.project_associated_file_data = this.formRest.project_associated_file_data; //项目代码
        },
        handleSave() {
            if (this.$store.state.project_associated_file_name == "null") {
                this.$message.warning("关键字段丢失了,请重新进入,跳转站点扫描中...");
                this.$router.push("/layout/projectManagement");
            } else {
                let params = {
                    token: localStorage.getItem("storeToken"),
                    project_associated_file_name: this.$store.state
                        .project_associated_file_name,
                    project_associated_file_data: this.$qj.QJBase64Encode(
                        this.form.project_associated_file_data
                    ),
                };
                console.log(params);
                this.$api.modify_cross_site_script_project(params).then((res) => {
                    if (res.code == 200) {
                        this.$message.success("修改成功");
                        this.handelModifyCrossSiteScriptProject();
                    } else {
                        console.log(res);
                        this.$message.error("请求似乎出了点小问题");
                    }
                });
            }
        },
    },
};

//   [
//     ({
//       label: "项目代码",
//       value: this.$qj.QJBase64Decode(
//         res.$message.project_associated_file_data
//       ),
//     },
//     {
//       label: "再或者以你任何想要的方式插入",
//       value: res.$message.exploit_path,
//     },
//     {
//       label: "将如下代码植入怀疑出现xss的地方",
//       value: res.$message.the_first_use,
//     },
//     {
//       label: "极限代码~！",
//       value: res.$message.the_second_use,
//     },
//     {
//       label: "图片插件",
//       value: res.$message.the_third_use,
//     },
//     {
//       label: "编码poc",
//       value: res.$message.coding_exploit,
//     })
//   ];
</script>

<style lang="scss" scoped>
.projectDetails {
    margin: 0;
    padding: 20px;
    padding-top: 30px;
    height: 100%;

    .projectDetails_bg {
        min-height: 100%;
        background: #fff;

        .item {
            text-align: center;

            .item_btn {
                margin-right: 5px;
                margin-left: 5px;
            }
        }
    }

    .projectDetails_bg /deep/ .ant-form-item {
        font-size: 16px;
    }

    .projectDetails_bg /deep/ .ant-form label {
        font-size: 18px;
        font-weight: 800;
    }

    .projectDetails_bg /deep/ .ant-input {
        color: #000;
        background-color: #f5f5f5;
    }

    .projectDetails_bg /deep/ .ant-input[disabled] {
        background-color: #f5f5f5;
        cursor:auto;
    }
}
</style>
