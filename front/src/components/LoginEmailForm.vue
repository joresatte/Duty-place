<template>
  <div class="field">
    <div class="ui left icon input big">
      <i class="email icon"></i>
      <InputText
        type="email"
        placeholder="Email"
        autocomplete="off"
        :value="renewEmail"
        @keyup="validateInput"
        @blur="validateInput"
        @change="ChangedEmail"
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
  name: 'LoginEmail',
  emits:['change', 'EmailChanged'],
  props:{
    renewEmail:{
      type: String,
      required: true,
    }
  },
  setup(props, context) {
    let email = ref("");
    const { validateEmailField, errors } = useEmailValidation();
    const validateInput = () => {
      validateEmailField("email", email.value);
    };
    const ChangedEmail= (event)=>{
        console.log(event.target.value)
        context.emit('EmailChanged', event.target.value)

    }
    return { email, errors, ChangedEmail, validateInput };
  },
};
</script>