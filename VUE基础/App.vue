<script setup>
// 定义vue属性
// onMounted 页面加载完毕后执行
import {ref, onMounted} from 'vue'

// 导入axios
import axios from "axios"

// 导入消息提示组件
import { ElMessage, ElMessageBox, rowContextKey } from 'element-plus'

// 定义并初始化数据对象
const com = ref({
  'name':'',
  'price':'',
  'number':'',
  'detail':'',
})

// 当页面元素全部加载完毕时 再获取数据
onMounted(()=>{
  getData()
})

// 获取后端数据
const list = ref([]) //初始化list 存储数据
const getData=()=>{
  axios.get("http://182.92.217.5:8001/computer/com/").then((res)=>{
    console.log(res.data.results.resultes),
    list.value = res.data.results.results
  }) // 实际的 results 包含在一个 results 对象内
}

// 定义表单动作函数
const handleClick = () => {
  console.log('click')
}

// 执行添加动作
const add=()=>{
  axios.post("http://182.92.217.5:8001/computer/com/", com.value).then((res)=>{
    if (res.data){
      ElMessage({
        message:"数据添加成功",
        type:"success",
      })
      // 添加完成后执行清空操作
      com.value={
        "name":"",
        "price":"",
        "number":"",
        "detail":"",
      }
      // 调用
      getData()
    }
  })
}

// 执行删除操作
const deleteClick=(pk)=>{
  ElMessageBox.confirm(
    '确定要删除该条数据吗?',
    'Warning',
    {
      confirmButtonText:'确认',
      cancelButtonText:'取消',
      type:'warning',
      center:true,
    }
  )
  .then(()=>{
    //点击确定
    axios.delete(`http://182.92.217.5:8001/computer/com/${pk}/`).then(res=>{
      if(res.status == 204){
        ElMessage({
          message:"删除成功",
          type:"success",
        })
        getData()
      }
    })
  })
}
</script>

<template>
    <div class="test">
    <h1 align="center">企业设备库存信息展示</h1>
    <el-table :data="list" style="width: 100%">
      <el-table-column fixed prop="id" label="ID" width="150" />
      <el-table-column prop="name" label="设备名称" width="120" />
      <el-table-column prop="price" label="设备价格" width="120" />
      <el-table-column prop="number" label="库存数量" width="120" />
      <el-table-column prop="detail" label="设备信息" width="600" />
      <el-table-column fixed="right" label="操作" min-width="120">
        <template #default="scope">
          <el-button link type="primary" size="small" @click="deleteClick(scope.row.id)">
            删除
          </el-button>
          <el-button link type="primary" size="small">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
  <hr/>
  <div class="form-container">
      <h3 class="form-title">添加数据</h3>
    <hr/>
    <el-form :model="form" label-width="auto" border style="max-width: 400px">
      <el-form-item label="设备名称:">
        <el-input v-model="com.name" />
      </el-form-item>
      <br/>
      <el-form-item label="设备价格:">
        <el-input-number v-model="com.price" :precision="2" :step="50" :min="0" />
      </el-form-item>
      <br/>
      <el-form-item label="库存数量:">
        <el-input-number v-model="com.number" :precision="0" :step="1" :min="0" />
      </el-form-item>
      <br/>
      <el-form-item label="设备信息:">
        <el-input
          v-model="com.detail"
          style="width: 240px"
          :autosize="{ minRows: 2, maxRows: 4 }"
          type="textarea"
          placeholder="请输入该设备备注信息或简介"
        />
      </el-form-item>
      <p>
        <el-button type="primary" @click="add">添加</el-button>
      </p>
    </el-form>
  </div>
  
  <br/>
  </div>
</template>

<style scoped>
.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  border: 1px solid #282828; /* 添加边框 */
  border-radius: 8px; /* 边框圆角 */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* 添加阴影 */
  max-width: 500px; /* 设置最大宽度 */
  margin: 0 auto; /* 居中对齐 */
  background-color: #fff; /* 背景颜色 */
}
.form-title {
  margin-bottom: 20px; /* 标题与表单之间的间距 */
  text-align: center; /* 标题居中 */
}
</style>
