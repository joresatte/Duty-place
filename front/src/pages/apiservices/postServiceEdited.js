import config from "@/config.js";

async function postServiceEdited(
    id,
    cat_id,
    user_name,
    text,
    intro,
    price,
    text_pictures,
    textarea,
    phone,
    email,
    city
){ 
    const settings = {
        method: "PUT",
        headers: {
           "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id: id,
            cat_id: cat_id,
            user_name: user_name,
            text: text,
            intro: intro,
            price: price,
            text_pictures: text_pictures,
            textarea: textarea,
            phone: phone,
            email: email,
            city: city
        }),
      };
    return await fetch(`${config.userService_Path}/by-category/${id}/${cat_id}/${text}`, settings),
           await fetch(`${config.userService_Path}/user_services/${id}/${cat_id}/${text}`, settings)
           .catch(err=> console.log(err.message))
     
  }
  export default postServiceEdited