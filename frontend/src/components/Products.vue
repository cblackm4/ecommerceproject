<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>Products</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>

            <v-data-table
              :headers="headers"
              :items="products"
              class="elevation-1"
            >
              <template v-slot:items="props">
                <td @click="goToProduct(props.item.id)"><img class="product-image" :src="props.item.image_src"/></td>
                <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.name }}</td>
                <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.description }}</td>
                <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.price }}</td>
                <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.inventory }}</td>
              </template>
            </v-data-table>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    data: () => ({
      products: [
        {
          id: 1,
          image_src: 'https://images-na.ssl-images-amazon.com/images/I/71W3BtGim9L._SL1300_.jpg',
          name: 'Milk-Bone Original Dog Treats',
          description: 'Contains 1 - 10 Lb Box Crunchy Texture Helps To Clean Teeth And Freshen Breath Fortified With 12 Vitamins And Minerals To Help Keep Dogs At Their BestWholesome, Tasty Treats That You Can Feel Good About Giving',
          price: 11.93,
          inventory: 10
        }
      ],
      headers: [
        { text: 'Image', value: 'image_src'},
        { text: 'Name', value: 'name'},
        { text: 'Description', value: 'description'},
        { text: 'Price', value: 'price'},
        { text: 'Quantity', value: 'inventory'},
      ],
    }),
    methods: {
      getProducts() {
        this.$axios.get('/api/products/').then(
          (response) => {
            this.products = response.data;
          }
        )
      },
      goToProduct(id) {
        this.$router.push('/products/' + id);
      }
    },
    beforeMount() {
      this.getProducts();
    },
  }
</script>

<style lang="sass">

  .product-image
    max-width: 200px
    max-height: 200px

</style>