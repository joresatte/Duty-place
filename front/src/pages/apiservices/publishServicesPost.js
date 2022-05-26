import config from "@/config.js";
import { reactive, ref } from "vue";

async function PublishServices(
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
        method: "POST",
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
      return await fetch(`${config.api_Path}/services/user_services`, settings),
             await fetch(`${config.api_Path}/services/by-category`, settings)
                    .catch(err=> console.log(err.message))
     
  }
  export default PublishServices

//   export async function PublishServices(
//     cat_id,
//     user_name,
//     text,
//     intro,
//     price,
//     text_pictures,
//     textarea,
//     phone,
//     email,
//     city
//   ){
//     const settings = {
//         method: "POST",
//         headers: {
//            "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//             id: getUserId(),
//             cat_id: cat_id,
//             user_name: user_name,
//             text: text,
//             intro: intro,
//             price: price,
//             text_pictures: text_pictures,
//             textarea: textarea,
//             phone: phone,
//             email: email,
//             city: city
//         }),
//       };
//     return  await fetch(`${config.api_Path}/services/user_services}`, settings),
//             await fetch(`${config.api_Path}/services/by-category}`, settings)
//               .catch(err=> console.log(err.message))
// }

