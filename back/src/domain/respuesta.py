response_user_service = [{
         "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas",
        "price": "por 7$ la hora",
        "text_pictures": "foto",
        "textarea": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao",
        
    },
    {
         "id": "service_2",
        "cat_id": "category_2",
        "user_name": "oshulem0",
        "text": "Limpiezas",
        "intro": "disponible para todo tipos de limpiezas",
        "price": "por 8$ la hora",
        "text_pictures": "foto",
        "textarea": "Limpiezas",
        "phone": "424-639-9574",
        "email": "fbadland0@bizjournals.com",
        "city": "Tayirove",
        
    },
    {
         "id": "service_50",
        "cat_id": "category_2",
        "user_name": "zegerton1",
        "text": "Limpiezas",
        "intro": "todo tipos de limpiezas",
        "price": "por 6$ la hora",
        "text_pictures": "foto",
        "textarea": "Limpiezas",
        "phone": "382-214-1560",
        "email": "wglenister1@latimes.com",
        "city": "Al Burayqah",
    }
    ]

response_get_service= [
    {
         "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas",
        "price": "por 7$ la hora",
        "text_pictures": "foto",
        "textarea": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao",
    }
]

response_category_list= [{
        "cat_id": "category_1",
        "text": "Mudanzas",
        "text_pictures": "text_pictures",
        
    },
    {
        "cat_id": "category_2",
        "text": "Limpiezas",
        "text_pictures": "text_pictures",
        
    },
]
regist_request= {
    "id": "service_1",
    "email": "reinabo@vince.com",
    "password": "password1",
    }
another_regist_request= {
    "id": "service_3",
    "email": "@vince.com",
    "password": "password1",
    }
login_request= {
    "email": "reinabo@vince.com",
    "password": "password1",
    }

login_response= {
    "id": "service_1",
    # "email": "reinabo@vince.com",
    }

another_login_request= {
    "email": "reinabo@vince.com",
    "password": "password50",
    }

regist_response= {
    "id": "service_1",
    # "email": "reinabo@vince.com",
    }

another_one_login_request= {
    "email": "fbadland0@bizjournals.com",
    "password": "password50",
    }

data_service={
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vince",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas",
        "price": "por 7$ la hora",
        "text_pictures": "foto",
        "textarea": "Mudanzas",
        "phone": "024-639-2574",
        "email": "reinabo@vince.com",
        "city": "Bilbao",
    }

response_service=[
     {
         "id": "service_2",
        "cat_id": "category_2",
        "user_name": "oshulem0",
        "text": "Limpiezas",
        "intro": "disponible para todo tipos de limpiezas",
        "price": "por 8$ la hora",
        "text_pictures": "foto",
        "textarea": "Limpiezas",
        "phone": "424-639-9574",
        "email": "fbadland0@bizjournals.com",
        "city": "Tayirove",
        
    },
    {
         "id": "service_50",
        "cat_id": "category_2",
        "user_name": "zegerton1",
        "text": "Limpiezas",
        "intro": "todo tipos de limpiezas",
        "price": "por 6$ la hora",
        "text_pictures": "foto",
        "textarea": "Limpiezas",
        "phone": "382-214-1560",
        "email": "wglenister1@latimes.com",
        "city": "Al Burayqah",
    }
]

updated=[
{
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vincen",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas en toda españa",
        "price": "por 5$ la hora",
        "text_pictures": "foto",
        "textarea": " profesionales en el sector de las Mudanzas",
        "phone": "024-679-2574",
        "email": "reinabes@vince.com",
        "city": "españa",
    }
]

updater={
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vincen",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas en toda españa",
        "price": "por 5$ la hora",
        "text_pictures": "foto",
        "textarea": " profesionales en el sector de las Mudanzas",
        "phone": "024-679-2574",
        "email": "reinabes@vince.com",
        "city": "españa",
    }

another_updater={
        "id": "service_2",
        "cat_id": "category_2",
        "user_name": "vincen",
        "text": "Mudanzas",
        "intro": "Realizamos mudanzas en toda españa",
        "price": "por 5$ la hora",
        "text_pictures": "foto",
        "textarea": " profesionales en el sector de las Mudanzas",
        "phone": "024-679-2574",
        "email": "reinabes@vince.com",
        "city": "españa",
    }

another_one_updater={
        "id": "service_1",
        "cat_id": "category_1",
        "user_name": "vincen",
        "text": "Limpiezas",
        "intro": "Realizamos mudanzas en toda españa",
        "price": "por 5$ la hora",
        "text_pictures": "foto",
        "textarea": " profesionales en el sector de las Mudanzas",
        "phone": "024-679-2574",
        "email": "reinabes@vince.com",
        "city": "españa",
    }


# {
#     'id': user_service.id,
#     'cat_id': user_service.cat_id,
#     'user_name': user_service.user_name,
#     'text': user_service.text,
#     'intro': user_service.intro,
#     'price': user_service.price,
#     'text_pictures': user_service.text_pictures,
#     'textarea': user_service.textarea,
#     'phone': user_service.phone,
#     'email': user_service.email,
#     'city': user_service.city
# },

#  json.loads( 
#                 cat_id= item["cat_id"],
#                 user_name= item["user_name"],
#                 text= item["text"],
#                 intro= item["intro"],
#                 price= item["price"],
#                 text_pictures= item["text_pictures"],
#                 textarea= item['textarea'],
#                 phone= item["phone"],
#                 email= item["email"],
#                 city= item["city"],)
#             )

#  {
#                 'cat_id': json.dumps(user_service['cat_id']),
#                 'user_name': json.dumps(user_service['user_name']),
#                 'text': json.dumps(user_service['text']),
#                 'intro': json.dumps(user_service['intro']),
#                 'price': json.dumps(user_service['price']),
#                 'text_pictures': json.dumps(user_service['text_pictures']),
#                 'textarea': json.dumps(user_service['textarea']),
#                 'phone': json.dumps(user_service['phone']),
#                 'email': json.dumps(user_service['email']),
#                 'city': json.dumps(user_service['city'])
# },