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

</style>