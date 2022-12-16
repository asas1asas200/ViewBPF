<template>
  <Line :data=lineData :options=lineOptions />
  <Pie :data=pieData :options=pieOptions style="max-height: 20vh" />
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import axios from 'axios'
import { Line, Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, TimeScale, CategoryScale, LinearScale, PointElement, LineElement, ArcElement, Legend } from 'chart.js'
import 'chartjs-adapter-moment'

ChartJS.register(Title, Tooltip, TimeScale, CategoryScale, LinearScale, PointElement, LineElement, ArcElement, Legend)

const programID = useRoute().params.id
let counts = [0, 0]

const lineData = await 
  axios.get(`http://localhost:5000/api/programs/${programID}/records`)
    .then((res) => {
      if(Object.keys(res.data).length === 0) return []
      let typeW = {
        label: 'Write latency',
        data: [],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        borderWidth: 1,
        radius: 0,
      }

      let typeR = {
        label: 'Read latency',
        data: [],
        fill: false,
        borderColor: 'rgb(255, 205, 86)',
        borderWidth: 1,
        radius: 0,
      }

      for(let data of res.data) {
        switch(data.data.type) {
          case 'W':
            typeW.data.push({x: data.time, y: data.data.lat})
            counts[0]++
            break
          case 'R':
            typeR.data.push({x: data.time, y: data.data.lat})
            counts[1]++
            break
        }
      }

      return {
        datasets: [typeR, typeW]
      }
    })
    .catch(err => {
      ElMessage({
      message: err,
      type: 'error'
      })
    })

const lineOptions = {
  animation: false,
  responsive: true,
  //parsing: false,
  scales: {
    x: {
      type: 'time',
      ticks: {
        color: 'white',
        source: 'auto',
        // Disabled rotation for performance
        maxRotation: 0,
        autoSkip: true,
      }
    },
    y: {
      min: 0,
      ticks: {
        color: 'white'
      }
    }
  },
  interaction: {
      mode: 'nearest',
      axis: 'x',
      intersect: false
  },
  plugins: {
    legend: {
      labels: {
        color: 'white'
      }
    }
  }
}

const pieData = {
  labels: ['Write', 'Read'],
  datasets: [{
    data: counts,
    backgroundColor: [
      'rgb(75, 192, 192)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
}

const pieOptions = {
  plugins: {
    legend: {
      labels: {
        color: 'white'
      }
    }
  }
}
</script>