<template>
  <v-container>
    <v-layout row wrap justify-center>
      <v-flex xs12 md9>
        <v-carousel>
          <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
          ></v-carousel-item>
        </v-carousel>
        <br />
        <v-layout align-center justify-center>
          <v-flex xs12 md8>
            <v-layout align-center column justify-center>
              <h1 class="display-2 font-weight-thin text-center">Shop Pawkages</h1>
            </v-layout>
          </v-flex>
        </v-layout>

        <v-container fluid grid-list-md>
          <v-layout row wrap justify-center fill-height>
            <v-flex v-for="card in cards" :key="card.title" v-bind="{ [`xs${card.flex}`]: true }">
              <v-card dark>
                <router-link :to="{ name: card.name, params: { cards: route}}"><v-img position="center" :src="card.src" height="400px">

                  <v-container fill-height fluid pa-2>
                    <v-layout fill-height>
                      <v-flex xs12 md9 align-end flexbox>
                        <span class="headline white--text" v-text="card.title">
                        </span>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-img>
                </router-link>
                <v-card-text>
                  {{ card.description }}
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
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
      ],
      route: '',
      cards: [
        {
          title: 'Products',
          src: require('@/assets/card1.jpg'),
          flex: 12,
          name: "Products",
          route: '../products',
          description: "Browse our robust collection of dog and cat food. You can find trusted brands for any general feeding need."
        },
        {
          title: 'Subscriptions',
          src: require('@/assets/card2.jpg'),
          flex: 6,
          name: "Subscriptions",
          route: '../subscriptions',
          description: "Find a product that you love? Created a recipe that you need for your furry friends diet? Set up a subscription and pay every month or every 6 months!"
        },
        {
          title: 'Recipes',
          src: require('@/assets/card3.jpg'),
          flex: 6,
          name: "Recipes",
          route: '../recipes',
          description: "Does basic nutrition not apply? Prefer to control what's in your animals diet? Browse our ingredients and create a recipe you need for any situation!"
        },
      ]
    })
  }
</script>

<style scoped lang="sass">
  a
    color: white
    text-decoration: none

  a:visited
    color: white
</style>
