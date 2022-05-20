import config from "@/config.js";

export async function deleteService(serviceId, serviceCatId){
    const settings = {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      };
    return await fetch(`${config.API_PATH}/by-category/${serviceId}/${serviceCatId}`, settings, {method: "DELETE"}),
           await fetch(`${config.API_PATH}/user_services/${serviceId}/${serviceCatId}`, settings, {method: "DELETE"})
      .catch(err=> console.log(err.message))
}
