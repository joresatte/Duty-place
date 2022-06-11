<template>
  <div class="service-detail-page">
  <h1 class="page">user page</h1>
    <!-- <h2>{{id}}</h2> -->
    <section class="services" v-for="user in users" :key="user">
    <div class="user-profile">
      <div><img :src= "user.text_pictures" alt="" class="image_category"><br></div>
      <div class="user-info">
        <h2>{{user.user_name}}</h2>
        <p><span class="phone"><i class="pi pi-phone" style="color: black;"/></span><br>{{user.phone}}</p>
        <p><span class="email"><i class="pi pi-envelope" style="color: yellow;"/></span><br> {{user.email}}</p>
        <p><span class="city"><i class="pi pi-map-marker" style="color: red;"/></span><br>{{user.city}}</p>
        <p class="intro">{{user.intro}}</p>
        <h4 class="price">{{user.price}}</h4>
        <p class="textarea">{{user.textarea}}</p>
      </div>
    </div>
    </section>
  
</div>
</template>

<script>
export default {
    nam:'userForm',
    props:{
        users:{
            type: Object,
            required: true
        }
    },
    emits:['remove'],
    data(){
      return{
      }
    }
}
</script>

<style scoped>
.services{
  display: grid;
  grid-auto-columns: auto;
  justify-content: space-around;
  padding: 2em;
  color: white;
  text-align:center;
  border-radius:10px;
  border: 2px solid #2bff00;
  margin: 20px;
  box-shadow:  2px 2px 4px #f10889;
  background: linear-gradient(90deg, rgba(3,3,27,0.33703903924851186) 14%, 
            rgba(10,10,142,0.33703903924851186) 23%, 
            rgba(8,17,37,1) 96%);
  
}

.service-detail-page{
  min-height: 100vh;
}
.page{
  margin: 0.5em;
  font-size: 2em;
  color: #53d9ed;
  text-shadow:  2px 2px 4px #f10889;
}
</style>