<template>
  <div>
    <h2>Корзина</h2>
    <cart-item
        v-for="(item, index) in CART"
        :key="item.id"
        :item="item"
        @deleteFromCart="deleteFromCart(index)"
    />
  </div>
</template>

<script>
import CartItem from "@/components/CartItem";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Cart",
  components: {
    CartItem,
  },
  computed: {
    ...mapGetters([
      "CART"
    ]),
  },
  methods: {
    ...mapActions([
      "DELETE_FROM_CART"
    ]),
    deleteFromCart(index) {
      this.DELETE_FROM_CART(index);
    },
  },
}
</script>

<style scoped>

</style>