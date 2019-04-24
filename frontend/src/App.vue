<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      absolute
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

    <v-toolbar dark>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Pawkages</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-title>Welcome, {{user.username}}<v-icon class="icon">account_circle</v-icon></v-toolbar-title>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn href="/accounts/logout/" flat>LOGOUT</v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <router-view></router-view>
    </v-content>

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
        {title:'Contact', icon: 'contact_support', route:'Contact'},
        {title:'Account', icon: 'account_box', route:'Account'},
      ],
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

</style>
