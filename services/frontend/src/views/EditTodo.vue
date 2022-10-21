<template>
    <section>
        <h2>Wijzig toedoe</h2>
        <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="task" class="form-label">Taak:</label>
                <input type="text" name="task" v-model="form.task" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <label for="detail" class="form-label">Omschrijving:</label>
                <textarea name="detail" v-model="form.detail" class="form-control col-sm-6"></textarea>
            </div>
            <div class="mb-3">
                <label for="due_date" class="form-label">Deadline:</label>
                <input type="datetime-local" name="due_date" v-model="form.due_date" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <label for="finished" class="form-label">Klaar?</label>
                <input type="checkbox" name="finished" v-model="form.finished" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <button type="submit" class="btn btn-success btn-sm">Wijzig</button>
            </div>
        </form>
    </section>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
    name: 'EditTodo',
    props: ['id'],
    data() {
        return {
            form: {
                task: '',
                detail: '',
                due_date: '',
                finished: false,
            },
        }
    },
    computed: {
        ...mapGetters({ currentTodo: 'stateCurrentTodo' }),
    },
    methods: {
        ...mapActions(['updateTodo', 'getTodo']),
        async submit() {
            console.log("Updating todo:", this.form);
            let todo = {
                id: this.id,
                form: this.form
            }
            await this.updateTodo(todo);
            console.log("Todo updated");
            this.$router.push("/todos");
        },
        async fillTodo() {
            console.log("Filling using todo:", this.currentTodo);
            this.form.task = this.currentTodo.task;
            this.form.detail = this.currentTodo.detail;
            this.form.due_date = this.currentTodo.due_date;
            this.form.finished = this.currentTodo.finished;
        }
    },
    async created() {
        console.log("Getting todo:", this.id);
        // get the todo from the backend
        await this.getTodo(this.id);
        // and fill the form with the data
        console.log("Filling form with todo:", this.currentTodo);
        await this.fillTodo();
    },

}
</script>