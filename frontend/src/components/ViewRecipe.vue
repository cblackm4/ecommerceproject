
<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex xs12 sm12 md4>
                    <v-card class="elevation-12">
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
                                <table style="width: 100%">
                                    <tr>
                                        <td>Pet Size: </td>
                                        <td>{{recipe.pet_size == 'CAT' ? 'Cat' : recipe.pet_size == 'SM' ? 'Small Dog' : recipe.pet_size == 'MD' ? 'Medium Dog' : recipe.pet_size == 'LG' ? 'Large Dog' : ''}}</td>
                                    </tr>
                                    <tr>
                                        <td>Description: </td>
                                        <td>{{recipe.description}}</td>
                                    </tr>
                                </table>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn dark>Edit Recipe</v-btn>
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
      recipe: {},
    }),
    methods: {
      getRecipe() {
        this.$axios.get('/api/recipes/' + this.$route.params.id + '/').then(
          (response) => {
            this.recipe = response.data;
          }
        )
      },
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
