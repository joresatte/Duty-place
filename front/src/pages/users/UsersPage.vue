<template>
<userForm :users="users"/>
</template>

<script>
import loginFetch from '@/pages/apiservices/loginFetch.js'
import userForm from '@/components/userForm.vue'
export default {
  props:['id'],
  name: 'userPage',
  components:{userForm},
  data(){
    return{
      users:[],
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
  }
}
</script>

<style>

</style>