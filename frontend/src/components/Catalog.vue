<template>
  <div id="catalog">
    <item/>
    <item/>
    <item/>
  </div>
</template>

<script>
import Item from "@/components/Item";

export default {
  name: "Catalog",
  components: {
    Item
  }
}
</script>

<style scoped lang="scss">
#catalog {
  display: grid;
}
</style>