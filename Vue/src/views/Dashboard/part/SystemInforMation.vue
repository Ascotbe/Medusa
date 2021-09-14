<template>
  <div class="systemInformation">
    <a-descriptions :column="NumberColumn" :size="'small'" bordered>
      <a-descriptions-item
        v-for="(item, i) in systemInformation"
        :key="i"
        :label="item.label"
        :span="item.span"
      >{{ item.data }}</a-descriptions-item>
    </a-descriptions>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { OverallMixins } from "@/js/Mixins/OverallMixins.js"
export default {
  mixins: [OverallMixins],
  name: "systemInformation",
  data () {
    return {
      NumberColumn: {
        xs: 1,
        sm: 2,
        md: 3,
      },
      systemInformation: {},
    };
  },
  computed: {
    ...mapGetters({
      token: "UserStore/token",
    }),
  },
  created () {
    this.handleHardwareInitialization();
  },
  methods: {
    handleHardwareInitialization () {
      let params = {
        token: this.token
      };
      this.$api.hardware_initialization(params).then((res) => {
        if (res.code == 200) {
          let list = [
            {
              label: "中央处理单元架构",
              data: res.message.central_processing_unit_architecture,
              span: 2,
            },
            {
              label: "中央处理单元数",
              data: res.message.central_processing_unit_count,
              span: 1,
            },
            {
              label: "内存大小",
              data: this.QJMemorySize(res.message.memory_total) + "Gb",
              span: 1,
            },
            {
              label: "系统启动时间",
              data: this.moment(res.message.server_start_time, "X"),
              span: 2,
            },
            {
              label: "系统信息",
              data: res.message.system_info,
              span: 2,
            },
            {
              label: "系统名称",
              data: res.message.system_name,
              span: 1,
            },
            {
              label: "系统架构",
              data: res.message.system_type,
              span: 2,
            },
            {
              label: "用户名称",
              data: res.message.user_name,
              span: 1,
            },
          ];
          this.systemInformation = list;
        } else {
          this.$message.error(res.message);
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.systemInformation {
  overflow: auto;
  height: 100%;
}

/*定义整体的宽度*/
.systemInformation::-webkit-scrollbar {
  width: 3px;
}

/*定义滚动条轨道*/
.systemInformation::-webkit-scrollbar-track {
  border-radius: 5px;
}

/*定义滑块*/
.systemInformation::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background: rgba(0, 255, 42, 0.5);
}
</style>
