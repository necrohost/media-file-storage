<template class="container">
  <div
    class="row align-items-center justify-content-center"
    style="height: 100vh"
  >
    <div class="col-sm-5 col-md-5 col-lg-5">
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input
            type="email"
            class="form-control"
            name="email"
            v-model="email"
            required
          />
        </div>
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input
            type="text"
            class="form-control"
            name="username"
            v-model="username"
            required
          />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            class="form-control"
            name="password"
            v-model="password"
            required
          />
        </div>
        <button type="submit" class="btn btn-success">
          <i class="fa-solid fa-user-plus"></i> Register
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";

export default {
  name: "Register",
  setup() {
    const user = useUserStore();
    return { user };
  },
  data() {
    return {
      email: "",
      username: "",
      password: "",
    };
  },
  methods: {
    submit() {
      this.user
        .register(this.email, this.username, this.password)
        .then(() => this.$router.push("/login"));
    },
  },
};
</script>
