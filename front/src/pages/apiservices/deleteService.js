import config from "@/config.js";

export async function deleteService(serviceId, serviceCatId){
    const settings = {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      };
    return await fetch(`${config.userService_Path}/user_services/${serviceId}/${serviceCatId}`, settings, {method: "DELETE"}),
           await fetch(`${config.userService_Path}/by-category/${serviceId}/${serviceCatId}`, settings, {method: "DELETE"})
   
}
