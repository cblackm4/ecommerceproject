<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      fixed
      temporary
    >
      <v-list class="pa-1">
        <v-list-tile avatar>
          <v-list-tile-avatar>
            <v-icon>person</v-icon>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>{{user.username}}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <v-list class="pt-0" dense>
        <v-divider></v-divider>
          <v-list-tile
            v-for="item in items"
            :key="item.title"
            avatar
            :to="item.route">

            <v-list-tile-avatar>
              <v-icon>{{item.icon}}</v-icon>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{item.title}}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile
            v-if="user.is_staff"
            :key="'Administration'"
            avatar
            :to="'Administration'">
            <v-list-tile-avatar>
              <v-icon>supervisor_account</v-icon>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>Administration</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <v-toolbar dark fixed>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-img :src="require('./assets/logo.png')" max-width="175px" max-height="175px" min-width="150px" min-heigh="150px"></v-img>
      <v-spacer></v-spacer>
      <!--Ideally, a v-if will be used to see if a user gave us a first name. If not it will default to the user name-->
      <v-toolbar-title>Hello, {{user.first_name}}!<v-icon class="icon">account_circle</v-icon></v-toolbar-title>
      <v-icon>shopping_cart</v-icon>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn href="/accounts/logout/" flat>LOGOUT</v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-parallax xs12 :src="require('./assets/heroimage.jpg')">
      <v-layout align-center column justify-center>
        <h1 class="display-2 font-weight-thin mb-3">Welcome to Pawkages!</h1>
        <v-btn dark flat href="#/Products">Shop Now</v-btn>
      </v-layout>
    </v-parallax>

    <v-content>
      <router-view></router-view>
    </v-content>

    <v-footer dark height="auto">
      <v-layout row wrap justify-center>
        <v-flex xs4 md3>
          <v-card-text>
            <div class="text-xs-center">
              <v-img :src="require('./assets/logo.png')" max-width="250px" max-height="250px" min-width="150px" min-heigh="150px"></v-img>
            </div>
          </v-card-text>
        </v-flex>

        <v-flex xs4 md3>
          <v-card-text>
            <div class="text-xs-center">
              Quick Links
            </div>
            <span>COMPANY:</span><br />
            <div
              v-for="(link, index) in links"
              :key="'link' + index"
            >{{ link.name }}</div>
          </v-card-text>
        </v-flex>

        <v-flex xs4 md3>
            <v-card-text>
              <div class="text-xs-center">
                Follow Us:
              </div>
              <div class="text-xs-center">
                <v-btn
                  v-for="(icon, index) in icons"
                  :key="'icon' + index"
                  class="mx-3 white--text"
                  icon
                >
                  <v-icon size="24px">{{ icon.src }}</v-icon>
                </v-btn>
              </div>
            </v-card-text>
        </v-flex>
      </v-layout>
    </v-footer>

  </v-app>
</template>

<script>

export default {
  name: 'App',
  components: {

  },
  data () {
    return {
      /* To add a new page to the toolbar, first import in router.js then add a new
      * array item with the name and route parameters.
      * Name: the name that will displayed in the toolbar
      * Route: the name of the component that needs to be routed
      */
      drawer: false,
      items: [
        {title:'Home', icon: 'home', route:"/"},
        {title:'Products', icon: 'pets', route:"Products"},
        {title:'Subscriptions', icon: '360', route: 'Subscriptions'},
        {title:'Contact', icon: 'contact_support', route:'Contact'},
        {title:'My Account', icon: 'account_box', route:'Account'},
      ],
      icons: [
        {src:'fab fa-facebook'},
        {src:'fab fa-twitter'},
        {src:'fab fa-instagram'}
      ],
      links: [
        {name: 'About Us'},
        {name: 'Contact Us'},
        {name: 'Shop'}
      ]
    }
  },
  computed: {
    user() {
      return this.$store.getters.user;
    }
  },
  methods: {
    getUser() {
      this.$axios.get('/api/users/' + this.$cookies.get('user') + '/').then(
        (response) => {
          const r = response.data;
          this.$store.commit('setUser', r);
        }
      )
    },
  },
  beforeMount() {
    this.getUser();
  },
}
</script>

<style lang="sass">

  .icon
    margin-right: 10px
    margin-left: 10px

  .shop a
    color: white

  .shop a:visited
    color: white

</style>
