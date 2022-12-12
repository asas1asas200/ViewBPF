<template>
  <div class="common-layout">
    <h1>Program {{info.name}}</h1>
    <el-scrollbar max-height="30vh">
      <el-collapse style="text-align: left;">
        <el-collapse-item title="Verifier Result">
          <highlightjs :code=verify style="overflow-x: auto;"/>
        </el-collapse-item>
        <el-collapse-item title="Code">
          <highlightjs :code=info.code />
        </el-collapse-item>
      </el-collapse>
    </el-scrollbar>
    <SimpleHttpParseCharts />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import axios from 'axios'
import { ElMessage } from 'element-plus'
import 'highlight.js/lib/common'
import 'highlight.js/styles/atom-one-dark.css'
import hljsVuePlugin from '@highlightjs/vue-plugin'
import SimpleHttpParseCharts from './charts/SimpleHttpParseCharts.vue'

const highlightjs = hljsVuePlugin.component

const route = useRoute()
const info = await axios.get('http://localhost:5000/api/programs/' + route.params.id + '/info').then(async (res) => {
  return res.data
}).catch(err => {
  ElMessage({
	message: err,
	type: 'error'
  })
})
const verify = await axios.get('http://localhost:5000/api/programs/' + route.params.id + '/verify').then(async (res) => {
  return res.data
}).catch(err => {
  ElMessage({
	message: err,
	type: 'error'
  })
})
</script>
