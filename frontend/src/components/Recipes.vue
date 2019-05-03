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
            <v-text-field v-model="search" append-icon="search" label="Search Recipes" single-line hide-details></v-text-field>

            <v-tooltip right>
            </v-tooltip>
          </v-toolbar>

          <v-data-table :headers="headers" :items="recipes" :search="search" class="elevation-1">
            <template v-slot:items="props">
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.name }}</td>
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.description }}</td>
              <td @click="goToRecipe(props.item.id)" class="text-xs-left">{{ props.item.pet_size == 'CAT' ? 'Cat' : props.item.pet_size == 'SM' ? 'Small Dog' : props.item.pet_size == 'MD' ? 'Medium Dog' : props.item.pet_size == 'LG' ? 'Large Dog' : '' }}</td>
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
          this.recipes = response.data;
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

