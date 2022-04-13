<template>
  <br><br>  
  <section class="page">
    {{welcome}}
  </section>
  <form @submit.prevent="handledClickOnCatagory" action="">
  <section class="categories" v-for="category in categories" :key="category.cat_id">
  <router-link :to="{name: 'ServicesByCategoryPage', params:{category_id: category.cat_id}}" >
    <img :src= "category.text_pictures" alt="" class="image_category"><br>
   <button @click="selectedCategory" class="category_button"><h1>{{category.text}}</h1></button>
  </router-link>
  </section>
  </form>
  <section class="text_style">
    <p>
      ¿Cómo funciona nuestro servicio 
      de cuidador/a interno/a
       Entendemos tus necesidades,
       definimos un servicio 
       personalizado y damos respuesta 
       en menos de 1 horas.
    </p>
  </section>
  <footer class="footer_style">
    <div>contact us</div>
    <div></div>
  </footer>
</template>

<script>
import {getCategories} from "@/pages/apiservices/api.js";
export default {
  name: 'Home',
  data(){
    return{
      welcome:"welcome to Services",
      categories:[],
     
    }
  },
  mounted(){
   this.loadData()
  },
  methods:{
    async loadData(){
      console.log("loadData")
      this.categories= await getCategories()
    },
  }
}
</script>
<style scoped>
 .category_button{
  border: 2px solid #FFE600;
  border-radius: 10px;
  text-align:center;
  margin: 1em;
  padding: 1em ;
  border-radius:10px;
  box-shadow:  2px 2px 4px #0D0A96;
}
.categories{
  display: grid;
  grid-auto-columns: 1fr 1fr 1fr 1fr;
  justify-content: space-around;
  padding: 2em;
  text-align:center;
  border-radius:10px;
  border: 2px solid #2bff00;
  margin: 20px;
  box-shadow:  2px 2px 4px #f10889;
  background: linear-gradient(90deg, rgba(3,3,27,0.33703903924851186) 14%, 
            rgba(10,10,142,0.33703903924851186) 23%, 
            rgba(8,17,37,1) 96%);
}
.page{
  margin: 0.5em;
  font-size: 2em;
  color: #53d9ed;
  text-shadow:  2px 2px 4px #f10889;
}

.footer_style{
  color: white;
  display: grid;
  grid-template-columns: auto;
  border: solid 2px;
  background: linear-gradient(90deg, rgba(3,3,27,0.33703903924851186) 14%, 
            rgba(10,10,142,0.33703903924851186) 23%, 
            rgba(8,17,37,1) 96%);
}
.text_style{
  color: linear-gradient(90deg, rgba(10,10,142,0.33703903924851186) 75%, rgba(8,17,37,1) 96%);;
  border: solid 1px rgb(3, 17, 100);
  padding: 1em;
  
}

</style>
