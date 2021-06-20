<template>
  <div>
    <h2>Корзина</h2>
    <cart-item
        v-for="item in CART"
        :key="item.id"
        :item="item"
    />
  </div>
</template>

<script>
import CartItem from "@/components/CartItem";
import {mapGetters} from "vuex";

export default {
  name: "Cart",
  components: {
    CartItem
  },
  computed: {
    ...mapGetters([
        "CART"
    ])
  },
}
</script>

<style scoped>

</style>