<template>
  <div class="app-container">
    <Header />
    <Navigator />
    <div :style="{ 'margin-left': sidebarWidth }">
      <RouterView />
    </div>
  </div>
</template>
<script>
import "@fortawesome/fontawesome-free/js/all";
import { sidebarWidth } from "./components/navbar/state";
import Navigator from "@/components/navbar/Navigator.vue";
import Header from "@/components/Header.vue";

export default {
  components: { Header, Navigator },
  data() {},
  mounted() {},
  methods: {},
  setup() {
    return { sidebarWidth };
  },
};
</script>
<style scoped>
.app-container {
    margin: 0 20px;

}
</style>
