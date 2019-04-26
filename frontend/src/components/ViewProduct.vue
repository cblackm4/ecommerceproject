<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12>
          <v-card>
            <v-toolbar dark flat>
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
    },
    beforeMount() {
      this.getProduct();
    },
  }
</script>

<style lang="sass">



</style>
