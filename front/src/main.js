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
import Toolbar from 'primevue/toolbar';
import Sidebar from 'primevue/sidebar';
import Tooltip from 'primevue/tooltip';
import FileUpload from 'primevue/fileupload';

const app= createApp(App);
app.use(ToastService);
app.use(PrimeVue)
app.use(router)
app.directive('tooltip', Tooltip);

app.component('Button', Button)
app.component('Toast', Toast)
app.component('InputText', InputText)
app.component('Toolbar', Toolbar)
app.component('Sidebar', Sidebar)
app.component('FileUpload', FileUpload)

app.mount('#app')