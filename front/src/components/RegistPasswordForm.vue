<template>
  <div class="field">
    <div class="password">
      <InputText
        type="password"
        placeholder="Password"
        autocomplete="off"
        :value="newPassword"
        @keyup="validateInput"
        @blur="validateInput"
        @change="onChangedPassword"
        v-tooltip.bottom="'password is required not less than 7 characters'" 
      />
    </div>
    <div class="ui basic label pointing red" v-if="errors.password">
      {{ errors.password }}
    </div>
  </div>
</template>

 <script>
import { ref} from "vue";
import usePasswordValidation from "./usePasswordValidation";
export default {
  props:{
    newPassword:{
       type: String,
       required: true,
    }
  },
  emits:['change', 'onPasswordChanged'],
  setup(props, context) {
    let password = ref("");
    const {validatePasswordField, errors } = usePasswordValidation();
    const validateInput = () => {
        validatePasswordField("password", password.value);
    };
    const onChangedPassword=(event)=>{
        console.log(event)
        context.emit('onPasswordChanged', event.target.value)
    }
     return { password, errors, onChangedPassword, validateInput };
  },
};
</script>