<template>
  <v-container>
    <v-layout row wrap justify-center>
      <v-flex xs9>
        <v-carousel>
          <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
          ></v-carousel-item>
        </v-carousel>
      </v-flex>
    </v-layout>
  </v-container>


</template>

<script>
  export default {
    data: () => ({
      items: [
        {
           src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
         },
         {
           src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
         },
         {
           src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
         },
         {
           src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
         }
      ]
    })
  }
</script>

<style>
</style>
