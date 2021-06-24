<template>
  <div class="cart-total">
    ЦЕНА: {{ sum_in_cart }}
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "CartTotal",
  computed: {
    ...mapGetters([
      'CART',
    ]),
    sum_in_cart: function () {
      let sum = 0;
      for (let item in this.CART)
        sum += Number(this.CART[item]['price']) * Number(this.CART[item]['count']);
      return sum;
    },
  },
}
</script>

<style scoped>

</style>