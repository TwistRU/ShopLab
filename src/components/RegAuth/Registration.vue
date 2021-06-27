<template>
  <div class="Reg">
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
    <div class="Reg__inputs">
      <p>First name</p>
      <input type="text" v-model="first_name">
      <p>Second name</p>
      <input type="text" v-model="second_name">
      <p>Email</p>
      <input type="email" v-model="email">
      <p>Login</p>
      <input type="text" v-model="login">
      <p>Password</p>
      <input type="password" v-model="password">
      <button @click="registerUser">Регистрация</button>
      <p>Уже есть аккаунт?
        <router-link :to="{name: 'auth'}">Авторизация</router-link>
      </p>
    </div>
  </div>
</template>

<script>

import axios from "axios";
import {host} from "@/main";

export default {
  name: "Registration",
  data() {
    return {
      email: '',
      login: '',
      password: '',
      first_name: '',
      second_name: '',
    }
  },
  methods: {
    registerUser() {
      axios({
        method: 'POST',
        url: host + '/auth/registration',
        data: {
          first_name: this.first_name,
          second_name: this.second_name,
          email: this.email,
          login: this.login,
          password: this.password,
        }
      }).then((response) => {
        this.$router.push({name: 'auth'});
        return response;
      })

    },
  }
}
</script>

<style scoped lang="scss">
.Reg {
  @include some_func()
}
</style>