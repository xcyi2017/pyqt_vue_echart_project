<template>
  <div class="panel">
    <Select class="selectArea" v-model="model1" @on-change="updateData">
      <Option v-for="item in chooseList" :value="item.value" :key="item.id">{{ item.label }}</Option>
    </Select>
    <div :id="id" ref="chartDom" class="chartArea"></div>
  </div>
</template>

<script>
import "echarts-gl"
import {openFile_1} from "@/api";


export default {
  name: "Scatter3dChart",
  props: ['id', 'dataset'],
  watch: {
    dataset: {
      handler() {
        this._setOption()
        this.setChart()
      },
      deep: true
    }
  },
  data() {
    return {
      response_data: [],
      chooseList: [
        {
          id: 'xyz',
          value: 'chart-xyz',
          label: '3d图'
        },
        {
          id: 'xy',
          value: 'chart-xy',
          label: 'xy图'
        },
        {
          id: 'xz',
          value: 'chart-xz',
          label: 'xz图'
        },
        {
          id: 'yz',
          value: 'chart-yz',
          label: 'yz图'
        }
      ],
      model1: '',
      data2d: [],
      option: {},
      myChart: null
    }
  },

  methods: {
    updateData(data) {
      if (data === 'chart-xy') {
        this.data2d = ['X', 'Y']
      } else if (data === 'chart-xz') {
        this.data2d = ['X', 'Z']
      } else if (data === 'chart-yz') {
        this.data2d = ['Y', 'Z']
      }
      console.log(this.data2d)
      this._setOption()
      this.setChart()
    },
    setChart() {
      this.$nextTick(()=>{
        this.myChart.clear()
        this.myChart.resize()
        this.myChart.setOption(this.option)

      })

    },
    _setOption() {
      let symbolSize = 2.5;
      let option1 = {
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
        grid3D: {
          lineStyle: {
            color: '#d2dbee'
          },
          axisPointer: {
            lineStyle: {
              color: '#d2dbee'
            }
          },
          viewControl: {
            projection: 'orthographic'
          }
        },
        visualMap: {
          calculable: true,
          max: 100,
          // 维度的名字默认就是表头的属性名
          dimension: 'Z',
          inRange: {
            color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
          }
        },
        xAxis3D: {
          type: 'category',
          name: 'x',
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

        },
        yAxis3D: {
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
        },
        zAxis3D: {
          name: 'z',
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
        },
        dataset: {
          dimensions: [
            'X',
            'Y',
            'Z',
            {name: 'Z', type: 'ordinal'}
          ],
          source: this.dataset.length ? this.dataset : [{'X': 0, "Y": 0, "Z": 0}]
        },
        series: [
          {
            type: 'scatter3D',
            symbolSize: symbolSize,
            encode: {
              x: 'x',
              y: 'y',
              z: 'z',
              tooltip: [0, 1, 2, 3, 4]
            }
          }
        ]
      }
      let option2 = {
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
        xAxis: {
          type: 'category',
          boundaryGap: false,
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
        },
        yAxis: {
          type: 'value',
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
        },
        //数据集
        dataset: {dimension:[
          'X',
            'Y',
            'Z'
          ],source: this.dataset},
        series: [
          {
            type: 'scatter',
            encode:{
              x:this.data2d[0],
              y:this.data2d[1]
            }
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
      this.option = this.model1 === 'chart-xyz' || this.model1 === '' ? option1 : option2
    },
    loadData() {
      openFile_1('')
          .then(res => {
            console.log("res_data", res.data);
            this.$store.commit("save_data", {name: this.id, value: this.setData(res.data)});
          })
    },
    setData(data) {
      return data
    }
  },
  mounted() {
    this.myChart = this.$echarts.init(document.getElementById(this.id))
    this._setOption()
    this.setChart()

  }
}
</script>

<style scoped lang="less">
@deep: ~'>>>';

.panel {
  height: 100%;
  width: 100%;
  position: relative;

  @{deep} .ivu-select {

    .ivu-select-selection {
      background-color: #1C5AB320;
      color: #fff;
      border-color: transparent;
    }

    .ivu-select-dropdown {
      background-color: #1C5AB3;
    }

    .ivu-select-item {
      color: #fff;
      background-color: #1C5AB3;

      &:hover {
        background-color: #0D2451;
      }

      &-focused {
        background-color: transparent;
      }
    }
  }

  .selectArea {
    position: absolute;
    top: 0.2rem;
    left: 0.2rem;
    width: 5rem;
    z-index: 2;
  }

  .chartArea {
    width: 99%;
    height: 99%;
    margin: auto;
    position: absolute;
    z-index: 1;
  }

}
</style>