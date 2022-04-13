<template>
<div >
<!-- <router-link class="h" to="/">Services</router-link> -->
<button class="h" @click="backToHomePage">Services</button>
</div>
</template>

<script>
export default {
   name: 'headerNav',
   data(){
      return{

      }
   },
   methods:{
      backToHomePage(){
         this.$router.push({path: '/'})
      }
   }
}
</script>

<style scoped>
.h{
background: linear-gradient(90deg, rgba(8,17,37,1) 
            22%, rgba(10,10,142,0.33703903924851186) 
            51%, rgba(2,2,11,0.33703903924851186) 
            56%);
 position: absolute;
 top: 0;
 left: 0;
 color: white;
 font-size: 1em;
 border-radius: 2px;
 text-decoration: none;
 padding: 0.2em;
}
</style>