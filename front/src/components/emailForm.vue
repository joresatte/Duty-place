<template>
  <div class="field">
    <div class="ui left icon input big">
      <i class="email icon"></i>
      <input
        type="email"
        placeholder="Email"
        autocomplete="off"
        :value="newEmail"
        @keyup="validateInput"
        @blur="validateInput"
        @change="onChangedEmail"
      />
    </div>
    <div class="ui basic label pointing red" v-if="errors.email">
      {{ errors.email }}
    </div>
  </div>
</template>
 <script>
import { ref} from "vue";
import useEmailValidation from "./useEmailValidation.js";
export default {
  props:{
    newEmail:{
      type: String,
      required: true,
    }
  },
  emits:['change'],
  setup(props, context) {
    let email = ref("");
    const { validateEmailField, errors } = useEmailValidation();
    const validateInput = () => {
      validateEmailField("email", email.value);
    };
    const onChangedEmail= (event)=>{
        console.log(event)
        context.emit('onEmailChanged', localStorage.setItem("registEmail", event.target.value))

    }
    return { email, errors, onChangedEmail, validateInput };
  },
};
</script>