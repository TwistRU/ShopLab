<template>
  <div id="main-wrapper">
    <Catalog/>
    <cart
        v-if="CART.length"
        id="cart"
    />
  </div>
</template>

<script>
import Catalog from "@/components/Catalog";
import Cart from "@/components/Cart";
import {mapGetters} from "vuex";

export default {
  name: "MainWrapper",
  components: {
    Cart,
    Catalog
  },
  computed: {
    ...mapGetters([
      "CART"
    ])
  }
}
</script>

<style scoped>
#main-wrapper {
  width: 55vw;
  margin: 0 auto;
}

#cart {
  max-width: 50vw;
}
</style>