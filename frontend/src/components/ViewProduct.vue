<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 md9>
          <v-card>
            <v-toolbar dark flat>
              <v-toolbar-title>{{product.name}}</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn @click="$router.push('/products/')" flat><v-icon>keyboard_arrow_left</v-icon>Back to Products</v-btn>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>

            <v-layout row wrap align-end>
              <v-flex xs12 md4>
                <v-card class="product-img">
                  <v-img :src="product.img_src"/>
                </v-card>
              </v-flex>

              <v-flex xs12 md8>
                <v-card class="product-info">
                  <v-card-title>Product Information</v-card-title>
                  <v-card-text>
                    <table>
                      <tr>
                        <th>{{product.name}}</th>
                      </tr>
                      <tr>
                        <td>${{product.price}}</td>
                      </tr>
                      <tr>
                        <td>{{product.inventory > 0 ? 'Instock: ' + product.inventory + ' left' : 'Out of Stock'}}</td>
                      </tr>
                    </table>
                    <v-btn dark @click="addToCart()">Add to Cart</v-btn>
                    <v-btn dark @click="$router.push('/Subscriptions')">Create A Subscription</v-btn>
                  </v-card-text>
                </v-card>
              </v-flex>

              <v-flex xs12 md12>
                <v-card class="product-desc">
                  <v-card-title>Product Description</v-card-title>
                  <v-card-text>
                    {{product.description}}
                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    data: () => ({
      product: {},
    }),
        methods: {
            getProduct() {
                this.$axios.get('/api/products/' + this.$route.params.id + '/').then(
                    (response) => {
                        this.product = response.data;
                    }
                )
            },
            addToCart() {
                var cartItems = this.$store.getters.cart,
                    cart = {};

                var products = cartItems.products;
                if (!products.includes(this.$route.params.id)) {
                    products.push(this.$route.params.id);
                }

                cart.products = products;
                cart.recipes = cartItems.recipes;

                this.$store.commit('setCart', cart);
            }
        },
    beforeMount() {
      this.getProduct();
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
