<template>
    <section>
        <h2>Gebruikersprofiel</h2>
        <p>Hallo, {{ user }}!</p>
        <button class="btn btn-danger" @click="deleteProfile">Verwijder mijn account</button>
    </section>
</template>


<script>
import { mapActions, mapGetters } from 'vuex';
export default {
    name: 'Profile',
    computed: {
        ...mapGetters({ user: 'stateUser' }),
    },
    methods: {
        ...mapActions(['deleteUser']),
        async deleteProfile() {
            try {
                await this.deleteUser();
                await this.$store.dispatch('logOut');
                this.$router.push('/');
            } catch (error) {
                console.log(error);
            }
        }
    }
}
</script>