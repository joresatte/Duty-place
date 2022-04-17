<template>
<userForm :users="users"/>
</template>

<script>
import {getUserServices} from '@/pages/apiservices/api.js';
import userForm from '@/components/userForm.vue'
export default {
  name:'userDetailesPage',
  components:{userForm},
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
/* .services{
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
} */
</style>