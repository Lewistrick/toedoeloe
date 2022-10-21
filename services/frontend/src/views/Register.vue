<template>
    <section>
        <h2>Nieuwe gebruiker</h2>
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
                <button type="submit" class="btn btn-success">Aanmelden</button>
            </div>
        </form>
    </section>
</template>

<script>
import { mapActions } from 'vuex';
export default {
    name: 'Register',
    data() {
        return {
            form: {
                username: '',
                password: ''
            }
        }
    },
    methods: {
        ...mapActions(['register']),
        async submit() {
            await this.register(this.form); // also calls logIn to set the token
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
