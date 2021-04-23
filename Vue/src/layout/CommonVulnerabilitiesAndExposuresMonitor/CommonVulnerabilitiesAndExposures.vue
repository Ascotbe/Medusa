<template>
  <a-row
    :gutter="[
      { xs: 8, sm: 16, md: 24, xs: 8 },
      { xs: 8, sm: 16, md: 24, lg: 32 },
    ]"
    class="common_vulnerabilities_and_exposures"
  >
    <a-col class="common_vulnerabilities_and_exposures_background">

  <a-table
    :columns="columns"
    :data-source="data"
    :scroll="{ x: 200}"
    :pagination="{ pageSize: 100, total:statistics}"
    @change="handle_nist_data_bulk_query"
  >
    <span slot="v2" slot-scope="v2">
      <a-tag v-if="v2[0] === ''">
        {{ "N/A" }}
      </a-tag>
      <a-tag v-else-if="Number(v2[0]) <= '4.0'" :color="'blue'">
        {{ v2[0]+" "+v2[1] }}
      </a-tag>
      <a-tag v-else-if="Number(v2[0])<= '7.0'" :color="'orange'">
        {{ v2[0]+" "+v2[1] }}
      </a-tag>
      <a-tag v-else-if="Number(v2[0])<= '9.0'" :color="'red'">
        {{ v2[0]+" "+v2[1] }}
      </a-tag>
      <a-tag v-else :color="'purple'">
        {{ v2[0]+" "+v2[1] }}
      </a-tag>


</span>
    <span slot="v3" slot-scope="v3">
      <a-tag v-if="v3[1] === ''">
        {{ "N/A" }}
      </a-tag>
      <a-tag v-else-if="v3[1] === 'LOW'" :color="'blue'">
        {{ v3[0]+" "+v3[1] }}
      </a-tag>
      <a-tag v-else-if="v3[1] === 'MEDIUM'" :color="'orange'">
        {{ v3[0]+" "+v3[1] }}
      </a-tag>
      <a-tag v-else-if="v2[1] === 'HIGH'" :color="'red'">
        {{ v3[0]+" "+v3[1] }}
      </a-tag>
      <a-tag v-else-if="v3[1] === 'CRITICAL'" :color="'purple'">
        {{ v3[0]+" "+v3[1] }}
      </a-tag>


</span>
      <p slot="expandedRowRender" slot-scope="record">
      {{ record.vulnerability_description }}
    </p>

  </a-table>

       </a-col>

  </a-row>
</template>
<style lang="scss" scoped>
.common_vulnerabilities_and_exposures{
  margin: 0;
  padding: 20px;
  padding-top: 20px;
  height: 100%;
  min-height: auto;
  .common_vulnerabilities_and_exposures_background {
    background: #fff;
  }
}
</style>



<script>
export default {
  name: "common_vulnerabilities_and_exposures",
  data() {
    return {
      columns: [
        {
          title: "CVE",
          dataIndex: "vulnerability_number",
          //fixed: "left",

        },
        {
          title: "CVSS v2",
          key:"v2",
          dataIndex: "v2",
          scopedSlots: { customRender: 'v2' },
        },
        {
          title: "CVSS v3",
          key:"v3",
          dataIndex: "v3",
          scopedSlots: { customRender: 'v3' },
        },
        {
          title: "Updated",
          key:"last_up_date",
          dataIndex: "last_up_date",
        },
        {
          title: "Vendors",
          key:"vendors",
          dataIndex: "vendors",
        },
        {
          title: "Products",
          key:"products",
          dataIndex: "products",
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
    this.handle_nist_statistics();
    this.handle_nist_data_bulk_query();
  },
  methods: {
    handle_nist_statistics()//个数统计函数
    {
            let params = {
        token: localStorage.getItem("storeToken"),
      };

      this.$api.nist_statistics(params).then((res) =>
      {

        if (res.code == 200) {
          this.statistics=res.message;

        } else {
          this.$message.error(res.message);
        }
      });

    },
    handle_nist_data_bulk_query(page_number) //查询函数
    {
      this.data=[]//对容器进行清空初始化
      let nist_data_page_number=0;//初始化默认值
      try{//获取页数，如果获取失败返回0的值
       nist_data_page_number=page_number.current;
      }catch (error)
       {
      nist_data_page_number=0;
      }
      let params = {
        token: localStorage.getItem("storeToken"),
        number_of_pages: nist_data_page_number,
      };

      this.$api.nist_data_bulk_query(params).then((res) =>
      {

        if (res.code == 200) {
          res.message.map((item) => {
            let tmp_data = {

        vulnerability_number:item.vulnerability_number,
        v3: [item.v3_base_score,item.v3_base_severity],
        v2: [item.v2_base_score,item.v2_base_severity],
        last_up_date: item.last_up_date,
        vulnerability_description: item.vulnerability_description,
        vendors: item.vendors,
        products: item.products,

            };
console.log('this is console.log',tmp_data)
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
