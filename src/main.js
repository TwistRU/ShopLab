import Vue from 'vue';
import App from './App.vue';
import store from "@/vuex/store";
import './assets/styles/styles.scss';
import router from "@/router/router";

Vue.config.productionTip = false;
const host = "https://shop-lab-fefu.herokuapp.com"
// const host = "http://7efd469e4910.ngrok.io/"
export {host}

new Vue({
    render: h => h(App),
    store,
    router,
}).$mount('#app');
