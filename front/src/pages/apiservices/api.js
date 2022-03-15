import config from "@/config.js";

export async function getCategories(){
    return fetch(`${config.router_Path}/categories`)
            .then(res => res.json())
            .catch(err=> console.log(err.message))

}

export async function getCategoriesServices(category_id){
    return fetch(`${config.router_Path}/services/by-category/${category_id}`)
            .then(res => res.json())
            .catch(err=> console.log(err.message))
}