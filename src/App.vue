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
        <router-link to="/" style="text-decoration: none !important">
            <v-img :src="require('./assets/logo.png')" max-width="175px" max-height="175px" min-width="150px" min-heigh="150px"></v-img>
        </router-link>
        <v-spacer></v-spacer>
        <!--Ideally, a v-if will be used to see if a user gave us a first name. If not it will default to the user name-->
        <v-toolbar-title>
            Hello, {{user.first_name}}!
            <router-link to="/account" style="text-decoration: none !important">
                <v-icon class="icon">account_circle</v-icon>
            </router-link>
        </v-toolbar-title>
        <router-link to="/cart" style="text-decoration: none !important; padding-right: 10px">
            <v-badge right v-model="show">
                <template v-slot:badge>
                    <span>{{cart.products.length + cart.recipes.length}}</span>
                </template>
                <v-icon>shopping_cart</v-icon>
            </v-badge>
        </router-link>
        <v-toolbar-items class="hidden-sm-and-down">
            <v-btn href="/accounts/logout/" flat>LOGOUT</v-btn>
        </v-toolbar-items>
    </v-toolbar>

    <v-parallax xs12 :src="require('./assets/heroimage.jpg')">
      <v-layout align-center column justify-center>
        <h1 class="display-2 font-weight-thin mx-auto">Welcome to Pawkages!</h1>
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
              <router-link :to="{ name: 'Home', params: { items: route}}"><v-img :src="require('./assets/logo.png')" max-width="250px" max-height="250px" min-width="150px" min-heigh="150px"></v-img></router-link>
            </div>
          </v-card-text>
        </v-flex>

        <v-flex xs4 md3>
          <v-card-text>
            <div class="text-xs-center">
              Quick Links
            </div>
            <span>COMPANY:</span><br />
            <v-list-tile
              dense
              v-for="link in links"
              :key="link.name"
              :to="link.route">
              <span>{{ link.name }}</span>
            </v-list-tile>
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
                  <div class="social-footer">
                    <a :href="icon.url" :target="icon.target"><v-icon size="24px">{{ icon.src }}</v-icon></a>
                  </div>
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
      route: '',
      items: [
        {title:'Home', icon: 'home', route:"/"},
        {title:'Products', icon: 'pets', route:"../products"},
        {title:'Subscriptions', icon: '360', route: '../subscriptions' },
        {title:'Recipes', icon: 'edit', route: '../recipes'},
        {title:'Contact', icon: 'contact_support', route:'../contact'},
        {title:'My Account', icon: 'account_box', route:'../account'},
      ],
      icons: [
        {
          src:'fab fa-facebook',
          url: 'https://www.facebook.com/',
          target: '_blank'
        },
        {
          src:'fab fa-twitter',
          url: 'https://www.twitter.com/',
          target: '_blank'
        },
        {
          src:'fab fa-instagram',
          url: 'https://www.instgram.com/',
          target: '_blank'
        }
      ],
      links: [
        {
          name: 'About Us',
          route: '../about'
        },
        {
          name: 'Contact Us',
          route: '../contact'
        },
        {
          name: 'Shop',
          route: '../products'
        }
      ]
    }
  },
        computed: {
            user() {
                return this.$store.getters.user;
            },
            cart() {
                return this.$store.getters.cart;
            },
            show() {
                return (this.$store.getters.cart.products.length + this.$store.getters.cart.recipes.length) > 0;
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
    this.$axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    this.$axios.defaults.xsrfCookieName = "csrftoken";
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

  .social-footer a
    color: white
    opacity: 0.7
    text-decoration: none

  .social-footer a:visited
    color: white

  .social-footer a:hover
    opacity: 1.0

</style>
