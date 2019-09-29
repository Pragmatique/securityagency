<template>
  <div id="app">
    <div class="card" v-for="user in users" v-bind:key="user.id" style="width: 36rem;">

        <div class="card-header"><button class="btn btn-clear float-right" @click="deleteUser(user)"></button>
            <img v-if="user.profile!==null && user.profile.photo!==null" class="card-img-center" :src="user.profile.photo" :alt="user.email" height="50px" width="50px" />
            <img v-else class="card-img-center" src="../assets/logo.png" :alt="user.email" height="50px" width="50px" />
            <div class="card-title">{{ user.email }}</div>
            <div class="card-subtitle">{{ moment(user.date_joined) }}</div>
        </div>
    </div>
  </div>
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
    },
    logger (object) {
      console.log(object)
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
    console.log(this.$store.users)
  }
}
</script>
<style>
  header {
    margin-top: 50px;
  }
</style>
