<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/logo.svg">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <el-button type="primary" @click="ping"> Ping </el-button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
import { ElMessage } from 'element-plus'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  methods: {
    ping() {
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
  }
}
</script>
