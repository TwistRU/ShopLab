<template>
  <div id="main-wrapper">
    <keep-alive>
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>

export default {
  name: "MainWrapper",
}
</script>

<style scoped>
#main-wrapper {
  width: 55vw;
  margin: 0 auto;
}
</style>