<template>
<br>
  <div id="nav">
    <router-link class="Home" to="/">Services</router-link>
    <br><br>
    <!-- <router-link to="/about">About</router-link> -->
  </div>
  <router-view/>
</template>

<style lang="stylus">
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  
}
img {
  width: 100%
  
}
#app
  font-family Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50

  .Home
    color white
    background-color #0725cc
    font-size 2em
    border-radius 10px
    padding 10px
    text-shadow 3px 3px 3px yellow

  *#app
  background:  #95DBE5FF;
</style>
