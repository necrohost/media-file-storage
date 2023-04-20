<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="submit">
      <label htmlFor="username">Username</label>
      <input type="text" name="username" v-model="username" required />
      <label htmlFor="password">Password</label>
      <input type="password" name="password" v-model="password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
// import api from '@/axios';
import { mapActions } from "vuex";

export default {
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
      // api.post('/token/', {
      //     username: this.username,
      //     password: this.password
      // })
      //     .then(response => {
      //         const token = response.data.access;
      //         // Store the token securely
      //         localStorage.setItem('token', token);
      //
      //         // Redirect to the home page or some other protected page
      //         this.$router.push('/');
      //     })
      //     .catch(error => {
      //         // Handle authentication errors
      //         console.error(error);
      //     });
    },
  },
};
</script>
