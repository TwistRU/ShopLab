<template>
  <div class="purchase">
    <div class="router-linki">
      <router-link :to="{name: 'cart'}">
        <div class="router-linki__link-to">
          Корзина: {{ CART.length }}
        </div>
      </router-link>
    </div>
    <h2>Итого: {{ sum_in_cart }}</h2>
    <p v-if="!CART.length">Корзина пуста</p>
    <PurchaseItem
        v-for="item in CART"
        :key="item['item_id']"
        :item="item"
    />
    <div class="router-linki__link-to buy" @click="buy">
      Купыт
    </div>
  </div>
</template>

import {mapActions, mapGetters} from "vuex";
<script>
import {mapActions, mapGetters} from "vuex";
import PurchaseItem from "@/components/Purchase/PurchaseItem";

export default {
  name: "Purchase",
  components: {
    PurchaseItem,
  },
  methods: {
    ...mapActions([
      'BUY_PRODUCTS_FROM_API'
    ]),
    buy() {
      this.BUY_PRODUCTS_FROM_API();
      this.$router.push({name: 'catalog'});
    },
  },
  computed: {
    ...mapGetters([
      "CART"
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
.buy{
  cursor: pointer;
}
.purchase {
  max-width: 50vw;
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
}
</style>