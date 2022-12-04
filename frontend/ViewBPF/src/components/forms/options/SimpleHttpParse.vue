<template>
  <el-form-item label="Interface Name">
    <el-input v-model="form.interfaceName" placeholder="default eth0" />
  </el-form-item>
</template>

<script setup>
const props = defineProps({
	form: Object
})
</script>