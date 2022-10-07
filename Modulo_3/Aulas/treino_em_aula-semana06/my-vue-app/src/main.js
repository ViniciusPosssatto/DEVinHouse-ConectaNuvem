import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

createApp(App)
  .use(vuetify)
  .mount('#app')

// // Import the functions you need from the SDKs you need
// import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
// // TODO: Add SDKs for Firebase products that you want to use
// // https://firebase.google.com/docs/web/setup#available-libraries

// // Your web app's Firebase configuration
// // For Firebase JS SDK v7.20.0 and later, measurementId is optional
// const firebaseConfig = {
//   apiKey: "AIzaSyB-IjlaPaA84_tLwDp-qcnfHNp46ClatoQ",
//   authDomain: "sample-devhouse-1ded3.firebaseapp.com",
//   databaseURL: "https://sample-devhouse-1ded3-default-rtdb.firebaseio.com",
//   projectId: "sample-devhouse-1ded3",
//   storageBucket: "sample-devhouse-1ded3.appspot.com",
//   messagingSenderId: "283533561588",
//   appId: "1:283533561588:web:84bbd6bb02ec7ab29858a1",
//   measurementId: "G-WKHQ6KHWBV"
// };

// // Initialize Firebase
// const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);