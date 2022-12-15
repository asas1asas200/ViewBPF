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
      <component :is="programMapping[form.program].form" :options="form.options"></component>
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

const highlightjs = hljsVuePlugin.component

const programs = [
  'Simple HTTP Parse',
  'Disk Snoop',
]

const programMapping = {
  'Simple HTTP Parse': {
    form: SimpleHttpParse,
    code: SimpleHttpParseCode,
    url: '/api/example/simple_http_parse'
  },
  'Disk Snoop': {
    form: DiskSnoop,
    code: DiskSnoopCode,
    url: '/api/example/disk_snoop'
  }
}


const code = ref(programMapping['Simple HTTP Parse'].code)

// do not use same name with ref
const form = reactive({
  name: '',
  program: 'Simple HTTP Parse',
  desc: '',
  code: code,
  options: {}
})

const onProgramChange = () => {
  code.value = programMapping[form.program].code
}

const onSubmit = () => 
  axios.post(`http://localhost:5000${programMapping[form.program].url}`, form).then(res => {
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

</script>
