<template>
<div id="app">
    <button
      type="button"
      class="btn-publish"
      @click="clickedToSwitchOnModal"
    >
      Publish Service
    </button>
    <publish-services-form-modal 
    :ObjServices="UserServices" 
    :CategoryObj="categoryId"
    @closeModal='shutDown'
    v-show="displayingModal"
    @changedObjServices='onObjServicesChanged'
    @changedObj="cat_id= $event"
    @handleClick="handleClick"/>
    </div>
<br><br>
<userService :User="users" @removeService="remove(userCatId)"/>
</template>

<script>
import PublishServicesFormModal from './PublishServicesForm.vue'
import loginFetch from '@/pages/apiservices/loginFetch.js'
import publishServices from '@/pages/apiservices/publishServicesPost.js'
import getCurrentUser from '@/pages/apiservices/getCurrentUser.js'
import userService from './userService.vue'
import { deleteService } from '../apiservices/deleteService'
import editForm from './editForm.vue'
export default {
  props:['id'],
  name: 'userPage',
  components:{userService, PublishServicesFormModal, editForm},
  data(){
   
    return{
      displayingModal: false,
      // displayingEditModal: false,
      users:[ ],
      text_pictures: '',
      categoryId:[
          {code: 'category_1', name:'Mudanzas'},
          {code: 'category_2', name:'Limpiezas'},
          {code: 'category_3', name:'Cuidados'},
          {code: 'category_4', name:'Mantenimientos'},
      ],
      UserServices:{
        id:'',
        intro:'',
        text:'',
        price:'',
        textarea:'',
        email:'',
        phone:'',
        city:'',
        user_name:'',
      }
    }
  }, 
  mounted(){
    this.loadData();
  },
  methods:{
    // editService(){
    //   this.displayingEditModal= true
    //   console.log(this.displayingEditModal)
    //   console.log(this.editService)
    // },
    async remove(eventId, eventCatId ){
      console.log(this.remove)
      await deleteService(eventId, eventCatId)
    },
    async loadData(){
      console.log(this.loadData)
      this.users= await loginFetch()
      console.log(this.users)
    },
    shutDown() {
        this.displayingModal = false;
    },
    clickedToSwitchOnModal(){
      this.displayingModal = true;
    },
    closeModal() {
        this.displayingModal = false;
    },
    // closeEditModal(){
    //   this.displayingEditModal= false
    // },
    onObjServicesChanged(UserServicesValues){
      console.table(UserServicesValues)
      this.UserServices= UserServicesValues
    },
     getCategoryID() {
      const categoryIdJson = localStorage.getItem("cat_name");
      const categoryId = JSON.parse(categoryIdJson);
      return categoryId.code;
    },
     getCategoryName() {
      const categoryNameJson = localStorage.getItem("cat_name");
      const categoryName = JSON.parse(categoryNameJson);
      return categoryName.name;
    },
    async handleClick(){
      console.log(this.handleClick)
      await publishServices(
        this.UserServices.id= getCurrentUser(), 
        this.cat_id= this.getCategoryID(),
        this.UserServices.user_name,
        this.text= this.getCategoryName(),
        this.UserServices.intro,
        this.UserServices.price,
        this.text_pictures= localStorage.getItem('upload'),
        this.UserServices.textarea,
        this.UserServices.phone,
        this.UserServices.email,
        this.UserServices.city
      )
      this.displayingModal= false
    },
  }
}
</script>

<style scoped>
.btn-publish{
background: linear-gradient(90deg, rgba(8,17,37,1) 0%, 
            rgba(10,10,142,0.33703903924851186) 59%, 
            rgba(3,3,25,0.33703903924851186) 79%);
 position: absolute;
 top: 10em;
 right: 0;
 color: white;
 font-size: 1em;
 border-radius: 2px;
 text-decoration: none;
 padding: 0.2em;
}

</style>