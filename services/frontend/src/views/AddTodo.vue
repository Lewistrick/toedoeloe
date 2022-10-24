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
                <div class="row">
                    <input type="button" class="btn btn-light col-md-1 m-3" value="Nu" @click="setNow" />
                    <input type="button" class="btn btn-light col-md-1 m-3" value="+1 uur" @click="addHours(1)" />
                    <input type="button" class="btn btn-light col-md-1 m-3" value="+2 uur" @click="addHours(2)" />
                    <input type="button" class="btn btn-light col-md-1 m-3" value="+1 dag" @click="addDays(1)" />
                    <input type="button" class="btn btn-light col-md-1 m-3" value="+3 dagen" @click="addDays(3)" />
                    <input type="button" class="btn btn-light col-md-1 m-3" value="+1 week" @click="addWeeks(1)" />
                </div>
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
        },
        setNow() {
            let date = new Date();
            this.form.due_date = new Date(date.getTime() - date.getTimezoneOffset() * 60 * 1000).toISOString().slice(0, 16);
        },
        addHours(hours) {
            let date = this.form.due_date ? new Date(this.form.due_date) : new Date();

            // add the number of hours specified
            date.setHours(date.getHours() + hours);

            // set the date back to the form
            this.form.due_date = new Date(date - date.getTimezoneOffset() * 60 * 1000).toISOString().slice(0, 16);
        },
        addDays(days) {
            this.addHours(days * 24);
        },
        addWeeks(weeks) {
            this.addDays(weeks * 7);
        },
    },
    mounted() {
        this.setNow();
    },
}
</script>
