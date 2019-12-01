<template>
  <div id="app">
    <GmapMap
  :center="{lat: 50.8479287, lng: 10.2462478}"
  :zoom="7"
  map-type-id="terrain"
  style="width: 500px; height: 300px"
>
  <GmapMarker
    :key="index"
    v-for="(m, index) in markers"
    :position="m.position"
    :clickable="true"
    :draggable="true"
    @click="center=m.position"
  />
</GmapMap>
  </div>
</template>

<script>
export default {
  data () {
    return {
      markers: [{
        position: {lat: 50.0, lng: 10.0}
      }, {
        position: {lat: 51.0, lng: 11.0}
      }]
    }
  },
  mounted: {

  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
