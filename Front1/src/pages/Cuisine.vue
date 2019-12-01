<template name="cuisine">
  <q-page class="sd">
    <q-header>
      <q-toolbar class="bg-yellow-8 align-center flex justify-between">
        <p class="q-ma-none fz">Выберите кухню</p>
        <img src="../statics/guy.svg" alt="guy">
      </q-toolbar>
    </q-header>

    <div class="q-pa-md">
      <div class="row q-mb-md justify-between">
        <router-link class="td col-6" to="/dishes"><div @click="posti(0)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/Russian.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[0].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
        <router-link class="td col-6" to="/dishes"><div @click="posti(1)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/Italia.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[1].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
      </div>
      <div class="row q-mb-md justify-between">
        <router-link class="td col-6" to="/dishes"><div @click="posti(2)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/Japan.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[2].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
        <router-link class="td col-6" to="/dishes"><div @click="posti(3)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/Mexica.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[3].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
      </div>
      <div class="row q-mb-md justify-between">
        <router-link class="td col-6" to="/dishes"><div @click="posti(4)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/China.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[4].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
        <router-link class="td col-6" to="/dishes"><div @click="posti(5)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/Franc.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[5].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
      </div>
      <div class="row justify-between">
        <router-link class="td col-6" to="/dishes"><div @click="posti(6)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/kartinka.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[6].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
        <router-link class="td col-6" to="/dishes"><div @click="posti(7)" class="col-6">
          <q-card class="my-card q-ma-xs">
          <div>
              <q-img
                  src="../statics/cuisines/Espanya.jpg"
                  basic
              >
              </q-img>

              <q-card-section>
                  <div class="text-black">{{ cuisines[7].name }}</div>
              </q-card-section>
          </div>
          </q-card>
        </div></router-link>
      </div>
    </div>
  </q-page>
</template>

<script>
import axios from 'axios'
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      cuisines: [
        { name: 'Русская кухня' },
        { name: 'Итальянская кухня' },
        { name: 'Японская кухня' },
        { name: 'Мексиканская кухня' },
        { name: 'Китайская кухня' },
        { name: 'Французская кухня' },
        { name: 'Армянская кухня' },
        { name: 'Испанская кухня' }
      ]
    }
  },
  methods: {
    ...mapMutations({
      lorem: 'example/loremSwitch'
    }),
    posti (n) {
      var str = this.cuisines[n].name
      axios
        .post('http://167.172.165.25:8091/get_dishes', { region: str })
        .then(response => (this.lorem(response)))
    }
  }
}
</script>

<style lang="scss" scoped>
@media (max-width: 450px){
  .my-card{
    max-width: 150px;
    min-height: 180px;
    min-width: 150px;
  }
}
@media (min-width: 450px){
  .my-card{
    max-width: 1050px;
    min-height: 180px;
    min-width: 160px;
  }
}
.td{
  text-decoration: none;
}
.fz{
  font-size: 20px;
}
.sd{
  background-image: url(../statics/bgLight.png);
  background-size: cover
}
</style>
