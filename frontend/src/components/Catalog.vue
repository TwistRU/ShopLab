<template>
  <div id="catalog">
    <CatalogItem
        v-for="product in PRODUCTS"
        :key="product.id"
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
      'GET_PRODUCTS_FROM_API'
    ]),
  },
  computed: {
    ...mapGetters([
      'PRODUCTS'
    ]),
  },
  mounted() {
    this.GET_PRODUCTS_FROM_API()
  }
}
</script>

<style scoped lang="scss">
#catalog {
  display: grid;
}
</style>