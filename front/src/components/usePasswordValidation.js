import { reactive } from "@vue/reactivity";
const errors = reactive({});
import useValidators from './validators'

export default function usePasswordValidation() {
    const { isEmpty, minLength } = useValidators();
    const validatePasswordField = (password, passwordValue) => {
        errors[password] = !passwordValue ? isEmpty(password, passwordValue) : minLength(password, passwordValue, 8)
    }
   
    return { errors, validatePasswordField }
}