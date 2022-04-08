<template>
  <div class="field">
    <div class="password">
      <input
        type="password"
        placeholder="Password"
        autocomplete="off"
        :value="password.password"
        @keyup="validateInput"
        @blur="validateInput"
        @change="onPasswordChanged"
      />
    </div>
    <div class="ui basic label pointing red" v-if="errors.password">
      {{ errors.password }}
    </div>
  </div>
</template>

 <script>
import { ref, watchEffect } from "vue";
import useFormValidation from "./useFormValidation";
export default {
  props:{
    password:{
       type: String,
       required: true,
    }
  },
  emits:['change'],
  setup(props, context) {
    let password = ref("");
    const { validatePasswordField, errors } = useFormValidation();
    const validateInput = () => {
      validatePasswordField("password", password.value);
    };
    watchEffect([password],(newValue)=>{
       console.log(newValue);
       onPasswordChanged=()=>{
            context.emit('change', newValue)
       }
    })
     return { password, errors, validateInput };
  },
};
</script>