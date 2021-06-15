<template>
  <div class="catalog-product">
    <div class="catalog-product-image">
      <img src="http://www.placehold.it/200x200" alt="img"/>
    </div>
    <div class="catalog-product-name">
      <p class="name">item_name</p>
    </div>
    <div class="catalog-product-stats">
      <p>5 звёзд</p>
    </div>
    <div class="product-buy">
      <div class="product-buy-price">
        <p>100</p>
        <p>₽</p>
      </div>
      <button class="wish-list-btn">
        ♥
      </button>
      <button class="buy-btn">
        Купить
      </button>
    </div>
    <div class="catalog-product-avails">
      <p>В наличии:</p>
      <p>10</p>
      <p>штук</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Item"
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

.catalog-product-name {
  @include grid-element-pos(2, 3, 1, 2);
  margin: 0 0 0 1%;
}

.catalog-product-stats {
  @include grid-element-pos(2, 3, 2, 3);
  margin: 0 0 0 1%;
}

.product-buy {
  @include grid-element-pos(3, 4, 1, 4);
  display: grid;
  //grid-column: 6;
  //grid-row: 3;
}

.product-buy-price {
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

.catalog-product-avails {
  @include grid-element-pos(2, 3, 3, 4);
  margin: 0 0 0 1%;
  display: flex;
}

</style>