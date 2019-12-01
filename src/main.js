import Vue from 'vue'
import App from './App.vue'
import * as VueGoogleMaps from 'vue2-google-maps'
 
Vue.use(VueGoogleMaps, {
  load: {
    // key: ' ',
    key: 'AIzaSyDiDdtYOqdXqeqdLyo3VcXHIKtrM8SmlWc',
    // libraries: 'places', 
  },
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
