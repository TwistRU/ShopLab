import Vue from 'vue';
import App from './App.vue';
import store from "@/vuex/store";
import './assets/styles/styles.scss';
import router from "@/router/router";

Vue.config.productionTip = false;
// const host = "https://fefu-shop-lab.herokuapp.com/"
const host = "http://436d5f4ce04f.ngrok.io"
export {host}

new Vue({
    render: h => h(App),
    store,
    router,
}).$mount('#app');
