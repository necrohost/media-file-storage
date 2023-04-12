<template>
    <h1>Register</h1>
    <form @submit.prevent="register" class="register-child">
        <input type="email" placeholder="Email address..." v-model="email"/>
        <input type="password" placeholder="Password..." v-model="password"/>
        <button type="submit">register</button>
    </form>
</template>

<script>
export default {
    name: "Register",
    data: () => {
        return {
            email: '',
            password: '',
        };
    },
    methods: {
        register() {

        }
    },
}
</script>

<style scoped>
    .register-child {
        width: 200px;
        text-align: center;
    }
    .register-child input {
        margin-bottom: 30px;
        padding: 7px;
        border: 1px dashed black;
    }
    .register-child button {
        border: none;
        padding: 7px 27px;
        background-color: #2c3e50;
        color: #f8f8f8;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 14px;

    }
    .register-child button:hover {
        background: #455a64;
    }
</style>