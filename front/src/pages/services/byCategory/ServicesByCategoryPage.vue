<template>
  <h1>Services By Category Page</h1>
  <!-- <p>{{category_id}} </p> -->
  <section v-for="index in services" :key="index" class="services">
 <h2>{{index.user_name}}</h2>
  <p><span class="phone">Phone Number:</span> {{index.phone}}</p>
  <p><span class="email">Email:</span> {{index.email}}</p>
  <p><span class="city">City: </span>{{index.city}}</p>
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

<style scope>
.services{
  display: grid;
  grid-auto-columns: 1fr 1fr 1f;
  justify-content: space-around;
  padding: 2em;
  text-align:center;
  border-radius:10px;
  border: 2px solid #2bff00;
  margin: 20px;
  box-shadow:  2px 2px 4px #f10889;
  background-color: #0fda9d2a;
}
</style>