import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import Files from "../views/Files.vue";
import Login from "../views/auth/Login.vue";
import Register from "../views/auth/Register.vue";
import Uploader from "@/components/navbar/UploadButton.vue";
import store from "@/store";

/**
 * @property {boolean} requiresAuth
 * @property {array} routes
 *
 */
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Files,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/upload",
      name: "upload",
      component: Uploader,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/cloud",
      name: "files",
      component: Files,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/shared-files",
      name: "shared-files",
      component: Files,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/register",
      name: "register",
      component: Register,
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: "/login",
      name: "login",
      component: Login,
      meta: {
        requiresAuth: false,
      },
    },
  ],
});
router.beforeEach((to, from, next) => {
  if (to.matched.some((route) => route.meta.requiresAuth)) {
    if (!store.state.isAuth) {
      next("/login");
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
