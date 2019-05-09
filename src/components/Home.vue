<template>
  <v-container>
    <v-layout row wrap justify-center>
      <v-flex xs12 md8>
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
           src: 'https://phz8.petinsurance.com/-/media/all-phz-images/2016-images-850/alternate_treats850.jpg'
         },
         {
           src: 'https://isteam.wsimg.com/neb/obj/MUY5QTVFRjA3Q0M5MEJGNjk4Q0E6ZmUyZWJiMzA1YjYxOThiNjE2YTY4NWYyZjQwMjcxZDc6Ojo6OjA=/:/cr=t:0,l:0,w:1000,h:434.4512195121951/rs=w:1200,h:1200'
         },
         {
           src: 'http://trashisfortossers.com/wp-content/uploads/2018/09/zero-waste-homemade-dog-treats-trash-is-for-tossers-cropped.jpg'
         },
         {
           src: 'https://static.boredpanda.com/blog/wp-content/uploads/2019/04/dogs-catching-treats-frei-schnauze-christian-vieler-254-5ca20b9835d48__700.jpg'
         }
      ]
    })
  }
</script>

<style>
</style>
