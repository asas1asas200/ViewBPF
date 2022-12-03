<template>
  <div class="common-layout">
  <el-container>
    <el-aside width="300px">
      <Sidebar/>
    </el-aside>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue'

export default {
  components: {
    Sidebar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
