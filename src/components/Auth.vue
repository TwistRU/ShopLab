<template>
  <div class="Auth">
    <div class="router-linki">
      <router-link :to="{name: 'catalog'}">
        <div class="router-linki__link-to">
          Вернуться к каталогу
        </div>
      </router-link>
      <router-link :to="{name: 'cart'}">
        <div class="router-linki__link-to">
          Корзина
        </div>
      </router-link>
    </div>
    <div class="Auth__inputs">
      <input type="text" v-model="login">
      <input type="password" v-model="password">
      <button @click="AUTHORIZE_USER">Авторизация</button>
    </div>
  </div>
</template>

<script>

import axios from "axios";
import {host} from "@/main";
import {mapActions} from 'vuex'

export default {
  name: "Auth",
  data() {
    return {
      login: '',
      password: ''
    }
  },
  methods: {
    ...mapActions([
        'SET_AUTHORIZATION',
    ]),
    AUTHORIZE_USER() {
      return axios({
        method: 'POST',
        url: host + '/auth/login',
        data: {
          login: this.login,
          password: this.password,
        }
      }).then((response) => {
        this.SET_AUTHORIZATION(response);
        this.login = '';
        this.password = '';
        this.$router.push({name:'catalog'});
        return response
      }).catch((response) => {
        console.log(response.error)
      })
    },
  }
}
</script>

<style scoped lang="scss">
.Auth {
  display: flex;
  flex-direction: column;
  max-width: 50vw;
  min-height: 50vw;

  &__inputs {
    padding-top: 10vw;
    display: flex;
    flex-direction: column;
  }
}
</style>