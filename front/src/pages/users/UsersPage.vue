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
    :uploadPicture="text_pictures"
    :CategoryObj="categoryId"
    @closeModal='shutDown'
    v-show="displayingModal"
    @changedObjServices='onObjServicesChanged'
    @uploaded="text_pictures= $event"
    @changedObj="cat_id= $event"
    @handleClick="handleClick"/>
    </div>
<br><br>
<userForm :users="users"/>
</template>

<script>
import config from "@/config.js";
import PublishServicesFormModal from './PublishServicesForm.vue'
import loginFetch from '@/pages/apiservices/loginFetch.js'
// import objectUserServices from '@/pages/apiservices/getObjectUserServices.js'
import PublishServices from '@/pages/apiservices/PublishServicesPost.js'
import userForm from '@/components/userForm.vue'
export default {
  props:['id'],
  name: 'userPage',
  components:{userForm, PublishServicesFormModal},
  data(){
    return{
      displayingModal: false,
      users:[],
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
    // this.loadObjectUserServices()
  },
  methods:{
    async loadData(){
      console.log(this.loadData)
      this.users= await loginFetch()
      console.log(this.users)
    },
    // async loadObjectUserServices(){
    //   console.log(this.loadObjectUserServices)
    //   this.UserServices= await objectUserServices()
    //   console.log(this.UserServices)
    // },
    shutDown() {
        this.displayingModal = false;
    },
    clickedToSwitchOnModal(){
      this.displayingModal = true;
    },
    closeModal() {
        this.displayingModal = false;
    },
    onObjServicesChanged(UserServicesValues){
      console.table(UserServicesValues)
      this.UserServices= UserServicesValues
    },
    getUserId() {
      const userJson = localStorage.getItem("dataUser");
      const user = JSON.parse(userJson);
      return user.id;
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
      await PublishServices(
        this.UserServices.id= this.getUserId(), 
        this.cat_id= this.getCategoryID(),
        this.UserServices.user_name,
        this.text= this.getCategoryName(),
        this.UserServices.intro,
        this.UserServices.price,
        this.text_pictures,
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
 top: 7em;
 right: 0;
 color: white;
 font-size: 1em;
 border-radius: 2px;
 text-decoration: none;
 padding: 0.2em;
}
</style>