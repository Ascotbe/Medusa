<template>
     <div class="tab-container">
     <el-tabs v-model="add_item" style="margin-top:15px;" type="border-card" >
     <el-tab-pane label="填写项目信息">
     <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
       <el-form-item label="项目信息" prop="name">
         <el-input v-model="ruleForm.name"></el-input>
       </el-form-item>
       <el-form-item label="项目成员" prop="member">
         <el-input v-model="ruleForm.member"></el-input>
       </el-form-item>

       <el-form-item label="优先级" prop="resource">
         <el-radio-group v-model="ruleForm.resource">
           <el-radio label="低优先级"></el-radio>
           <el-radio label="中优先级"></el-radio>
           <el-radio label="高优先级"></el-radio>
         </el-radio-group>
       </el-form-item>
       <el-form-item label="项目描述" prop="desc">
         <el-input type="textarea" v-model="ruleForm.desc"></el-input>
       </el-form-item>
       <el-form-item label="描述限制" prop="list">
         <el-radio-group v-model="ruleForm.list">
           <el-radio label="黑名单"></el-radio>
           <el-radio label="白名单"></el-radio>
         </el-radio-group>
       </el-form-item>
       <el-form-item>
         <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
         <el-button @click="resetForm('ruleForm')">重置</el-button>
       </el-form-item>
     </el-form>
     </el-tab-pane>
     </el-tabs>
     </div>
</template>


<script>
   export default {
      data() {
       return {
         ruleForm: {
            name: '',
            member: '',
            resource: '',
            desc: '',
            list: '',
            },
             rules: {
               name: [
                 { required: true, message: '请输入项目信息', trigger: 'blur' },
                 { min: 1, max: 15, message: '长度在 1 到 15 个字符', trigger: 'blur' }
               ],
               member: [
                 { required: true, message: '请填写项目成员', trigger: 'blur'}
               ],
               resource: [
                 { required: true, message: '请填写优先级别', trigger: 'change' }
               ],
               desc: [
                 { required: true, message: '请填写项目描述', trigger: 'blur' }
               ],
               list: [
                 {  required: true, message: '请选择描述限制', trigger: 'blur'}
               ]
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
                   message: '创建失败',
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
