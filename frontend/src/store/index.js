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

const t = localStorage.getItem(TOKEN_STORAGE_KEY)
console.log(t)
HTTP.defaults.headers.Authorization = `Bearer ${t}`
console.log(HTTP.defaults.headers.Authorization)

Vue.use(Vuex)
// Состояние
const state = {
  users: [], // список заметок
  authenticating: false,
  error: false,
  token: localStorage.getItem(TOKEN_STORAGE_KEY)
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
    localStorage.removeItem(TOKEN_STORAGE_KEY)
    delete HTTP.defaults.headers.Authorization
    state.token = null
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
    HTTP.defaults.headers.Authorization = `Bearer ${token}`
    console.log(HTTP.defaults.headers.Authorization)
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
      console.log('result from api call', user)
      return user
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
  updateProfile ({ commit }, config) {
    User.updateProfile(config)
  },
  login ({ commit }, payload) {
    commit(LOGIN_BEGIN)
    return auth
      .login(payload.email, payload.email, payload.password)
      .then(({ data }) => commit(SET_TOKEN, data.token))
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
  },
  createUserFull ({ commit, dispatch }, userData) {
    User.create(userData.initialData).then(user => {
      debugger
      commit(ADD_USER, user)
      User.updateProfile({
        id: user.profile.id,
        formData: userData.formData
      })
      console.log('result from api call', user)
    })
    /* return new Promise((resolve, reject) => {
      // Do something here... lets say, a http call using vue-resource
      dispatch('createUser', userData.initialData).then(response => {
        resolve(response)
      }, error => {
        reject(error)
      })
    }).then(response => {
      User.updateProfile({
        id: response.json().id,
        formData: userData.formData
      })
    }) */
    /* dispatch('createUser', userData.initialData).then(response => {
      User.updateProfile({
        id: response.data.id,
        formData: userData.formData
      })
    }) */
  }
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
