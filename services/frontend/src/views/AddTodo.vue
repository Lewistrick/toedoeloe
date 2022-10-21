<template>
    <section>
        <h2>Nieuwe toedoe</h2>
        <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="task" class="form-label">Taak:</label>
                <input type="text" name="task" v-model="form.task" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <label for="detail" class="form-label">Omschrijving:</label>
                <textarea name="detail" v-model="form.detail" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <label for="due_date" class="form-label">Deadline:</label>
                <input type="datetime-local" name="due_date" v-model="form.due_date" class="form-control col-sm-6" />
            </div>
            <div class="mb-3">
                <button type="submit" class="btn btn-success">Toevoegen</button>
            </div>
        </form>
    </section>
</template>

<script>
import { mapActions } from 'vuex';
export default {
    name: 'AddTodo',
    data() {
        return {
            form: {
                task: '',
                detail: '',
                due_date: '',
            },
        }
    },
    methods: {
        ...mapActions(['createTodo']),
        async submit() {
            console.log("Creating todo:", this.form);
            console.log("(details:)", this.form.task, this.form.detail, this.form.due_date);
            await this.createTodo(this.form);
            console.log("Todo created");
            this.$router.push("/todos");
        }
    }
}
</script>
