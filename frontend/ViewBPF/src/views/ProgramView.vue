<template>
  <div class="common-layout">
    <el-container>
      <el-header>Program {{route.params.id}}</el-header>
      <el-main>{{info}}</el-main>
    </el-container>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { ElMessage } from 'element-plus'

const route = useRoute()
const info = ref('')
axios.get('http://localhost:5000/api/programs/' + route.params.id).then(res => {
  console.log(res.data)
  info.value = res.data
}).catch(err => {
  ElMessage({
    message: err,
    type: 'error'
  })
})
</script>