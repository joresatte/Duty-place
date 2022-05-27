<template>
<input class="filteredCategory" type="text" v-model="filteredCategory" placeholder="¿Que servicio buscas?"/>
<section class="page">
    {{welcome}}
  </section>
<div class="container">
  <div class="box">
    <span>Cuidados</span>
    <img @click="onClick('category_3')" src="@/assets/images/cuidadoMa.jpg">
  </div>
  <div class="box">
    <span>Mantenimientos</span>
    <img @click="onClick('category_4')" src="@/assets/images/images1.jpg">
  </div>
  <div class="box">
    <span>Limpiezas</span>
    <img @click="onClick('category_2')" src="@/assets/images/images4.jpg">
  </div>
  <div class="box">
    <span>Mudanzas</span>
    <img @click="onClick('category_1')" src="@/assets/images/images.png">
  </div>
</div>
  <br><br> 
  <form @submit.prevent="handledClickOnCatagory" action="">
  <section class="categories" v-for="category in categoryFiltered" :key="category.cat_id">
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
      categories:{},
      filteredCategory:'',
     
    }
  },
  mounted(){
   this.loadData()
  },
  // watch: { 
  //   newCategories: {        
  //       handler (newData) {
  //         const currentObject = JSON.stringify(newData)
  //         this.firstCategory= Json.parse(currentObject)    
  //         localStorage.getItem('current', currentObject)      
  //       },
  //       deep: true
  //     }      
  //   },
 computed:{
    objectValues(){
      const result= []
      for(const index of this.categories){
        result.push(index.val)
      }
    },
    categoryFiltered(){
     const categories= this.categories
     const filtered= this.filteredCategory.toLowerCase()
     if (!filtered) {
        return categories;
      }
    const result= Object.values(categories).filter((service) => {return service.text.toLowerCase().includes(filtered) })
    return result
   }
 },
  methods:{
    async loadData(){
      console.log("loadData")
      this.categories= await getCategories()
      console.log(this.categories)
    },
    
    onClick(catId){
      this.$router.push({
        name: 'ServicesByCategoryPage',
        params:{category_id: catId}
      })
    },
  }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');
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
.container {
  display: flex;
  width: 100%;
  padding: 4% 2%;
  box-sizing: border-box;
  height: 50vh;
}

.box {
  flex: 1;
  overflow: hidden;
  transition: .5s;
  margin: 0 2%;
  box-shadow: 0 20px 30px rgba(0,0,0,.1);
  line-height: 0;
}

.box > img {
  width: 100%;
  height: calc(100% - 5vh);
  object-fit: cover; 
  transition: .5s;
}

.box:hover { flex: 1 1 30%; }
.box:hover {
  width: 100%;
  height: 100%;
}
span{
  font-size: 1.5em;
  display: block;
  text-align: center;
  height: 10vh;
  line-height: 2.6;
  color: #2fa8ba;
  text-shadow:  1px 1px 3px #f10889;
}

</style>
