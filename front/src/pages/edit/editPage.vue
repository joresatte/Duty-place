<template>
<main class="edit_page">
    <h1 class="page">Edit Service Page</h1>
    <div class="edit-page">
        <section>
            <img class="img-to-edit" :src="service.text_pictures" alt="">
        </section>
           <section >
               <input type="file"
                              accept="image/png, image/jpeg"
                              required
                              :value="service.upload"
                              @input="service.upload"
                              title="Select file"
                            >
           </section>
               <section class="modal-body">
                  <input type="text"
                          required
                          v-model="service.user_name"
                          placeholder="User Name"
                         > <br>
                  <input type="text"
                          required
                          v-model="service.intro"
                          placeholder="introduce your service"
                         ><br>
                  <input type="text"
                          required
                          v-model="service.price"
                          placeholder="service price by hour"
                         ><br>
                  <input type="email"
                          required
                          v-model="service.email"
                          placeholder="Add email"
                         ><br>
                  <input type="text"
                          required
                          v-model="service.phone"
                          placeholder="Add phone"
                         ><br>
                  <input type="text"
                          required
                          v-model="service.city"
                          placeholder="Add city"
                         >
                         <br><br>
                  <textarea name="textarea"
                          required
                          v-model="service.textarea"
                          placeholder="describe your services"
                         ></textarea>
               </section>
        
                <button
                  type="button"
                  class="btn-green"
                  @click="handleEditModalClick"
                >
                  Save services
                </button>
    </div>
</main>
        <br>
</template>

<script>
import {getServiceToEdit} from '@/pages/apiservices/getServiceToEdit'
import postServiceEdited from '@/pages/apiservices/postServiceEdited'

export default {
    name:'editPage',
    props:['id', 'cat_id', 'text'],
    data(){
        return{
            service:{
                "id": " ",
                "cat_id": " ",
                "user_name": " ",
                "text": "",
                "intro": " ",
                "price": " ",
                "text_pictures": "",
                "textarea": " ",
                "phone": " ",
                "email": " ",
                "city": " ",
            }
        }
    },
    mounted(){
        this.loadData()
    },
    methods:{
        async loadData(){
            console.log(this.loadData)
            const id = localStorage.getItem('eventId')
            const catId = localStorage.getItem('eventCatId') 
            const text = localStorage.getItem('eventText')
            this.service= await getServiceToEdit(id, catId, text)
            console.log(this.service)
        },
        async handleEditModalClick(){
            console.log(this.handleEditModalClick)
            await postServiceEdited(
                this.service.id= localStorage.getItem('eventId'),
                this.service.cat_id= localStorage.getItem('eventCatId') ,
                this.service.user_name,
                this.service.text= localStorage.getItem('eventText'),
                this.service.intro,
                this.service.price,
                this.service.text_pictures,
                this.service.textarea,
                this.service.phone,
                this.service.email,
                this.service.city,
            )
            this.$router.push(
                {
                    path: '/user/:id',
                    name: 'usersPage',
                }
            )
        },
        input(event){
            console.log('image',  event.target.value)
            console.table('Image', event.target.files[0])
            const reader= new FileReader()
            reader.readAsDataURL(event.target.files[0])
            reader.onload= (e)=>{
            this.service.text_pictures= e.target.result
        }
        },
    },
}
</script>

<style scoped>
.img-to-edit{
    width: 50%;
}
.edit_page{
  min-height: 100vh;
}
.edit-page{
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
</style>