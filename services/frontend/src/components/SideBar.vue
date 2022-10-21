<template>
    <nav id="sidebarMenu" class="col-md-3 sidebar">
        <div class="sidebar-sticky">
            <h1>Toedoeloe v3</h1>

            <hr />

            <router-link to="/">
                <div class="nav-link">Start</div>
            </router-link>

            <div v-if="isLoggedIn" class="nav flex-column">
                <router-link to="/todos"><div class="nav-link">Toedoes</div></router-link>
                <router-link to="/profile"><div class="nav-link">Profiel</div></router-link>
                <div class="nav-link" @click="logout">Uitloggen</div>
            </div>

            <div v-else class="nav flex-column">
                <router-link to="/login"><div class="nav-link">Inloggen</div></router-link>
                <router-link to="/register"><div class="nav-link">Aanmelden</div></router-link>
            </div>

        </div>
    </nav>
</template>

<script>
export default {
    name: 'SideBar',
    computed: {
        isLoggedIn() {
            return this.$store.getters.isLoggedIn;
        }
    },
    methods: {
        logout() {
            this.$store.dispatch('logOut');
            this.$router.push('/');
        }
    }
}
</script>

<style scoped>
.sidebar {
    padding-left: 2em;
    padding-top: 2em;
}

.nav-link {
    color: #ccc;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #579;
    text-align: center;
    margin: 1em 0;
}

.nav-link:hover {
    color: #024;
    background-color: #68a;
}

a:hover {
    text-decoration: none;
}

</style>