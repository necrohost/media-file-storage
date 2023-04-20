import {createRouter, createWebHistory} from 'vue-router'

import HomeView from '../views/HomeView.vue'
import Files from '../views/Files.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Uploader from "@/components/navbar/UploadButton.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'navigator',
            component: HomeView
        },
        {
            path: '/upload',
            name: 'upload',
            component: Uploader
        },
        {
            path: '/files',
            name: 'files',
            component: Files
        },
        {
            path: '/register',
            name: 'register',
            component: Register
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
    ]
})

export default router
