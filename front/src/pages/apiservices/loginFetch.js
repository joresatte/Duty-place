import config from "@/config.js";
import { reactive, ref } from "vue";
// import axios from 'axios';

function getUserId() {
  const userJson = localStorage.getItem("dataUser");
  const user = JSON.parse(userJson);
  return user.id;
}

function loginFetch(){
  const userId= getUserId()
  const settings = {
      method: "GET",
      headers: {
         "Content-Type": "application/json",
      },
    };
    return fetch(`${config.userService_Path}/user_services/${userId}`, settings)
            .then(async response => await response.json())
            .catch(err=> console.log(err.message))
   
}
export default loginFetch
