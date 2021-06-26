import Vue from "vue";
import VueRouter from "vue-router"
import Catalog from "@/components/Catalog";
import Cart from "@/components/Cart";
import Auth from "@/components/Auth";

Vue.use(VueRouter);

let router = new VueRouter({
    routes: [
        {
            path: '/',
            name: 'catalog',
            component: Catalog,
        },
        {
            path: '/cart',
            name: 'cart',
            component: Cart,
        },
        {
            path: '/auth',
            name: 'auth',
            component: Auth,
        },
    ]
})

export default router;