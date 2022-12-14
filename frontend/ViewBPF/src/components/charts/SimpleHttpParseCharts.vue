<template>
  <Line :data="data" :options=options />
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import axios from 'axios'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, TimeScale, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'
import 'chartjs-adapter-moment'

ChartJS.register(Title, Tooltip, TimeScale, CategoryScale, LinearScale, PointElement, LineElement)

const programID = useRoute().params.id
const socket = io("http://localhost:5000");

socket.on("connect", () => {
  console.log("[Socketio] Connected to server")
})

socket.on(`${programID}/update`, () => updateChart())

async function updateChart() {
  const result = await axios.get(`http://localhost:5000/api/programs/${programID}/records`).then(async (res) => {
    if(Object.keys(res.data).length === 0) return []
    let counts = new Map();
    for(let record of res.data) {
      let time = record.time.slice(0, -3)
      if (counts.has(time)) {
        let data = counts.get(time)
        data.counts++
        data.log.push(record.data)
        counts.set(time, data)
      } else {
        counts.set(time, {counts: 1, log: [record.data]})
      }
    }

    let ret = []
    counts.forEach((value, key) => ret.push({x: key, nested: value}))
    return ret
  }).catch(err => {
    ElMessage({
    message: err,
    type: 'error'
    })
  })

  data.value = {
    datasets: [{
      label: 'HTTP Request Counts',
      data: result,
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1,
      stepped: true,
    }],
  }
}

const options = {
  scales: {
    x: {
      type: 'time',
      ticks: {
        color: 'white',
      }
    },
    y: {
      min: 0,
      ticks: {
        color: 'white'
      }
    }
  },
  parsing: {
    xAxisKey: 'x',
    yAxisKey: 'nested.counts'
  },
  plugins: {
    tooltip: {
      callbacks: {
        label: function(context) {
            let label = context.dataset.label || ''

            if (label) {
                label += ': '
            }
            if (context.parsed.y !== null) {
                label += context.parsed.y;
            }
            return [].concat(label, context.raw.nested.log)
        },
      }
    },
    legend: {
      labels: {
        color: 'white'
      }
    }
  }
}

const data = ref({})
await updateChart()
</script>
