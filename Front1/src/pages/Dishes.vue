<template name="dishes">
  <q-page>
    <q-header>
      <q-toolbar class="q-pt-sm q-pb-sm q-pl-md q-pr-md bg-yellow-8 flex justify-between">
        <div>
        <q-input
          class="bg-white"
          color="grey-8"
          v-model="search"
          debounce="1000"
          dense
          filled
          square
          placeholder="Найти"
        >
          <template v-slot:append>
          <q-icon name="search" />
          </template>
        </q-input>
        </div>
        <img src="../statics/guy.svg" alt="guy">
      </q-toolbar>
    </q-header>
    <div class="column q-pa-md">
      <router-link class="td col-12" to="/final"><div class="q-mb-sm" v-for="(dish, i) in lor" :key="i">
        <q-card @click="posti(i)" class="my-card">
          <img class="imag" :src="url[i]">

          <q-card-section>
            <div class="text-h6 text-grey-9">{{ dish }}</div>
          </q-card-section>
        </q-card>
      </div></router-link>
    </div>
  </q-page>
</template>

<script>
import axios from 'axios'
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      search: ''
    }
  },
  computed: {
    lor: {
      get () {
        return this.$store.state.example.lorem.data.dishes
      }
    },
    url: {
      get () {
        return this.$store.state.example.lorem.data.urls
      }
    }
  },
  methods: {
    ...mapMutations({
      lorem: 'example/dishSwitch'
    }),
    posti (n) {
      var str = this.lor[n]
      axios
        .post('http://167.172.165.25:8091/get_ingredients', { name: str })
        .then(response => (this.lorem(response)))
    }
  }
}
</script>

<style lang="scss" scoped>
.td{
  text-decoration: none;
}
</style>
