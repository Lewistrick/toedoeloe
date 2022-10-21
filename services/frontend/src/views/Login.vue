<template>
    <section>
        <h2>Inloggen</h2>
        <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="username" class="form-label">Gebruikersnaam:</label>
                <input type="text" name="username" v-model="form.username" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Wachtwoord:</label>
                <input type="password" name="password" v-model="form.password" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <button type="submit" class="btn btn-success">Inloggen</button>
            </div>
        </form>
    </section>
</template>

<script>
import { mapActions } from 'vuex';
export default {
    name: 'Login',
    data() {
        return {
            form: {
                username: '',
                password: ''
            }
        }
    },
    methods: {
        ...mapActions(['logIn']),
        async submit() {
            const User = new FormData();
            User.append('username', this.form.username);
            User.append('password', this.form.password);
            await this.logIn(User);
            this.$router.push('/dashboard');
        }
    },
    beforeCreate() {
        if (this.$store.getters.isLoggedIn) {
            this.$router.push('/dashboard');
        }
    }
}
</script>
