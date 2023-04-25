import Vue from 'vue'
import Router from 'vue-router'
import HomePage from "@/views/HomePage.vue";
import Scatter3dChart from "@/views/charts/Scatter3dChart.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/scatter',
      name: 'Scatter3dChart',
      component:Scatter3dChart
    }
  ]
})
