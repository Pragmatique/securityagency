<template lang="pug">
  #app
    .card(v-for="user in users")
      .card-header
        button.btn.btn-clear.float-right(@click="deleteUser(user)")
        .card-title {{ user.email }}
        .card-subtitle {{ user.created_at }}
      .card-body {{ user.username }}
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'user-list',
  computed: mapGetters(['users']),
  methods: {
    deleteUser (user) {
      // Вызываем действие `deleteUser` из нашего хранилища, которое
      // попытается удалить заметку из нашех базы данных, отправив запрос к API
      this.$store.dispatch('deleteUser', user)
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
