import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/'
})
