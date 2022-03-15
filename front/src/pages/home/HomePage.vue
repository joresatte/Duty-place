<template>
  <section class="home">
    {{welcome}}
  </section>
  <form @submit.prevent="handledClickOnCatagory" action="">
  <section class="categories" v-for="category in categories" :key="category.cat_id">
  <router-link :to="{name: 'ServicesByCategoryPage', params:{category_id: category.cat_id}}" >
   <button @click="selectedCategory" class="category_button"><h1>{{category.text}}</h1></button>
  </router-link>
  </section>
  </form>
  {{categories}}
</template>

<script>
import {getCategories} from "../apiservices/api.js";
export default {
  name: 'Home',
  // components: {
  //   HelloWorld
  // },
  data(){
    return{
      welcome:"welcome to Duty-Place",
      categories:[],
      // selectCategory:'',
      // currentCategory: localStorage.category_id
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
  background-color: #0fda9d2a;
}
.home{
  margin: 0.5em;
  font-size: 2em;
  color: #0725cc;
  text-shadow:  2px 2px 4px #f10889;
}

</style>
