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
                        <td></td>
                        <td>{{ props.item.frequency }}</td>
                        <td>{{ props.item.active }}</td>
                    </template>
                </v-data-table>

                <v-data-table :headers="headers" :items="subs" class="elevation-1" hide-actions>
                        <template v-slot:items="props">
                            <td>{{ props.item.id }}</td>
                            <td>{{ props.item.frequency }}</td>
                            <td>

                                <v-data-table :headers="productHeaders" :items="props.item.products" hide-actions>
                                    <template v-slot:items="product_props">
                            <td @click="goToProduct(props.item.id)"><img class="product-image" :src="props.item.img_src" /></td>
                            <td @click="goToProduct(props.item.id)" class="text-xs-left">{{ product_props.item.name }}</td>
                            <td @click="goToProduct(props.item.id)" class="text-xs-left">{{ product_props.item.description }}</td>
                            <td @click="goToProduct(props.item.id)" class="text-xs-left">{{ product_props.item.price }}</td>
                            <td @click="goToProduct(props.item.id)" class="text-xs-left">{{ product_props.item.inventory }}</td>

                        </template>
                    </v-data-table>
                </td>
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
            ],
            productHeaders: [
                {
                    text: 'Image',
                    value: 'img_src'
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
                {
                    text: 'Quantity',
                    value: 'inventory'
                },
            ],
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

</style>
