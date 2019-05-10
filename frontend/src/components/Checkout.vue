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
            <v-switch v-model="user_info" label="Do not use information from pawkages account: "></v-switch>
            <v-card-text>
              <v-form>
                <div v-if="user_info">
                  <v-text-field name="First Name" label="First Name" type="text"></v-text-field>
                  <v-text-field name="Last Name" label="Last Name" type="text"></v-text-field>
                  <v-text-field name="Shipping Address" label="Shipping Address" type="text"></v-text-field>
                  <v-text-field name="Billing Address" label="Billing Address" type="text"></v-text-field>
                </div>
                <div v-else>
                  <v-alert type="info" :value="true">
                    Information from your pawkages account will be used for this order
                  </v-alert>
                </div>
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
    }/*,
    methods: {
      order() {
        this.text = "We received your order. Have a nice day!";
        this.snackbar = true;

      },

      getCustomer() {
        this.$axios.get('/api/customers/' + this.$cookies.get('user') + '/').then(
          (response) => {
            this.customer = response.data;
          }
        )
      }
    }*/
  }

</script>

<style>

</style>
