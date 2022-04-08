import { reactive } from "@vue/reactivity";
const errors = reactive({});
import useValidators from './validators'

export default function useEmailValidation() {
    const { isEmpty, isEmail } = useValidators();
    
    const validateEmailField = (email, emailValue) => {
        errors[email] = !emailValue ? isEmpty(email, emailValue) : isEmail(email, emailValue)
    }
    return { errors, validateEmailField }
}