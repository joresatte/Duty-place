<template>
  <div class="field">
    <div class="ui left icon input big">
      <InputText
        type="email"
        icon="pi pi"
        placeholder="Email"
        autocomplete="off"
        :value="newEmail"
        @keyup="validateInput"
        @blur="validateInput"
        @change="onNewEmailChanged"
        v-tooltip.bottom="'email is required and should be like exemple@exemple.es'" 
      />
    </div>
    <div class="ui basic label pointing red" >
      {{msg }}
    </div>
  </div>
</template>
 <script>
 import Swal from 'sweetalert2'
export default {
  emits:['change', 'onEmailChanged'],
  props:{
    newEmail:{
      type: String,
      required: true,
    }
  },
  data(){
    return{
      msg:'required example@example.es',
    }
  },
  methods:{
    validateInput(){
      const reEmail= RegExp("[a-zA-Z0-9!#$%&'*_+-]([\.]?[a-zA-Z0-9!#$%&'*_+-])+@[a-zA-Z0-9]([^@&%$\/()=?¿!.,:;]|\d)+[a-zA-Z0-9][\.][a-zA-Z]{2,4}([\.][a-zA-Z]{2})?")
      if(this.newEmail==null|| this.newEmail == ''){
        this.msg='Email field is required'
      }else if(!reEmail.test(this.newEmail)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'please enter a correct Email',
            footer: '<a href="http://localhost:8080/">the email and password fields are required</a>'
          })
      }else{
        this.msg= ("the email " + valor + " correct")
      }
    },
    onNewEmailChanged(event){
      console.log(event.target.value)
      this.$emit('onEmailChanged', event.target.value)
    },
  }
};
</script>