<template>
  <div class="catalog">
    <div class="router-linki">
      <router-link :to="{name: 'cart'}">
        <div class="router-linki__link-to">
          Корзина: {{ CART.length }}
        </div>
      </router-link>
      <router-link :to="{name: 'auth'}">
        <div class="router-linki__link-to">
          Авторизация
        </div>
      </router-link>
    </div>

    <h2>Каталог</h2>
    <CatalogItem
        v-for="product in PRODUCTS"
        :key="product['item_id']"
        v-bind:product_data="product"
    />
  </div>
</template>

<script>
import CatalogItem from "@/components/CatalogItem";
import {mapActions, mapGetters} from "vuex"

export default {
  name: "Catalog",
  components: {
    CatalogItem,
  },
  methods: {
    ...mapActions([
      'GET_PRODUCTS_FROM_API',
    ]),
  },
  computed: {
    ...mapGetters([
      'PRODUCTS',
      'CART',
    ]),
  },
  mounted() {
    this.GET_PRODUCTS_FROM_API();
  }
}
</script>

<style scoped lang="scss">

.catalog {
  display: grid;

  &__link-to-cart {
    top: 10px;
    padding: $padding;
    border: solid 1px #aeaeae;
  }
}
</style>