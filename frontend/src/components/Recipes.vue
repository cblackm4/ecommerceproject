<template>
<v-content>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 md9>
        <v-card>
            <v-toolbar dark flat>
                <v-toolbar-title>Recipes</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-text-field v-model="search" append-icon="search" label="Search Recipes" single-line hide-details></v-text-field>
                <v-btn @click="$router.push('/recipeEditor/-1')" flat><v-icon>add</v-icon>Create New Recipe</v-btn>
                <v-tooltip right>
                </v-tooltip>
            </v-toolbar>

          <v-data-table :headers="headers" :items="recipes" :search="search" class="elevation-1" hide-actions>
            <template v-slot:items="props">
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.name }}</td>
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.description }}</td>
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.pet_size == 'CAT' ? 'Cat' : props.item.pet_size == 'SM' ? 'Small Dog' : props.item.pet_size == 'MD' ? 'Medium Dog' : props.item.pet_size == 'LG' ? 'Large Dog' : '' }}</td>
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">${{ formatPrice(props.item.cost) }}</td>
            </template>

            <template v-slot:no-results>
              <v-alert :value="true" color="error" icon="warning">
                Your search for "{{ search }}" found no results.
              </v-alert>
            </template>

            <template v-slot:no-data>
                <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                    You don't have any recipes saved yet.
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
    recipes: [],
    search: '',
    headers: [{
        text: 'Recipe Title',
        value: 'name'
      },
      {
        text: 'Description',
        value: 'description'
      },
      {
        text: 'Pet Size',
        value: 'pet_size'
      },
      {
        text: 'Recipe Cost',
        value: 'cost'
      }
    ],
  }),
        methods: {
            getRecipes() {
                this.$axios.get('/api/recipes/').then(
                    (response) => {
                        var userRecipes = response.data, currentRecipe, recipeCost;

                        for (var r = 0; r < userRecipes.length; r++) {
                            currentRecipe = userRecipes[r];
                            recipeCost = 0;
                            for (var i = 0; i < currentRecipe.ingredients.length; i++) {
                                recipeCost += currentRecipe.ingredients[i].price;
                            }

                            currentRecipe.cost = recipeCost;
                        }

                        this.recipes = userRecipes;
                    }
                )
            },
            goToRecipe(id) {
                this.$router.push('/recipes/' + id);
            },
            formatPrice(value) {
                let val = (value / 1).toFixed(2)
                return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
            }
        },
  beforeMount() {
    this.getRecipes();
  },
}
</script>

<style lang="sass">
  .product-image
    padding: 1em
    max-width: 12.5em
    max-height: 12.5em
</style>
