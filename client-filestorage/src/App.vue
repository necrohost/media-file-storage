<template>
  <div class="app-container">
    <div>
      <Navigator />
    </div>
    <div :style="{ 'margin-left': sidebarWidth }">
      <RouterView />
    </div>
  </div>
</template>
<script>
import "@fortawesome/fontawesome-free/js/all";
import { sidebarWidth } from "./components/navbar/state";
import Navigator from "@/components/navbar/Navigator.vue";

export default {
  components: { Navigator },
  data() {
    return {};
  },
  mounted() {},
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/login");
    },
  },
  setup() {
    return { sidebarWidth };
  },
};
</script>
<style scoped></style>
