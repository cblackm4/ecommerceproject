<template>

  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="light-blue">
                <v-toolbar-title>Contact Us</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip right>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field name="First Name" label="First Name" type="text"></v-text-field>
                  <v-text-field name="Last Name" label="Last Name" type="text"></v-text-field>
                  <v-text-field name="Order" label="Order Number (optional)" type="text"></v-text-field>
                  <v-text-field name="Email" label="Email" type="Email"></v-text-field>
                  <v-text-field name="Reason for Contact" label="Reason for Contact" type="text"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="light-blue">Send</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      drawer: null
    }),
    props: {
      source: String
    }
  }
</script>
