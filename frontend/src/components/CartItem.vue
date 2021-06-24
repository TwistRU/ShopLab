<template>
  <div class="cart-item__wrapper">
    <div class="cart-item__product-image">
      <img :src="imgUrl" alt="img"/>
    </div>
    <div class="cart-item__product_info">
      <div class="cart-item__name">
        <p>{{ item['name'] }}</p>
      </div>
      <button
          class="cart-item__delete_btn"
          @click="$emit('deleteFromCart')"
      >
        Удалить
      </button>
    </div>

    <div class="cart-item__amount">
      <div class="cart-item__product-count-buttons">
        <div class="count-buttons">
          <button class="minus-btn">
            -
          </button>
          <input
              v-model="item['count']"
              type="number"
              min="1"
              :max="item['available']"
          >
          <button class="plus-btn">
            +
          </button>
        </div>
        <div
            class="cart-item__item-price"
            v-if="item['count'] !== '1'"
        >
          <p>{{ item['price'] }} ₽/шт</p>
        </div>
      </div>
      <div class="cart_item__product-price">
        <div class="price">
          <p>{{ totalItemPrice }}₽</p>
        </div>
        <div class="cart_item__available">
          <p>В наличии: {{ item['available'] }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    item: {
      type: Object,
      required: true,
    }
  },
  computed: {  // TODO delete
    imgUrl: function () {
      return "http://www.placehold.it/200x200?text=" + this.item['image'].toString();
    },
    totalItemPrice: function () {
      return this.item['price'] * Number(this.item['count']);
    },
  },
  mounted() {
    this.$set(this.item, 'count', '1')
  },
}
</script>

<style lang="scss" scoped>
.cart-item__wrapper {
  display: grid;
  grid-template-columns: 0.5fr 1fr 0.75fr;

  box-shadow: 0 0 1px 0;
  border-radius: $radius;
  padding: $padding * 2;
  margin-bottom: $margin * 2;
  background-color: #FFF;
}

//.cart-item__product-thumbnail {
//  display: flex;
//  flex-direction: row;
//  padding: 0 10px;
//  margin: auto 0;
//}

.cart-item__product-image {
  max-width: 130px;
  max-height: 130px;
  margin: auto;

  img {
    object-fit: scale-down;
    width: 100%;
    height: 100%;
  }
}

.cart-item__product_info {
  margin-left: 18px;
  display: grid;
  grid-template-rows: 1.2fr 1fr;
}

.catalog-product__name {
  min-width: 14vw;
}

.cart-item__delete_btn {
  margin-top: 10px;
  max-height: 20px;
  max-width: 100px;
}

.cart-item__amount {
  display: flex;
  justify-content: flex-end;
  margin-top: 17px;
}

.cart-item__product-count-buttons {
  margin: 0 auto;
  padding-left: 5px;
}

.count-buttons {

  .minus-btn {
    width: 2vw;
  }

  input {
    width: 2vw;
  }

  .plus-btn {
    width: 2vw
  }
}

.cart-item__item-price {
}

.cart_item__product-price {
  margin-top: 0;
  display: grid;
  grid-template-rows: 1.2fr 1fr;
}

.price {
  text-align: right;
  padding-right: 5px;
  font-size: 22px;

  p {
    margin-block: 0;
  }
}

.cart_item__available {

}

</style>