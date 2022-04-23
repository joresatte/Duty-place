
<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          login the default title!
        </slot>
        <button
          type="button"
          class="btn-close"
          @click="closeModal"
        >
          x
        </button>
      </header>

      <section class="modal-body">
        <slot name="body">
          login the default body!
          <input type="file" 
                  accept="image/png, image/jpeg"
                  required 
                  :value="ObjServices.text_pictures" 
                  @change="onServices"
                >
        </slot>
       </section>
       <br>
       <section class="modal-body">
        <slot name="body">
          login the default body!
          <input type="password" 
                  required 
                  :value="ObjServices.user_name" 
                  @change="onServices"
                 >    
          <input type="password" 
                  required 
                  :value="ObjServices.intro" 
                  @change="onServices"
                 >
          <input type="password" 
                  required 
                  :value="ObjServices.price" 
                  @change="onServices"
                 >
          <input type="password" 
                  required 
                  :value="ObjServices.textarea" 
                  @change="onServices"
                 >
          <input type="password" 
                  required 
                  :value="ObjServices.email" 
                  @change="onServices"
                 >
          <input type="password" 
                  required 
                  :value="ObjServices.phone" 
                  @change="onServices"
                 >
          <input type="password" 
                  required 
                  :value="ObjServices.city" 
                  @change="onServices"
                 >                             
        </slot>
       </section>
       <br>
       <section class="modal-body">
        <slot name="body">
          login the default body!
          <v-select 
          v-model="selectedCategory"
          :options='ObjServices.cat_id'
          :reduce='name => name.code'
          aria-placeholder="select category services">

          </v-select>
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
          log in 
        </button>
        <br>
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
        selectedCategory:''
      }
    },
    methods: {
      closeModal() {
        this.$emit('closeModal');
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedEmailPassword', {
          email: event.target.value,
          password: this.SignUp.email
        })
      },
      onServices(event){
        console.log(event.target.value)
        this.$emit('changedEmail', {
          email: this.SignUp.email,
          password: event.target.value
        })
      },
      handleClick(){
        console.log(this.handleRegist)
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
    padding: 15px;
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
    padding: 20px 10px;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
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
  }
</style>