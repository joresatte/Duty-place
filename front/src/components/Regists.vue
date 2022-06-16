<template>
  <h1>regists page </h1>
  <emailForm :email="email" @onEmailChanged="onChangedEmail"/>
  <passwordForm :password="password" @onPasswordChanged="onChangedPassword"/>
  <button @click="saveClicked">CREATE ACCOUNT</button>
</template>

<script>
import emailForm from './emailForm.vue';
import passwordForm from './passwordForm.vue';
import getRegistPost from '@/pages/apiservices/getRegistPost.js'

export default {
    name: 'registsPage',
    components:{emailForm, passwordForm},
    setup(){
        const {email, password}= getRegistPost()
        
        const onChangedEmail= (newEmail)=>{
            console.log(newEmail)
        }
        const onChangedPassword=(newPassword)=>{
            console.log(newPassword )
        }
        const saveClicked= async ()=> {
            await getRegistPost()
            console.log(getRegistPost)
        }

        return {email, password, onChangedEmail, onChangedPassword, saveClicked}
    }

}
</script>

<style>

</style>