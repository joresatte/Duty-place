import { reactive, ref } from "vue";
import config from "@/config.js";

function getLoginPost (){
    const email= ref(localStorage.getItem("loginEmail"))
    const password= ref(localStorage.getItem("loginPassword"))
    const settings = reactive( {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        email: email.value,
        password: password.value,
    }),
  })
  const response = ref( fetch(`${config.login_Path}/login/Authenticated`, settings));
  return {response, email, password}

}
export default getLoginPost