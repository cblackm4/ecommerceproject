<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 md9>
          <v-card>
            <v-toolbar dark flat>
              <v-toolbar-title>Edit Subscription</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn @click="$router.push('/subscriptions/')" flat><v-icon>keyboard_arrow_left</v-icon>Back to Subscriptions</v-btn>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>

            <v-card-text>
                <v-form>
                    <table style="width: 100%; padding-left: 20px; font-family: Roboto;">
                        <tr>
                            <td style="padding-top: 8px; padding-bottom: 16px"><h3>Status: </h3></td>
                            <td>{{ subs.active }}</td>
                        </tr>
                        <tr>
                            <td valign="top" style="padding-bottom: 8px; width: 120px"><h3>Subscription: </h3></td>
                            <td>{{ subs.frequency }}</td>
                        </tr>
                    </table>
                </v-form>
            </v-card-text>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancelSub()" dark><v-icon>delete</v-icon>Cancel Subscription</v-btn>
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
      subs: {},
      products: [],
      recipes: [],
      headers: [
        {
          text: 'Recipes',
          value: 'recipes'
        },
        {
          text: 'Products',
          value: 'products'
        },
        {
          text: 'Subscription Length',
          value: 'frequency'
        },
        {
          text: 'Active?',
          value: 'active'
        },
        {
          text: '',
          value: 'edit'
        }
      ],
    }),
    methods: {
        getSubs() {
            this.$axios.get('/api/subscriptions/').then(
                (response) => {
                    this.subs = response.data;
                }
            )
        },
        cancelSub() {
            this.$axios.delete('/api/subscriptions/' + this.$route.params.id + '/').then(
                () => {
                    this.$router.push('/subscriptions/');
                }
            );
        },
    },
    beforeMount() {
        this.getSubs();
    },
}
</script>

<style>

</style>
