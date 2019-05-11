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
            <v-layout row wrap align-center justify-center>
              <v-flex xs12 md9>
                <v-card class="product-img">
                    <div>
                        Subtotal: ${{ formatPrice(subtotal) }}
                        <v-spacer></v-spacer>
                        Tax (8.25%): ${{ formatPrice(subtotal*0.825) }}
                        <v-spacer></v-spacer>
                        Shipping: FREE
                        <v-spacer></v-spacer>
                        Grand Total: ${{ formatPrice(subtotal + (subtotal*0.825)) }}
                    </div>
                </v-card>
              </v-flex>
            </v-layout>
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
        data: () => ({
            cartItems: { products: [], recipes: [] },
            allItems: [],
            subtotal: 0,
            user: null,
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
            }
            ],
            componentKey: 0,
        }),
        methods: {
            getCart() {
                this.user = this.$store.getters.user;
                this.subtotal = 0.0;
                this.allItems = [];

                var subTotal = 0;
                this.cartItems = this.$store.getters.cart;
                this.show = (this.cartItems.products.length + this.cartItems.recipes.length) > 0;

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

                            currentRecipe.price = recipeCost;
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
            formatPrice(value) {
                let val = (value / 1).toFixed(2)
                return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
            }
        },
  beforeMount() {
    this.getCart();
  },
}
</script>

<style>
</style>
