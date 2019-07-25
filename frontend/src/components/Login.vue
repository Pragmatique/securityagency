<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Sign in</h1>
      <label>Email</label>
      <input required v-model='Email' type='text' placeholder='Name' />
      <label>Password</label>
      <input
        required
        v-model='Password'
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
      Email: '',
      Password: ''
    }
  },
  methods: {
    login () {
      let Email = this.Email
      let Password = this.Password
      console.log(Email, Password)
      this.$store.dispatch('login', {
        Email: Email,
        Password: Password
      })
    }

  },
  mounted () {
    this.login()
  }
}
</script>
