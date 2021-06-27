<template>
  <div class="cart-total">
    <p>ЦЕНА: {{ sum_in_cart }}</p>
    <button v-if="CART.length"
            @click="purchaseBtn">
      Приобрести
    </button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "CartTotal",
  methods: {
    purchaseBtn() {
      if(this.GET_USER.authorized){
        this.$router.push({name:'purchase'})
      }else{
        this.$router.push({name:'auth'})
      }
    },
  },
  computed: {
    ...mapGetters([
      'CART',
      'GET_USER',
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

<style scoped lang='scss'>
.cart-total {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>