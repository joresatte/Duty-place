import config from "@/config";
import { v4 as uuidv4 } from "uuid";

async function postRequest (name, email, subject, comments){
    const id = uuidv4()
    const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id: id,
            name: name,
            email: email,
            subject: subject,
            comments: comments
        }),
      }
      const response= await fetch(`${config.api_Path}/request`, settings)
            return response

}
export default postRequest