import Vue from 'vue'
import App from './App.vue'

let app = createApp(App)

app.directive('demo', {
  beforeMounted(el, binding, vnode) {
    console.log(el)
  }
})
