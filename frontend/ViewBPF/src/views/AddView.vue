<template>
  <el-tabs v-model="activeName">
    <el-tab-pane label="Examples" name="examples"><example-form /></el-tab-pane>
    <el-tab-pane label="Custom" name="custom">The development of custom eBPF programs is in progress.</el-tab-pane>
  </el-tabs>
</template>
<script setup>
import { ref } from 'vue'
import ExampleForm from '@/components/forms/ExampleForm.vue'

const activeName = ref('examples')
</script>
<style>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
</style>
