export default function useValidators() {

    const isEmpty = (fieldName, fieldValue) => {
        return !fieldValue ? "The " + fieldName + " field is required" : "";
    }

    const minLength = (fieldName, fieldValue, min) => {
        return fieldValue.length < min ? `The ${fieldName} field must be atleast ${min} characters long` : "";
    }

    const isEmail = (email, newEmail) => {
        let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return !re.test(newEmail) ? "This email is not a valid " + email + " address" : "";
    }
    return { isEmpty, minLength, isEmail }
}