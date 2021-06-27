import Vue from "vue";
import VueRouter from "vue-router"
import Catalog from "@/components/Catalog/Catalog";
import Cart from "@/components/Cart/Cart";
import Auth from "@/components/RegAuth/Auth";
import Registration from "@/components/RegAuth/Registration";
import Purchase from "@/components/Purchase/Purchase";
import AdminAddItems from "@/components/Admin/AdminAddItems";

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
        {
            path: '/purchase',
            name: 'purchase',
            component: Purchase,
        },
        {
            path: '/admin',
            name: 'admin',
            component: AdminAddItems,
        }
    ]
})

export default router;