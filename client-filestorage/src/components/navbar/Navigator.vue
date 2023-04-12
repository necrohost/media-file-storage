<script>
import NavLink from "./NavLink.vue";
import {collapsed, toggleNav, sidebarWidth} from "./state";

export default {
    props: {},
    components: {
        NavLink,
    },
    setup() {
        return {
            collapsed,
            toggleNav,
            sidebarWidth,
        };
    },
    methods: {
        chooseFiles() {
            document.getElementById("fileUpload").click();
        },
    },
};
</script>
<template>
    <div class="navigator" :style="{ width: sidebarWidth }">
        <h1>
      <span v-if="collapsed">
        <i class="fas fa-cloud"></i>
      </span>
            <span v-else>c l o u d</span>
        </h1>

        <input id="fileUpload" type="file" hidden/>
        <button @click="chooseFiles" class="choose-file">upload</button>

        <NavLink to="/files" icon="fas fa-box-archive">Files</NavLink>
        <NavLink to="/shared-files" icon="fas fa-share-nodes">Shared</NavLink>
        <NavLink to="/trash" icon="fas fa-trash" class="trash">Trash</NavLink>

        <span
                class="collapse-icon"
                :class="{ 'rotate-180': collapsed }"
                @click="toggleNav"
        >
      <i class="fas fa-angle-double-left"></i>
    </span>
    </div>
</template>

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

.navigator {
    color: white;
    background-color: var(--sidebar-bg-color);

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

.choose-file {
    text-transform: uppercase;
    border: 1px solid rgba(255, 255, 255, 0.7);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    height: 40px;
    margin-bottom: 10px;
    font-size: 16px;
    letter-spacing: 1px;
    width: 100%;
}

.choose-file:hover {
    background-color: #455a64;
}
</style>
