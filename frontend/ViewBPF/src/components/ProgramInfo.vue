<template>
  <div class="common-layout">
    <h1>Program {{info.name}}
      <el-tag :type=info.tagType>
        {{info.state}}
      </el-tag>
    </h1>
    <div style="margin-bottom: 10px;">
    <el-button v-if="info.state === 'running'" type="danger" @click="stop" plain>Stop</el-button>
    </div>
    <el-scrollbar max-height="30vh">
      <el-collapse style="text-align: left;">
        <el-collapse-item title="Verifier Result">
          <highlightjs :code=verify style="overflow-x: auto;"/>
        </el-collapse-item>
        <el-collapse-item title="Code">
          <highlightjs :code=info.code />
        </el-collapse-item>
        <el-collapse-item v-if="info.state === 'error'" title="Error Message">
          <highlightjs :code="info.error_message" />
        </el-collapse-item>
      </el-collapse>
    </el-scrollbar>
    <component :is=charts></component>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
import 'highlight.js/lib/common'
import 'highlight.js/styles/atom-one-dark.css'
import hljsVuePlugin from '@highlightjs/vue-plugin'
import SimpleHttpParseCharts from './charts/SimpleHttpParseCharts.vue'
import DiskSnoopChart from './charts/DiskSnoopCharts.vue'

const highlightjs = hljsVuePlugin.component

const chartsMapping = {
  'Simple HTTP Parse': SimpleHttpParseCharts,
  'Disk Snoop': DiskSnoopChart
}

const route = useRoute()
const router = useRouter()

const info = await axios.get('http://localhost:5000/api/programs/' + route.params.id + '/info').then(async (res) => {
  switch(res.data.state) {
    case 'running':
      res.data.tagType = 'success'
      break
    case 'error':
      res.data.tagType = 'warning'
      break
    case 'finished':
      res.data.tagType = ''
      break
  }
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
const charts = chartsMapping[info.program]

const stop = () => {
  ElMessageBox.confirm(
    'This will stop the program. Continue?',
    'Warning',
    {
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel',
      type: 'warning',
    }
  )
    .then(() => {
      axios.get(`http://localhost:5000/api/programs/${route.params.id}/stop`).then(
        () => {
          ElMessage({
            type: 'success',
            message: 'Stop completed',
          })
          router.go()
        }
      ).catch(err => {
        ElMessage({
          type: 'error',
          message: err,
        })
      })
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: 'Stop canceled',
      })
    })
}
</script>
