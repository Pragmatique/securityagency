import axios from 'axios'
import router from '../router'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/'
})

HTTP.interceptors.response.use((response) => {
  return response
}, (error) => {
  if (error.response.status === 401) {
    router.push('/login')
  }
  return Promise.reject(error)
}
)
