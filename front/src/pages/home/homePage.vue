<template>
  <h2>{{welcome}} </h2>
  <section>
    <form @submit.prevent="clickbutton"  action="">
    <button><select v-model="selectedUser">
      <option :value="null" disabled>select user</option>
        <option v-for="user in users" :key="user.id" :value="user">{{user.name}}</option>
      
    </select>
    </button>
    </form>
  </section>
</template>
<script>
import {useStorage} from "@vueuse/core"
export default {
    data(){
      return{
        welcome:"Welcome To Your Contacts Schedule",
        users:{},
        selectedUser: null,
        localUser: useStorage('user', {}),

      }
    },
    mounted(){
      this.loadData()
    },
    methods:{
      async loadData(){
        console.log('users')
        this.users=[
  {
    "id": "user-1", 
    "name": "joseba"
  }, 
  {
    "id": "user-2", 
    "name": "josu"
  }
]
      },
      clickbutton(){
        //console.log("usuarios")
        this.localUser={id: this.selectedUser.id,
                        name: this.selectedUser.name
                        }
                
        this.$router.push("/contact");

      }
    }
}
</script>

<style>

</style>