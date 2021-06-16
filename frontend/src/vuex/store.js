import Vue from "vue";
import Vuex from 'vuex';
import axios from "axios";

Vue.use(Vuex);

let store = new Vuex.Store({
    state: {
        products: [],
        update_time: 0
    },
    mutations: {
        SET_PRODUCTS_TO_STATE: (state, products) => {
            state.products = products.products;
            state.update_time = products.time;
        }
    },
    actions: {
        GET_PRODUCTS_FROM_API({commit}) {
            return axios('http://localhost:3000/data', {
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
        }
    },
    getters: {
        PRODUCTS(state) {
            return state.products;
        }
    }
});

export default store;