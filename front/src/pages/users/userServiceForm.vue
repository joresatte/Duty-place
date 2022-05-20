<template>
  <div class="service-detail-page">
  <h1 class="page">user page</h1>
    <!-- <h2>{{id}}</h2> -->
    <section class="services" v-for="index in User" :key="index.id">
      <img :src= "index.text_pictures" alt="" class="image_category"><br>
      <h2>{{index.user_name}}</h2>
      <p><span class="phone">Phone Number:</span><br>{{index.phone}}</p>
      <p><span class="email">Email:</span><br> {{index.email}}</p>
      <p><span class="city">City: </span><br>{{index.city}}</p>
      <p class="intro">{{index.intro}}</p>
      <h4 class="price">{{index.price}}</h4>
      <p class="textarea">{{index.textarea}}</p>
      <button class="btn-remove" @click="remove(index.cat_id)">Remove</button>
    </section>
</div>
</template>

<script>
export default {
    nam:'userForm',
    props:{
        User:{
            type: Object,
            required: true
        }
    },
    emits:['remove', 'removeService'],
    data(){
      return{
      }
    },
    methods:{
      remove(event){
        console.log(this.remove)
        console.log(event)
        this.$emit('removeService', event)
      },
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