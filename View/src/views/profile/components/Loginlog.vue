<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of loginlog" :key="index" :timestamp="item.timestamp" placement="top">
        <el-card>
          <h5>{{ item.title }}</h5>
          <p>{{ item.content }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginlog: [
        {
          timestamp: '2020/3/20',
          IP: '127.0.0.1',
          content: '福建省南平市'
        },
        {
          timestamp: '2020/3/21',
          IP: '127.0.0.1',
          content: '福建省南平市'
        },
        {
          timestamp: '2020/3/22',
          IP: '127.0.0.1',
          content: '福建省南平市'
        },
        {
          timestamp: '2020/3/23',
          IP: '127.0.0.1',
          content: '福建省南平市'
        }
      ]
    }
  }
}
</script>
