<template>
<div class="service-detail-page">
  <h1>user page</h1>
    <!-- <h2>{{id}}</h2> -->
    <section class="services" v-for="user in users" :key="user">
    <img :src= "user.text_pictures" alt="" class="image_category"><br>
    <h2>{{user.user_name}}</h2>
    <p><span class="phone">Phone Number:</span><br>{{user.phone}}</p>
    <p><span class="email">Email:</span><br> {{user.email}}</p>
    <p><span class="city">City: </span><br>{{user.city}}</p>
    <p class="intro">{{user.intro}}</p>
    <h4 class="price">{{user.price}}</h4>
    <p class="textarea">{{user.textarea}}</p>
    </section>
  
</div>
  
  
 

</template>

<script>
import {getUserServices} from '@/pages/apiservices/api.js'
export default {
  name:'userDetailesPage',
  props:['id'],
  data(){
    return{
      users:[],
    }
  },
  mounted(){
    this.loadUser();
  },
  methods:{
    async loadUser(){
      console.log(this.loadUser)
      const userId= this.id
      this.users= await getUserServices(userId)
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
  border-radius:10px;
  border: 2px solid #2bff00;
  margin: 20px;
  box-shadow:  2px 2px 4px #f10889;
  background-color:white;
  
}

.service-detail-page{
  min-height: 100vh;
}
</style>