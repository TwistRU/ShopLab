<template>
  <div class="catalog">
    <router-link :to="{name: 'cart'}">
      <div class="catalog__link-to-cart">
        Корзина: {{ CART.length }}
      </div>
    </router-link>
    <h2>Каталог</h2>
    <CatalogItem
        v-for="product in PRODUCTS"
        :key="product['id']"
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
    this.GET_PRODUCTS_FROM_API()
  }
}
</script>

<style scoped lang="scss">
.catalog {
  display: grid;

  &__link-to-cart {
    position: absolute;
    top: 10px;
    right: 10px;
    padding: $padding;
    border: solid 1px #aeaeae;
  }
}
</style>