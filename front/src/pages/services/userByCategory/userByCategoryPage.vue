<template>
  <h1>{{this.params.$router.id}}</h1>
</template>

<script>
export default {
  name:'userDetailesPage',
  props:['id'],
  data(){
    return{
      user:[],
    }
  },
  mounted(){
    this.loadUser();
  },
  methods:{
     async loadUser(){
      //  const userId= this.user.id;
      //  await fetch(`${config.api_Path}/services/by-category/${category_id}`)
      //       .then(res => res.json())
      //       .catch(err=> console.log(err.message))
     }
  },

}
</script>

<style>

</style>