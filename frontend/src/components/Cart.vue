<template>
<v-content>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 md9>
          <v-card>
              <v-toolbar dark flat>
                  <v-toolbar-title>Cart</v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-spacer></v-spacer>
                  <v-spacer></v-spacer>
                  <v-spacer></v-spacer>
                  <v-spacer></v-spacer>
                  <v-tooltip right>
                  </v-tooltip>
              </v-toolbar>
              <v-data-table :headers="headers" :items="allItems" class="elevation-1" :key="componentKey" hide-actions>
                  <template v-slot:items="props">
                      <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.name }}</td>
                      <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.description }}</td>
                      <td @click="goToRecipe(props.item.id)" class="text-xs-left">${{ props.item.price }}</td>
                      <td>
                          <v-tooltip bottom>
                              <template v-slot:activator="{ on }">
                                  <v-icon @click="removeItem(props.item)" v-on="on">cancel</v-icon>
                              </template><span>Remove Item</span>
                          </v-tooltip>
                      </td>
                  </template>

                  <template v-slot:no-data>
                      <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                          You don't have any recipes in your cart.
                      </v-alert>
                  </template>
              </v-data-table>
              <table style="width: 100%;">
                  <tr>
                      <td valign="top" style="padding-bottom: 8px; padding-top: 16px; padding-left: 35px"><h3>Subtotal: </h3></td>
                      <td style="float: right; padding-right: 108px; padding-top: 16px; font-weight: 400; font-size: 13px;">
                          ${{ subtotal }}
                      </td>
                  </tr>
              </table>
              <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn dark>Proceed to Checkout</v-btn>
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
            cartItems: { products: [], recipes: [] },
            allItems: [],
            subtotal: 0,
            search: '',
            headers: [{
                text: 'Name',
                value: 'name',
                sortable: false
            },
            {
                text: 'Description',
                value: 'description',
                sortable: false
            },
            {
                text: 'Price',
                value: 'price',
                sortable: false
            },
            { text: 'Remove', value: '', sortable: false }
        ],
            componentKey: 0,
        }),
        methods: {
            getCart() {
                this.subtotal = 0.0;
                this.allItems = [];

                var subTotal = 0;
                if (this.$cookies.get('cart') != null && this.$cookies.get('cart') != undefined) {
                    this.cartItems = this.$cookies.get('cart');
                }
                else {
                    this.cartItems = { products: [], recipes: [] };
                    this.$cookies.set('cart', this.cartItems);
                }

                this.$axios.get('/api/recipes/').then(
                    (response) => {
                        var userRecipes = response.data,
                            currentRecipe, cartRecipe,
                            recipeCost;

                        for (var r = 0; r < userRecipes.length; r++) {
                            currentRecipe = userRecipes[r];
                            recipeCost = 0;
                            for (var i = 0; i < currentRecipe.ingredients.length; i++) {
                                recipeCost += currentRecipe.ingredients[i].price;
                            }

                            currentRecipe.price = recipeCost.toFixed(2);
                            currentRecipe.isRecipe = true;
                        }

                        subTotal = 0;
                        for (var i = 0; i < this.cartItems.recipes.length; i++) {
                            cartRecipe = this.cartItems.recipes[i];
                            for (var r = 0; r < userRecipes.length; r++) {
                                currentRecipe = userRecipes[r];
                                if (currentRecipe.id == cartRecipe) {
                                    subTotal += currentRecipe.price;
                                    this.allItems.push(currentRecipe);
                                }
                            }
                        }
                        this.subtotal += parseFloat(subTotal);
                    }
                )

                this.$axios.get('/api/products/').then(
                    (response) => {
                        var products = response.data,
                            cartProduct, currentProduct;

                        subTotal = 0;
                        for (var i = 0; i < this.cartItems.products.length; i++) {
                            cartProduct = this.cartItems.products[i];
                            for (var r = 0; r < products.length; r++) {
                                currentProduct = products[r];
                                if (currentProduct.id == cartProduct) {
                                    subTotal += currentProduct.price;
                                    currentProduct.isRecipe = false;
                                    this.allItems.push(currentProduct);
                                }
                            }
                        }
                        this.subtotal += parseFloat(subTotal);
                    }
                )
            },
            removeItem(removedItem) {
                // first remove the cart cookie
                this.$cookies.remove('cart');

                // remove the item from the object to be stored in the cookie
                var cart = {}, newRecipes = [], newProducts = [];
                if (removedItem.isRecipe) {
                    newProducts = this.cartItems.products;
                    for (var i = 0; i < this.cartItems.recipes.length; i++) {
                        if (this.cartItems.recipes[i] != removedItem.id) {
                            newRecipes.push(this.cartItems.recipes[i]);
                        }
                    }
                }
                else {
                    newRecipes = this.cartItems.recipes;
                    for (var i = 0; i < this.cartItems.products.length; i++) {
                        if (this.cartItems.products[i] != removedItem.id) {
                            newProducts.push(this.cartItems.products[i]);
                        }
                    }
                }

                // Reset the cookie
                cart.products = newProducts;
                cart.recipes = newRecipes;

                console.log(cart);
                this.$cookies.set('cart', cart);

                this.componentKey += 1;
                this.getCart();
            }
        },
  beforeMount() {
    this.getCart();
  },
}
</script>

<style lang="sass">
  .product-image
    padding: 1em
    max-width: 12.5em
    max-height: 12.5em
</style>
