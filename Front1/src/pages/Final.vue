<template name="final">
  <q-page class="">
    <q-header>
        <q-toolbar class="q-pt-sm q-pb-sm q-pl-md q-pr-md bg-yellow-8 flex justify-between">
            <div>
                {{ dishu.name }}
            </div>
            <img src="../statics/guy.svg" alt="guy">
            <img src="../statics/favorite.svg" alt="favorite">
            <router-link to="otzyv"><img src="../statics/check.svg" alt="check"></router-link>
        </q-toolbar>
    </q-header>
    <div class="q-pa-md">
        <q-img class="q-mb-md" :src="url" alt="Photo"></q-img>
        <div class="q-mb-md text-grey-9">{{ dishu.description }}</div>
        <div class="q-mb-md text-grey-9 text-h5">Что купить?</div>
        <div>
            <ol>
                <li class="lic" v-for="(ingr, i) in dishu.ingredients" :key="i">
                    <div class="flex justify-between">
                        <p>{{ ingr }}</p>
                    </div>
                </li>
            </ol>
        </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  computed: {
    dishu: {
      get () {
        return this.$store.state.example.dish.data
      }
    },
    url: {
      get () {
        return this.$store.state.example.dish.data.photo
      }
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
