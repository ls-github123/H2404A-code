<script lang="ts" setup>
// 定义vue属性
import { ref, onMounted, computed, reactive } from 'vue'
// 导入axios
import axios from 'axios'
// 导入消息提示组件
import { ElMessage, ElMessageBox } from 'element-plus'
// 图标数据导入
import {
  Delete,
  Edit,
  Search,
} from '@element-plus/icons-vue'

// 初始化表单数据
let data = ref([])

// 分页数据
let query = ref({
  "page":1,
  "size":5,
  "search":'', // 搜索参数 
})
let total = ref(0)
const changepage = (number) => {
  query.value.page = number;
  getData();
}

// 获取表单分类数据数据
let catedata = ref([])
const getCate = () => {
  axios.get("http://127.0.0.1:8000/api/cate/")
  .then(res => {
    console.log(res.data);
    catedata.value = res.data;
  })
}

// 获取后端留言表单数据
const getData = () => {
  axios.get("http://127.0.0.1:8000/api/message/", {params:query.value})
  .then((res) => {
    console.log(res.data);
    data.value = res.data.results.results;
    total.value = res.data.count // 获取总记录数 为分页器赋值
  })
}

// 页面元素加载完毕后调用数据接口
onMounted(() => {
  getCate(); // 获取分类数据
  getData(); // 获取留言表单数据
})

// 执行留言单条编辑操作
const EditMessageForm = ref(false)
const EditForm = ref({
  id: '',
  title:'',
  author:'',
  content:'',
  cate: '',
})
const openDialog = (row: { id: string; title: string; author: string; content: string; cate: string; }) => {
  console.log(EditForm.value.cate);
  EditForm.value = { ...row };
  EditMessageForm.value = true
}
// 保存数据
const confirmEdit = async() => {
  // 将 cate 字段转换为字符串类型
  EditForm.value.cate = EditForm.value.cate.toString();
  // 打印转换后的 EditForm.value 确认内容
  // console.log('即将提交的表单数据:', EditForm.value);
  try{
    const response = await axios.put(`http://127.0.0.1:8000/api/message/${EditForm.value.id}/`, EditForm.value)
    console.log('修改数据', response.data);
    getData();
    EditMessageForm.value = false // 保存成功后关闭对话框
  }
  catch (error) {
    console.error('数据修改失败', error)
  }
}

// 执行删除操作
const deleteClick = (pk: number) => {
  ElMessageBox.confirm(
    '确定要删除该条信息吗?',
    'Warning',
    {
      confirmButtonText:'确认',
      cancelButtonText:'取消',
      type:'warning',
      center:true,
    }
  )
  .then(() => {
    // 点击确定
    axios.delete(`http://127.0.0.1:8000/api/message/${pk}/`)
    .then(res => {
      if (res.status == 204){
        ElMessage({
          // 点击删除
          type:"success",
          message:"删除成功"
        })
        getData() // 删除成功刷新表单数据
      }
    })
    .catch(error => {
      ElMessage({
        type:'error',
        message:'删除失败,请检查重试',
      });
    })
  })
  .catch(() => {
    // 点击取消
    ElMessage({
      type:'info',
      message:'取消删除',
    })
  })
}

// 执行数据添加操作
const IsAddOpen = ref(false)
const MessageInfo = ref ({
  title:'',
  author:'',
  content:'',
  cate:'',
})
const AddOpen = () => {
  IsAddOpen.value = true
}
const formLabelWidth = ''
const saveinfo = () => {
  axios.post("http://127.0.0.1:8000/api/message/", MessageInfo.value)
  .then(res => {
    if (res.data.status == 200){
      ElMessage.success("信息提交成功");
      getData();
      // 清空表单信息
      MessageInfo.value = {
        "title":"",
        "author":"",
        "content":"",
        "cate":"",
      }
      IsAddOpen.value = false; // 清空信息后关闭对话框
    }
  })
  .catch(error => {
    ElMessage({
      type:'error',
      message:'提交失败,请检查重试',
    });
    console.error('提交失败', error);
  })
}
// 取消添加
const CancleSave = () => {
  // 清空表单信息
  MessageInfo.value = {
    "title":"",
    "author":"",
    "content":"",
    "cate": "",
  }
  ElMessage({
    type:'info',
    message:'取消添加'
  })
  // 关闭对话框
  IsAddOpen.value = false
}

