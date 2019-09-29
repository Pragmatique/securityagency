<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Login</h1>
      <label>Email</label>
      <input required v-model='email' type='text' placeholder='Name' />
      <label>Password</label>
      <input
        required
        v-model='password'
        type='password'
        placeholder='Password'
      />
      <hr />
      <button type='submit'>Login</button>
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    submitForm (event) {
      this.login()
      this.email = ''
      this.password = ''
    },
    login () {
      let email = this.email
      let password = this.password
      console.log(email, password)
      this.$store.dispatch('login', {
        email: email,
        password: password
      }).then(() => this.$router.push({name: 'Home'}))
    }

  }
}
</script>
