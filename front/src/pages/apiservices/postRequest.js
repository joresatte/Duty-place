import config from "@/config";

async function postRequest (id, name, subject, comments){
    const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id: id,
            name: name,
            subject: subject,
            comments: comments,
        }),
      }
      const response= await fetch(`${config.api_Path}/login/Authenticated`, settings)
            return response

}
export default postRequest