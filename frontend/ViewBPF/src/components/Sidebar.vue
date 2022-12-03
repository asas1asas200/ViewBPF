<template>
  <el-menu style="height: 100vh;" active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo" text-color="#fff" :default-active="currentPath">
    <router-link to="/">
      <el-menu-item index="/">
        <el-icon><icon-menu /></el-icon>
        <span>Navigator Two</span>
      </el-menu-item>
    </router-link>
    <router-link to="/about">
      <el-menu-item index="/about">
        <el-icon><document /></el-icon>
        <span>Navigator Three</span>
      </el-menu-item>
    </router-link>
    <el-menu-item index="3">
      <el-icon><setting /></el-icon>
      <span>Navigator Four</span>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
import {
  Document,
  Menu as IconMenu,
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
</script>
