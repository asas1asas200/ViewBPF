<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="Program name">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="Program">
      <el-radio-group v-model="form.program" @change="onProgramChange">
        <el-radio v-for="program in programs" :label="program" />
      </el-radio-group>
    </el-form-item>
    <el-collapse-transition>
      <component :is="formMapping[form.program]" :options="form.options"></component>
    </el-collapse-transition>
    <el-form-item label="Code">
      <el-scrollbar max-height="60vh">
        <highlightjs class="code-content" language="c"
          :code=code style="text-align: left;" />
      </el-scrollbar>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>
</template>


<script setup>
import axios from 'axios'
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import 'highlight.js/lib/common'
import hljsVuePlugin from '@highlightjs/vue-plugin'
import 'highlight.js/styles/atom-one-dark.css'
import SimpleHttpParse from '@/components/forms/options/SimpleHttpParse.vue'
import SimpleHttpParseCode from '@/assets/codes/http-parse-simple.c'
import DiskSnoop from '@/components/forms/options/DiskSnoop.vue'
import DiskSnoopCode from '@/assets/codes/disk-snoop.c'

const programs = [
  'Simple HTTP Parse',
  'Disk Snoop',
]

const formMapping = {
  'Simple HTTP Parse': SimpleHttpParse,
  'Disk Snoop': DiskSnoop
}

const sampleCodeMapping = {
  'Simple HTTP Parse': SimpleHttpParseCode,
  'Disk Snoop': DiskSnoopCode
}

const highlightjs = hljsVuePlugin.component

const code = ref(sampleCodeMapping['Simple HTTP Parse'])

// do not use same name with ref
const form = reactive({
  name: '',
  program: 'Simple HTTP Parse',
  desc: '',
  code: code,
  options: {}
})

const onProgramChange = () => {
  code.value = sampleCodeMapping[form.program]
}

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
