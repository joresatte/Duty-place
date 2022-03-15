<template>
  <h1>Services By Category Page</h1>
  <p>{{category_id}} </p>
  <section>
 <h2>{{services.user_name}}</h2>
  <p>{{services.phone}}</p>
  <p>{{services.email}}</p>
  <p>{{services.city}}</p>
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