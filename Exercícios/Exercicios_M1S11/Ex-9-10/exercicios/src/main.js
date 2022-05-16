import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'
import store from '@/store'
import VueToast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
import VueLoading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

const app = createApp(App);

app.use(router);
app.use(store);
app.use(VueToast);
app.use(VueLoading);
app.mount('#app');
