<template>
     <div class="tab-container">
     <el-tabs v-model="add_plug" style="margin-top:15px;" type="border-card" >
     <el-tab-pane label="高级扫描">
     <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
       <el-form-item label="添加目标" prop="describe">
         <el-input type="textarea" v-model="ruleForm.describe" placeholder="每次最多创建200个扫描目标(一行一条),其余部分将被忽略！"></el-input>
       </el-form-item>
       <el-form-item label="任务周期" prop="service">
         <el-input v-model="ruleForm.service"></el-input>
       </el-form-item>
       <el-form-item label="抓取时间" prop="thanks">
         <el-input v-model="ruleForm.thanks"></el-input>
       </el-form-item>
       <el-form-item label="分析时间" prop="describe" style="width: 800px;">分钟
         <el-input type="textarea" v-model="ruleForm.describe"></el-input>
       </el-form-item>
       <el-form-item label="漏洞危害" prop="danger">
         <el-input v-model="ruleForm.danger"></el-input>
       </el-form-item>
       <!-- 插件代码考虑是否使用特定的文本域 -->
       <el-form-item>
         <el-button type="primary" @click="submitForm('ruleForm')">立即添加</el-button>
         <el-button @click="resetForm('ruleForm')">重置</el-button>
       </el-form-item>
     </el-form>
     </el-tab-pane>
     </el-tabs>
     </div>
</template>


<script>
   const cityOptions = ['上海', '北京', '广州', '深圳'];
   export default {
      data() {
       return {
         ruleForm: {
            name: '',
            type: '',
            service: '',
            thanks: '',
            describe: '',
            danger: '',
            propose: '',
            code: '',
            checkboxGroup1: ['上海'],
            cities: cityOptions
            },
             rules: {
               name: [
                 { required: true, message: '请输入插件名称', trigger: 'blur' },
                 { min: 1, max: 15, message: '长度在 1 到 15 个字符', trigger: 'blur' }
               ],
               type: [
                 { required: true, message: '请填写漏洞类型', trigger: 'blur'},
                 { min: 1, max: 25, message: '长度在 1 到 25 个字符', trigger: 'blur' }
               ],
               describe: [
                 { required: true, message: '请描述漏洞情况', trigger: 'change' }
               ],
               danger: [
                 { required: true, message: '请描述危害', trigger: 'blur' }
               ],
               propose: [
                 {  required: true, message: '请提供建议', trigger: 'blur'}
               ],
               code: [
                 {  required: true, message: '请输入代码', trigger: 'blur'}
               ],
             }
           };
         },
         methods: {
           submitForm(formName) {
             this.$refs[formName].validate((valid) => {
               if (valid) {
                 this.$notify({
                   title: 'Success',
                   message: '创建成功',
                   type: 'success',
                   duration: 2000
                 })
               } else {
                 this.$notify({
                   title: 'Success',
                   message: '创建成功',
                   type: 'success',
                   duration: 2000
                 })
                 return false;
               }
             });
           },
           resetForm(formName) {
             this.$refs[formName].resetFields();
           }
         }
       }
</script>
