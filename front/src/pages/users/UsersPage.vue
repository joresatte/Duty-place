<template>
<userForm :users="user"/>
  <h1> users pages</h1>
</template>

<script>
import { ref, onMounted } from '@vue/reactivity'
import userForm from '@/components/userForm.vue'
export default {
  name: 'userPage',
  components:{userForm},
  setup(){
    const user= ref([])
    const loadData= async()=>{
      user.value= await loginFetch()
    }
    onMounted(()=> loadData)
    return {user, loadData}
  }

}
</script>

<style>

</style>