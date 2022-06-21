<template>
<main class="edit_page">
    <h1 class="page">Edit Service Page</h1>
    <div class="edit-page">
        <section>
            <img class="img-to-edit" :src="service.text_pictures" alt="">
        </section>
           <section >
               <label class="uploadPicture" for="uploadPicture">Cambiar imagen</label>
               <FileUpload type="file"
                              mode="basic"
                              name="demo[]"
                              url=""
                              :auto="true" 
                              chooseLabel="New Picture"
                              accept="image/png, image/jpeg"
                              required
                              @input="upload"
                              title="Select file"
                            ></FileUpload>
           </section>
               <section class="modal-body">
                  <div class="p-float-label p-input-icon-right">
                      <i class="pi pi-user" />
                      <InputText type="text"
                              required
                              v-model="service.user_name"
                              placeholder="User Name"
                             />
                  </div><br>
                  <div class="p-float-label p-input-icon-right">
                      <i class="pi pi-user-plus" />
                      <InputText type="text"
                              required
                              v-model="service.intro"
                              placeholder="introduce your service"
                             />
                  </div><br>
                  <div class="p-float-label p-input-icon-right">
                      <i class="pi pi-euro" />
                      <InputText type="text"
                              required
                              v-model="service.price"
                              placeholder="service price by hour"
                             />
                  </div><br>
                  <div class="p-float-label p-input-icon-right">
                      <i class="pi pi-envelope" />
                      <InputText type="email"
                              required
                              v-model="service.email"
                              placeholder="Add email"
                             />
                  </div><br>
                  <div class="p-float-label p-input-icon-right">
                      <i class="pi pi-phone" />
                      <InputText type="text"
                              required
                              v-model="service.phone"
                              placeholder="Add phone"
                             />
                  </div>
                  <br>
                  <div class="p-float-label p-input-icon-right">
                      <i class="pi pi-map-marker"/>
                      <InputText type="text"
                              required
                              v-model="service.city"
                              placeholder="Add city"
                             />
                  </div>
                         <br><br>
                  <div>
                      <Textarea name="textarea"
                              rows="5" cols="30"
                              required
                              v-model="service.textarea"
                              placeholder="describe your services"
                             />
                  </div>
               </section>
                <Button
                  icon="pi pi-check"
                  label="Save services"
                  type="button"
                  class="btn-handleEditClick"
                  @click="handleEditClick"
                >
                </Button>
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
                "id": '',
                "cat_id":'', 
                "user_name": '',
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
        upload(event){
            console.log('image',  event.target.value)
            console.table('Image', event.target.files[0])
            const reader= new FileReader()
            reader.readAsDataURL(event.target.files[0])
            reader.onload= (e)=>{
            this.service.text_pictures= e.target.result
           }
        },
        async loadData(){
            console.log(this.loadData)
            const text = localStorage.getItem('eventText') 
            console.log(text)
            this.service= await getServiceToEdit(this.id, this.cat_id, text)
            console.log(this.service)
        },
        async handleEditClick(){
            console.log(this.handleEditClick)
            
            if(
                this.service.id!= '' ||
                this.service.cat_id!= ''||
                this.service.user_name!= ''||
                this.service.text!= ''||
                this.service.price!= ''||
                this.service.text_pictures!= ''||
                this.service.textarea!= ''||
                this.service.phone!= ''||
                this.service.email!= ''||
                this.service.city!= ''

                ){
                    await postServiceEdited(
                this.service.id= this.id,
                this.service.cat_id= this.cat_id ,
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
            }else{
               Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong!',
                    footer: '<a href="http://localhost:8080/"> all the fields are required</a>'
                })
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
.uploadPicture{
    margin-right: 0.3em;
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