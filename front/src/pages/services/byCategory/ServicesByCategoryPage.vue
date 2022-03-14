<template>
  <h1>Services By Category Page</h1>
  <p>{{category_id}} </p>
</template>

<script>
export default {
  name: 'ServicesByCategoryPage',
  props:['category_id'],
  data(){
    return{
      categoryServices: [],
    }
  },
  async mounted(){
    await fetch(`${config.route_Path}/services/by-category/` + this.category_id)
    .then(res => res.json())
    .then(data => this.categoryServices = data)
    .catch(err=> console.log(err.message))
  }

}
</script>

<style>

</style>