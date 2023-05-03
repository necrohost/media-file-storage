<template class="container">
  <div
    class="row align-items-center justify-content-center"
    style="height: 100vh"
  >
    <div class="col-sm-5 col-md-5 col-lg-5">
      <form @submit.prevent="submit">
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
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="check" />
          <label class="form-check-label" for="check">Remember pass?</label>
        </div>
        <button type="submit" class="btn btn-success">
          <i class="fa-solid fa-right-to-bracket"></i> Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
// import api from '@/axios';
import { mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["login"]),
    submit() {
      this.login({ username: this.username, password: this.password })
        .then(() => this.$router.push("/files"))
        .catch((e) => {
          this.$notify({
            type: "error",
            title: "Error logging in",
            text: e.response.status === 401 ? "Wrong credentials" : null,
          });
        });
    },
  },
};
</script>
<style scoped></style>
