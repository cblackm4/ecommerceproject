<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 md9>
          <v-card>
            <v-toolbar dark flat>
              <v-toolbar-title>Account Settings</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip right>
              </v-tooltip>
              <template v-slot:extension>
                <v-tabs
                  v-model="tab_selection"
                  color="transparent"
                  slider-color="white"
                >
                  <v-tab
                    v-for="tab in tabs"
                    :key="tab.name"
                  >
                    {{ tab.name }}
                  </v-tab>
                </v-tabs>
              </template>
            </v-toolbar>
            <v-card-text v-if="tab_selection === 0">
              <v-form>
                <v-text-field name="username" :disabled="true" label="Username" type="text" v-model="user.username"></v-text-field>
                <v-text-field name="first_name" label="First Name" type="text" v-model="user.first_name"></v-text-field>
                <v-text-field name="last_name" label="Last Name" type="text" v-model="user.last_name"></v-text-field>
                <v-text-field name="email" label="Email" type="Email" v-model="user.email"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-text v-if="tab_selection === 1">
              <v-form>
                <v-text-field name="shipping_address" label="Shipping Address" type="text" v-model="customer.shipping_address"></v-text-field>
                <v-text-field name="billing_address" label="Billing Address" type="text" v-model="customer.billing_address"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="save" dark>Save</v-btn>
              <v-btn dark>Reset Password</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-snackbar
      v-model="snackbar"
      :timeout="5000"
      color="green"
      bottom
      right>
      {{snackbarMessage}}
      <v-btn
        @click="snackbar = false;"
        flat>
        Close
      </v-btn>
    </v-snackbar>
  </v-content>
</template>

<script>
  export default {
    data() {
      return {
        customer: {
          shipping_address: '',
          billing_address: ''
        },
        snackbar: false,
        snackbarMessage: "",
        tab_selection: null,
        tabs: [
          { name: 'User' },
          { name: 'Customer' }
        ]
      }
    },
    computed: {
      user() {
        return this.$store.getters.user;
      }
    },
    methods: {
      save() {
        if (this.tab_selection === 0) {
          this.$axios.put('/api/users/' + this.$cookies.get('user') + '/', this.user).then(
            (response) => {
              this.$store.commit('setUser', response.data);
              this.snackbarMessage = "Save successful!";
              this.snackbar = true;
            }
          );
        } else if (this.tab_selection === 1) {
          this.$axios.put('/api/customers/' + this.$cookies.get('user') + '/', this.customer).then(
            (response) => {
              this.snackbarMessage = "Save successful!";
              this.snackbar = true;
            }
          );
        }
      },
      getCustomer() {
        this.$axios.get('/api/customers/' + this.$cookies.get('user') + '/').then(
          (response) => {
            this.customer = response.data;
          }
        )
      },
    },
    beforeMount() {
      this.getCustomer();
    }
  }
</script>

<style>
</style>
