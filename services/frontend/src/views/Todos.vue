<template>
    <section>
        <h2>Toedoes</h2>
        <p>Je hebt {{ todos.length }} toedoes, waarvan {{ getUnfinishedTodos().length }} openstaande.</p>
        <div class="row row-cols-4">
            <!-- Big button for new task -->
            <div class="card todo shadow newtask" @click="createTodo">
                <div class="card-body limited inline">
                    <p class="card-text bigplus">+</p>
                </div>
            </div>

            <!-- First show unfinished todos -->
            <div v-for="todo in getUnfinishedTodos()" :key="todo.id" class="card todo shadow">
                <div class="card-header">{{ todo.task }}</div>
                <div class="card-body limited">
                    <p class="card-text">{{ todo.detail }}</p>
                </div>
                <div class="card-footer right">
                    <button class="btn btn-success btn-sm" @click="toggleFinished(todo.id)">
                        <font-awesome-icon icon="fa-solid fa-circle-check" />
                    </button>
                    <span class="spacer"></span>
                    <router-link :to="{name: 'EditTodo', params:{id: todo.id}}" class="btn btn-light btn-sm">
                        <font-awesome-icon icon="fa-solid fa-pencil" />
                    </router-link>
                </div>
            </div>
        </div>

        <hr />

        <!-- Then show finished todos -->
        <div v-if="getFinishedTodos().length > 0">
            <h2>Klaar</h2>
            <div class="row row-cols-4">
                <div v-for="todo in getFinishedTodos()" :key="todo.id" class="card done shadow">
                    <div class="card-header">{{ todo.task }}</div>
                    <div class="card-body limited">
                        <p class="card-text">{{ todo.detail }}</p>
                    </div>
                    <div class="card-footer right">
                        <button class="btn btn-warning btn-sm" @click="toggleFinished(todo.id)">
                            <font-awesome-icon icon="fa-solid fa-hand-point-up" />
                        </button>
                        <span class="spacer"></span>
                        <router-link :to="{name: 'EditTodo', params:{id: todo.id}}" class="btn btn-light btn-sm">
                            <font-awesome-icon icon="fa-solid fa-pencil" />
                        </router-link>
                        <span class="spacer"></span>
                        <button class="btn btn-danger btn-sm" @click="deleteMe(todo.id)">
                            <font-awesome-icon icon="fa-solid fa-trash" />
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <p>Je hebt geen afgeronde toedoes.</p>
        </div>
    </section>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
    name: 'Todos',
    computed: {
        ...mapGetters({ todos: 'stateTodos' }),
    },
    methods: {
        ...mapActions(['getTodos', 'toggleTodoFinish', 'deleteTodo']),
        async createTodo() {
            this.$router.push("/addtodo");
        },
        getUnfinishedTodos() {
            return this.todos.filter((t) => !t.finished);
        },
        getFinishedTodos() {
            return this.todos.filter((t) => t.finished);
        },
        async toggleFinished(id) {
            await this.toggleTodoFinish(id);
            await this.getTodos();
        },
        async deleteMe(id) {
            await this.$store.dispatch('deleteTodo', id);
            await this.getTodos();
        },
    },
    async created() {
        await this.getTodos();
    }
}
</script>

<style scoped>
.todo {
    color: #ccc;
    background-color: #579;
    border: 1px solid #ccc;
    border-radius: 10px;
    height: 180px;
    padding: 0px;
    margin: 10px;
    /* overflow: hidden; */
}

.done {
    color: #ccc;
    background-color: #456;
    border: 1px solid #ccc;
    border-radius: 10px;
    height: 180px;
    padding: 0px;
    margin: 10px;
    /* overflow: hidden; */
}

.limited {
    overflow: hidden;
}

.newtask {
    position: relative;
    background-color: #79b;
    text-align: center;
}

.newtask:hover {
    background-color: #8ac;
}

.inline {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: inline-block;
}

.bigplus {
    margin: auto;
    font-size: 5em;
}

.right {
    text-align: right;
}

.spacer {
    padding-right: 10px;
}
</style>