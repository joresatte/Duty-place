<template>
<Regists/>
  <section class="home">
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
  <section class="message">
    <p>
      ¿Cómo funciona nuestro servicio 
      de cuidador/a interno/a
       Entendemos tus necesidades,
       definimos un servicio 
       personalizado y damos respuesta 
       en menos de 1 horas.
    </p>
  </section>
  <footer class="down">
    <div>contact us</div>
    <div></div>
  </footer>
</template>

<script>
import Regists from "@/components/Regists.vue";
import {getCategories} from "@/pages/apiservices/api.js";
export default {
  name: 'Home',
  components: {Regists},
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
    }
  }
}
</script>
<style scoped>
/* .button{
padding:10px;
border-radius:5px;
background-color:#6457A6;
color:#ffffff;
box-shadow:  2px 2px 4px #0D0A96;
cursor:pointer;
 }   */
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
  background-color: #6E8898FF;
}
.home{
  margin: 0.5em;
  font-size: 2em;
  color: #53d9ed;
  text-shadow:  2px 2px 4px #f10889;
}

.down{
  display: grid;
  grid-template-columns: auto;
  border: solid 2px;
  background-color: rgb(16, 215, 215);
}
.message{
  color: white;
  border: solid 1px white;
  padding: 1em;
  
}
</style>
