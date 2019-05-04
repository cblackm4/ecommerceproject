<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 md9>

            <v-card>
                <v-toolbar dark flat>
                    <v-toolbar-title>Subscriptions</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-spacer></v-spacer>
                    <v-spacer></v-spacer>
                    <v-spacer></v-spacer>
                    <v-spacer></v-spacer>
                </v-toolbar>

                <v-data-table :headers="headers" :items="subs"  class="elevation-1" hide-actions>
                        <template v-slot:items="props" >
                            <td>
                              <v-data-table  :items="props.item.recipes" hide-actions hide-headers dense>
                                <template v-slot:no-data>
                                    <div>
                                      <v-icon>warning</v-icon> Not Subscribed to any Recipes
                                    </div>
                                </template>
                                <template v-slot:items="recipe_props">
                                  <td>{{ recipe_props.item.name }}</td>
                                </template>
                              </v-data-table>
                            </td>
                            <td>
                              <v-data-table  :items="props.item.products" hide-actions hide-headers dense>
                                <template v-slot:no-data>
                                  <div>
                                    <v-icon>warning</v-icon> Not Subscribed to any Products
                                  </div>
                                </template>
                                <template v-slot:items="product_props">
                                  <td>{{ product_props.item.name }}</td>
                                </template>
                              </v-data-table>
                            </td>
                            <td>{{ props.item.frequency | format }}</td>
                            <td>{{ props.item.active }}</td>
                            <td>
                              <v-btn dark @click="goToSub(props.item.id)">Edit</v-btn>
                            </td>
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
            subs: [],
            products: [],
            recipes: [],
            headers: [
              {
                text: 'Recipes',
                value: 'recipes'
              },
              {
                text: 'Products',
                value: 'products'
              },
              {
                text: 'Subscription Length',
                value: 'frequency'
              },
              {
                text: 'Active?',
                value: 'active'
              },
              {
                text: '',
                value: 'edit'
              }
            ],
            // Apply filter to frequency field -- needs more work? Currently doesn't work
            filters: {
              format: function (value) {
                if (!value) return ''
                value = value.toString()
                return value.charAt(0).toUpperCase() + "days"
              }
            }
        }),
        methods: {
            getSubs() {
                this.$axios.get('/api/subscriptions/').then(
                    (response) => {
                        this.subs = response.data;
                        console.log(this.subs);
                    }
                )
            },
            goToSub(id) {
                this.$router.push('/subscriptions/' + id);
            }
        },
        beforeMount() {
            this.getSubs();
        },
    }
</script>

<style>
  tbody tr:nth-of-type(odd) {
   background-color: rgba(0, 0, 0, .05);
  }
</style>
