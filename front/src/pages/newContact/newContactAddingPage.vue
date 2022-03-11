<template>
  <form @submit.prevent="addNewContact" class="add">
  <input type="text" v-model="contact.firstName" placeholder="First Name" class=""/><br><br>
  <input type="text" v-model="contact.lastName" placeholder="Last Name" class=""/><br><br>
  <input type="email" v-model="contact.email" placeholder="Email" class=""/><br><br>
  <input type="number" v-model="contact.phone" placeholder="Phone" class=""/><br><br><br>
  <button>Save Contact</button>
  </form>
</template>

<script>
import { v4 as uuidv4 } from 'uuid';
import config from "@/config.js"
uuidv4();
export default {
   data(){
       return{
           contact:{
                firstName: '',
                lastName: '',
                email:'',
                phone:''
           },
       }
   },
   methods:{
       addNewContact(){
            if(this.firstName&&this.lastName &&this.email&&this.phone !==''){
                this.contact.Id= uuidv4()
				const settings={
					method:'POST',
					body:JSON.stringify(this.contact),
					headers:{
						'Content-Type': 'application/json'
					}
				}
				fetch(`${config.API_PATH}/contact`, settings)
			}
			else{
				alert ("must fill all camps before saving")
			}
				this.firstName='';
				this.lastName='';
				this.email='';
                this.phone=''
       }
   }
}
</script>

<style>

</style>