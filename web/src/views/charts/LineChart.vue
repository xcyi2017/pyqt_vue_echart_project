<template>
  <div class="panel">

    <div :id='id' ref="data" class="chartArea"></div>

  </div>
</template>

<script>
import {openFile, msgListener} from "@/api";


export default {
  name: 'LineChart',
  props: ['data', 'id'],
  data() {
    return {
      chart: null
    }
  },
  watch: {
    data: { // 监听父组件传来的值
      handler() {
        this.setChart()
      },
      deep: true
    },
  },
  methods: {
    loadData() {
      openFile("")
          .then(res => {
            this.$store.commit("save_data", {name: this.id, value: this.setData(res)});
          })
    },

    setData(raw_data) { // 数据模拟

      let data = []
      for (let i = 0; i < raw_data['PlayTime'].length; i++) {
        data.push([
          raw_data["PlayTime"][i],
          raw_data["LoadValue"][i]
        ])
      }
      return data
    },

    // 上网行为分析
    setChart() {
      let option = {
        animation: true,
        smooth: true,

        dataZoom: [//目录模式所需要对应的设置，start,end表示初始化的范围，取值0-100
          {
            type: 'inside',
            start: 0,
            end: 100
          },
          {
            show: true,
            type: 'slider',
            backgroundColor: 'rgba(47,69,84,0)',
            dataBackground: {//数据阴影的样式。
              lineStyle: {color: "#75deef"},//阴影的线条样式
              areaStyle: {opacity: 0.1, color: "#d2dbee"},//阴影的填充样式
            },
            showDetail: true,
            textStyle: {color: "#75deef"}, // 字体样式
            borderColor: "",//边框颜色
            start: 0,
            end: 100
          }
        ],
        toolbox: {
          show: true,
          right: '4%',
          feature: {
            mark: {show: true},

            saveAsImage: {
              icon: 'path://M 955.1 632.7 c -10.5 -82 -84.4 -141.4 -167.1 -141.4 h -42.8 V 451 c 0 -124.1 -93.4 -232.6 -217.2 -240.9 c -135.8 -9.1 -249.2 98.8 -249.2 232.7 v 48.5 H 236 c -82.7 0 -156.5 59.3 -167.1 141.4 c -12.8 99.3 64.6 184.2 161.4 184.2 h 563.5 c 96.7 0 174.1 -84.9 161.3 -184.2 Z m -324 -9.7 l -97.5 97.5 c -5.9 5.9 -13.8 8.8 -21.6 8.4 c -7.8 0.3 -15.7 -2.5 -21.6 -8.4 L 392.9 623 c -11.3 -11.3 -11.3 -29.6 0 -40.8 l 5.7 -5.7 c 11.3 -11.3 29.6 -11.3 40.8 0 l 39.2 39.2 V 450.3 c 0 -18.3 14.8 -33.2 33.2 -33.2 h 0.5 c 18.3 0 33.2 14.8 33.2 33.2 v 165.3 l 39.2 -39.2 c 11.3 -11.3 29.6 -11.3 40.8 0 l 5.7 5.7 c 11.2 11.3 11.2 29.6 -0.1 40.9 Z',
              show: true,
              excludeComments: ['toolbox', 'dataZoom'],
              pixelRatio: 2,
              title: '保存图片',
              type: 'png',
              iconStyle: {
                color: '#d2dbee'
              }
            },
            myTool1: {
              show: true,
              title: '导入数据',
              icon: 'path://M954.5 632.7c-10.5-82-84.4-141.4-167.1-141.4h-42.8V451c0-124.1-93.4-232.6-217.2-240.9-135.8-9.1-249.2 98.8-249.2 232.7v48.5h-42.8c-82.7 0-156.5 59.3-167.1 141.4-12.8 99.3 64.5 184.2 161.3 184.2h563.5c96.8 0 174.1-84.9 161.4-184.2z m-324-68.7l-5.7 5.7c-11.3 11.3-29.6 11.3-40.8 0l-39.2-39.2v165.3c0 18.3-14.8 33.2-33.2 33.2h-0.5c-18.3 0-33.2-14.8-33.2-33.2V530.5l-39.2 39.2c-11.3 11.3-29.6 11.3-40.8 0l-5.7-5.7c-11.3-11.3-11.3-29.6 0-40.8l97.5-97.5c5.9-5.9 13.8-8.8 21.6-8.4 7.8-0.3 15.7 2.5 21.6 8.4l97.5 97.5c11.4 11.2 11.4 29.5 0.1 40.8z',
              onclick: () => {
                this.loadData()
              },
              iconStyle: {
                color: '#d2dbee'
              }
            },
            myTool2: {
              show: true,
              title: "还原",
              icon: 'path://M 683.6 288.4 l -21.2 26.2 c -12 14.8 -2.6 36.9 16.3 38.7 l 165.9 15.4 c 21.9 2 38.8 -18.8 32.3 -39.8 l -49.6 -159 c -5.7 -18.2 -29.3 -22.7 -41.2 -7.9 l -32.9 40.6 c -85.1 -62.9 -194.4 -89.5 -305.7 -67.7 C 290 165.7 166.1 295.6 142.7 454.4 c -35.4 239.2 149.1 444.7 381.5 444.7 c 159.8 0 301.2 -98 358.9 -243.9 c 9.3 -23.4 4.8 -51.5 -15.1 -66.9 c -31.2 -24.2 -73.4 -10.4 -86.3 23.3 c -48.2 126.3 -183.8 203.5 -325.3 169.1 C 352.3 755.3 271 668 252.8 562.4 c -30 -173.9 103.1 -324.7 271.4 -324.7 c 58.2 -0.1 113.5 18.1 159.4 50.7 Z',
              onclick: () => {
                this.setChart()
              },
              iconStyle: {
                color: '#d2dbee',
                size: 14
              }
            }
          }
        },
        tooltip: { // hover 提示框
          trigger: 'axis',
          axisPointer: {
            type: 'line'
          },
          backgroundColor: '#11367a',
          textStyle: {
            color: '#6dd0e3',
            fontSize: 10,
          }
        },
        xAxis: [{
          name: 'x',
          axisLine: {
            show: true,
            lineStyle: {
              color: '#1a3c58'
            }
          },
          nameTextStyle: {
            color: "#75deef",
            fontSize: ".8rem",
            padding: [0, 15, -10, 0]
          },
          axisTick: {show: true},
          axisLabel: {
            showMaxLabel: true,
            textStyle: {
              color: '#75deef',
              fontSize: 9,
              fontWeight: 'normal'
            }
          },
          minorTick: { // 分刻度
            show: true
          },
          minorSplitLine: { // 分刻度线
            show: false
          },
          splitLine: {show: false},
        }],
        yAxis: [{
          name: 'y',
          axisLine: {
            show: true,
            lineStyle: {
              color: '#1a3c58'
            }
          },
          nameTextStyle: {
            color: "#75deef",
            fontSize: "0.8rem",
            padding: [0, 15, 0, 0]
          },
          axisTick: {show: true},
          minorTick: { // 分刻度
            show: true
          },
          minorSplitLine: { // 分刻度线
            show: false
          },
          splitLine: {show: false},
          axisLabel: {
            showMaxLabel: true,
            textStyle: {
              color: '#75deef',
              fontSize: 9,
              fontWeight: 'normal'
            },
            formatter: function (value) {
              let v;
              const res = value.toString();
              let numN1 = 0;
              let numN2 = 1;
              let num1 = 0;
              let num2 = 0;
              let t1 = 1;
              for (let k = 0; k < res.length; k++) {
                if (res[k] === ".")
                  t1 = 0;
                if (t1)
                  num1++;
                else
                  num2++;
              }
              if (Math.abs(value) < 1 && res.length > 4) {
                for (let i = 2; i < res.length; i++) {
                  if (res[i] === "0") {
                    numN2++;
                  } else if (res[i] === ".")
                    continue;
                  else
                    break;
                }
                v = parseFloat(value);
                v = v * Math.pow(10, numN2);
                return v.toString() + "e-" + numN2;
              } else if (num1 > 4) {
                if (res[0] === "-")
                  numN1 = num1 - 2;
                else
                  numN1 = num1 - 1;
                v = parseFloat(value);
                v = v / Math.pow(10, numN1);
                if (num2 > 4)
                  v = v.toFixed(4);
                return v.toString() + "e" + numN1;
              } else
                return parseFloat(value);
            }
          }
        }],
        //数据集
        series: [
          {
            type: 'line',
            //显示数据点标记
            symbol: 'none',
            showSymbol: false,
            smooth: true,
            lineStyle: {
              width: 1,
              color: {
                type: 'linear',
                x: 1,
                y: 0,
                x2: 0,
                y2: 0,
                colorStops: [
                  {
                    offset: 0, color: 'rgba(51, 231, 252, 1)' // 0% 处的颜色
                  },
                  {
                    offset: 1, color: 'rgba(11, 120, 227, 1)' // 100% 处的颜色
                  }
                ],
                globalCoord: false // 缺省为 false
              }
            },
            //是否裁剪超出坐标系部分的图形
            clip: false,
            //数据
            data: this.data
          }
        ],
        itemStyle: {
          normal: {
            color: {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [
                {
                  offset: 0, color: 'rgba(250, 206, 21, 1)' // 0% 处的颜色
                },
                {
                  offset: 1, color: 'rgba(253, 116, 48, 1)' // 100% 处的颜色
                }
              ],
              globalCoord: false // 缺省为 false
            }
          },
        }
      }

      let myChart = this.$echarts.getInstanceByDom(this.$refs.data)
      if (myChart == null)
        myChart = this.$echarts.init(document.getElementById(this.id))

      myChart.clear()
      myChart.resize()
      myChart.setOption(option)


    },
    receive
        (msg) {
      console.log("receive", msg)
    }
  },
  created() {
    msgListener.add(this.receive);
  }
  ,
  beforeDestroy() {
    msgListener.remove(this.receive);
  },
  mounted() {
    this.setChart()
  }

}
</script>

<style lang="less" scoped>
.panel {
  height: 100%;
  width: 100%;
  display: flex;

  .chartArea {
    width: 99%;
    height: 99%;
    margin: auto;

  }
}

</style>
