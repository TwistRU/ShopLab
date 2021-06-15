<template>
  <div id="main-wrapper">
    <Catalog/>
  </div>
</template>

<script>
import Catalog from "@/components/Catalog";

export default {
  name: "MainWrapper",
  components: {
    Catalog
  }
}
</script>

<style scoped>
#main-wrapper {
  max-width: 1000px;
  margin: 0 auto;
}
</style>