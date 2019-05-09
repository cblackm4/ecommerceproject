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
                            </v-toolbar>
                            <v-spacer></v-spacer>
                            <v-tooltip right>
                            </v-tooltip>
                        </v-toolbar>
                        <v-card-text>
                          <v-form>
                            <v-combobox :items="sub_type" label="Subscription Type"></v-combobox>

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

                            <v-data-table :headers="headers" :items="subs.recipes" :key="componentKey"
                                          hide-actions>
                                <template v-slot:items="props">
                                    <td class="text-xs-left">{{ props.item.name }}</td>
                                    <td class="text-xs-left">{{ props.item.description }}</td>
                                    <td class="text-xs-left">${{ props.item.price }}</td>
                                    <td><v-tooltip bottom>
                                    <template v-slot:activator="{ on }">

                                    </template><span>Remove Item</span></v-tooltip></td>
                                </template>

                                <template v-slot:no-data>
                                    <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                                        Select ingredients to add to this recipe
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
                                        <v-btn @click="addRecipe()" dark><v-icon>add</v-icon></v-btn>
                                    </td>
                                </tr>
                            </table>

                            <v-data-table :headers="headers" :items="subs.products" :key="componentKey"
                                          hide-actions>
                                <template v-slot:items="props">
                                    <td class="text-xs-left">{{ props.item.name }}</td>
                                    <td class="text-xs-left">{{ props.item.description }}</td>
                                    <td class="text-xs-left">${{ props.item.price }}</td>
                                    <td><v-tooltip bottom>
                                    <template v-slot:activator="{ on }">

                                    </template><span>Remove Item</span></v-tooltip></td>
                                </template>

                                <template v-slot:no-data>
                                    <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                                        Select ingredients to add to this recipe
                                    </v-alert>
                                </template>
                            </v-data-table>

                            <table style="width: 100%;     border-top: 1px solid lightgray;">
                                <tr>
                                    <td valign="top" style="padding-bottom: 8px; padding-top: 16px; padding-left: 35px"><h3>Recipe Price: </h3></td>
                                    <td style="float: right; padding-right: 120px; padding-top: 16px; font-weight: 400; font-size: 13px;">

                                    </td>
                                </tr>
                            </table>
                          </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn @click="saveSubscription()" dark>Save Subscription</v-btn>
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
            recipes: [],
            products: [],
            newSub: true,
            componentKey: 0,
            selectedRecipe: null,
            selectedProduct: null,
            sub_type: [
              {
                text: '30 Days',
                value: 'thirty_days'
              },
              {
                text: '6 Months',
                value: 'six_months'
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
            getSubs() {
                this.$axios.get('/api/subscriptions/').then(
                    (response) => {
                        this.subs = response.data;
                    }
                )
                this.$axios.get('/api/recipes/').then(
                    (response) => {
                        this.recipes = response.data;
                        console.log(this.recipes);
                    }
                )
                this.$axios.get('/api/products/').then(
                    (response) => {
                        this.products = response.data;
                        console.log(this.products);
                    }
                )
            },
            addRecipe() {
              this.subs.recipes.push(this.selectedRecipe);
            },
            addProducts() {
              this.subs.products.push(this.selectedProduct);
            }
        },
        beforeMount() {
            this.getSubs();
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
