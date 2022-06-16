<template>
<div >
<span class="h">
   <Button
      style="color:aliceblue;"
      class="p-button-outlined p-button-success"
      type="button"
      label="Services"
      icon="pi pi-home" iconPos="left"
      @click="backToHomePage">
   </Button>
</span>
</div>
</template>

<script>
export default {
   name: 'headerNav',
   data(){
      return{

      }
   },
   methods:{
      backToHomePage(){
         this.$router.push({path: '/'})
      }
   }
}
</script>

<style scoped>
.h{
 position: absolute;
 top: 0em;
 left: 0;
 color: white;
 font-size: 1em;
 border-radius: 2px;
 text-decoration: none;
 padding: 0.2em;
}
</style>