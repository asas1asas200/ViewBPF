<template>
  <el-menu style="height: 100vh;" active-text-color="#ffd04b" background-color="#545c64" text-color="#fff" :default-active="currentPath" :collapse="isCollapsed" router>
    <el-menu-item index="/">
      <el-icon><icon-menu /></el-icon>
      <span>Home</span>
    </el-menu-item>
    <el-menu-item index="/add">
      <el-icon><circle-plus-filled /></el-icon>
      <span v-show="!isCollapsed">New</span>
    </el-menu-item>
    <el-menu-item index="/about">
      <el-icon><info-filled /></el-icon>
      <span>About</span>
    </el-menu-item>
    <el-menu-item index="#">
      <el-icon><setting /></el-icon>
      <span>Settings</span>
    </el-menu-item>
  </el-menu>
</template>

<style scoped>
  .el-menu:not(.el-menu--collapse) {
    width: 300px;
  }
</style>

<script lang="ts" setup>
import {
  Menu as IconMenu,
  CirclePlusFilled,
  InfoFilled,
  Setting,
} from '@element-plus/icons-vue'

import { useRoute } from 'vue-router'
import { watch, ref } from 'vue'

const route = useRoute()
const currentPath = ref(route.path)

//FIXME: The path will change twice when the page is refreshed
watch(
  () => route.path,
  path => {
    currentPath.value = path
  },
)

const isCollapsed = ref(false)

const handleResize = () => {
      if (window.innerWidth < 960) {
        isCollapsed.value = true
      } else {
        isCollapsed.value = false
      }
}

window.addEventListener('resize', handleResize)
handleResize()
</script>
