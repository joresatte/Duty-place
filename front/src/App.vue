<template>
<br>
  <div id="nav">
    <router-link class="Home" to="/">Duty-Place</router-link>
    <br><br>
    <!-- <router-link to="/about">About</router-link> -->
  </div>
  <router-view/>
</template>

<style lang="stylus">
#app
  font-family Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  margin-top 60px

  .Home
    color white
    background-color #0725cc
    font-size 2em
    border-radius 10px
    padding 10px
    text-shadow 3px 3px 3px yellow

  *#app
  background: black;
</style>
