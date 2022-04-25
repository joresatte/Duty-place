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
    @closeModal='shutDown'
    v-show="displayingModal"
    @changedObjServices='onObjServicesChanged'/>
    </div>
<br><br>
<userForm :users="users"/>
{{UserServices[0][cat_id]}}
</template>

<script>
import PublishServicesFormModal from './PublishServicesForm.vue'
import loginFetch from '@/pages/apiservices/loginFetch.js'
import userForm from '@/components/userForm.vue'
export default {
  props:['id'],
  name: 'userPage',
  components:{userForm, PublishServicesFormModal},
  data(){
    return{
      displayingModal: false,
      users:[],
      UserServices:[
        {text_pictures: ''},
        {intro:''},
        {price:''},
        {textarea:''},
        {email:''},
        {phone:''},
        {city:''},
        {user_name:''},
        {cat_id:[
          {code: 'category_1', name:'Mudanzas'},
          {code: 'category_2', name:'Limpiezas'},
          {code: 'category_3', name:'Cuidados'},
          {code: 'category_4', name:'Mantenimientos'},
          ]},
          {text:[
          {code: 'category_1', name:'Mudanzas'},
          {code: 'category_2', name:'Limpiezas'},
          {code: 'category_3', name:'Cuidados'},
          {code: 'category_4', name:'Mantenimientos'},
          ]}, 
      ],
    }
  }, 
  mounted(){
    this.loadData()
  },
  methods:{
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
    onObjServicesChanged(UserServicesValues){
      console.table(UserServicesValues)
      this.UserServices= UserServicesValues
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