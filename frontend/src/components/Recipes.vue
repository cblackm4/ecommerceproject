<template>
<v-content>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12>
        <v-card class="elevation-12">
            <v-toolbar dark flat>
                <v-toolbar-title>Recipes</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-btn @click="$router.push('/recipeEditor/-1')" flat><v-icon>add</v-icon>Create New Recipe</v-btn>
                <v-tooltip right>
                </v-tooltip>
            </v-toolbar>

          <v-data-table :headers="headers" :items="recipes" class="elevation-1">
            <template v-slot:items="props">
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.name }}</td>
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.description }}</td>
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.pet_size == 'CAT' ? 'Cat' : props.item.pet_size == 'SM' ? 'Small Dog' : props.item.pet_size == 'MD' ? 'Medium Dog' : props.item.pet_size == 'LG' ? 'Large Dog' : '' }}</td>
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
      }
    ],
  }),
  methods: {
    getRecipes() {
      this.$axios.get('/api/recipes/').then(
          (response) => {
              var allRecipes = response.data,
                  userRecipes = [], currentRecipe,
                  currentUser = this.$cookies.get('user');
              
              for (var r = 0; r < allRecipes.length; r++) {
                  currentRecipe = allRecipes[r];
                  if (currentRecipe.user == currentUser) {
                      userRecipes.push(currentRecipe);
                  }
              }

              this.recipes = userRecipes;
              console.log(this.recipes);
        }
      )
    },
    goToRecipe(id) {
      this.$router.push('/recipes/' + id);
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

