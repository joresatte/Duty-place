<template>
  <div class="field">
    <div class="password">
      <input
        type="password"
        placeholder="Password"
        autocomplete="off"
        :value="renewPassword"
        @keyup="validateInput"
        @blur="validateInput"
        @change="PasswordChanged"
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
  name:'LoginPassword',
  props:{
    renewPassword:{
       type: String,
       required: true,
    }
  },
  emits:['change', 'ChangedPassword'],
  setup(props, context) {
    let password = ref("");
    const {validatePasswordField, errors } = usePasswordValidation();
    const validateInput = () => {
        validatePasswordField("password", password.value);
    };
    const PasswordChanged=(event)=>{
        console.log(event)
        context.emit('ChangedPassword', event.target.value)
    }
     return { password, errors, PasswordChanged, validateInput };
  },
};
</script>