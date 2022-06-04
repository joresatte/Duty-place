import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';

import Button from 'primevue/button';
import 'primevue/resources/themes/saga-blue/theme.css'
import 'primevue/resources/primevue.min.css'                
import 'primeicons/primeicons.css'
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';

const app= createApp(App);
app.use(ToastService);
app.use(PrimeVue)
app.use(router)

app.component('Button', Button)
app.component('Toast', Toast)
app.component('InputText', InputText)

app.mount('#app')