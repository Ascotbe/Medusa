<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of timeline" :key="index" :timestamp="item.timestamp" placement="top">
        <el-card>
          <h4>{{ item.title }}</h4>
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
      timeline: [
        {
          timestamp: '2020/3/20',
          title: '1.0',
          content: 'Medo初步形成'
        },
        {
          timestamp: '2020/3/21',
          title: '1.1',
          content: '修改若干错误'
        },
        {
          timestamp: '2020/3/22',
          title: '1.2',
          content: '修改若干错误'
        },
        {
          timestamp: '2020/3/23',
          title: '1.3',
          content: '调试上线'
        }
      ]
    }
  }
}
</script>
