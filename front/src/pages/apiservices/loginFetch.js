import config from "@/config.js";
import { reactive, ref } from "vue";

async function  loginFetch(){
    const settings = reactive({
        method: "GET",
        headers: {
           "Content-Type": "application/json",
        },
      });
      const response = ref (await fetch(`${config.userService_Path}/user_services/${localStorage.getItem('user')}`, settings));
      const contacts = ref (await response.value.json());
      return {contacts, response, settings } 
}
export default loginFetch