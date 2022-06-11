<template>
<span class="p-input-icon-left" style="position: absolute; top: 10em; left: 0em; " v-show="displayInput">
            <i class="pi pi-search" style="color: blue;"/>
            <InputText 
            type="text" v-model="filteredOption" 
            placeholder="Search" 
            style="width: 8em; color: blue;"/>
</span>
  <h1 class="page">Services By Category Page</h1>
  <!-- <p>{{category_id}} </p> -->
  <section v-for="index in filteredOptionService" :key="index" class="services">
  <div class="user-profile">
    <div><img :src= "index.text_pictures" alt="" class="image_category"></div>
    <div class="user-info">
      <h2>{{index.user_name}}</h2>
      <p><span class="phone"><i class="pi pi-phone" style="color: black;"/></span><br> {{index.phone}}</p>
      <p><span class="email"><i class="pi pi-envelope" style="color: yellow;"/></span><br> {{index.email}}</p>
      <p><span class="city"><i class="pi pi-map-marker" style="color: red;"/></span><br>{{index.city}}</p>
    </div>
  </div>
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
      filteredOption:'',
      displayInput: true,
    }
  },
  mounted(){
    this.loadData()
  },
  computed:{
    isValidFilter(){
      for (const category of this.services){
        if(
          category.phone.toLowerCase().includes(this.filteredOption.toLowerCase())||
          category.email.toLowerCase().includes(this.filteredOption.toLowerCase())||
          category.city.toLowerCase().includes(this.filteredOption.toLowerCase())||
          category.price.toLowerCase().includes(this.filteredOption.toLowerCase())||
          category.user_name.toLowerCase().includes(this.filteredOption.toLowerCase())
          ){
          return true
        }
      }
    },
    filteredOptionService(){
      const services= this.services
      const filtered= this.filteredOption
      if(!this.isValidFilter){
        return services
      }else{
        return Object.values(services).filter((option)=>{
          return option.phone.toLowerCase().includes(filtered.toLowerCase())||
                option.email.toLowerCase().includes(filtered.toLowerCase())||
                option.city.toLowerCase().includes(filtered.toLowerCase())||
                option.price.toLowerCase().includes(filtered.toLowerCase())||
                option.user_name.toLowerCase().includes(filtered.toLowerCase());
       })
      }
      
   }
  },
  methods:{
    async loadData(){
      console.log("loadData-services")
      let categoryId = this.category_id;
      this.services= await getCategoriesServices(categoryId)
    },
    handleClick(){
      this.displayInput=! this.displayInput
    },
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
  margin-left: 3em;
  color: white;
  padding: 0.2em;
  background: linear-gradient(90deg, rgba(3,3,27,0.33703903924851186) 14%, 
            rgba(10,10,142,0.33703903924851186) 23%, 
            rgba(8,17,37,1) 96%);
}
</style>