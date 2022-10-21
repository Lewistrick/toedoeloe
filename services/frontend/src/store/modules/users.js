import axios from 'axios';

const state = {
    user: null,
};

const getters = {
    isLoggedIn: state => !!state.user,
    stateUser: state => state.user,
};

const actions = {
    async register({ dispatch }, user) {
        await axios.post('register', user);

        // logging in is done using a form, we must create it first
        const usrform = new FormData();
        usrform.append('username', user.username);
        usrform.append('password', user.password);
        await dispatch('logIn', usrform);
    },
    async logIn({ commit }, user) {
        await axios.post('login', user);
        await commit('setUser', user.get('username'));
    },
    async logOut({ commit }) {
        let user = null;
        commit('logout', user);
    },
    async deleteUser() {
        console.log('deleting user:', state.user);
        await axios.delete("users/delete");
    }
};

const mutations = {
    setUser(state, username) {
        state.user = username;
    },
    logout(state, user) {
        state.user = user;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
