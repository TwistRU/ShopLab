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
        v-for="(item, index) in sorted_cart"
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
    sorted_cart: function () {
      function heapsort(array) {
        function heapify(n, i) {
          let i_max = i;
          let left = i * 2 + 1;
          let right = i * 2 + 2;

          if (left < n && array[i_max]['name'] < array[left]['name'])
            i_max = left;

          if (right < n && array[i_max]['name'] < array[right]['name'])
            i_max = right;

          if (i_max !== i) {
            let temp = array[i];
            array[i] = array[i_max];
            array[i_max] = temp;
            heapify(n, i_max);
          }
        }

        let n = array.length;
        for (let i = Math.floor(n / 2); i > -1; --i)
          heapify(n, i);
        for (let i = Math.floor(n / 2); i > -1; --i) {
          let temp = array[i];
          array[i] = array[0];
          array[0] = temp;
          heapify(i, 0);
        }
      }
      let cart = this.CART.slice();
      if (cart.length === 0)
        return cart;
      heapsort(cart)
      return cart;
    },
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