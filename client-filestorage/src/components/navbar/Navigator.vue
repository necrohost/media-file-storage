<template>
  <div class="navigator" id="navbar" :style="{ width: sidebarWidth }">
    <h1>
      <i class="fa fa-cloud"></i>
    </h1>
    <UploadButton />
    <NavLink to="/cloud" icon="fas fa-box-archive">Files</NavLink>
    <NavLink to="/shared-files" icon="fas fa-share-nodes">Shared</NavLink>
    <NavLink to="/trash" icon="fas fa-trash" class="trash">Trash</NavLink>
    <LogoutButton />
    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleNav"
    >
      <i class="fas fa-angle-double-left"></i>
    </span>
  </div>
</template>
<script>
import UploadButton from "./UploadButton.vue";
import NavLink from "./NavLink.vue";
import { collapsed, toggleNav, sidebarWidth } from "./state";
import LogoutButton from "@/components/LogoutButton.vue";

export default {
  data() {
    return {};
  },
  props: {},
  components: {
    NavLink,
    UploadButton,
    LogoutButton,
  },
  setup() {
    return {
      collapsed,
      toggleNav,
      sidebarWidth,
    };
  },
  created() {
    window.addEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      if (window.pageYOffset > 0) {
        document.getElementById("navbar").style.top = "0";

        document.getElementById("navbar").style.bottom = "70px";
        document.getElementById("navbar").style.borderRadius = "0 0 0 5px";
      } else {
        document.getElementById("navbar").style.top = "70px";

        document.getElementById("navbar").style.bottom = "0";
        document.getElementById("navbar").style.borderRadius = "5px 0 0 0";
      }
    },
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  unmounted() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>
<style>
:root {
  --sidebar-bg-color: black;
  --sidebar-item-active: #ffffff;
  --sidebar-item-hover: #808080;
  --sidebar-text-color: #ffffff;
  --sidebar-text-color-active: #000;
  --accent-header-color: red;
    --accent-files-color: black;
}

button,
input[type="submit"],
input[type="reset"] {
  background: none;
  border: none;
  font: inherit;
  cursor: pointer;
  outline: inherit;
}
</style>
<style scoped>
h1 {
  text-align: center;
  margin-bottom: 20px;
}

.fa-cloud {
  font-size: 50px;
  width: 100%;
}

.navigator {
  color: var(--sidebar-text-color);
  background-color: var(--sidebar-bg-color);
  position: fixed;
  z-index: 1;
  top: 70px;
  bottom: 0;
  padding: 1em;
  transition: 60ms;
  display: flex;
  flex-direction: column;
  border-radius: 5px 0 0 5px;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.5em;
  color: rgba(255, 255, 255, 0.7);
  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
</style>
