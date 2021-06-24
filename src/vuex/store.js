import Vue from "vue";
import Vuex from 'vuex';
import axios from "axios";

Vue.use(Vuex);

let host = "https://fefu-shop-lab.herokuapp.com/"
// let host = 'http://192.168.1.43:5000/'

let store = new Vuex.Store({
    state: {
        // products
        products: [],

        // cart
        cart: [],
    },
    mutations: {
        // products
        SET_PRODUCTS_TO_STATE: (state, products) => {
            state.products = products.products;
        },

        // cart
        ADD_TO_CART: (state, product) => {
            state.cart.push(product);
        },
        DELETE_FROM_CART: (state, index) => {
            state.cart.splice(index, 1);  // удалить 1 элемент начиная с индекса index
        },
    },
    actions: {
        // products
        GET_PRODUCTS_FROM_API({commit}) {
            return axios({
                method: "get_list",
                url: host.toString() + '/api/v1/item',
                params: {
                    page: 1,
                    page_limit: 50
                }
            })
                .then((products) => {
                    commit('SET_PRODUCTS_TO_STATE', products.data);
                    return products;
                })
                .catch((error) => {
                    console.log(error);
                    return error;
                })
        },

        // cart
        ADD_TO_CART({commit}, product) {
            commit('ADD_TO_CART', product);
        },
        DELETE_FROM_CART({commit}, index) {
            commit('DELETE_FROM_CART', index);
        },
    },
    getters: {
        // products
        PRODUCTS(state) {
            return state.products;
        },

        // cart
        CART(state) {
            return state.cart;
        },
    },
});

export default store;