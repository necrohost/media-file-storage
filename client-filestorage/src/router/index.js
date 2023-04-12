import {createRouter, createWebHistory} from 'vue-router'

import HomeView from '../views/HomeView.vue'
// import Upload from '../views/Upload.vue'
import Files from '../views/Files.vue'
import Navigator from '../components/navbar/Navigator.vue'
// import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'navigator',
            component: HomeView
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
    ]
})

export default router
