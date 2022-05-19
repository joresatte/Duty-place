import config from "@/config.js";


export async function deleteService(serviceId, serviceCatId){
    const settings = {
        method: "DELETE",
        headers: {
          Authorization: getUserId(contactId),
        },
      };
    return await fetch(`${config.API_PATH}/by-category/<id>/<cat_id>/${serviceId}/${serviceCatId}`, settings, {method: "DELETE"}),
           await fetch(`${config.API_PATH}/user_services/<id>/<cat_id>/${serviceId}/${serviceCatId}`, settings, {method: "DELETE"})
      .then(res => res.json())
      .catch(err=> console.log(err.message))
}
