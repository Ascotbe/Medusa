<template>
  <el-table :data="list" border fit highlight-current-row style="width: 100%">
    <div class="demo-input-suffix">
      属性方式：
      <el-input
        placeholder="请选择日期"
        suffix-icon="el-icon-date"
        v-model="input1">
      </el-input>
      <el-input
        placeholder="请输入内容"
        prefix-icon="el-icon-search"
        v-model="input2">
      </el-input>
    </div>
  </el-table>
</template>

<script>
import { fetchList } from '@/api/article'

  export default {
    data() {
      return {
        input1: '',
        input2: ''
      }
    }
  }
</script>
