<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 md9>
          <v-card>
            <v-toolbar dark flat>
              <v-toolbar-title>Checkout</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field name="first_name" label="First Name" type="text" v-model="user.first_name"></v-text-field>
                <v-text-field name="last_name" label="Last Name" type="text" v-model="user.last_name"></v-text-field>
                <v-text-field name="email" label="Email" type="Email" v-model="user.email"></v-text-field>
                <v-text-field name="Shipping Address" label="Shipping Address" type="text"></v-text-field>
                <v-text-field name="Billing Address" label="Billing Address" type="text"></v-text-field>
                <v-text-field name="Card Number" label="Card Number" type="text"></v-text-field>
                <v-text-field name="CVV" label="CVV" type="text"></v-text-field>
                <v-text-field name="Zip Code" label="Zip Code" type="text"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn dark>Place Order</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    data () {
      return {
        user_info: true,
        /*snackbar: false,
        text: ''*/
      }
    },
    computed: {
      user() {
        return this.$store.getters.user;
      }
    }
  }
</script>

<style>
</style>
