<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>Contact Us</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field prepend-icon="person" name="First Name" label="First Name" type="text"></v-text-field>
                <v-text-field prepend-icon="person" name="Last Name" label="Last Name" type="text"></v-text-field>
                <v-text-field prepend-icon="confirmation_number" name="Order" label="Order Number (optional)" type="text"></v-text-field>
                <v-text-field prepend-icon="email" name="Email" label="Email" type="Email"></v-text-field>
                <!--80 character limit for contact reason-->
                <v-textarea prepend-icon="format_quote" name="Reason for Contact" label="Reason for Contact" type="text" counter="80" :rules="[rules.length(80)]" no-resize></v-textarea>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary">Send</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    data: () => ({
      drawer: null,
      rules: {
        length: len => v => (v || '').length <= len || `Too many characters, please limit your comment to ${len} characters`
      }
    }),
    props: {
      source: String
    }
  }
</script>
