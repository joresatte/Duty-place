<template>
  <div class="service-detail-page">
  <h1 class="page">user page</h1>
    <!-- <h2>{{id}}</h2> -->
    <section class="services" v-for="index in User" :key="index.id">
      <div class="user-profile">
        <div>
          <img :src= "index.text_pictures" alt="" class="image_category"><br></div>
        <div class="user-info">
          <h2>{{index.user_name}}</h2>
          <p><span class="phone"><i class="pi pi-phone" style="color: black;"/></span><br>{{index.phone}}</p>
          <p><span class="email"><i class="pi pi-envelope" style="color: yellow;"/></span><br> {{index.email}}</p>
          <p><span class="city"><i class="pi pi-map-marker" style="color: red;"/></span><br>{{index.city}}</p>
          <p class="intro">{{index.intro}}</p>
          <h4 class="price">{{index.price}}</h4>
          <p class="textarea">{{index.textarea}}</p>
        </div>
      </div>
      <div class=" edit_remove">
        <button class="btn-remove" @click="remove(index.id, index.cat_id)">Remove</button>
        <div></div>
        <button class="btn-edit" @click="editService(index.id, index.cat_id, index.text)">Edit service</button>
      </div>
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
    emits:['editService', 'removeService'],
    data(){
      return{
      }
    },
    methods:{
      async remove(serviceId, userCatId){
        console.log(serviceId, userCatId)
        this.$emit('removeService', serviceId, userCatId)
      },
      editService(eventId, eventCatId, eventText){
        console.log(eventId, eventCatId, eventText)
        localStorage.setItem('eventText', eventText)
        this.$router.push(
          {
            path: '/services/user_services/:id/:category_id/',
            name: 'editPage',
            params:{
              id: eventId,
              cat_id: eventCatId
            }
          }
        )
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