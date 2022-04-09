<template>
<section class="regist-login">
  <button @click="onBtnCliked" class="btn-regist"> Sign up
    <section v-show="showRegist" class="show-regist">
       <emailForm :newEmail="email" @onEmailChanged="onChangedEmail($event)"/>
        <passwordForm :newPassword="password" @onPasswordChanged="onChangedPassword($event)"/>
      <button @click="ClickToRegist">CREATE ACCOUNT</button>
      </section>
  </button>|
  <button @click="BtnCliked" class="btn-login"> Log in
    <section v-show="showLogin" class="show-login">
       <emailForm :newEmail="email" @onEmailChanged="onChangedEmail($event)"/>
        <passwordForm :newPassword="password" @onPasswordChanged="onChangedPassword($event)"/>
      <button @click="ClickToLogIn">Log in</button>
      </section>
  </button>
</section>
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
import emailForm from '../../components/emailForm.vue'
import passwordForm from '../../components/passwordForm.vue';
import getRegistPost from '@/pages/apiservices/getRegistPost.js'
import getLoginPost from '@/pages/apiservices/getLoginPost.js'
import {getCategories} from "@/pages/apiservices/api.js";
export default {
  name: 'Home',
  components: {emailForm, passwordForm},
  data(){
    return{
      welcome:"welcome to Services",
      categories:[],
      email:'',
      password: '',
      showRegist: false,
      showLogin: false,
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
    onChangedEmail(newEmail){
            console.log(newEmail)
            // email.value = newEmail
      },
    onChangedPassword(newPassword){
          console.log(newPassword )
          //  password.value= newPassword
      },
    async ClickToRegist (){
          await getRegistPost()
          console.log(getRegistPost)
          this.email='';
          this.password=''
          this.$router.push('/')
      },
      onBtnCliked(){
        this.showRegist= !this.showRegist
      },
      BtnCliked(){
        this.showLogin= !this.showLogin
      },
      async ClickToLogIn(){
        await getLoginPost()
        console.log(getLoginPost)
        this.email='';
        this.password=''
        this.$router.push('/')
      }

  }
}
</script>
<style scoped>
 .regist-login{
   display: flex;
   float: right;
   
 }
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
