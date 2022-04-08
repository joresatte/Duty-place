<template>
  <h1>regists page </h1>
  <emailForm :email="email" @changed="onEmailChange"/>
  <passwordForm :password="password" @change="onPasswordChange"/>
  <button @click="saveClicked">CREATE ACCOUNT</button>
</template>

<script>
import {ref} from 'vue'
import emailForm from './emailForm.vue';
import passwordForm from './passwordForm.vue';
import getRegistPost from '@/pages/apiservices/getRegistPost.js'

export default {
    name: 'registsPage',
    components:{emailForm, passwordForm},
    setup(){
        const email= ref('')
        const password= ref('')
        
        function onEmailChange(newEmail){
            email.value = newEmail
        }
        function onPasswordChange(newPassword){
             password.value= newPassword
        }
        const saveClicked= async ()=> {
            await getRegistPost()
        }

        return {email, password, onEmailChange, onPasswordChange, saveClicked}
    }

}
</script>

<style>

</style>