<template>
  <main class="publish-page">
    <div class="">
      <header class="">
          all camps are required!
      </header>
      <section class="PService-body">
          Upload picture!
          <input type="file"
                  class="upload-file" 
                  accept="image/png, image/jpeg"
                  required  
                  @input="upload"
                  title="Select file"
                >
       </section>
       <section class="">
          <input type="text" 
                  required 
                  v-model="ObjServices.user_name" 
                  placeholder="User Name"
                 > <br>   
          <input type="text" 
                  required 
                  v-model="ObjServices.intro" 
                  placeholder="introduce your service"
                 ><br>
          <input type="text" 
                  required 
                  v-model="ObjServices.price" 
                  placeholder="service price by hour"
                 ><br>
          <input type="email" 
                  required 
                  v-model="ObjServices.email" 
                  placeholder="Add email"
                 ><br>
          <input type="number" 
                  required 
                  v-model="ObjServices.phone" 
                  placeholder="Add phone"
                 ><br>
          <input type="text" 
                  required 
                  v-model="ObjServices.city" 
                  placeholder="Add city"
                 >
                 <br><br>
          <textarea name="textarea" 
                  required 
                  v-model="ObjServices.textarea" 
                  placeholder="describe your services"
                 ></textarea>                            
       </section>
       <section class="">
          select category services!
          <section>
          <select class="select-service-option" @change="selectedOption" v-model="selectedCategory">
          <option class="select-service-option" value="">Select category service</option>
          <option v-for="index in categoryId" :key="index.code" :value="index">
          {{index.name}}
          </option>
          </select>
           </section>
       </section>
       <br>
        <footer class="modal-footer">
          <button
            type="button"
            class="btn-green"
            @click="handleClick"
          >
            Publish services
          </button><br><br>
          <button
            type="button"
            class="btn-green"
            @click="getBack"
          >
            Get back to previous page
          </button>
        </footer>
    </div>
  </main>
</template>
<script>
import getCurrentUser from '@/pages/apiservices/getCurrentUser.js'
import publishServices from '@/pages/apiservices/publishServicesPost.js'
  export default {
    name: 'PublishServicesPage',
    props:['id'],
    data(){
      return{
        selectedCategory:'',
        text_pictures: '',
        categoryId:[
            {code: 'category_1', name:'Mudanzas'},
            {code: 'category_2', name:'Limpiezas'},
            {code: 'category_3', name:'Cuidados'},
            {code: 'category_4', name:'Mantenimientos'},
        ],
        ObjServices:{
            id:'',
            intro:'',
            text:'',
            price:'',
            textarea:'',
            email:'',
            phone:'',
            city:'',
            user_name:'',
        },
      }
    },
    methods: {
      upload(event){
        console.log('image',  event.target.value)
        console.table('Image', event.target.files[0])
        const reader= new FileReader()
        reader.readAsDataURL(event.target.files[0])
        if(!event.target.files[0]){
          return;
        }
        reader.onload= (e)=>{
          this.text_pictures= e.target.result
          localStorage.setItem('upload', this.uploadPicture)
          console.log('onload',this.uploadPicture)
        }
      },
      selectedOption(event){
        console.log(event.target.value)
        localStorage.setItem('cat_name', JSON.stringify(this.selectedCategory))
        console.log(this.selectedCategory)
      },
      getBack(){
          this.$router.push(
              {
                path: '/user/:id',
                name: 'usersPage',
                params:{
                    id: getCurrentUser()
                }
              }
          )
          console.log(getCurrentUser())
      },
      getCategoryName() {
          const categoryNameJson = localStorage.getItem("cat_name");
          const categoryName = JSON.parse(categoryNameJson);
          return categoryName.name;
      },
      getCategoryID() {
          const categoryIdJson = localStorage.getItem("cat_name");
          const categoryId = JSON.parse(categoryIdJson);
          return categoryId.code;
      },
      async handleClick(){
        console.log(this.handleClick)
        await publishServices(
          this.ObjServices.id= getCurrentUser(), 
          this.cat_id= this.getCategoryID(),
          this.ObjServices.user_name,
          this.text= this.getCategoryName(),
          this.ObjServices.intro,
          this.ObjServices.price,
          this.text_pictures,
          this.ObjServices.textarea,
          this.ObjServices.phone,
          this.ObjServices.email,
          this.ObjServices.city
      )
        this.$router.push(
              {
                path: '/user/:id',
                name: 'usersPage',
                params:{
                    id: getCurrentUser()
                }
              }
          )
     },
    },
  };
</script>
<style scoped>
  .modal-header,
  .modal-footer {
    padding: 1.5em;
    display: flex;
  }
  .header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }
  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
    justify-content: flex-end;
  }
  .PService-body {
    position: relative;
    padding: 2em 2em;
    color: #efecf4;
  }
  .btn-green {
    color: white;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
    height: 2em;
  }
  .publish-page{
  display: grid;
  grid-auto-columns: auto;
  justify-content: space-around;
  height: 30em;
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
</style>