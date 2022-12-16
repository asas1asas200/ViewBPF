<template>
  <div class="home">
    <h1>ViewBPF</h1>
    <el-scrollbar max-height="90vh">
      <el-card v-for="program in programs" @click="router.push({path: `/program/${program.key}`})" :class="program.state">
        <el-row class="transition-box">
          <el-col :span="2">
            <el-icon>
              <Loading v-if="program.state === 'running'" />
              <Finished v-else-if="program.state === 'finished'" />
              <CircleCloseFilled v-else />
            </el-icon>
            {{program.state}}
          </el-col>
          <el-col :span="8">{{program.name}}</el-col>
          <el-col :span="14">{{program.key}}</el-col>
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

  .el-card.running {
    background-color: rgb(28, 37, 24);
    border-color: rgb(62, 107, 39);
    color: rgb(103, 194, 58);
  }

  .el-card.running:hover {
    background-color: rgb(78, 142, 47);
    border-color: rgb(78, 142, 47);
    color: white;
  }

  .el-card.error {
    background-color: rgb(41, 34, 24);
    border-color: rgb(125, 91, 40);
    color: rgb(230, 162, 60);
  }
  .el-card.error:hover {
    background-color: rgb(230, 162, 60);
    border-color: rgb(230, 162, 60);
    color: white;
  }

  .el-card.finished {
    background-color: rgb(24, 34, 44);
    border-color: rgb(42, 89, 138);
    color: rgb(64, 158, 255);
  }

  .el-card.finished:hover {
    background-color: rgb(51, 117, 185);
    border-color: rgb(51, 117, 185);
    color: white;
  }
</style>

<script setup>
// @ is an alias to /src
import axios from 'axios'
import { ElMessage } from 'element-plus'
import { Loading, Finished, CircleCloseFilled } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter();
const programs = ref([]);
axios.get('http://localhost:5000/api/programs').then(res => {
  axios.get('http://localhost:5000/api/programs/state').then(states => {
    programs.value = res.data
    for(let i = 0; i < programs.value.length; i++) {
      programs.value[i].state = states.data[programs.value[i].key]
    }
    console.log(programs.value)
  })
}).catch(err => {
  ElMessage({
    message: err,
    type: 'error'
  })
})
</script>
