
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
         {{ObjServices.cat_id}}
        <slot name="body">
          select category services!
          <!-- <select name="" @change="onServices" v-model="selectedCategory" :reduce='name => name.code'> 
            <option value="">select Category service</option>
            <option v-for="index in ObjServices[8]" :value="index.code" :key="index">
              {{index}}
            </option>
           </select> -->
           <section>
           <select name="name" @change="onServices" v-model="selectedCategory" :reduce='name => name.code'>
          <option value="">select Category service</option>
          <option v-for="index in ObjServices.cat_id" :key="index.code" :value="index" :selected="name=index" >
          {{index.name}}
          </option>
          </select>
           </section>
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
    emits:['change', 'changedPasswordEmail', 'closeModal'],
    props:{
      ObjServices:{
        type:Object,
        required: true
      },
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
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          text_pictures: event.target.value,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          intro: this.event.target.value,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          price: this.event.target.value,
        })
      },
       onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          textarea: this.event.target.value,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          email: this.event.target.value,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          phone: this.event.target.value,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          city: this.event.target.value,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          user_name: this.event.target.value,
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedObjServices', {
          cat_id: this.event.target.value,
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