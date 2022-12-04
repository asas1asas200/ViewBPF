<template>
  <el-menu style="height: 100vh;" active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo" text-color="#fff" :default-active="currentPath">
    <router-link to="/">
      <el-menu-item index="/">
        <el-icon><icon-menu /></el-icon>
        <span>Home</span>
      </el-menu-item>
    </router-link>
    <router-link to="/add">
      <el-menu-item index="/add">
        <el-icon><circle-plus-filled /></el-icon>
        <span>New</span>
      </el-menu-item>
    </router-link>
    <router-link to="/about">
      <el-menu-item index="/about">
        <el-icon><info-filled /></el-icon>
        <span>About</span>
      </el-menu-item>
    </router-link>
    <el-menu-item index="3">
      <el-icon><setting /></el-icon>
      <span>Settings</span>
    </el-menu-item>
  </el-menu>
</template>

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
</script>
