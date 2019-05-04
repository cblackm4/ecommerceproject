
<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex xs12 md9>
                    <v-card>
                        <v-toolbar dark flat>
                            <v-toolbar dark flat>
                                <v-toolbar-title>{{newRecipe ? 'Create a New Recipe' : 'Edit ' + recipe.name}}</v-toolbar-title>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                                <v-tooltip right>
                                </v-tooltip>
                            </v-toolbar>
                            <v-spacer></v-spacer>
                            <v-tooltip right>
                            </v-tooltip>
                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-text-field name="name" label="Enter a Recipe Name" type="text" v-model="recipe.name"></v-text-field>
                                <v-combobox :items="pet_sizes"
                                            v-model="recipe.pet_sizeName"
                                            label="Select a Pet Size">
                                </v-combobox>
                                <v-textarea name="input-7-1"
                                            label="Add a Recipe Description"
                                            v-model="recipe.description">
                                </v-textarea>
                                <table style="width: 100%">
                                    <tr>
                                        <td>
                                            <v-combobox :items="ingredients"
                                                        :key="ingredients.name"
                                                        v-model="selectedIngredient"
                                                        label="Select an Ingredient to add">
                                            </v-combobox>
                                        </td>
                                        <td style="text-align:right; width: 4%">
                                            <v-btn @click="AddIngredient()" dark><v-icon>add</v-icon></v-btn>
                                        </td>
                                    </tr>
                                </table>
                                <v-data-table :headers="headers" :items="recipe.ingredients" :key="componentKey"
                                              hide-actions>
                                    <template v-slot:items="props">
                                        <td><img class="product-image" :src="props.item.img_src" /></td>
                                        <td class="text-xs-left">{{ props.item.name }}</td>
                                        <td class="text-xs-left">{{ props.item.description }}</td>
                                        <td class="text-xs-left">${{ props.item.price }}</td>
                                        <td class="text-xs-left">
                                            <v-icon @click="removeIngredient(props.item)">
                                                delete
                                            </v-icon>
                                        </td>
                                    </template>

                                    <template v-slot:no-data>
                                        <v-alert :value="true" color="transparent" style="color: rgba(0,0,0,0.54)">
                                            Select ingredients to add to this recipe
                                        </v-alert>
                                    </template>
                                </v-data-table>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn @click="SaveRecipe()" dark>Save Recipe</v-btn>
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
            ingredients: [],
            newRecipe: true,
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
            { text: 'Actions', value: 'name', sortable: false }
            ],
            pet_sizes: [{
                text: 'Cat',
                value: 'CAT'
            },
            {
                text: 'Small Dog',
                value: 'SM'
            },
            {
                text: 'Medium Dog',
                value: 'MD'
            },
            {
                text: 'Large Dog',
                value: 'LG'
            },
            ],
            snackbar: false,
            snackbarMessage: "",
            selectedIngredient: null,
            componentKey: 0,
        }),
        methods: {
            getRecipe() {
                this.$axios.get('/api/ingredients/').then(
                    (response) => {
                        var ingredientVal = response.data;
                        for (var i = 0; i < ingredientVal.length; i++) {
                            ingredientVal[i].text = ingredientVal[i].name;
                            ingredientVal[i].value = ingredientVal[i].id;
                        }
                        this.ingredients = ingredientVal;
                    }
                )

                if (this.$route.params.id != -1) {
                    this.newRecipe = false;
                    this.$axios.get('/api/recipes/' + this.$route.params.id + '/').then(
                        (response) => {
                            this.recipe = response.data;
                            for (var i = 0; i < this.pet_sizes.length; i++) {
                                if (this.pet_sizes[i].value == this.recipe.pet_size) {
                                    this.recipe.pet_sizeName = this.pet_sizes[i].text;
                                }
                            }
                        }
                    )
                }
                else {
                    this.recipe.ingredients = [];
                }
            },
            SaveRecipe() {
                if (this.recipe.pet_sizeName.value != undefined && this.recipe.pet_sizeName.value != null) {
                    this.recipe.pet_size = this.recipe.pet_sizeName.value;
                }
                if (!this.newRecipe) {

                    this.$axios.put('/api/recipes/' + this.$route.params.id + '/', this.recipe, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                        .then(response => {
                            this.$router.push('/recipes/' + response.data.id + '/');
                        })
                }
                else {
                    this.recipe.user = this.$cookies.get('user');

                    this.$axios.post('/api/recipes/', this.recipe, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                        .then(response => {
                            this.$router.push('/recipes/' + response.data.id + '/');
                        })
                }
            },
            AddIngredient() {
                this.recipe.ingredients.push(this.selectedIngredient);
                this.componentKey += 1;
            },
            removeIngredient(ingredient) {
                var existingIngredients = this.recipe.ingredients,
                    newIngredients = [];

                for (var i = 0; i < existingIngredients.length; i++) {
                    if (existingIngredients[i].id != ingredient.id) {
                        newIngredients.push(existingIngredients[i]);
                    }
                }
                this.recipe.ingredients = newIngredients;
                this.componentKey += 1;
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
