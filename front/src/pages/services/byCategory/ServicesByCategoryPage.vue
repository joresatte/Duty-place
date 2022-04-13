<template>
  <h1 class="page">Services By Category Page</h1>
  <!-- <p>{{category_id}} </p> -->
  <section v-for="index in services" :key="index" class="services">
  <img :src= "index.text_pictures" alt="" class="image_category"><br>
 <h2>{{index.user_name}}</h2>
  <p><span class="phone">Phone Number:</span><br> {{index.phone}}</p>
  <p><span class="email">Email:</span><br> {{index.email}}</p>
  <p><span class="city">City: </span><br>{{index.city}}</p>
  <router-link class="details"  :to="{ name: 'userDetailesPage', params:{id: index.id}}" >details</router-link>
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
      let categoryId = this.category_id;
      this.services= await getCategoriesServices(categoryId)
    }
  },

}
</script>

<style scoped>
.services{
  display: grid;
  grid-auto-columns: auto;
  justify-content: space-around;
  padding: 2em;
  text-align:center;
  color: white;
  border-radius:10px;
  border: 2px solid #2bff00;
  margin: 20px;
  box-shadow:  2px 2px 4px #f10889;
  background: linear-gradient(90deg, rgba(8,17,37,1) 8%, 
            rgba(3,3,27,0.33703903924851186) 45%, 
            rgba(10,10,142,0.33703903924851186) 78%);
}
.email{
  font-size: 1.5rem;
}
.phone{
  font-size:1.5rem;
}
.city{
  font-size: 1.5rem;
}
.details{
  color: rgb(37, 137, 231);
  background: white;
  padding: 0.2em;
}
</style>