<template>
  <h1>Services By Category Page</h1>
  <p>{{category_id}} </p>
  <section>
 <h2>{{services.user_name}}</h2>
  <p>{{services.phone}}</p>
  <p>{{services.email}}</p>
  <p>{{services.city}}</p>
  </section>

</template>

<script>
import config from "@/config.js";
export default {
  name: 'ServicesByCategoryPage',
  props:['category_id'],
  data(){
    return{
      services: [],
    }
  },
  async mounted(){
    await fetch(`${config.route_Path}/services/by-category/` + this.category_id)
    .then(res => res.json())
    .then(data => this.services = data)
    .catch(err=> console.log(err.message))
  }

}
</script>

<style>

</style>