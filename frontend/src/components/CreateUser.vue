<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    .form-group
      .col-3
        label.form-label first_name
      .col-9
        input.form-input(type="text" v-model="first_name" placeholder="Type first_name...")
    .form-group
      .col-3
        label.form-label father_name
      .col-9
        input.form-input(type="text" v-model="father_name" placeholder="Type father_name...")
    .form-group
      .col-3
        label.form-label last_name
      .col-9
        input.form-input(type="text" v-model="last_name" placeholder="Type last_name...")
    .form-group
      .col-3
        label.form-label email
      .col-9
        input.form-input(type="email" v-model="email" placeholder="Type email...")
    .form-group
      .col-3
        label.form-label department
      .col-9
        input.form-input(type="text" v-model="department" placeholder="Type department...")
    .form-group
      .col-3
        label.form-label position
      .col-9
        input.form-input(type="text" v-model="position" placeholder="Type position...")
    .form-group
      .col-3
        label.form-label phone
      .col-9
        input.form-input(type="text" v-model="phone" placeholder="Type phone...")
    .form-group
      .col-3
        label.form-label password
      .col-9
        input.form-input(type="password" v-model="password" placeholder="Type password...")
    .form-group
      .col-3
        label.form-label address
      .col-9
        input.form-input(type="text" v-model="address" placeholder="Type address...")
    .form-group
      .col-3
        label.form-label city
      .col-9
        input.form-input(type="text" v-model="city" placeholder="Type city...")
    .form-group
      .col-3
        label.form-label photo
      .col-9
        input.form-input(type="file" v-on:change="handleFileUpload" placeholder="Set photo...")
    .form-group
      .col-3
      .col-9
        button.btn.btn-primary(type="submit") Create
</template>
<script>
export default {
  name: 'create-user',
  data () {
    return {
      'username': '',
      'first_name': '',
      'father_name': '',
      'last_name': '',
      'email': '',
      'department': '',
      'position': '',
      'phone': '',
      'password': '',
      'address': '',
      'city': '',
      'photo': null

    }
  },
  methods: {
    handleFileUpload (event) {
      this.photo = event.target.files[0]
      // this.photo = this.$refs.files[0]
    },
    submitForm (event) {
      this.createUser()
      // Т.к. мы уже отправили запрос на создание заметки строчкой выше,
      // нам нужно теперь очистить поля title и body

      this.first_name = ''
      this.father_name = ''
      this.last_name = ''
      this.email = ''
      this.department = ''
      this.position = ''
      this.phone = ''
      this.password = ''
      this.address = ''
      this.city = ''
      this.photo = null
      // preventDefault нужно для того, чтобы страница
      // не перезагружалась после нажатия кнопки submit
      event.preventDefault()
    },
    createUser () {
      /* const objectToFormData = require('object-to-formdata')
      let rawData = {
        first_name: this.first_name,
        father_name: this.father_name,
        last_name: this.last_name,
        email: this.email,
        department: this.department,
        position: this.position,
        phone: this.phone,
        password: this.password,
        profile: {
          address: this.address,
          city: this.city,
          photo: this.photo
        }
      }
      rawData = JSON.stringify(rawData) */
      /* let formData = objectToFormData(rawData) */
      /* let rawData1 = {
        first_name: this.first_name,
        father_name: this.father_name,
        last_name: this.last_name,
        email: this.email,
        department: this.department,
        position: this.position,
        phone: this.phone,
        password: this.password,
        profile: {
          address: this.address,
          city: this.city,
          photo: this.photo
        }
      }
      rawData1 = JSON.stringify(rawData1) */

      const rawData2 = {
        address: this.address,
        city: this.city,
        photo: null
      }
      let formData2 = new FormData()
      formData2.append('address', this.address)
      formData2.append('city', this.city)
      if (this.photo) {
        formData2.append('photo', this.photo, this.photo.name)
      } else {
        formData2.append('photo', null)
      }
      /* for (var pair of formData.entries()) {
        console.log(pair[0] + ', ' + pair[1])
      } */
      // Вызываем действие `createNote` из хранилища, которое
      // отправит запрос на создание новой заметки к нашему API.
      let config = {
        initialData: {
          username: this.username,
          first_name: this.first_name,
          father_name: this.father_name,
          last_name: this.last_name,
          email: this.email,
          department: this.department,
          position: this.position,
          phone: this.phone,
          password: this.password,
          profile: rawData2
        },
        formData: formData2
      }

      this.$store.dispatch('createUserFull', config)
      this.$router.push('/userlist')
    }
  }
}
</script>
