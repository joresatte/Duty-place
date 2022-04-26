
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
                  :value="ObjServices.text_pictures" 
                  @change="onServices"
                  title="Select file"
                >
                <label for="select file"></label>
        </slot>
       </section>
       <section class="modal-body">
        <slot name="body">
          <input type="password" 
                  required 
                  :value="ObjServices.user_name" 
                  @change="onServices"
                  placeholder="User Name"
                 > <br>   
          <input type="password" 
                  required 
                  :value="ObjServices.intro" 
                  @change="onServices"
                  placeholder="introduce your service"
                 ><br>
          <input type="password" 
                  required 
                  :value="ObjServices.price" 
                  @change="onServices"
                  placeholder="service price by hour"
                 ><br>
          <input type="password" 
                  required 
                  :value="ObjServices.email" 
                  @change="onServices"
                  placeholder="Add email"
                 ><br>
          <input type="password" 
                  required 
                  :value="ObjServices.phone" 
                  @change="onServices"
                  placeholder="Add phone"
                 ><br>
          <input type="password" 
                  required 
                  :value="ObjServices.city" 
                  @change="onServices"
                  placeholder="Add city"
                 >
                 <br><br>
          <textarea type="password" 
                  required 
                  :value="ObjServices.textarea" 
                  @change="onServices"
                  placeholder="describe your services"
                 ></textarea><br>                             
        </slot>
       </section>
       <section class="modal-body">
        <slot name="body">
          select category services!
          <select name="" @change="onServices" v-model="selectedCategory" :reduce='name => name.code'> 
            <option value="">select Category service</option>
            <option v-for="item in ObjServices.cat_id" :value="item" :key="item.code">
              {{item.name}}
            </option>
        </select>
        </slot>
       </section>
      <footer class="modal-footer">
        <slot name="footer">
          This is the default footer!
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
    emits:['change', 'changedPasswordEmail', 'changedObjServices', 'closeModal'],
    props:{
      ObjServices:{
        type:Object,
        required: true
      },
    },
    data(){
      return{
        selectedCategory:''
      }
    },
    methods: {
      closeModal() {
        this.$emit('closeModal');
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          text_pictures: event.target.value,
          cat_id: this.ObjServices.cat_id,
          intro: this.ObjServices.intro,
          price: this.ObjServices.price,
          textarea: this.ObjServices.textarea,
          email: this.ObjServices.email,
          phone: this.ObjServices.phone,
          city: this.ObjServices.city,
          user_name: this.ObjServices.user_name,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          intro: event.target.value,
          text_pictures: this.ObjServices.text_pictures,
          cat_id: this.ObjServices.cat_id,
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
          text_pictures: ObjServices.text_pictures,
          cat_id: this.ObjServices.cat_id,
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
          text_pictures: ObjServices.text_pictures,
          cat_id: this.ObjServices.cat_id,
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
          text_pictures: ObjServices.text_pictures,
          cat_id: this.ObjServices.cat_id,
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
          text_pictures: ObjServices.text_pictures,
          cat_id: this.ObjServices.cat_id,
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
          text_pictures: ObjServices.text_pictures,
          cat_id: this.ObjServices.cat_id,
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
          text_pictures: ObjServices.text_pictures,
          cat_id: this.ObjServices.cat_id,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          cat_id: event.target.value,
          user_name: this.ObjServices.user_name,
          city: this.ObjServices.city,
          phone: this.ObjServices.phone,
          email: this.ObjServices.email,
          textarea: this.ObjServices.textarea,
          price: this.ObjServices.price,
          intro: this.ObjServices.intro,
          text_pictures: this.ObjServices.text_pictures,
        })
      },
      handleClick(){
        console.log(this.handleClick)
        this.$router.go({
          path: '/about',
          name: 'About',
        })
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
</style>