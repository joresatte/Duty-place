<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          all camps are required!
        </slot>
      </header>

      <section class="modal-body">
        <slot name="body">
          Upload picture!
          <input type="file" 
                  accept="image/png, image/jpeg"
                  required 
                  :value="uploadPicture" 
                  @input="upload"
                  title="Select file"
                >
        </slot>
       </section>
       <section class="modal-body">
          <input type="text" 
                  required 
                  v-model="ObjServices.user_name" 
                  @changed="onServices"
                  placeholder="User Name"
                 > <br>   
          <input type="text" 
                  required 
                  v-model="ObjServices.intro" 
                  @changed="onServices"
                  placeholder="introduce your service"
                 ><br>
          <input type="text" 
                  required 
                  v-model="ObjServices.price" 
                  @changed="onServices"
                  placeholder="service price by hour"
                 ><br>
          <input type="email" 
                  required 
                  v-model="ObjServices.email" 
                  @changed="onServices"
                  placeholder="Add email"
                 ><br>
          <input type="number" 
                  required 
                  v-model="ObjServices.phone" 
                  @changed="onServices"
                  placeholder="Add phone"
                 ><br>
          <input type="text" 
                  required 
                  v-model="ObjServices.city" 
                  @changed="onServices"
                  placeholder="Add city"
                 >
                 <br><br>
          <textarea name="textarea" 
                  required 
                  v-model="ObjServices.textarea" 
                  @changed="onServices"
                  placeholder="describe your services"
                 ></textarea>                            
       </section>
       <section class="ObjCategorymodal-body">
          select category services!
          <section>
          <select class="select-service-option" @change="selectedOption" v-model="selectedCategory">
          <option class="select-option" value="">Select category service</option>
          <option v-for="index in CategoryObj" :key="index.code" :value="index">
          {{index.name}}
          </option>
          </select>
           </section>
       </section>
      <footer class="modal-footer">
        <slot name="footer">
        </slot>
        <button
          type="button"
          class="btn-green"
          @click="handleClick"
        >
          Save services
        </button>
        <br>
        <button
          type="button"
          class="btn-green"
          @click="closeModal"
        >
          Close Modal
        </button>
      </footer>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'PublishServicesFormModal',
    emits:[
      'changed', 'changedPasswordEmail', 
      'changedObjServices', 'closeModal', 
      'uploaded','changedObj', 'handleClick',
      'input'
    ],
    props:{
      ObjServices:{
        type:Object,
        required: true
      },
      CategoryObj:{
        type: Array,
       required: true
      }
    },
    data(){
      return{
        selectedCategory:'',
        uploadPicture: '',
      }
    },
    methods: {
      closeModal() {
        this.$emit('closeModal');
      },
      upload(event){
        console.log('image',  event.target.value)
        console.table('Image', event.target.files[0])
        const reader= new FileReader()
        reader.readAsDataURL(event.target.files[0])
        reader.onload= (e)=>{
          this.uploadPicture= e.target.result
          localStorage.setItem('upload', this.uploadPicture)
          console.log('onload',this.uploadPicture)
        }
      },
      selectedOption(event){
        console.log(event.target.value)
        this.$emit('changedObj', event.target.value)
        localStorage.setItem('cat_name', JSON.stringify(this.selectedCategory))
        console.log(this.selectedCategory)
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          intro: event.target.value,
          price: this.ObjServices.price,
          textarea: this.ObjServices.textarea,
          email: this.ObjServices.email,
          phone: this.ObjServices.phone,
          city: this.ObjServices.city,
          user_name: this.ObjServices.user_name
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          price: event.target.value,
          intro: this.ObjServices.intro,
          textarea: this.ObjServices.textarea,
          email: this.ObjServices.email,
          phone: this.ObjServices.phone,
          city: this.ObjServices.city,
          user_name: this.ObjServices.user_name
        })
      },
       onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          textarea: event.target.value,
          price: this.ObjServices.price,
          intro: this.ObjServices.intro,
          email: this.ObjServices.email,
          phone: this.ObjServices.phone,
          city: this.ObjServices.city,
          user_name: this.ObjServices.user_name
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          email: event.target.value,
          textarea: this.ObjServices.textarea,
          price: this.ObjServices.price,
          intro: this.ObjServices.intro,
          phone: this.ObjServices.phone,
          city: this.ObjServices.city,
          user_name: this.ObjServices.user_name
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          phone: event.target.value,
          email: this.ObjServices.email,
          textarea: this.ObjServices.textarea,
          price: this.ObjServices.price,
          intro: this.ObjServices.intro,
          city: this.ObjServices.city,
          user_name: this.ObjServices.user_name
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          city: event.target.value,
          phone: this.ObjServices.phone,
          email: this.ObjServices.email,
          textarea: this.ObjServices.textarea,
          price: this.ObjServices.price,
          intro: this.ObjServices.intro,
          user_name: this.ObjServices.user_name
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          user_name: event.target.value,
          city: this.ObjServices.city,
          phone: this.ObjServices.phone,
          email: this.ObjServices.email,
          textarea: this.ObjServices.textarea,
          price: this.ObjServices.price,
          intro: this.ObjServices.intro,
        })
      },
      handleClick(){
        console.log(this.handleClick)
        this.$emit('handleClick')
        this.$router.resolve({
        path: '/user/:id',
        name: 'usersPage',
      })
      },
    },
  };
</script>
<style scoped>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 1.5em;
    display: flex;
  }

  .modal-header {
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

  .modal-body {
    position: relative;
    padding: 2em 2em;
    color: #5c0bde;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 2em;
    padding: 2em;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
    height: 2em;
  }
  .select{
    position: relative;
    bottom: 0em;
    color: #190f13;
  }
  .ObjCategorymodal-body{
    position: relative;
    bottom: 1em;
    color: #5c0bde;
  }
</style>