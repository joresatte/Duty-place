import config from "@/config.js";
import getCurrentUser from './getCurrentUser.js'

function loginFetch(){
  const userId= getCurrentUser()
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
