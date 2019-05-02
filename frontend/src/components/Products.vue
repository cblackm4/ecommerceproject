<template>
<v-content>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12>
        <v-card class="elevation-12">
          <v-toolbar dark flat>
            <v-toolbar-title>Products</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-text-field v-model="search" append-icon="search" label="Search Product" single-line hide-details></v-text-field>

            <v-tooltip right>
            </v-tooltip>
          </v-toolbar>



          <v-data-table :headers="headers" :items="products" :search="search" class="elevation-1">
            <template v-slot:items="props">
              <td @click="goToProduct(props.item.id)"><img class="product-image" :src="props.item.img_src" /></td>
              <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.name }}</td>
              <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.description }}</td>
              <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.price }}</td>
              <td @click="goToProduct(props.item.id)" class="text-xs-right">{{ props.item.inventory }}</td>
            </template>

            <template v-slot:no-results>
         <v-alert :value="true" color="error" icon="warning">
           Your search for "{{ search }}" found no results.
         </v-alert>

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
    products: [],
    search: '',
    headers: [{
        text: 'Image',
        value: 'img_src'
      },
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
        text: 'Quantity',
        value: 'inventory'
      },
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
    padding: 1em
    max-width: 12.5em
    max-height: 12.5em
</style>
