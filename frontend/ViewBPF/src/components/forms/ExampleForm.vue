<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="Activity name">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="Program">
      <el-radio-group v-model="form.program">
        <el-radio v-for="program in programs" :label="program" />
      </el-radio-group>
    </el-form-item>
    <el-collapse-transition>
    <simple-http-parse :form="form" v-show="form.program === 'Simple HTTP Parse'"/>
    </el-collapse-transition>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { reactive } from 'vue'
import SimpleHttpParse from '@/components/forms/options/SimpleHttpParse.vue'

const programs = [
  'Simple HTTP Parse',
  'Disk Monitoring',
]

// do not use same name with ref
const form = reactive({
  name: '',
  program: '',
  desc: '',
  interfaceName: '',
})

const onSubmit = () => {
  console.log('submit!', form)
}
</script>
