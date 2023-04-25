<template>
  <div class="page1">
    <Row class="listTop">
      <Col span="8">
        <div class="content">
          <span class='title'><span class="title-6">模块一分析</span></span>
          <span class="angle1"></span>
          <span class="angle2"></span>
          <span class="angle3"></span>
          <span class="angle4"></span>
          <LineChart :data="$store.state.chart_data.chart_1_data" id="chart_1_data" ref="chart1"></LineChart>
        </div>
      </Col>
      <Col span="8">
        <div class="content">
          <span class='title'><span class="title-6">模块二分析</span></span>
          <span class="angle1"></span>
          <span class="angle2"></span>
          <span class="angle3"></span>
          <span class="angle4"></span>
          <Scatter3dChart :dataset="$store.state.chart_data.chart_2_data"  id="chart_2_data" ref='chart2'></Scatter3dChart>
        </div>
      </Col>
      <Col span="8">
        <div class="content">
          <span class='title'><span class="title-6">模块三分析</span></span>
          <span class="angle1"></span>
          <span class="angle2"></span>
          <span class="angle3"></span>
          <span class="angle4"></span>
          <LineChart :data="$store.state.chart_data.chart_3_data" id='chart_3_data' ref="chart3"></LineChart>
        </div>
      </Col>
    </Row>
    <Row class="listBottom">
      <Col span='8'>
        <div class="content">
          <span class="title"><span class="title-6">模块四分析</span></span>
          <span class="angle1"></span>
          <span class="angle2"></span>
          <span class="angle3"></span>
          <span class="angle4"></span>
          <LineChart :data="$store.state.chart_data.chart_4_data" id='chart_4_data' ref="chart4"></LineChart>
        </div>
      </Col>
      <Col span='8'>
        <div class="content">
          <span class="title"><span class="title-6">模块五分析</span></span>
          <span class="angle1"></span>
          <span class="angle2"></span>
          <span class="angle3"></span>
          <span class="angle4"></span>
          <LineChart :data="$store.state.chart_data.chart_5_data" id='chart_5_data' ref="chart5"></LineChart>
        </div>
      </Col>
      <Col span='8'>
        <div class="content">
          <span class="title"><span class="title-6">模块六分析</span></span>
          <span class="angle1"></span>
          <span class="angle2"></span>
          <span class="angle3"></span>
          <span class="angle4"></span>
          <LineChart :data="$store.state.chart_data.chart_6_data" id="chart_6_data" ref="chart6"></LineChart>
        </div>
      </Col>
    </Row>
  </div>
</template>

<script>
import LineChart from "@/views/charts/LineChart.vue"
import Scatter3dChart from "@/views/charts/Scatter3dChart.vue"

export default {
  name: "ContentPage",
  components: {
    Scatter3dChart,
    LineChart,
  },
  data() {
    return {
      resizeFn: null
    }
  },
  mounted() {
    this.resizeFn = this.$debounce(() => {
      // 通过捕获系统的onresize事件触发我们需要执行的事件
      for (let i = 1; i < 7; i++)
        this.$refs['chart' + i].setChart();

    }, 500)
    window.addEventListener('resize', this.resizeFn)

  },
  beforeDestroy() {
    window.removeEventListener('resize', this.resizeFn)
  }
}
</script>

<style scoped lang="less">
.page1 {
  height: 100%;
  width: 100%;
  padding: 14px 20px 20px;
  background: #03044A;
  overflow: hidden;

  .listTop, .listBottom {
    height: 50%;

    .ivu-col {
      height: 100%;

      .content {
        width: 98%;
        margin-top: 20px;
        height: calc(~ "100% - 20px");
        border: 1px solid #0D2451;
        position: relative;
      }
    }
  }

}
</style>
