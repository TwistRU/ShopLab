import Vue from "vue";
import VueRouter from "vue-router"
import Catalog from "@/components/Catalog";
import Cart from "@/components/Cart";
import Auth from "@/components/Auth";
import Registration from "@/components/Registration";

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
        {
            path: '/reg',
            name: 'registration',
            component: Registration,
        },
    ]
})

export default router;