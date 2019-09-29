import axios from 'axios'

export default function setup () {
  axios.interceptors.response.use((response) => { // intercept the global error
    console.log(response.status)
    return response
  }, function (error) {
    // this.$router.push({name: 'login'})
    console.log('Step1')
    // let originalRequest = error.config
    if (error.response.status === 401) { // if the error is 401 and hasent already been retried
      this.$router.push({name: 'Login'})
      console.log('Step2')
    }
    // Do something with response error
    return Promise.reject(error)
  })
}
