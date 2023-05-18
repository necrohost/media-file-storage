import { defineStore, acceptHMRUpdate } from "pinia";
import api from "@/axios";
export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    isAuth: false,
  }),
  persist: true,
  actions: {
    async register(email, username, password) {
      return await api
        .post("auth/register/", { email, username, password })
        .then((response) => {
          console.log(response.data);
        });
    },
    async login(username, password) {
      return await api
        .post("auth/login/", { username, password })
        .then((response) => {
          const token = response.data.access;
          localStorage.setItem("access_token", token);
          this.$patch((state) => (state.isAuth = true));
        });
    },
    logout() {
      localStorage.removeItem("access_token");
      this.$patch((state) => (state.isAuth = false));
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot));
}
