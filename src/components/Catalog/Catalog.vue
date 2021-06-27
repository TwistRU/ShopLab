<template>
  <div class="catalog">
    <div class="router-linki">
      <router-link :to="{name: 'cart'}">
        <div class="router-linki__link-to">
          Корзина: {{ CART.length }}
        </div>
      </router-link>
      <router-link
          v-if="!GET_USER.authorized"
          :to="{name: 'auth'}"
      >
        <div class="router-linki__link-to">
          Авторизация
        </div>
      </router-link>
      <div v-else
           class="router-linki__link-to catalog__logout"
           @click="LOGOUT(); $router.push({name: 'auth'})">
        Выход
      </div>
      <router-link v-if="GET_USER.role === 1" :to="{name: 'admin'}">
        <div class="router-linki__link-to">
          Админ
        </div>
      </router-link>
    </div>

    <h2>Каталог</h2>
    <CatalogItem
        v-for="product in PRODUCTS"
        :key="product['item_id']"
        v-bind:product_data="product"
    />
    <div class="pages">
      <div class="btn" @click="previous_page">
        <p>&lt;&lt;</p>
      </div>
      <p> Стр.{{ CURRENT_PAGE.currentPage }} </p>
      <div class="btn" @click="next_page">
        <p>&gt;&gt;</p>
      </div>
    </div>
  </div>
</template>
// TODО Сделать страницу товара
<script>
import CatalogItem from "@/components/Catalog/CatalogItem";
import {mapActions, mapGetters, mapMutations} from "vuex"

export default {
  name: "Catalog",
  components: {
    CatalogItem,
  },
  methods: {
    ...mapMutations([
      'SET_CURRENT_PAGE'
    ]),
    ...mapActions([
      'GET_PRODUCTS_FROM_API',
      'LOGOUT',
    ]),
    previous_page() {
      this.SET_CURRENT_PAGE(Math.max(this.CURRENT_PAGE.currentPage - 1, 1));
      this.GET_PRODUCTS_FROM_API();
    },
    next_page() {
      this.SET_CURRENT_PAGE(Math.min(this.CURRENT_PAGE.currentPage + 1, this.CURRENT_PAGE.maxPage));
      this.GET_PRODUCTS_FROM_API();
    },
  },
  computed: {
    ...mapGetters([
      'GET_USER',
      'PRODUCTS',
      'CART',
      'CURRENT_PAGE',
    ]),
  },
  mounted() {
    this.GET_PRODUCTS_FROM_API();
  }
}
</script>

<style scoped lang="scss">

.pages {
  display: flex;
  flex-direction: row;
  justify-content: center;

  .btn {
    cursor: pointer;
  }
}

.catalog {
  display: grid;

  &__logout {
    cursor: pointer;
  }

  &__link-to {
    top: 10px;
    padding: $padding;
    border: solid 1px #aeaeae;
  }
}
</style>