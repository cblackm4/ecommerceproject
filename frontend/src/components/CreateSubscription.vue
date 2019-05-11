<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex xs12 md9>
                    <v-card>
                        <v-toolbar dark flat>
                            <v-toolbar dark flat>
                                <v-toolbar-title>Create New Subscription</v-toolbar-title>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-btn @click="$router.push('/subscriptions/')" flat><v-icon>keyboard_arrow_left</v-icon>Back to Subscriptions</v-btn>
                                <v-tooltip right>
                                </v-tooltip>
                            </v-toolbar>
                            <v-spacer></v-spacer>
                            <v-tooltip right>
                            </v-tooltip>
                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-combobox v-model="subs.frequency" :items="sub_type" label="Select a Subscription Type"></v-combobox>

                                <table style="width: 100%">
                                    <tr>
                                        <td>
                                            <v-combobox :items="recipes"
                                                        :key="recipes.name"
                                                        v-model="selectedRecipe"
                                                        label="Select a Recipe to add">
                                            </v-combobox>
                                        </td>
                                        <td style="text-align:right; width: 4%">
                                            <v-btn @click="addRecipe()" dark><v-icon>add</v-icon></v-btn>
                                        </td>
                                    </tr>
                                </table>

                                <v-data-table :headers="headers" :items="subs.recipes"
                                              hide-actions>
                                    <template v-slot:items="props">
                                        <td class="text-xs-left">{{ props.item.name }}</td>
                                        <td class="text-xs-left">{{ props.item.description }}</td>
                                        <td class="text-xs-left">${{ formatPrice(props.item.price) }}</td>
                                        <td><v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-icon @click="removeRecipe(props.item)" v-on="on">cancel</v-icon>
                                        </template><span>Remove Item</span></v-tooltip></td>
                                    </template>

                                    <template v-slot:no-data>
                                        <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                                            No recipes added to this subscription.
                                        </v-alert>
                                    </template>
                                </v-data-table>

                                <table style="width: 100%">
                                    <tr>
                                        <td>
                                            <v-combobox :items="products"
                                                        :key="products.name"
                                                        v-model="selectedProduct"
                                                        label="Select a Product to add">
                                            </v-combobox>
                                        </td>
                                        <td style="text-align:right; width: 4%">
                                            <v-btn @click="addProducts()" dark><v-icon>add</v-icon></v-btn>
                                        </td>
                                    </tr>
                                </table>


                                <v-data-table :headers="headers" :items="subs.products"
                                              hide-actions>
                                    <template v-slot:items="props">
                                        <td class="text-xs-left">{{ props.item.name }}</td>
                                        <td class="text-xs-left">{{ props.item.description }}</td>
                                        <td class="text-xs-left">${{ formatPrice(props.item.price) }}</td>
                                        <td><v-tooltip bottom>
                                        <template v-slot:activator="{ on }">
                                            <v-icon @click="removeProduct(props.item)" v-on="on">cancel</v-icon>
                                        </template><span>Remove Item</span></v-tooltip></td>
                                    </template>

                                    <template v-slot:no-data>
                                        <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                                            No products added to this subscription.
                                        </v-alert>
                                    </template>
                                </v-data-table>

                                <table style="width: 100%;     border-top: 1px solid lightgray;">
                                    <tr>
                                        <td valign="top" style="padding-bottom: 8px; padding-top: 16px; padding-left: 35px"><h3>Subscription Total ({{ subs.frequency.text }}): </h3></td>
                                        <td style="float: right; padding-right: 120px; padding-top: 16px; font-weight: 400; font-size: 13px;"></td>
                                    </tr>
                                </table>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn @click="saveSubscription()" dark>Save Subscription</v-btn>
                        </v-card-actions>

                        <v-dialog dark v-model="confirmSub" persistent max-width="500">
                          <v-card>
                            <v-card-title class="headline">Success!</v-card-title>
                            <v-card-text>Thank you for creating a subscription with Pawkages! Redirecting you to your subscriptions page...
                            <div class="text-xs-center">
                              <v-progress-circular
                                indeterminate
                                color="white"
                              ></v-progress-circular></div></v-card-text>
                          </v-card>
                        </v-dialog>

                        <v-dialog dark v-model="errorDialog" persistent max-width="500">
                          <v-card>
                            <v-card-title class="headline">Error Creating Subscription</v-card-title>
                            <v-card-text>Make sure that you have selected a subscription type and have added at least one (1) recipe or product to your subscription.</v-card-text>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="white" flat @click="errorDialog = false">OK!</v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
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
              user: '',
              recipes: [],
              products: [],
              frequency: '',
              active: ''
            },
            recipes: [],
            products: [],
            selectedSub: null,
            selectedRecipe: null,
            selectedProduct: null,
            errorDialog: false,
            confirmSub: false,
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
            { text: 'Actions', value: 'name', sortable: false }
            ],
        }),
        methods: {
            getData() {
                this.$axios.get('/api/recipes/').then(
                    (response) => {
                        var userRecipes = response.data, currentRecipe, recipeCost;

                        for (var r = 0; r < userRecipes.length; r++) {
                            currentRecipe = userRecipes[r];
                            recipeCost = 0;
                            for (var i = 0; i < currentRecipe.ingredients.length; i++) {
                                recipeCost += currentRecipe.ingredients[i].price;
                            }

                            currentRecipe.price = recipeCost;
                            currentRecipe.text = currentRecipe.name;
                            currentRecipe.value = currentRecipe.id;
                        }

                        this.recipes = userRecipes;
                    }
                )
                this.$axios.get('/api/products/').then(
                    (response) => {
                        var products = response.data;
                        for (var i = 0; i < products.length; i++) {
                            products[i].text = products[i].name;
                            products[i].value = products[i].id;
                        }
                        this.products = products;
                    }
                )
            },
            addRecipe() {
              this.subs.recipes.push(this.selectedRecipe);
            },
            addProducts() {
                this.subs.products.push(this.selectedProduct);
            },
            removeRecipe(recipe) {
              this.subs.recipes.pop(recipe);
            },
            removeProduct(product) {
              this.subs.products.pop(product);
            },
            saveSubscription() {
              var frequency = this.subs.frequency.value;
              var products = this.subs.products;
              var recipes = this.subs.recipes;

              // If frequency is not selected and at least one recipe or product is not chosen - display an error to the user
              if (frequency != undefined && frequency != null) {
                  if (products.length != 0 || recipes.length != 0) {

                      this.subs.active = true;
                      this.subs.frequency = frequency;
                      this.subs.user = this.$cookies.get('user');

                      console.log(this.subs);

                      // API post
                      this.$axios.post('/api/subscriptions/', this.subs).then(
                          (response) => {
                              this.$router.push('/subscriptions/' + response.data.id + '/');
                          })

                  } else {
                  this.errorDialog = true;
                }
              } else {
                this.errorDialog = true;
              }
            },
            formatPrice(value) {
                let val = (value / 1).toFixed(2)
                return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
            }
        },
        beforeMount() {
            this.getData();
        },
  }
</script>

<style lang="sass">
  .product-img
    margin: 2em

  .product-info
    margin-left: 4em
    margin-right: 2em
    margin-bottom: 2em

  .product-desc
    margin: 2em

</style>
