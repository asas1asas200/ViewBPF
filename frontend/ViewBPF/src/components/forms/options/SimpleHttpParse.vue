<template>
  <el-form-item label="Interface Name">
    <el-input v-model="options.interface" placeholder="default eth0" />
  </el-form-item>
</template>

<script setup>
const props = defineProps({
	options: Object
})
</script>