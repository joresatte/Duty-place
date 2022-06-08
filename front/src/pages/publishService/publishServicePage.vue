<template>
  <main class="publish-page">
    <div class="">
      <header class="">
          all camps are required!
      </header>
       <FileUpload name="demo[]" url="" @input="upload" accept="image/png, image/jpeg">
            <template #empty>
                <p v-tooltip.left="'Drag and drop your files here to upload'" >
                <i class="pi pi-cloud-upload" />
                Drag and drop files here to upload.
                </p>
            </template>
        </FileUpload>
        <br>
       <section class="">
          <div class="p-float-label p-input-icon-right">
            <i class="pi pi-user" />
            <InputText type="text"
                    required
                    v-model="ObjServices.user_name"
                    placeholder="User Name"
                   />
          </div> <br><br>   
          <div class="p-float-label p-input-icon-right">
            <i class="pi pi-user-plus" />
            <InputText type="text"
                    required
                    v-model="ObjServices.intro"
                    placeholder="introduce your service"
                   />
          </div><br><br>
          <div class="p-float-label p-input-icon-right">
            <i class="pi pi-euro" />
            <InputText type="text"
                    required
                    v-model="ObjServices.price"
                    placeholder="service price by hour"
                   />
          </div><br><br>
          <div class="p-float-label p-input-icon-right">
            <i class="pi pi-envelope" />
            <InputText type="email"
                    required
                    v-model="ObjServices.email"
                    placeholder="Add email"
                   />
          </div><br><br>
          <div class="p-float-label p-input-icon-right">
            <i class="pi pi-phone" />
            <InputText type="number"
                    required
                    v-model="ObjServices.phone"
                    placeholder="Add phone"
                   />
          </div><br><br>
          <div class="p-float-label p-input-icon-right">
            <i class="pi pi-map-marker"/>
            <InputText type="text"
                    required
                    v-model="ObjServices.city"
                    placeholder="Add city"
                   />
          </div>
                 <br><br>
          <Textarea name="textarea" 
                  rows="5" cols="30" 
                  required 
                  v-model="ObjServices.textarea" 
                  placeholder="describe your services"
                 />                            
       </section>
       <section class="">
          <section v-tooltip.left="'select services'">
            <Dropdown v-model="selectedCategory" @change="selectedOption"   :options="categoryId" optionLabel="name" placeholder="Select category service" :filter="true">
            <template>
                <div v-for="index in categoryId" :key="index.code" :value="index">{{index.name}}</div>
            </template>
        </Dropdown>
           </section>
       </section>
       <br>
        <footer class="modal-footer">
          <span >
            <Button
              icon="pi pi-check"
              label="Publish services"
              type="button"
              @click="handleClick"
            >
            </Button>
          </span>
          <br><br>
          <span >
            <Button
              icon="pi pi-step-backward"
              label="Get back to previous page"
              type="button" 
              @click="getBack"
            >
            </Button>
          </span>
        </footer>
    </div>
  </main>
  {{ObjServices.text}}
</template>
<script>
import getCurrentUser from '@/pages/apiservices/getCurrentUser.js'
import publishServices from '@/pages/apiservices/publishServicesPost.js'
  export default {
    name: 'PublishServicesPage',
    props:['id'],
    data(){
      return{
        selectedCategory:'',
        text_pictures: '',
        categoryId:[
            {code: 'category_1', name:'Mudanzas'},
            {code: 'category_2', name:'Limpiezas'},
            {code: 'category_3', name:'Cuidados'},
            {code: 'category_4', name:'Mantenimientos'},
        ],
        ObjServices:{
            id:'',
            intro:'',
            text:'',
            price:'',
            textarea:'',
            email:'',
            phone:'',
            city:'',
            user_name:'',
        },
      }
    },
    methods: {
      upload(event){
        console.log('image',  event.target.value)
        console.table('Image', event.target.files[0])
        const reader= new FileReader()
        reader.readAsDataURL(event.target.files[0])
        if(!event.target.files[0]){
          return;
        }
        reader.onload= (e)=>{
          this.text_pictures= e.target.result
          localStorage.setItem('upload', this.uploadPicture)
          console.log('onload',this.text_pictures)
        }
      },
      selectedOption(event){
        console.log(event)
        localStorage.setItem('cat_name', JSON.stringify(this.selectedCategory))
        console.log(this.selectedCategory)
      },
      getBack(){
          this.$router.push(
              {
                path: '/user/:id',
                name: 'usersPage',
                params:{
                    id: getCurrentUser()
                }
              }
          )
          console.log(getCurrentUser())
      },
      getCategoryName() {
        console.log(this.getCategoryName)
          const categoryNameJson = localStorage.getItem("cat_name");
          const categoryName = JSON.parse(categoryNameJson);
          console.log(categoryName.name)
          return categoryName.name;
      },
      getCategoryID() {
          const categoryIdJson = localStorage.getItem("cat_name");
          const categoryId = JSON.parse(categoryIdJson);
          return categoryId.code;
      },
      async handleClick(){
        console.log(this.handleClick)
         if(
                this.service.id!= '' ||
                this.service.cat_id!= ''||
                this.service.user_name!= ''||
                this.service.text!= ''||
                this.service.price!= ''||
                this.service.text_pictures!= ''||
                this.service.textarea!= ''||
                this.service.phone!= ''&& this.service.phone.length == 9 ||
                this.service.email!= '' && re_email.match(this.service.email)||
                this.service.city!= ''

            ){
              await publishServices(
          this.ObjServices.id= getCurrentUser(), 
          this.cat_id= this.getCategoryID(),
          this.ObjServices.user_name,
          this.text= this.getCategoryName(),
          this.ObjServices.intro,
          this.ObjServices.price,
          this.text_pictures,
          this.ObjServices.textarea,
          this.ObjServices.phone,
          this.ObjServices.email,
          this.ObjServices.city
            )
        this.$router.push(
              {
                path: '/user/:id',
                name: 'usersPage',
                params:{
                    id: getCurrentUser()
                }
              }
             )
                }else{
                  Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong!',
                    footer: '<a href="http://localhost:8080/">the email and password fields are required</a>'
              })
            }
        },
     },
  };
</script>
<style scoped>
  .modal-header,
  .modal-footer {
    padding: 1.5em;
    display: flex;
  }
  .header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }
  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
    justify-content: flex-end;
  }
  .PService-body {
    position: relative;
    padding: 2em 2em;
    color: #efecf4;
  }
  .btn-green {
    color: white;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
    height: 2em;
  }
  .publish-page{
  display: grid;
  grid-auto-columns: auto;
  justify-content: space-around;
  height: 50%;
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
.btnGreen {
  color: white;
  background: linear-gradient(90deg, rgba(4,15,38,1) 0%,
              rgba(11,11,157,0.33703903924851186) 28%,
              rgba(26,47,51,0.8076272745426296) 55%);
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}
</style>