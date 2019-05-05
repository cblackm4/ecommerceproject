
<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex xs12 md9>
                    <v-card>
                        <v-toolbar dark flat>
                            <v-toolbar dark flat>
                                <v-toolbar-title>{{recipe.name}}</v-toolbar-title>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-btn @click="$router.push('/recipes/')" flat><v-icon>keyboard_arrow_left</v-icon>Back to Recipes</v-btn>
                                <v-tooltip right>
                                </v-tooltip>
                            </v-toolbar>
                            <v-spacer></v-spacer>
                            <v-tooltip right>
                            </v-tooltip>
                        </v-toolbar>
                        <v-card-text>
                            <v-form>

                                <table style="width: 100%; padding-left: 20px; padding-top: 8px; font-family: Roboto;">
                                    <tr>
                                        <td valign="top"  style="padding-bottom: 16px"><h3>Pet Size: </h3></td>
                                        <td valign="top" >{{recipe.pet_size == 'CAT' ? 'Cat' : recipe.pet_size == 'SM' ? 'Small Dog' : recipe.pet_size == 'MD' ? 'Medium Dog' : recipe.pet_size == 'LG' ? 'Large Dog' : ''}}</td>
                                    </tr>
                                    <tr>
                                        <td valign="top" style="padding-bottom: 8px; width: 120px"><h3>Description: </h3></td>
                                        <td valign="top">{{recipe.description}}</td>
                                    </tr>
                                    <tr>
                                        <td style="padding-top: 8px"><h3>Ingredients </h3></td>
                                        <td></td>
                                    </tr>
                                </table>
                                <v-data-table :headers="headers" :items="recipe.ingredients" :show-pagination="false" hide-actions>
                                    <template v-slot:items="props">
                                        <td><img class="product-image" :src="props.item.img_src" /></td>
                                        <td class="text-xs-left">{{ props.item.name }}</td>
                                        <td class="text-xs-left">{{ props.item.description }}</td>
                                        <td class="text-xs-left">${{ props.item.price }}</td>
                                    </template>

                                    <template v-slot:no-data>
                                        <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                                           There are no ingredients saved for this recipe
                                        </v-alert>
                                    </template>
                                </v-data-table>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn dark @click="DeleteRecipe()" ><v-icon>delete</v-icon>Delete</v-btn>
                            <v-btn dark @click="EditRecipe()">Edit Recipe</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
        <v-snackbar v-model="snackbar"
                    :timeout="5000"
                    color="green"
                    bottom
                    right>
            {{snackbarMessage}}
            <v-btn @click="snackbar = false;"
                   flat>
                Close
            </v-btn>
        </v-snackbar>
    </v-content>
</template>

<script>
  export default {
        data: () => ({
            recipe: {},
            headers: [{
                text: 'Image',
                value: 'img_src',
                sortable: false
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
            ],
            snackbar: false,
            snackbarMessage: "",
        }),
        methods: {
            getRecipe() {
                this.$axios.get('/api/recipes/' + this.$route.params.id + '/').then(
                    (response) => {
                        this.recipe = response.data;
                    }
                )
            },
            DeleteRecipe() {
                this.$axios.delete('/api/recipes/' + this.$route.params.id + '/').then(
                    () => {
                        this.snackbarMessage = "Recipe Deleted";
                        this.snackbar = true;
                        this.$router.push('/recipes/');
                    }
                );
            },
            EditRecipe() {
                this.$router.push('/recipeEditor/'+ this.$route.params.id + '/');
            }
        },
    beforeMount() {
      this.getRecipe();
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
