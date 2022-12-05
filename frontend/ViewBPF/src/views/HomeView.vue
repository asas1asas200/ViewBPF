<template>
  <div class="home">
    <h1>ViewBPF</h1>
    <el-scrollbar>
      <el-card v-for="program in programs">
        <el-row class="transition-box">
          <el-col :span="8">{{program.name}}</el-col>
          <el-col :span="16">{{program.key}}</el-col>
        </el-row>
      </el-card>
    </el-scrollbar>
    <el-button type="primary" @click="ping"> Ping </el-button>
    <el-button type="success" @click="test"> Test </el-button>
  </div>
</template>

<style scoped>
  .el-card {
    cursor: pointer;
    margin-bottom: 10px;
  }
</style>

<script setup>
// @ is an alias to /src
import axios from 'axios'
import { ElMessage } from 'element-plus'
import { ref } from 'vue'

const programs = ref([]);
axios.get('http://localhost:5000/api/programs').then(res => {
  console.log(res.data)
  programs.value = res.data
}).catch(err => {
  ElMessage({
    message: err,
    type: 'error'
  })
})

const ping = () => {
  axios.get('http://localhost:5000/api/ping').then(res => {
    ElMessage({
      message: res.data,
      type: 'success'
    })
  }).catch(err => {
    ElMessage({
      message: err,
      type: 'error'
    })
  })
}
const test = () => {
  axios.get('http://localhost:5000/api/example/test').then(res => {
    ElMessage({
      message: res.data,
      type: 'success'
    })
  }).catch(err => {
    ElMessage({
      message: err,
      type: 'error'
    })
  })
}
</script>
