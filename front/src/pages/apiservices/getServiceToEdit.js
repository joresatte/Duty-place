import config from "@/config.js";

export async function getServiceToEdit(id, catId, text){
    return await fetch(`${config.api_Path}/services/user_services/${id}/${catId}/${text}`)
            .then(res => res.json())
            .catch(err=> console.log(err.message))
}