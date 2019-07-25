import Vue from 'vue'
import Vuex from 'vuex'
import auth from '../api/auth'
import { User } from '../api/users'
import { HTTP } from '../api/common'

import {
  ADD_USER,
  REMOVE_USER,
  SET_USERS,
  LOGIN_BEGIN,
  LOGIN_FAILURE,
  LOGIN_SUCCESS,
  LOGOUT,
  REMOVE_TOKEN,
  SET_TOKEN
} from './mutation-types.js'

const TOKEN_STORAGE_KEY = 'TOKEN_STORAGE_KEY'

Vue.use(Vuex)
// Состояние
const state = {
  users: [] // список заметок
}
// Геттеры
const getters = {
  users: state => state.users, // получаем список заметок из состояния
  isAuthenticated: state => !!state.token
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
  },

  [LOGIN_BEGIN] (state) {
    state.authenticating = true
    state.error = false
  },
  [LOGIN_FAILURE] (state) {
    state.authenticating = false
    state.error = true
  },
  [LOGIN_SUCCESS] (state) {
    state.authenticating = false
    state.error = false
  },
  [LOGOUT] (state) {
    state.authenticating = false
    state.error = false
  },
  [SET_TOKEN] (state, token) {
    localStorage.setItem(TOKEN_STORAGE_KEY, token)
    HTTP.defaults.headers.Authorization = `Token ${token}`
    state.token = token
  },
  [REMOVE_TOKEN] (state) {
    localStorage.removeItem(TOKEN_STORAGE_KEY)
    delete HTTP.defaults.headers.Authorization
    state.token = null
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
  },
  login ({ commit }, { Email, Password }) {
    commit(LOGIN_BEGIN)
    return auth
      .login(Email, Email, Password)
      .then(({ data }) => commit(SET_TOKEN, data.key))
      .then(() => commit(LOGIN_SUCCESS))
      .catch(() => commit(LOGIN_FAILURE))
  },
  logout ({ commit }) {
    return auth
      .logout()
      .then(() => commit(LOGOUT))
      .finally(() => commit(REMOVE_TOKEN))
  },
  initialize ({ commit }) {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY)

    if (token) {
      commit(SET_TOKEN, token)
    } else {
      commit(REMOVE_TOKEN)
    }
  }
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
