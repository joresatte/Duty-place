
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
                  :value="uploadPicture.text_pictures" 
                  @changed="upload"
                  title="Select file"
                >
        </slot>
       </section>
       <section class="modal-body">
          <input type="text" 
                  required 
                  v-model="ObjServices.user_name" 
                  @change="onServices"
                  placeholder="User Name"
                 > <br>   
          <input type="text" 
                  required 
                  v-model="ObjServices.intro" 
                  @change="onServices"
                  placeholder="introduce your service"
                 ><br>
          <input type="text" 
                  required 
                  v-model="ObjServices.price" 
                  @change="onServices"
                  placeholder="service price by hour"
                 ><br>
          <input type="email" 
                  required 
                  v-model="ObjServices.email" 
                  @change="onServices"
                  placeholder="Add email"
                 ><br>
          <input type="number" 
                  required 
                  v-model="ObjServices.phone" 
                  @change="onServices"
                  placeholder="Add phone"
                 ><br>
          <input type="text" 
                  required 
                  v-model="ObjServices.city" 
                  @change="onServices"
                  placeholder="Add city"
                 >
                 <br><br>
          <textarea name="textarea" 
                  required 
                  v-model="ObjServices.textarea" 
                  @change="onServices"
                  placeholder="describe your services"
                 ></textarea>                            
       </section>
       <section class="modal-body">
          select category services!
          <section>
          <select class="select" @onchanged="CategoryObj" v-model="selectedCategory">
          <option value="">select Category service</option>
          <option v-for="(index) in CategoryObj.cat_id" :key="index.code" :value="index.code">
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
      'change', 'changedPasswordEmail', 
      'changedObjServices', 'closeModal', 
      'changed', 'uploaded', 'onchanged', 
      'changedObj', 'handleClick'
    ],
    props:{
      ObjServices:{
        type:Object,
        required: true
      },
      uploadPicture:{
        type: String,
        default:''
      },
      CategoryObj:{
        type: Array,
       default:[]
      }
    },
    data(){
      return{
        selectedCategory:'',
      }
    },
    methods: {
      closeModal() {
        this.$emit('closeModal');
      },
      upload(event){
        console.log('image',  event.target.value)
        this.$emit('uploaded', event.target.value)
        console.table('Image', event.target.files[0])
        const reader= new FileReader()
        reader.readAsDataURL(event.target.files[0])
        reader.onload= (e)=>{
          this.uploadPicture= e.target.result
        }
      },
      ObjCategory(event){
        console.log(event.target.value)
        this.$emit('changedObj', JSON.stringify(event.target.value))
        localStorage.setItem('cat_name', this.selectedCategory.name)
        console.log(this.selectedCategory.name)
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
      },
    },
  };
</script>
<style>
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
    position: absolute;
    top: 0em;
    left: 6em;
  }
</style>