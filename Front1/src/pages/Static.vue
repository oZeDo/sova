<template name="static">
    <q-page class="sd">
        <q-header>
            <q-toolbar class="bg-yellow-8 align-center flex justify-between">
                <p class="q-ma-none fz">Рикардо Милый</p>
            </q-toolbar>
        </q-header>
        <div class="q-pr-md q-pl-md q-pt-lg q-pb-lg">
            <div class="text-grey-9">
                <div class="text-h5 q-mb-sm">Статистика</div>
                <div class="flex justify-between"><p>Съедено блюд</p><p>28</p></div>
                <div class="flex justify-between"><p>Сэкономлено руб.</p><p>459</p></div>
                <div class="flex justify-between"><p>Пройдено км</p><p>17.1</p></div>
                <div class="flex justify-between"><p>Средняя оценка</p><p>1.0</p></div>
            </div>
            <div>
                <div class="text-h5">Достижения</div>
                <div class="q-mb-sm flex justify-between items-center text-grey-6"><div width="5%"><div class="text-we">Death Stranding</div><div class="text-ex">Пройти 10 км</div></div><div>17.1/10</div></div>
                <div class="q-mb-sm flex justify-between items-center text-grey-9"><div width="5%"><div class="text-we">На массу</div><div class="text-ex">Съесть 5 блюд с мясом</div></div><div>4/5</div></div>
                <div class="q-mb-sm flex justify-between items-center text-grey-6"><div width="5%"><div class="text-we">Огорчило</div><div class="text-ex">Средняя оценка менее 2.0</div></div><div>1.0/2.0</div></div>
                <div class="q-mb-sm flex justify-between items-center text-grey-9"><div width="5%"><div class="text-we">stonks</div><div class="text-ex">Сэкономить 500 рублей</div></div><div>459/500</div></div>
                <div class="flex justify-between items-center text-grey-9"><div width="5%"><div class="text-we">Книга рецептов</div><div class="text-ex">50 блюд в избранном</div></div><div>3/50</div></div>
            </div>
        </div>
    </q-page>
</template>

<script>
export default {
  data () {
    return {
      title: 'omi'
    }
  }
}
</script>

<style lang="scss" scoped>
.fz{
    font-size: 20px;
}
.text-ex{
    font-size: 12px;
}
.text-we{
    font-size: 18px;
    margin-bottom: -5px;
}
.sd{
  background-image: url(../statics/bgLight.png);
  background-size: cover
}
</style>
