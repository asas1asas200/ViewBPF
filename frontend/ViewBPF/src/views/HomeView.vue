<template>
  <div class="home">
    <h1>ViewBPF</h1>
    <el-scrollbar max-height="90vh">
      <el-card v-for="program in programs" @click="router.push({path: `/program/${program.key}`})">
        <el-row class="transition-box">
          <el-col :span="8">{{program.name}}</el-col>
          <el-col :span="16">{{program.key}}</el-col>
        </el-row>
      </el-card>
    </el-scrollbar>
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
import { useRouter } from 'vue-router';

const router = useRouter();
const programs = ref([]);
axios.get('http://localhost:5000/api/programs').then(res => {
  programs.value = res.data
}).catch(err => {
  ElMessage({
    message: err,
    type: 'error'
  })
})
</script>
