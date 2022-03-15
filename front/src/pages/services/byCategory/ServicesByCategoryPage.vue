<template>
  <h1>Services By Category Page</h1>
  <p>{{category_id}} </p>
  <section v-for="index in services" :key="index">
 <h2>{{index.user_name}}</h2>
  <p>{{index.phone}}</p>
  <p>{{index.email}}</p>
  <p>{{index.city}}</p>
  </section>

</template>

<script>
import {getCategoriesServices} from "@/pages/apiservices/api.js";

export default {
  name: 'ServicesByCategoryPage',
  props:['category_id'],
  data(){
    return{
      services: [],
    }
  },
  mounted(){
    this.loadData()
  },
  methods:{
    async loadData(){
      console.log("loadData-services")
      let categoryId = this.$route.params.category_id;
      this.services= await getCategoriesServices(categoryId)
    }
  },

}
</script>

<style>

</style>