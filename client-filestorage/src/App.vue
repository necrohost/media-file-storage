<script>
import {RouterLink, RouterView} from 'vue-router'
import Navigator from './components/navbar/Navigator.vue'
import {sidebarWidth} from './components/navbar/state'
import '@fortawesome/fontawesome-free/js/all'
import Header from "@/views/Header.vue";

export default {
    data() {
        return {
            isAuth: true,
        }
    },
    components: {Header, Navigator},
    setup() {
        return {sidebarWidth}
    }
}
</script>

<template>

    <Navigator v-if="isAuth"/>
    <router-link to="register">Reg</router-link>
    <div :style="{ 'margin-left': sidebarWidth }">
        <RouterView/>
    </div>
</template>

<style scoped>
</style>
