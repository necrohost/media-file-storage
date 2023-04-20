<template>
    <div class="navigator" :style="{ width: sidebarWidth }">
        <h1>
            <span v-if="collapsed">
                <i class="fas fa-cloud"></i>
            </span>
            <span v-else>C L O U D</span>
        </h1>
        <UploadButton/>
        <NavLink to="/files" icon="fas fa-box-archive">Files</NavLink>
        <NavLink to="/shared-files" icon="fas fa-share-nodes">Shared</NavLink>
        <NavLink to="/trash" icon="fas fa-trash" class="trash">Trash</NavLink>
        <div class="logout-con">
            <i class="fa-solid fa-right-from-bracket"></i>
            <button @click="logout" class="logout">Logout</button>
        </div>
        <span class="collapse-icon" :class="{ 'rotate-180': collapsed }" @click="toggleNav">
        <i class="fas fa-angle-double-left"></i>
    </span>
    </div>
</template>
<script>
import UploadButton from "./UploadButton.vue";
import NavLink from "./NavLink.vue";
import {collapsed, toggleNav, sidebarWidth} from "./state";
import { mapActions, mapState } from "vuex";

export default {
    data() {
        return {
            token: null
        };
    },
    props: {},
    components: {
        NavLink, UploadButton
    },
    setup() {
        return {
            collapsed,
            toggleNav,
            sidebarWidth,
        };
    },
    methods: {
        ...mapActions(["logout"]),
        logout() {
            // Clear the token from localStorage or any other secure storage mechanism
            localStorage.removeItem('token');
            // Redirect to the login page or some other public page
            this.$router.push('/login');
        }
    },
    mounted() {
        // Retrieve the token from localStorage or any other secure storage mechanism
        this.token = localStorage.getItem('token');
    },
};
</script>
<style>
:root {
    --sidebar-bg-color: #2c3e50;
    --sidebar-item-hover: #455a64;
    --sidebar-item-active: #455a64;
}
</style>
<style scoped>
h1 {
    text-align: center;
    margin-bottom: 20px;;
}

.fa-cloud {
    font-size: 17px;
}

.navigator {
    color: white;
    background-color: black;

    float: left;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 0.5em;

    transition: 0.3s ease;

    display: flex;
    flex-direction: column;
}

.collapse-icon {
    position: absolute;
    bottom: 0;
    padding: 0.75em;

    color: rgba(255, 255, 255, 0.7);

    transition: 0.2s linear;
}

.rotate-180 {
    transform: rotate(180deg);
    transition: 0.2s linear;
}

button,
input[type="submit"],
input[type="reset"] {
    background: none;
    border: none;
    padding: 0;
    font: inherit;
    cursor: pointer;
    outline: inherit;
}
.logout-con {
    position: absolute;
    bottom: 60px;
    display: inline-block;
    cursor: pointer;
    border: 1px solid white;
    border-radius: 5px;
    color: white;
    text-align: center;
    width: 90%;
    padding: 6px;
    font-size: 17px;

}

.logout {
    text-transform: uppercase;
    margin-left: 6px;
    color: white;
}
.logout-con:active {
    color: black;
    background-color: white;
}
</style>
