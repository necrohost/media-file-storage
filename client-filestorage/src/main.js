import { createApp } from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

import store from "@/store";
import './assets/main.css'


const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')