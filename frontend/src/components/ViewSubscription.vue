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
                            <td style="padding-top: 8px; padding-bottom: 8px"><h3>Status: </h3></td>
                            <td><h3>{{ subs.active }}</h3></td>
                        </tr>
                        <tr>
                            <td valign="top" style="padding-top: 8px; padding-bottom: 8px; width: 120px"><h3>Subscription: </h3></td>
                            <td><h3>{{ subs.frequency }}</h3></td>
                        </tr>
                    </table>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn @click="" dark><v-icon>edit</v-icon>Edit Details</v-btn>
                    </v-card-actions>
                </v-form>
            </v-card-text>

            <v-card-text><h3>Recipes</h3></v-card-text>
            <v-data-table :headers="headers" :items="subs.recipes" :show-pagination="false" :key="recipeKey" hide-actions>
              <template v-slot:items="props">
                  <td class="text-xs-left">{{ props.item.name }}</td>
                  <td class="text-xs-left">{{ props.item.description }}</td>
                  <td class="text-xs-left">${{ props.item.price }}</td>
                  <td><v-tooltip bottom><template v-slot:activator="{ on }"><v-icon @click="removeRecipe(props.item)" v-on="on">cancel</v-icon></template><span>Remove Item</span></v-tooltip></td>
              </template>
              <template v-slot:no-data>
                  <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                     You are not currently subscribed to any recipes.
                  </v-alert>
              </template>
            </v-data-table>

            <v-card-text><h3>Products</h3></v-card-text>
            <v-data-table :headers="headers" :items="subs.products" :show-pagination="false" :key="productKey" hide-actions>
              <template v-slot:items="props">
                  <td class="text-xs-left">{{ props.item.name }}</td>
                  <td class="text-xs-left">{{ props.item.description }}</td>
                  <td class="text-xs-left">${{ props.item.price }}</td>
                  <td><v-tooltip bottom><template v-slot:activator="{ on }"><v-icon @click="removeProduct(props.item)" v-on="on">cancel</v-icon></template><span>Remove Item</span></v-tooltip>

                  </td>
              </template>
              <template v-slot:no-data>
                  <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                     You are not currently subscribed to any products.
                  </v-alert>
              </template>
            </v-data-table>

            <v-dialog v-model="dialog" max-width="290">
              <v-card>
                <v-card-title class="headline">Remove Item?</v-card-title>
                <v-card-text>By clicking "YES," this item will be removed from your subscription. This action cannot be undone. If you wish
                to resubscribe to the item, you will have to readd the item to your subscription.</v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="green darken-1" flat @click="dialog = false, agreed = false">Disagree</v-btn>
                  <v-btn color="green darken-1" flat @click="dialog = false, agreed = true">Agree</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

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
      recipeKey: 0,
      productKey: 0,
      dialog: false,
      agreed: false,
    }),
    methods: {
        getSubs() {
            this.$axios.get('/api/subscriptions/' + this.$route.params.id + '/').then(
                (response) => {
                    var subscriptionData = response.data,
                        currentRecipe,
                        recipeCost;

                    for (var r = 0; r < subscriptionData.recipes.length; r++) {
                        currentRecipe = subscriptionData.recipes[r];
                        recipeCost = 0;
                        for (var i = 0; i < currentRecipe.ingredients.length; i++) {
                            recipeCost += currentRecipe.ingredients[i].price;
                        }

                        currentRecipe.price = recipeCost.toFixed(2);
                    }
                    this.subs = subscriptionData;

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
        removeRecipe(recipe) {
          var currentRecipe = this.subs.recipes, updatedRecipes = [];

          for (var i = 0; i < currentProducts.length; i++) {
            if (currentProducts[i].id != product.id) {
              updatedProducts.push(currentProducts[i]);
              console.log(currentProducts[i]);
            }
          }
          this.subs.products = updatedProducts;
          this.recipeKey += 1;
        },
        removeProduct(product) {
          //this.dialog = true;
          console.log("prcoess");
          var currentProducts = this.subs.products, updatedProducts = [];

          for (var i = 0; i < currentProducts.length; i++) {
            if (currentProducts[i].id != product.id) {
              updatedProducts.push(currentProducts[i]);
              console.log(currentProducts[i]);
            }
          }
          this.subs.products = updatedProducts;
          this.productKey += 1;
        },
    },
    beforeMount() {
        this.getSubs();
    },
}
</script>

<style>

</style>
