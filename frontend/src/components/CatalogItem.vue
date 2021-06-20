<template>
  <div class="catalog-product">
    <div class="catalog-product-image">
      <img :src="imgUrl" :alt="product_data['image']"/>  <!-- TODO delete -->
      <!--      <img :src="product_data.image" alt="img"/>-->  <!-- TODO uncomment -->
    </div>
    <div class="catalog-product__name">
      <p class="name">{{ nameAndInfoForDisplay }}</p>
    </div>
    <div class="catalog-product__stats">
      <p>{{ product_data['rating'] }} звёзд</p>
    </div>
    <div class="product-buy">
      <div class="product-buy__price">
        <p>{{ product_data['price'] }}₽</p>
      </div>
      <button class="wish-list-btn">
        ♥
      </button>
      <button
          v-if="!product_data['available']"
          class="buy-btn"
          disabled
      >
        Нет в наличии
      </button>
      <button
          v-else-if="this.CART().indexOf(product_data) === -1"
          class="buy-btn"
          @click="addToCart"
      >
        Купить
      </button>
      <button
          v-else
          class="buy-btn"
      >
        В корзине
      </button>
    </div>
    <div class="catalog-product__avails">
      <p>В наличии: {{ product_data['available'] }} штук</p>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Item",
  props: {
    product_data: {
      type: Object,
      required: true,
      default() {
        return {}
      },
    },
  },
  computed: {  // TODO delete
    imgUrl: function () {
      return "http://www.placehold.it/200x200?text=" + this.product_data['image'].toString();
    },
    nameAndInfoForDisplay: function () {
      let tempString = this.product_data['name'];
      if (this.product_data['more_info'])
        tempString += ' [' + this.product_data['more_info'] + ']';
      return tempString;
    }
  },
  methods: {
    ...mapActions([
      "ADD_TO_CART",
    ]),
    ...mapGetters([
      "CART",
    ]),
    addToCart() {
      this.ADD_TO_CART(this.product_data);
    },
  },
}
</script>

<style scoped lang="scss">
.catalog-product {
  display: grid;
  width: 100%;
  box-shadow: 0 0 1px 0;
  border-radius: $radius;
  padding: $padding * 2;
  margin-bottom: $margin * 2;
  grid-template-columns: 0.8fr 3fr 0.7fr;
  background-color: #FFF;
}

.catalog-product-image {
  @include grid-element-pos(1, 1, 1, 4);
  max-width: 150px;
  max-height: 150px;

  img {
    object-fit: scale-down;
    width: 100%;
    height: 100%;
  }
}

.catalog-product__name {
  @include grid-element-pos(2, 3, 1, 2);
  margin: 0 0 0 2%;
}

.catalog-product__stats {
  @include grid-element-pos(2, 3, 2, 3);
  margin: 0 0 0 2%;
}

.product-buy {
  @include grid-element-pos(3, 4, 1, 4);
  display: grid;
}

.product-buy__price {
  @include grid-element-pos(2, 3, 1, 2);
  display: flex;
}

.wish-list-btn {
  @include grid-element-pos(1, 2, 2, 3);
  width: 60%;
  height: 50%;
  margin: 0 2px auto auto;

}

.buy-btn {
  @include grid-element-pos(2, 3, 2, 3);
  width: 100%;
  height: 50%;
  margin: 0 auto auto 2px;
}

.catalog-product__avails {
  @include grid-element-pos(2, 3, 3, 4);
  margin: 0 0 0 2%;
}

</style>