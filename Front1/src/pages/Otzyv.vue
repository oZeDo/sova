<template>
    <q-page>
        <div class="column flex items-center" >
            <div class="col text-grey-9 text-bold ozenka text-center" >Оцените этот нереальный рисунок карандашом</div>
            <div class="col">
                <q-rating
        v-model="ratingModel"
        size="3.5em"
        color="red-6"
        icon="favorite_border"
        icon-selected="favorite"
      /></div>
      <div class="col text-grey-9 text-bold share text-center">Поделись своей едой</div>
      <div class="col socity">
      <a class="q-mr-sm" href="#">
          <q-btn round color="yellow-8">
          <q-avatar>
            <img src="../statics/vk.png" alt="">
          </q-avatar>
          </q-btn>
      </a>
      <a class="q-ml-sm" href="#">
          <q-btn round color="primary">
          <q-avatar>
            <img src="../statics/twit.png" alt="">
          </q-avatar>
          </q-btn>
      </a></div>
     <div><q-btn outline color="grey-9 q-pr-md q-pl-md" class="full-width" label="Вернуться на главную" to="login"/></div>
        </div>
    </q-page>
</template>
<script>
export default {
  data () {
    return {
      ratingModel: 0
    }
  }
}
</script>
<style lang="scss" scoped>
.ozenka {
    font-family: 'Roboto';
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    margin-top: 182px;
    margin-bottom: 25px;
}
.share {
    font-family: Roboto;
    font-style: normal;
    font-weight: 300;
    height: 12px;
    margin-top: 10px;
    margin-bottom: 10px;
}
.socity {
    margin-bottom: 100px;
}
</style>
