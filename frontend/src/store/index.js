import Vue from 'vue'
import Vuex from 'vuex'
import { User } from '../api/users'
import {
  ADD_USER,
  REMOVE_USER,
  SET_USERS
} from './mutation-types.js'

Vue.use(Vuex)
// Состояние
const state = {
  users: [] // список заметок
}
// Геттеры
const getters = {
  notes: state => state.users // получаем список заметок из состояния
}
// Мутации
const mutations = {
  // Добавляем заметку в список
  [ADD_USER] (state, user) {
    state.users = [user, ...state.users]
  },
  // Убираем заметку из списка
  [REMOVE_USER] (state, { id }) {
    state.users = state.users.filter(user => {
      return user.id !== id
    })
  },
  // Задаем список заметок
  [SET_USERS] (state, { users }) {
    state.users = users
  }
}
// Действия
const actions = {
  createUser ({ commit }, userData) {
    User.create(userData).then(user => {
      commit(ADD_USER, user)
    })
  },
  deleteUser ({ commit }, user) {
    User.delete(user).then(response => {
      commit(REMOVE_USER, user)
    })
  },
  getUsers ({ commit }) {
    User.list().then(users => {
      commit(SET_USERS, { users })
    })
  }
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
