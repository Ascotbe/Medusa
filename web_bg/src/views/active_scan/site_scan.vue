 <template>
   <div class="app-container">
     <div class="filter-container">
       资产搜索：
       <el-input v-model="listQuery.title" placeholder="请输入" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
       <el-select v-model="listQuery.importance" placeholder="星级" clearable style="width: 90px" class="filter-item">
         <el-option v-for="item in importanceOptions" :key="item" :label="item" :value="item" />
       </el-select>
       <el-select v-model="listQuery.type" placeholder="类型" clearable class="filter-item" style="width: 130px">
         <el-option v-for="item in calendarTypeOptions" :key="item.key" :label="item.display_name" :value="item.key" />
       </el-select>
       <el-select v-model="listQuery.sort" style="width: 140px" class="filter-item" @change="handleFilter">
         <el-option v-for="item in sortOptions" :key="item.key" :label="item.label" :value="item.key" />
       </el-select>
       <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
         搜索
       </el-button>
       <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
         添加
       </el-button>
       <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
         导出
       </el-button>
     </div>

     <el-table
       :key="tableKey"
       v-loading="listLoading"
       :data="list"
       border
       fit
       highlight-current-row
       style="width: 100%;"
       @sort-change="sortChange"
     >
       <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80" :class-name="getSortClass('id')">
         <template slot-scope="{row}">
           <span>{{ row.id }}</span>
         </template>
       </el-table-column>
       <el-table-column label="日期" width="150px" align="center">
         <template slot-scope="{row}">
           <span>{{ row.timestamp | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
         </template>
       </el-table-column>
       <el-table-column label="我的资产" min-width="150px">
         <template slot-scope="{row}">
           <span class="link-type" @click="handleUpdate(row)">{{ row.title }}</span>
           <el-tag>{{ row.type | typeFilter }}</el-tag>
         </template>
       </el-table-column>
       <el-table-column label="类型" width="80px">
         <template slot-scope="{row}">
           <svg-icon v-for="n in + row.importance" :key="n" icon-class="star" class="meta-item__icon" />
         </template>
       </el-table-column>
       <el-table-column label="状态" class-name="status-col" width="100">
         <template slot-scope="{row}">
           <el-tag :type="row.status | statusFilter">
             {{ row.status }}
           </el-tag>
         </template>
       </el-table-column>
       <el-table-column label="Actions" align="center" width="230" class-name="small-padding fixed-width">
         <template slot-scope="{row,$index}">
           <el-button type="primary" size="mini" @click="handleUpdate(row)">
             编辑
           </el-button>
           <el-button v-if="row.status!='published'" size="mini" type="success" @click="handleModifyStatus(row,'published')">
             完成
           </el-button>
           <el-button v-if="row.status!='draft'" size="mini" @click="handleModifyStatus(row,'draft')">
             草稿
           </el-button>
           <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="handleDelete(row,$index)">
             删除
           </el-button>
         </template>
       </el-table-column>
     </el-table>

     <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

     <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
       <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
         <el-form-item label="类型" prop="type">
           <el-select v-model="temp.type" class="filter-item" placeholder="请选择">
             <el-option v-for="item in calendarTypeOptions" :key="item.key" :label="item.display_name" :value="item.key" />
           </el-select>
         </el-form-item>
         <el-form-item label="日期" prop="timestamp">
           <el-date-picker v-model="temp.timestamp" type="datetime" placeholder="请填写日期" />
         </el-form-item>
         <el-form-item label="标题" prop="title">
           <el-input v-model="temp.title" />
         </el-form-item>
         <el-form-item label="状态">
           <el-select v-model="temp.status" class="filter-item" placeholder="请选择">
             <el-option v-for="item in statusOptions" :key="item" :label="item" :value="item" />
           </el-select>
         </el-form-item>
         <el-form-item label="星级">
           <el-rate v-model="temp.importance" :colors="['#99A9BF', '#F7BA2A', '#FF9900']" :max="3" style="margin-top:8px;" />
         </el-form-item>
         <el-form-item label="标记">
           <el-input v-model="temp.remark" :autosize="{ minRows: 2, maxRows: 4}" type="textarea" placeholder="请输入" />
         </el-form-item>
       </el-form>
       <div slot="footer" class="dialog-footer">
         <el-button @click="dialogFormVisible = false">
           取消
         </el-button>
         <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
           确认
         </el-button>
       </div>
     </el-dialog>

     <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
       <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
         <el-table-column prop="key" label="Channel" />
         <el-table-column prop="pv" label="Pv" />
       </el-table>
       <span slot="footer" class="dialog-footer">
         <el-button type="primary" @click="dialogPvVisible = false">确认</el-button>
       </span>
     </el-dialog>
   </div>
 </template>

 <script>
 import { fetchList, fetchPv, createArticle, updateArticle } from '@/api/article'
 import waves from '@/directive/waves' // waves directive
 import { parseTime } from '@/utils'
 import Pagination from '@/components/Pagination' // secondary package based on el-pagination

 const calendarTypeOptions = [
   { key: 'CN', display_name: '已完成' },
   { key: 'US', display_name: '中断' },
   { key: 'JP', display_name: '超时' },
   { key: 'EU', display_name: '进行中' }
 ]

 // 关键字不修改是因为复用组件，找起来有点麻烦，先改大致的后来再改关键字
 const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
   acc[cur.key] = cur.display_name
   return acc
 }, {})

 export default {
   name: 'ComplexTable',
   components: { Pagination },
   directives: { waves },
   filters: {
     statusFilter(status) {
       const statusMap = {
         published: 'success',
         draft: 'info',
         deleted: 'danger'
       }
       return statusMap[status]
     },
     typeFilter(type) {
       return calendarTypeKeyValue[type]
     }
   },
   data() {
     return {
       tableKey: 0,
       list: null,
       total: 0,
       listLoading: true,
       listQuery: {
         page: 1,
         limit: 20,
         importance: undefined,
         title: undefined,
         type: undefined,
         sort: '+id'
       },
       importanceOptions: [1, 2, 3],
       calendarTypeOptions,
       sortOptions: [{ label: 'ID升序', key: '+id' }, { label: 'ID 降序', key: '-id' }],
       statusOptions: ['待扫描', '已完成', '草稿'],
       temp: {
         id: undefined,
         importance: 1,
         remark: '',
         timestamp: new Date(),
         title: '',
         type: '',
         status: '草稿'
       },
       dialogFormVisible: false,
       dialogStatus: '',
       textMap: {
         update: 'Edit',
         create: 'Create'
       },
       dialogPvVisible: false,
       pvData: [],
       rules: {
         type: [{ required: true, message: '请选择类型', trigger: 'change' }],
         timestamp: [{ type: 'date', required: true, message: '请填写时间', trigger: 'change' }],
         title: [{ required: true, message: '请输入标题', trigger: 'blur' }]
       },
       downloadLoading: false
     }
   },
   created() {
     this.getList()
   },
   methods: {
     getList() {
       this.listLoading = true
       fetchList(this.listQuery).then(response => {
         this.list = response.data.items
         this.total = response.data.total

         // Just to simulate the time of the request
         setTimeout(() => {
           this.listLoading = false
         }, 1.5 * 1000)
       })
     },
     handleFilter() {
       this.listQuery.page = 1
       this.getList()
     },
     handleModifyStatus(row, status) {
       this.$message({
         message: '操作成功',
         type: 'success'
       })
       row.status = status
     },
     sortChange(data) {
       const { prop, order } = data
       if (prop === 'id') {
         this.sortByID(order)
       }
     },
     sortByID(order) {
       if (order === 'ascending') {
         this.listQuery.sort = '+id'
       } else {
         this.listQuery.sort = '-id'
       }
       this.handleFilter()
     },
     resetTemp() {
       this.temp = {
         id: undefined,
         importance: 1,
         remark: '',
         timestamp: new Date(),
         title: '',
         status: '草稿',
         type: ''
       }
     },
     handleCreate() {
       this.resetTemp()
       this.dialogStatus = 'create'
       this.dialogFormVisible = true
       this.$nextTick(() => {
         this.$refs['dataForm'].clearValidate()
       })
     },
     createData() {
       this.$refs['dataForm'].validate((valid) => {
         if (valid) {
           this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
           // this.temp.author = 'vue-element-admin'
           createArticle(this.temp).then(() => {
             this.list.unshift(this.temp)
             this.dialogFormVisible = false
             this.$notify({
               title: 'Success',
               message: '创建成功',
               type: 'success',
               duration: 2000
             })
           })
         }
       })
     },
     handleUpdate(row) {
       this.temp = Object.assign({}, row) // copy obj
       this.temp.timestamp = new Date(this.temp.timestamp)
       this.dialogStatus = 'update'
       this.dialogFormVisible = true
       this.$nextTick(() => {
         this.$refs['dataForm'].clearValidate()
       })
     },
     updateData() {
       this.$refs['dataForm'].validate((valid) => {
         if (valid) {
           const tempData = Object.assign({}, this.temp)
           tempData.timestamp = +new Date(tempData.timestamp) 
           updateArticle(tempData).then(() => {
             const index = this.list.findIndex(v => v.id === this.temp.id)
             this.list.splice(index, 1, this.temp)
             this.dialogFormVisible = false
             this.$notify({
               title: 'Success',
               message: '更新成功',
               type: 'success',
               duration: 2000
             })
           })
         }
       })
     },
     handleDelete(row, index) {
       this.$notify({
         title: 'Success',
         message: '删除成功',
         type: 'success',
         duration: 2000
       })
       this.list.splice(index, 1)
     },
     handleFetchPv(pv) {
       fetchPv(pv).then(response => {
         this.pvData = response.data.pvData
         this.dialogPvVisible = true
       })
     },
     handleDownload() {
       this.downloadLoading = true
       import('@/vendor/Export2Excel').then(excel => {
         const tHeader = ['timestamp', 'title', 'type', 'importance', 'status']
         const filterVal = ['timestamp', 'title', 'type', 'importance', 'status']
         const data = this.formatJson(filterVal)
         excel.export_json_to_excel({
           header: tHeader,
           data,
           filename: 'table-list'
         })
         this.downloadLoading = false
       })
     },
     formatJson(filterVal) {
       return this.list.map(v => filterVal.map(j => {
         if (j === 'timestamp') {
           return parseTime(v[j])
         } else {
           return v[j]
         }
       }))
     },
     getSortClass: function(key) {
       const sort = this.listQuery.sort
       return sort === `+${key}` ? 'ascending' : 'descending'
     }
   }
 }
 </script>
