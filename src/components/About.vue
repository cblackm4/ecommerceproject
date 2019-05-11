<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 md9>
          <v-card>
            <v-toolbar dark flat>
              <v-toolbar-title>About Us</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-tooltip right>
              </v-tooltip>
            </v-toolbar>

            <v-img
                  height= "250px"
                  :src="require('@/assets/aboutus.jpg')"
                  class="grey lighten-2"
                >
              </v-img>

            <v-card-text>

              Pet owners often wish to provide their furry family members the same care and consideration that they take in their own diets or have pets with
              special dietary needs and restrictions that make buying food and treats difficult. Our website can help pet owners buy or create custom-made treats
              for their pets. If you are looking for quality dog products,then you are looking at the right direction for we are the company that will always be
              there to cater all your pet needs. We are the company that you can trust for your pets' needs. We promise to deliver you the kind of service that
              you and your pets truly deserve.
              <br/><br />
              If you have any suggestions please let us know through our <router-link :to="{ name: 'Contact', params: { item: route}}">Contact Us</router-link> page
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
  export default {
    data: () => ({
      items: [
        {title:'Home', icon: 'home', route:"/"},
        {title:'Products', icon: 'pets', route:"../products"},
        {title:'Subscriptions', icon: '360', route: '../subscriptions' },
        {title:'Recipes', icon: 'edit', route: '../recipes'},
        {title:'Contact', icon: 'contact_support', route:'../contact'},
        {title:'My Account', icon: 'account_box', route:'../account'},
      ]
    })
  }
</script>
