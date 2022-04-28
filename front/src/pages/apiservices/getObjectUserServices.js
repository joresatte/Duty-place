import config from "@/config.js";

function objectUserServices(){
    const settings = {
        method: "GET",
        headers: {
           "Content-Type": "application/json",
        },
      };
      return fetch(`${config.userService_Path}/object_services}`, settings)
              .then(async response => await response.json())
              .catch(err=> console.log(err.message))  
  }
  export default objectUserServices