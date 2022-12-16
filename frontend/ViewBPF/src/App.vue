<template>
  <div class="common-layout">
  <el-container>
    <el-aside style="position: sticky;">
      <Sidebar />
    </el-aside>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
  </div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue'
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1 {
  font-size: 32px;
  color: #409EFF;
  margin-bottom: 10px;
}

.el-aside {
  max-width: fit-content;
}
</style>
