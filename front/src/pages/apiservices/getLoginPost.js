import config from "@/config.js";

function getLoginPost (email, password){
    const settings = {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        email: email,
        password: password,
    }),
  }
  return fetch(`${config.login_Path}/login/Authenticated`, settings)
            .then(async response => await response.json())
            .catch(err=> console.log(err.message))
}
export default getLoginPost

