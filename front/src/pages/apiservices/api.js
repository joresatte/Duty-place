import config from "@/config.js";

/*
export async function getCategories(){
    const response = await fetch(`${config.router_Path}/categories`);
    return await response.json(); 

}
*/
export async function getCategories(){
    return fetch(`${config.router_Path}/categories`)
            .then(res => res.json())
            .catch(err=> console.log(err.message))

}