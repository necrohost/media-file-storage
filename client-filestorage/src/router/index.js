import { createRouter, createWebHistory } from "vue-router";

import Files from "../views/Files.vue";
import Login from "../views/auth/Login.vue";
import Register from "../views/auth/Register.vue";
import { useUserStore } from "@/stores/user";

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
      path: "/trash",
      name: "trash",
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
router.beforeEach((to, from) => {
  const user = useUserStore();
  console.log(user.isAuth);
  if (to.meta.requiresAuth && !user.isAuth)
    return {
      path: "/login",
      query: { redirect: to.fullPath },
    };
});

export default router;
