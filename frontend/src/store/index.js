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
const getDefaultState = () => {
  return {
    users: [], // список заметок
    authenticating: false,
    error: false,
    token: localStorage.getItem(TOKEN_STORAGE_KEY)
  }
}

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
    state = getDefaultState()
    // state.authenticating = false
    // state.error = false
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
  async createUser ({ commit }, userData) {
    try {
      const user = await User.create(userData)
      await commit(ADD_USER, user)
    } catch (error) {
      console.error(error)
    }
    /* User.create(userData).then(user => {
      commit(ADD_USER, user)
      console.log('result from api call', user)
      return user
    }) */
  },
  async deleteUser ({ commit }, user) {
    try {
      await User.delete(user)
      await commit(REMOVE_USER, user)
    } catch (error) {
      console.error(error)
    }
    /* User.delete(user).then(response => {
      commit(REMOVE_USER, user)
    }) */
  },
  async getUsers ({ commit }) {
    try {
      const users = await User.list()
      console.log(users)
      await commit(SET_USERS, { users })
      console.log(state.users)
    } catch (error) {
      console.error(error)
    }
    /* User.list().then(users => {
      commit(SET_USERS, { users })
    }) */
  },
  updateProfile ({ commit }, config) {
    User.updateProfile(config)
  },
  async login ({ commit }, payload) {
    try {
      commit(LOGIN_BEGIN)
      const data = await auth.login(payload.email, payload.email, payload.password)
      console.log(data)
      await commit(SET_TOKEN, data.data.token)
      await commit(LOGIN_SUCCESS)
    } catch (error) {
      console.error(error)
      commit(LOGIN_FAILURE)
    }
    /* commit(LOGIN_BEGIN)
    return auth
      .login(payload.email, payload.email, payload.password)
      .then(({ data }) => commit(SET_TOKEN, data.token))
      .then(() => commit(LOGIN_SUCCESS))
      .catch(() => commit(LOGIN_FAILURE)) */
  },
  async logout ({ commit }) {
    try {
      await auth.logout
      return await commit(LOGOUT)
    } catch (error) {
      console.error(error)
    } finally {
      commit(REMOVE_TOKEN)
    }
    /* return auth
      .logout()
      .then(() => commit(LOGOUT))
      .finally(() => commit(REMOVE_TOKEN)) */
  },
  initialize ({ commit }) {
    try {
      const token = localStorage.getItem(TOKEN_STORAGE_KEY)
      if (token) {
        commit(SET_TOKEN, token)
      } else {
        commit(REMOVE_TOKEN)
      }
    } catch (error) {
      console.error(error)
    }
  },
  async createUserFull ({ commit, dispatch }, userData) {
    try {
      const user = await User.create(userData.initialData)
      const profile = await User.updateProfile({
        id: user.profile.id,
        formData: userData.formData
      })
      user.profile = profile
      commit(ADD_USER, user)
    } catch (error) {
      console.error(error)
    }
  }
  /* createUserFull ({ commit, dispatch }, userData) {
    User.create(userData.initialData).then(user => {
      console.log('result from api call', user)
      return User.updateProfile({
        id: user.profile.id,
        formData: userData.formData
      }).then(profile => {
        user.profile = profile
        return user
      })
    }).then(user => { commit(ADD_USER, user) })
    *//* return new Promise((resolve, reject) => {
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
    }) *//*
    *//* dispatch('createUser', userData.initialData).then(response => {
      User.updateProfile({
        id: response.data.id,
        formData: userData.formData
      })
    }) *//*
  } */
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
