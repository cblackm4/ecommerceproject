<template>
  <v-app>

    <v-toolbar dark>
      <v-toolbar-side-icon></v-toolbar-side-icon>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat v-for='(menu, index) in menus' :key='index' :to="menu.route">
          {{menu.name}}
        </v-btn>
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
      menus: [
        {name:'Home', route:"Home"},
        {name:'Contact', route:'Contact'},
        {name:'Account', route:'Account'},
      ]
    }
  },
}
</script>
