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
                        <v-btn @click="editDetails()" dark><v-icon>edit</v-icon>Edit Details</v-btn>
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

            <v-dialog dark v-model="cancelDialog" persistent max-width="500">
              <v-card>
                <v-card-title class="headline">Cancel Subscription?</v-card-title>
                <v-card-text>By clicking "YES," this subscription will be cancelled immediately.</v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="white" flat @click="cancelDialog = false">No</v-btn>
                  <v-btn color="white" flat @click="cancelDialog = false; cancelSub();">Yes, I want to cancel.</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <v-dialog dark v-model="confirmCancel" persistent max-width="500">
              <v-card>
                <v-card-title class="headline">:(</v-card-title>
                <v-card-text>We're sad to see you go! We hope you consider resubscribing in the future. If you wish to re-subscribe at any point, you can setup a new subscription by visiting the
                  <router-link to='/create-subscription/:id?'>
                    <a>Create Subscription</a>
                  </router-link> page.
                   Redirecting you to your subscriptions page...
                <div class="text-xs-center">
                  <v-progress-circular
                    indeterminate
                    color="white"
                  ></v-progress-circular></div></v-card-text>
              </v-card>
            </v-dialog>

            <v-dialog dark v-model="editDetail" persistent max-width="600">
              <v-card>
                <v-card-title class="headline">Chnage Subscription Type</v-card-title>
                <v-card-text>
                  <v-combobox v-model="subs.frequency" :items="sub_type" label="Select a Subscription Type"></v-combobox>
                </v-card-text>
                <v-card-actions>
                  <v-btn color="white" flat @click="editDetail = false">Cancel</v-btn>
                  <v-spacer></v-spacer>

                  <v-btn color="white" flat @click="editDetail = false; changeSub();">Accept</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <v-dialog dark v-model="saveDialog" persistent max-width="500">
              <v-card>
                <v-card-title class="headline">Adjusting Your Settings</v-card-title>
                <v-card-text>Your changes will be reflected on your account immediately. Redirecting you to your subscriptions.
                <div class="text-xs-center">
                  <v-progress-circular
                    indeterminate
                    color="white"
                  ></v-progress-circular></div></v-card-text>
              </v-card>
            </v-dialog>

            <v-card-actions>
              <v-btn @click="cancelDialog=true" dark><v-icon>delete</v-icon>Cancel Subscription</v-btn>
              <v-spacer></v-spacer>
              <v-btn @click="saveSub()" dark><v-icon>save_alt</v-icon>Save Changes</v-btn>
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
      subs: {
      },
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
      sub_type: [
        {
          text: '30 Days',
          value: '30 00:00:00'
        },
        {
          text: '6 Months',
          value: '180 00:00:00'
        },
      ],
      recipeKey: 0,
      productKey: 0,
      cancelDialog: false,
      confirmCancel: false,
      saveDialog: false,
      agreed: false,
      editDetail: false,
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

                    // Convert data into readable format
                    for (var j in subscriptionData) {
                      if (subscriptionData.frequency == "30 00:00:00") {
                        subscriptionData.frequency = "30 days";
                      }
                      if (subscriptionData.frequency == "180 00:00:00") {
                        subscriptionData.frequency = "6 Months";
                      }
                      if (subscriptionData.active == true) {
                        subscriptionData.active = "Active";
                      }
                      if (subscriptionData.active == false) {
                        subscriptionData.active = "Inactive";
                      }
                    }

                    this.subs = subscriptionData;

                }
            )
        },
        changeSub() {
          var frequency = this.subs.frequency.value;
          if (frequency != undefined && frequency != null) {
            if (frequency == "30 00:00:00") {
              this.subs.frequency = "30 Days";
            } else if (frequency == "180 00:00:00") {
              this.subs.frequency = "6 Months";
            }
          } else {
            frequency = this.subs.frequency;
          }
        },
        cancelSub() {
            this.$axios.delete('/api/subscriptions/' + this.$route.params.id + '/').then(
            (response) => {
                this.confirmCancel = true;
                setTimeout(() =>
                  this.$router.push('/subscriptions/'), 3000);
            })
        },
        removeRecipe(recipe) {
          var currentRecipe = this.subs.recipes, updatedRecipes = [];

          for (var i = 0; i < currentRecipe.length; i++) {
            if (currentRecipe[i].id != recipe.id) {
              updatedRecipes.push(currentRecipe[i]);
              console.log(currentRecipe[i]);
            }
          }
          this.subs.recipes = updatedRecipes;
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
        editDetails() {
          this.editDetail = true;
        },
        saveSub() {

          var editedSub = {
            "user": this.$cookies.get('user'),
            "recipes": this.subs.recipes,
            "products": this.subs.products,
            "frequency": this.subs.frequency.value,
            "active": this.subs.active
          }

          this.$axios.put('/api/subscriptions/' + this.$route.params.id + '/', editedSub).then(
              (response) => {
                this.confirmSub = true;
                setTimeout(() =>
                  this.$router.push('/subscriptions/' + response.data.id + '/'), 2000);
              },
              (error) => { alert("fail"); }
            )
        }
    },
    beforeMount() {
        this.getSubs();
    },
}
</script>

<style>

</style>
