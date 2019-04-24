
<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>Account Settings</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field name="username" :disabled="true" label="Username" type="text" v-model="user.username"></v-text-field>
                <v-text-field name="first_name" label="First Name" type="text" v-model="user.first_name"></v-text-field>
                <v-text-field name="last_name" label="Last Name" type="text" v-model="user.last_name"></v-text-field>
                <v-text-field name="email" label="Email" type="Email" v-model="user.email"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="light-blue">Save</v-btn>
              <v-btn color="light-blue">Reset Password</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    data() {
    return {
        user: {
          username: null,
          first_name: null,
          last_name: null,
          email: null,
          password: null
        }
      }
    },
    methods: {
      getUser() {
        this.$axios.get('/api/users/' + this.$cookies.get('user') + '/').then(
          (response) => {
            this.user = response.data;
          }
        )
      },
    },
    beforeMount() {
      this.getUser();
    },
  }
</script>

<style>
</style>
