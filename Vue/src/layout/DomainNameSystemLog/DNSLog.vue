<template>
  <a-row
    :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 8, sm: 16, md: 24, lg: 32 },
    ]"
    class="domain_name_system_log"
  >
    <a-col class="domain_name_system_log_background">
<img style="display:block;margin-left:auto;
margin-right: auto;width:200px;padding: 20px;" src="../../assets/DomainNameSystemLogLogo.gif"  width="70">
 <hr style="height:5px;border:none;border-top:5px ridge green;padding: 20px;width:80%" />
<div style="width: 80%;height: 80%;margin-left: auto;margin-right: auto;">
  <a-table
    :columns="columns"
    :data-source="data"
    :scroll="{ x: 200}"
    :pagination="{ pageSize: 100, total:statistics}"
    @change="handle_domain_name_system_log"
  >
  </a-table>
  <!-- <p>{{ statistics }}</p> -->
</div>

<!-- <p>{{ data }}</p> -->
       </a-col>

  </a-row>
</template>
<style lang="scss" scoped>
.domain_name_system_log{
  margin: 0;
  padding: 20px;
  padding-top: 20px;
  height: 100%;
  min-height: auto;
  .domain_name_system_log_background {
    background: #fff;
  }
}
</style>



<script>
export default {
  name: "domain_name_system_log",
  data() {
    return {
      columns: [
        {
          title: "DNS Query Record",
          dataIndex: "domain_name",
          fixed: "left",
          width:"45%"

        },
        {
          title: "IP Address",
          dataIndex: "ip",
          width:"30%"
        },
        {
          title: "Created Time",
          dataIndex: "creation_time",
          width:"25%"
        },
      ],
      data: [],
      statistics:0,
      options: [],
    };
  },
  mounted() {
    this.columns.map((item) => {
      let itemlist = {
        value: item.dataIndex,
        label: item.title,
      };


      this.options.push(itemlist);
      //console.log('this is console.log',this.options);
    });
    this.handle_domain_name_system_log();
    this.handle_domain_name_system_log_statistics();
  },
  methods: {
    handle_domain_name_system_log_statistics()//个数统计函数
    {
            let params = {
        token: localStorage.getItem("storeToken"),
      };

      this.$api.domain_name_system_log_statistics(params).then((res) =>
      {

        if (res.code == 200) {
          this.statistics=res.message;

        } else {
          this.$message.error(res.message);
        }
      });

    },
    handle_domain_name_system_log(page_number) //查询函数
    {
      this.data=[]//对容器进行清空初始化
      let domain_name_system_log_page_number=0;//初始化默认值
      try{//获取页数，如果获取失败返回0的值
       domain_name_system_log_page_number=page_number.current;
      }catch (error)
       {
      domain_name_system_log_page_number=0;
      }
      let params = {
        token: localStorage.getItem("storeToken"),
        number_of_pages: domain_name_system_log_page_number,
      };

      this.$api.domain_name_system_log(params).then((res) =>
      {

        if (res.code == 200) {
          res.message.map((item) => {
            let tmp_data = {
              domain_name: item.domain_name,
              ip: item.ip,
              creation_time: item.creation_time,

            };

            this.data.push(tmp_data);//把获取到的数据存放到容器中


          });

          //console.log('this is console.log',this.data.length)
        } else {
          this.$message.error(res.message);
        }
      });
    },


  },
};

</script>
