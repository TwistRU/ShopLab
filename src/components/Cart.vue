<template>
  <div class="cart">
    <router-link :to="{name: 'catalog'}">
      <div class="cart__link-to-catalog">
        Вернуться к каталогу
      </div>
    </router-link>
    <h2>Корзина</h2>
    <p v-if="!CART.length">Корзина пуста</p>
    <cart-item
        v-for="(item, index) in CART"
        :key="item['item_id']"
        :item="item"
        @deleteFromCart="deleteFromCart(index)"
    />
    <cart-total/>
  </div>
</template>

<script>
import CartItem from "@/components/CartItem";
import {mapActions, mapGetters} from "vuex";
import CartTotal from "@/components/CartTotal";

export default {
  name: "Cart",
  components: {
    CartTotal,
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

<style lang="scss" scoped>

.cart {
  max-width: 50vw;

  &__link-to-catalog {
    position: absolute;
    top: 10px;
    right: 10px;
    padding: $padding;
    border: solid 1px #aeaeae;
  }
}

</style>