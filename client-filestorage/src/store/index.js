import Vue from 'vue'
import Vuex from 'vuex'
import axios from "@/axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userFiles: [],
    hasOpenSession: false,
  },
  mutations: {
    setUserFiles(state, files) {
      state.userFiles = [...files]
    },
    setHasOpenSession(state, val) {
      state.hasOpenSession = !!val
    }
  },
  actions: {
    login({commit}, {username, password}) {
      return axios
        .post("/login", {username, password})
        .then(() => commit("setHasOpenSession", true))
    },
    logout({commit}) {
      return axios.post('/logout')
        .then(() => commit('setHasOpenSession', false))
        .then(deleteAllCookies)
        .catch(console.error)
    },
    getUserFiles({commit}) {
      return axios.get('/files')
        .then(res => {
          commit('setUserFiles', res.data)
          console.log(res)
        });
    }
  }
})

function deleteAllCookies() {
//   var cookies = document.cookie.split(";");

//   for (var i = 0; i < cookies.length; i++) {
//       var cookie = cookies[i];
//       var eqPos = cookie.indexOf("=");
//       var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
//       document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
//   }
}
