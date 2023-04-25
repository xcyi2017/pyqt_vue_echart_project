// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview';
import './assets/less/index.less';
import * as echarts from 'echarts'

import utils from "./lib/utils";
import {store} from "@/store";

Vue.prototype.$echarts = echarts
Vue.config.productionTip = false

Vue.use(iView)
Vue.use(utils)


/* eslint-disable no-new */
new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app')
