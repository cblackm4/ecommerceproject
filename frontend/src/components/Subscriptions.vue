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

            <v-data-table :headers="headers" :items="subs" class="elevation-1" hide-actions>
              <template v-slot:items="props">
                <td>{{ props.item.id }}</td>
                <td>{{ props.item.recipes }}</td>
                <td>{{ props.item.products }}</td>
                <td>{{ props.item.frequency }}</td>
                <td>{{ props.item.active }}</td>
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
      headers: [{
          text: 'Subscription ID',
          value: 'id'
        },
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
      ]
    }),
    methods: {
      getSubs() {
        this.$axios.get('/api/subscriptions/').then(
          (response) => {
            this.subs = response.data;
          }
        )
        console.log(this.subs);
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

</style>