</script>

<template>
  <div class="test">
    <h1 align="center">留言信息展示</h1>
    <!--数据添加模块-->
    <div class="add">
        <div class="addbutton">
          <el-button plain @click="AddOpen">
            添加信息
          </el-button>
        </div>
        <el-dialog v-model="IsAddOpen" title="填写留言信息" width="500">
        <el-form :model="MessageInfo">
          <el-form-item label="留言标题:" :label-width="formLabelWidth">
            <el-input v-model="MessageInfo.title" autocomplete="off" />
          </el-form-item>
          <el-form-item label="留言人:" :label-width="formLabelWidth">
            <el-input v-model="MessageInfo.author" autocomplete="off" />
          </el-form-item>
          <el-form-item label="留言内容:" :label-width="formLabelWidth">
            <el-input v-model="MessageInfo.content" autocomplete="off" />
          </el-form-item>
          <el-form-item label="留言类型:" :label-width="formLabelWidth">
            <el-select v-model="MessageInfo.cate" placeholder="请选择留言类型">
              <el-option
                v-for="(item, key) in catedata"
                :key="key"
                :value="item.id.toString()"
                :label="item.name">
                {{ item.name }}
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <template #footer>
          <div class="dialog-footer">
            <el-button @click="CancleSave">取消</el-button>
            <el-button type="primary" @click="saveinfo">
              提交信息
            </el-button>
          </div>
        </template>
      </el-dialog>
    </div>

    <el-table :data="data" style="width: 100%">
      <el-table-column fixed prop="id" label="ID" width="60" />
      <el-table-column prop="title" label="留言标题" width="120" />
      <el-table-column prop="author" label="留言人" width="120" />
      <el-table-column prop="content" label="留言内容" width="580" />
      <el-table-column prop="cate" label="留言类型" width="120" />
      <el-table-column fixed="right" label="操作" min-width="120">
        <!--操作模块-->
        <template #default="scope">
          <el-button type="primary" :icon="Edit" circle @click="openDialog(scope.row)" /> <!--编辑-->
          <el-button type="danger" :icon="Delete" circle @click="deleteClick(scope.row.id)"/> <!--删除-->
        </template>
      </el-table-column>
    </el-table>
    <!--信息编辑表单模块-->
    <el-dialog v-model="EditMessageForm" title="编辑信息" width="500">
        <el-form :model="EditForm">
          <el-form-item label="留言标题:">
            <el-input v-model="EditForm.title" autocomplete="off" />
          </el-form-item>
          <el-form-item label="留言人:">
            <el-input v-model="EditForm.author" autocomplete="off" />
          </el-form-item>
          <el-form-item label="留言内容:" >
            <el-input v-model="EditForm.content" autocomplete="off" />
          </el-form-item>
          <el-form-item label="留言类型:" :label-width="formLabelWidth">
            <el-select v-model="EditForm.cate" placeholder="请选择留言类型">
              <el-option
                v-for="(item, key) in catedata"
                :key="key"
                :value="item.id.toString()"
                :label="item.name">
                
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <template #footer>
          <div class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取消</el-button>
            <el-button type="primary" @click="confirmEdit">保存</el-button>
          </div>
        </template>
    </el-dialog>
    <!--分页选择器模块-->
    <el-pagination background layout="prev, pager, next" :total="total" :page-size="query.size" @current-change="changepage" 
    class="pagination-center" />
  </div>
</template>

<style scoped>
.pagination-center {
  display: flex;
  justify-content: center; /* 居中对齐 */
  margin-top: 20px;
}
</style>