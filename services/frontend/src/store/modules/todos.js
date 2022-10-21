import axios from 'axios';

const state = {
    todos: [],
    currentTodo: null,
};

const getters = {
    stateTodos: state => state.todos,
    stateCurrentTodo: state => state.currentTodo,
};

const actions = {
    async getTodos({ commit }) {
        const response = await axios.get('todos/');
        commit('setTodos', response.data);
    },
    async getTodo({ commit }, id) {
        const response = await axios.get(`todos/${id}`);
        commit('setTodo', response.data);
    },
    async createTodo({ commit }, taskform) {
        const response = await axios.post('todos/', taskform);
        commit('addTodo', response.data);
    },
    async updateTodo({ commit }, task) {
        const response = await axios.put(`todos/${task.id}`, task.form);
        commit('setTodo', response.data);
    },
    async toggleTodoFinish({ commit }, id) {
        const response = await axios.put(`todos/${id}/toggle_finished`);
        commit('setTodo', response.data);
    },
    async deleteTodo({ commit }, id) {
        const response = await axios.delete(`todos/${id}`);
        commit('unsetTodo');
    }
};

const mutations = {
    setTodos: (state, todos) => (state.todos = todos),
    addTodo: (state, todo) => state.todos.push(todo),
    setTodo: (state, todo) => (state.currentTodo = todo),
    unsetTodo: (state) => (state.currentTodo = null),
};

export default {
    state,
    getters,
    actions,
    mutations
};