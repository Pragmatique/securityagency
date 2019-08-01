import { HTTP } from './common'
export const User = {
  create (config) {
    /* const headers = {
      'Content-Type': 'multipart/form-data'
    } */
    return HTTP.post('/users/', config).then(response => {
      return response.data
    })
  },
  delete (user) {
    return HTTP.delete(`/users/${user.id}/`)
  },
  list () {
    return HTTP.get('/users/').then(response => {
      return response.data
    })
  },
  updateProfile (config) {
    const headers = {
      'Content-Type': 'multipart/form-data'
    }
    return HTTP.put(`/userprofiles/${config.id}/`, config.formData, headers).then(response => {
      return response.data
    })
  }
}
