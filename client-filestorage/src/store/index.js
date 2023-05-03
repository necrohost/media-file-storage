import Vuex, { useStore } from "vuex";
import { createStore } from "vuex-extensions";
import api from "@/axios";
import createPersistedState from "vuex-persistedstate";

export default createStore(Vuex.Store, {
  plugins: [createPersistedState()],
  state: {
    files: {},
    isAuth: false,
  },
  mutations: {
    SET_FILES(state, files) {
      state.files = [...files];
    },
    HAS_AUTH(state, val) {
      state.isAuth = !!val;
    },
    DELETE_FILE(state, id) {
      const index = state.files.findIndex((file) => file.id === id);
      state.files.splice(index, 1);
    },
  },
  actions: {
    register({ commit }, { email, username, password }) {
      return api.
        post("/register/", { email, username, password}).
        then((response) => {
          console.log(response.data)
      })
    },
    login({ commit }, { username, password }) {
      return api
        .post("/login/", { username, password })
        .then((response) => {
          const token = response.data.access;
          localStorage.setItem("token", token);
        })
        .then(() => commit("HAS_AUTH", true));
    },
    logout({ commit }) {
      {
        localStorage.removeItem("token");
        commit("HAS_AUTH", false);
        commit("SET_FILES", []);
      }
    },
    getSharedFiles({ commit }) {
      return api.get("/files/shared/").then((res) => {
        commit("SET_FILES", res.data);
        console.log(res);
      });
    },
    getFiles({ commit }) {
      return api.get("/files.json").then((res) => {
        commit("SET_FILES", res.data);
        console.log(res);
      });
    },
    deleteFileById({ commit }, file_id) {
      return api.delete("/files/" + file_id + "/").then((res) => {
        commit("DELETE_FILE", file_id);
        return true;
      });
    },
  },
});
