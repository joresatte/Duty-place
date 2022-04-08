import { reactive, ref } from "vue";
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";

function getRegistPost (){
    const email= ref('')
    const password= ref('')
    const id = ref(uuidv4())
    const settings = reactive( {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        id: id.value,
        email: email.value,
        password: password.value,
    }),
  })
  const response = ref( fetch(`${config.regist_Path}/regists`, settings));
  return {response, email, password}

}
export default getRegistPost