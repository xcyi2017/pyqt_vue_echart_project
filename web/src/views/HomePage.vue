<template>
  <div class="app">
    <div class="header">
      <div class="header-title">
        数据可视化平台
      </div>
    </div>
    <ContentPage class="page"></ContentPage>
  </div>
</template>

<script>
import ContentPage from "./components/ContentPage.vue";


export default {
  name: "HomePage",
  components: {
    ContentPage,

  },
  data() {
    return {
      flag: false,
      resizeFn: null
    }
  },
  mounted() {
    window.addEventListener('resize', this.resizeFn)
  }
}
</script>

<style scoped lang="less">
.app {
  width: 100%;
  height: 100%;
  background: #03044A;

  .header {
    height: 1rem;
    width: 100%;
    background: #03044A;
    display: flex;
    justify-content: space-between;
    align-items: center;
    justify-items: center;

    .header-title {
      color: #75deef;
      font-size: 1rem;
      letter-spacing: 0.5rem;
      margin:auto;
    }
  }

  .page {
    height: calc(~ '100% - 1rem');
  }

}

</style>
