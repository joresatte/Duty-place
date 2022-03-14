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
      category_id: this.$route.params.category_id
    }
  }

}
</script>

<style>

</style>