<template>
  <div class="field">
    <div class="ui left icon input big">
      <i class="email icon"></i>
      <input
        type="email"
        placeholder="Email"
        autocomplete="off"
        :value="email.email"
        @keyup="validateInput"
        @blur="validateInput"
        @changed="onEmailChanged"
      />
    </div>
    <div class="ui basic label pointing red" v-if="errors.email">
      {{ errors.email }}
    </div>
  </div>
</template>
 <script>
import { ref, watchEffect } from "vue";
import useEmailValidation from "./useEmailValidation.js";
export default {
  props:{
    email:{
      type: String,
      required: true,
    }
  },
  emits:['changed'],
  setup(props, context) {
    let email = ref("");
    const { validateEmailField, errors } = useEmailValidation();
    const validateInput = () => {
      validateEmailField("email", email.value);
    };
    watchEffect([email], (newVal) => {
        console.log(newVal);
        onEmailChanged=()=>{
          context.emit("changed", {newVal})
       }
    })
    
    return { email, errors, validateInput };
  },
};
</script>