import Vuex from "vuex";
import api from "@/axios";
import createPersistedState from "vuex-persistedstate";

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    files: {},
    isAuth: false,
  },
  mutations: {
    setFiles(state, files) {
      state.files = [...files];
    },
    hasAuth(state, val) {
      state.isAuth = !!val;
    },
  },
  actions: {
    login({ commit }, { username, password }) {
      return api
        .post("/token/", { username, password })
        .then((response) => {
          const token = response.data.access;
          localStorage.setItem("token", token);
        })
        .then(() => commit("hasAuth", true));
    },
    logout({ commit }) {
      return api
        .post("/logout")
        .then(() => localStorage.removeItem("token"))
        .then(() => commit("hasAuth", false))
        .then(this.$router.push("/login"))
        .catch(console.error);
    },
    getFiles({ commit }) {
      return api.get("/files.json").then((res) => {
        commit("setFiles", res.data);
        console.log(res);
      });
    },
  },
});
