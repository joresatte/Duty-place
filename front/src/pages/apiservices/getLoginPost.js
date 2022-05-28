import config from "@/config.js";

async function getLoginPost (email, password){
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
  const response= await fetch(`${config.login_Path}/login/Authenticated`, settings)
        return response
            
}
export default getLoginPost

