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
      <p>Login</p>
      <input type="text" v-model="login">
      <p>Password</p>
      <input type="password" v-model="password">
      <button @click="AUTHORIZE_USER">Авторизация</button>
      <p>Нет аккаунта? <router-link :to="{name: 'registration'}">Регистрация</router-link></p>
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
        this.$router.push({name: 'catalog'});
        return response
      }).catch((response) => {
        console.log(response.error)
      })
    },
  }
}
</script>

<style scoped lang="scss">
.Auth{
  @include some_func()
}
</style>