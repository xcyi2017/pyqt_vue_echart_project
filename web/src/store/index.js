import Vuex from "vuex"
import Vue from "vue";

Vue.use(Vuex)


export var store = new Vuex.Store({
    state: {
        chart_data: {
            chart_1_data: [],
            chart_2_data: [],
            chart_3_data: [],
            chart_4_data: [],
            chart_5_data: [],
            chart_6_data: [],
        }
    },

    mutations: {
        save_data(state, val) {
            state.chart_data[val.name] = val.value;
        }
    }
})