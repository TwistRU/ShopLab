import Vue from "vue";
import Vuex from 'vuex';
import axios from "axios";

Vue.use(Vuex);

import {host} from '@/main'

let store = new Vuex.Store({
    state: {
        // products
        products: [],
        countOfAllItems: 100,
        currentPage: 1,
        pageLimit: 2,
        // user
        authorized: false,
        access_token: '',
        refresh_token: '',
        // cart
        cart: [],
    },
    mutations: {
        // products
        SET_PRODUCTS_TO_STATE: (state, products) => {
            state.products = products.products;
            // state.countOfAllItems = products.countOfAllItems;
        },
        //user
        SET_AUTHORIZED: (state, data) => {
            state.authorized = data['auth_state'];
            state.access_token = data['access_token'];
            state.refresh_token = data['refresh_token'];
        },
        LOGOUT: (state) => {
            state.authorized = false;
            state.refresh_token = '';
            state.access_token = '';
        },
        // catalog
        SET_CURRENT_PAGE: (state, page) => {
            state.currentPage = page;
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
        GET_PRODUCTS_FROM_API({commit, state}) {
            return axios({
                method: "get_list",
                url: host + '/api/v1/item',
                params: {
                    page: state.currentPage,
                    page_limit: state.pageLimit,
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
        // eslint-disable-next-line no-unused-vars
        BUY_PRODUCTS_FROM_API({commit}) {
            return axios({
                method: 'POST',
                url: host + '/api/v1/buy',
                Authorization: this.access_token,
                data: {
                    'items': this.CART.map((item) => {
                        item['quantity'] = item['count'];
                    }),
                }
            }).catch((response) => {
                console.log(response)
                return response
            })
        },
        // user
        SET_AUTHORIZATION({commit}, response) {
            commit('SET_AUTHORIZED', response)
        },
        LOGOUT({commit}) {
            commit('LOGOUT')
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
        // catalog
        CURRENT_PAGE(state){
            return {currentPage: state.currentPage, maxPage: Math.ceil(state.countOfAllItems/state.pageLimit)}
        },
        // products
        PRODUCTS(state) {
            return state.products;
        },
        // user
        IS_AUTHORIZED(state) {
            return state.authorized;
        },
        // cart
        CART(state) {
            return state.cart;
        },
    },
});

export default store;