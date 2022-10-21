<template>
  <div id="app" class="row">
    <SideBar />
    <div class="main container col-md-9">
      <router-view />
    </div>
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue';
export default {
  components: {
    SideBar
  },
  head: {
    link: [
      {
        rel: 'stylesheet',
        href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
      }
    ]
  }
}
</script>

<style>

html {
  height: 100%;
}

body {
  height: 100%;
  color: #ccc;
  font-family: Calibri, Arial, sans-serif;
  background-color: #357;
}

hr {
  border-top: 1px solid #579;
  width: 100%;
}

.main {
  /* border-left: 1px solid #ccc; */
  padding-top: 2.5em;
  padding-left: 2em;
}

</style>
