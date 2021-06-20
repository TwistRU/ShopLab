import Vue from "vue";
import Vuex from 'vuex';
import axios from "axios";

Vue.use(Vuex);

let store = new Vuex.Store({
    state: {
        // products
        products: [],
        update_time: 0,

        // cart
        cart: [],
    },
    mutations: {
        // products
        SET_PRODUCTS_TO_STATE: (state, products) => {
            state.products = products.products;
            state.update_time = products.time;
        },

        // cart
        ADD_TO_CART: (state, product) => {
            state.cart.push(product);
        },
    },
    actions: {
        // products
        GET_PRODUCTS_FROM_API({commit}) {
            return axios('http://192.168.1.43:3000/data', {
                method: "get"
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