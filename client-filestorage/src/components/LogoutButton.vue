<template>
  <div class="logout-container">
    <a @click="submitLogout" class="logout">
      <i class="fa-solid fa-right-from-bracket"></i>
      <span v-if="!collapsed">Logout</span>
    </a>
  </div>
</template>
<script>
import { collapsed } from "@/components/navbar/state";
import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const user = useUserStore();
    return { user };
  },
  data() {
    return {
      collapsed,
    };
  },
  methods: {
    submitLogout() {
      this.user.logout();
      this.$router.push("/login");
    },
  },
};
</script>
<style scoped>
.logout-container {
  width: 100%;
  margin-bottom: 20px;
}

.logout-container span {
  margin-left: 5px;
}

.logout-container a {
  margin-top: 20px;
  display: inline-block;
  cursor: pointer;
  border: 1px solid white;
  color: white;
  text-align: center;
  width: 97%;
  padding: 6px;
  text-transform: uppercase;
}

.logout-container a:hover {
  color: black;
  background-color: white;
  border-radius: 3px;
  transition: 0.2s ease;
  box-shadow: 0 0 1px 0 white inset, 0 0 1px 0 white;
}
</style>
