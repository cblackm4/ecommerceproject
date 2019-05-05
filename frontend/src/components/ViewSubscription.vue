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

            <v-card-text>Recipes</v-card-text>
            <v-data-table :headers="headers" :items="subs.recipes" :show-pagination="false" hide-actions>
                <template v-slot:items="props">
                    <td class="text-xs-right">{{ props.item.name }}</td>
                    <td class="text-xs-right">{{ props.item.description }}</td>
                    <td class="text-xs-right">${{ props.item.price }}</td>
                    <td><v-tooltip bottom><template v-slot:activator="{ on }"><v-icon @click="removeRecipe()" v-on="on">cancel</v-icon></template><span>Remove Item</span></v-tooltip></td>
                </template>
            </v-data-table>

            <v-card-text>Products</v-card-text>
            <v-data-table :headers="headers" :items="subs.products" :show-pagination="false" hide-actions>
                <template v-slot:items="props">
                    <td class="text-xs-right">{{ props.item.name }}</td>
                    <td class="text-xs-right">{{ props.item.description }}</td>
                    <td class="text-xs-right">${{ props.item.price }}</td>
                    <td><v-tooltip bottom><template v-slot:activator="{ on }"><v-icon @click="removeProduct()" v-on="on">cancel</v-icon></template><span>Remove Item</span></v-tooltip></td>
                </template>
            </v-data-table>

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
          text: 'Name',
          value: 'name'
        },
        {
          text: 'Description',
          value: 'description'
        },
        {
          text: 'Price',
          value: 'price'
        },
        {
          text: 'Actions',
          value: 'actions'
        }
      ],
    }),
    methods: {
        getSubs() {
            this.$axios.get('/api/subscriptions/' + this.$route.params.id + '/').then(
                (response) => {
                    this.subs = response.data;
                    console.log(this.subs);
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
        removeRecipe() {

        },
        removeProduct() {

        }
    },
    beforeMount() {
        this.getSubs();
    },
}
</script>

<style>

</style>
