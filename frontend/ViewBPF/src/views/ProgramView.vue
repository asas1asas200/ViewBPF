<template>
  <Suspense>
    <template #default>
      <program-info />
    </template>
    <template #fallback>
      <div v-loading="true" element-loading-text="Loading..." element-loading-background="transparent" style="height: 100%;"></div>
    </template>
  </Suspense>
</template>
<style scoped>
.el-loading-mask {
  background: transparent;
}
</style>
<script setup>
import { defineAsyncComponent } from 'vue';
const ProgramInfo = defineAsyncComponent(() => import('@/components/ProgramInfo.vue'));
</script>