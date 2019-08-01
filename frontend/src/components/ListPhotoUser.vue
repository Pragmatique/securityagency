<template>
  <div id="app">
    <div class="card" v-for="user in users">
        <div class="card-header"><button class="btn btn-clear float-right" @click="deleteUser(user)"></button>
            <div class="card-title">{{ user.email }}</div>
            <div class="card-subtitle">{{ moment(user.date_joined) }}</div>
        </div>
        <div class="card-img"><img src={{user.photo}} /></div>
    </div>
  </div>
  #app
    .card(v-for="user in users")
      .card-header
        button.btn.btn-clear.float-right(@click="deleteUser(user)")
        .card-title {{ user.email }}
        .card-subtitle {{ moment(user.date_joined) }}
      .card-img
        img(src='user.photo')
</template>
<script>
import { mapGetters } from 'vuex'
import moment from 'moment'
export default {
  name: 'user-list',
  computed: mapGetters(['users']),
  methods: {
    deleteUser (user) {
      // Вызываем действие `deleteUser` из нашего хранилища, которое
      // попытается удалить заметку из нашех базы данных, отправив запрос к API
      this.$store.dispatch('deleteUser', user)
    },
    moment (date) {
      return moment(date).format('Do MMMM YYYY')
    }
  },
  filters: {
    moment (date) {
      return moment(date).format('MM Do YYYY')
    }
  },
  beforeMount () {
    // Перед тем как загрузить страницу, нам нужно получить список всех
    // имеющихся заметок. Для этого мы вызываем действие `getNotes` из
    // нашего хранилища
    this.$store.dispatch('getUsers')
  }
}
</script>
<style>
  header {
    margin-top: 50px;
  }
</style>
