import config from "@/config.js";

export async function getCategories(){
    return await fetch(`${config.api_Path}/categories`)
            .then(res => res.json())
            .catch(err=> console.log(err.message))

}

export async function getCategoriesServices(category_id){
    return await fetch(`${config.api_Path}/services/by-category/${category_id}`)
            .then(res => res.json())
            .catch(err=> console.log(err.message))
}

export async function getUserServices(id){
    return await fetch(`${config.api_Path}/services/user_services/${id}`)
            .then(res => res.json())
            .catch(err=> console.log(err.message))
}