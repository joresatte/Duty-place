<template>
<router-link to="/contact/add" ><button>add contact</button></router-link><br><br>
  <section class="contact-list">
    <article
      class="contact-item"
      v-for="contact in contacts"
      :key="contact.phone"
    >
    <h2>{{ contact.first_name }}</h2>
    <p>{{ contact.last_name }}</p>
    <p>{{ contact.phone }}</p><br>
    <router-link :to="{name:'contactdetails', params:{id: contact.id}}" ><button>detaills</button></router-link><br><br>
    <button class="remove" @click="del(contact)" >remove contact</button>
    </article>
  </section>
</template>

<script>
import { useStorage } from "@vueuse/core";
import Swal from 'sweetalert2';
import config from "@/config.js"
export default {
  name: "contacts",
  data() {
    return {
      contacts: [],
      localUser: useStorage("user", {}),
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const settings = {
        method: "GET",
        headers: {
          Authorization: this.localUser.id
        },
      };
      const response = await fetch(`${config.API_PATH}/contact`, settings);
      this.contacts = await response.json();
    },
    async del(contact){
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
          fetch(`${config.API_PATH}/contact/${contact.id}`, {method: "DELETE"})
          this.loadData(fetch(`${config.API_PATH}/contact`))
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
        )
      }
    })
    }
  },
};
</script>

<style scoped>
h1 {
  font-style: italic;
}
.contact-item {
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>
