<template>
<!-- <h1>contact.id</h1> -->
  <section class="contact-details">
  <h2>{{ contact.first_name }}</h2>
  <p>{{ contact.last_name }}</p>
  <p>{{ contact.full_name }}</p>
  <p>{{ contact.email }}</p>
  <p>{{ contact.phone }}</p>
  <br><br>
  |<router-link :to="{name:'contactdetails'}" @click="removeContact" ><button>remove contact</button></router-link>|
  |<router-link :to="{name: 'contactsPage'}"><button>Pagina anterior</button></router-link>|
  </section>
</template>

<script>
import { useStorage } from "@vueuse/core";
import config from "@/config.js"
import Swal from 'sweetalert2';
window.Swal= Swal;
export default {
  name:'contactdetails',
  props:['id'],
  data() {
    return {
      contact: [],
      Response:'',
      localUser: useStorage("user", {}),
    };
  },
  async mounted() {
    let contactId = this.id;
    const settings = {
        method: "GET",
        headers: {
          Authorization: this.localUser.id,
        },
      };
    const response= await fetch(`${config.API_PATH}/contact/${contactId}`, settings)
    this.contact= await response.json();
  },
  methods:{
    removeContact(){
          Swal.fire({
      title: 'estas seguro?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {
          this.Response= fetch(`${config.API_PATH}/contact/${this.id}`, {method: "DELETE"});
          this.$router.push('/contact')
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
        )
      }
    })
     
    }
  }
}
</script>

<style scoped>
.contact-details {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>