<template name="login">
  <q-page class="sd adapt column flex items-center justify-center q-pt-lg q-pr-md q-pl-md q-pb-lg">
    <q-toggle
      color="yellow"
      v-model="yellow"
      @click="darkTheme"
    />
    <div class="q-mt-md q-mb-xl column justify-center items-center">
      <img src="../statics/logo_login.png" alt="logo">
    </div>
    <div class="full-width">
      <q-input class="input-log q-mb-sm q-field--focused" v-model="login" color="grey-9" outlined label="Логин"   />
      <q-input class="input-log q-mb-lg q-field--focused" v-model="password" color="grey-9" outlined label="Пароль" />
    </div>
    <q-btn to="/cuisine" align="around" class="full-width td q-mb-sm" color="yellow-8" label="Войти" />
    <router-link class="td flex justify-center q-mb-xl" to="/cuisine">
      <p>Регистрация</p>
    </router-link>
    <q-btn to="cuisine" outline align="around" color="black" text-color="black" class="full-width td self-end" label="Продолжить" />
  </q-page>
</template>

<script>
export default {
  data () {
    return {
      password: '',
      login: '',
      yellow: false
    }
  }
}
</script>

<style lang="scss" scoped>
.td{
  text-decoration: none;
  border-color: black;
  color: black;
}
.adapt{
  width: 360px;
  height: 640px;
  margin: 0 auto;
}
.sd{
  background-image: url(../statics/bgLight.png);
  background-size: cover
}
</style>
