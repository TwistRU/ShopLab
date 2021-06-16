<template>
  <div class="catalog-product">
    <div class="catalog-product-image">
      <img :src="imgUrl" :alt="product_data.image"/>  <!-- TODO delete -->
<!--      <img :src="product_data.image" alt="img"/>-->  <!-- TODO uncomment -->
    </div>
    <div class="catalog-product__name">
      <p class="name">{{ product_data.name }}</p>
    </div>
    <div class="catalog-product__stats">
      <p>{{ product_data.rating }} звёзд</p>
    </div>
    <div class="product-buy">
      <div class="product-buy__price">
        <p>{{ product_data.price }}₽</p>
      </div>
      <button class="wish-list-btn">
        ♥
      </button>
      <button class="buy-btn">
        Купить
      </button>
    </div>
    <div class="catalog-product__avails">
      <p>В наличии: {{ product_data.available }} штук</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Item",
  props: {
    product_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  computed: {  // TODO delete
    imgUrl: function() {
      return "http://www.placehold.it/200x200?text=" + this.product_data.image.toString();
    }
  }
}
</script>

<style scoped lang="scss">
.catalog-product {
  display: grid;
  width: 100%;
  box-shadow: 0 0 8px 0;
  border-radius: $radius;
  padding: $padding * 2;
  margin-bottom: $margin * 2;
  grid-template-columns: 0.8fr 3fr 0.8fr;
}

.catalog-product-image {
  @include grid-element-pos(1, 1, 1, 4);
  width: 100%;
  height: 100%;

  img {
    width: 100%;
    height: 100%;
    border-radius: $radius;
  }
}

.catalog-product__name {
  @include grid-element-pos(2, 3, 1, 2);
  margin: 0 0 0 1%;
}

.catalog-product__stats {
  @include grid-element-pos(2, 3, 2, 3);
  margin: 0 0 0 1%;
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
  margin: 0 0 0 1%;
}

</style>