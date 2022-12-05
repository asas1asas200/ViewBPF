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
    <simple-http-parse :options="form.options" v-if="form.program === 'Simple HTTP Parse'"/>
    </el-collapse-transition>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import axios from 'axios';
import { reactive } from 'vue'
import SimpleHttpParse from '@/components/forms/options/SimpleHttpParse.vue'
import { ElMessage } from 'element-plus';

const programs = [
  'Simple HTTP Parse',
  'Disk Monitoring',
]

// do not use same name with ref
const form = reactive({
  name: '',
  program: '',
  desc: '',
  options: {}
})

const onSubmit = () => {
  switch(form.program) {
    case 'Simple HTTP Parse':
      axios.post('http://localhost:5000/api/example/simple_http_parse', form).then(res => {
        ElMessage({
          message: res.data,
          type: 'success'
        })
      }).catch(err => {
        ElMessage({
          message: err,
          type: 'error'
        })
      })
      console.log(form)
      break
    case 'Disk Monitoring':
      console.log(form)
      break
    default:
      console.log('No program selected')
  }
}
</script>
