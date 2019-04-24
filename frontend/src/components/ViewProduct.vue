<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>{{product.name}}</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn @click="$router.push('/products/')" flat><v-icon>keyboard_arrow_left</v-icon>Back to Products</v-btn>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>

            

          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    data: () => ({
      product: {
        id: 1,
        image_src: 'https://images-na.ssl-images-amazon.com/images/I/71W3BtGim9L._SL1300_.jpg',
        name: 'Milk-Bone Original Dog Treats',
        description: 'Contains 1 - 10 Lb Box Crunchy Texture Helps To Clean Teeth And Freshen Breath Fortified With 12 Vitamins And Minerals To Help Keep Dogs At Their BestWholesome, Tasty Treats That You Can Feel Good About Giving',
        price: 11.93,
        inventory: 10
      }
    }),
    methods: {
      getProduct() {
        this.$axios.get('/api/products/' + this.$route.params.id + '/').then(
          (response) => {
            this.product = response.data;
          }
        )
      },
    },
    beforeMount() {
      this.getProduct();
    },
  }
</script>

<style lang="sass">



</style>