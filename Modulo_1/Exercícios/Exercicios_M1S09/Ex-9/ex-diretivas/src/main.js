import {createApp} from 'vue'
import App from './App.vue'

let app = createApp(App)

app.directive('px-up', (el) => {
    el.addEventListener('mouseenter', () => {
        el.style = 'font-size: 25px'
    })
})
app.directive('px-down', (el) => {
    el.addEventListener('mouseleave', () => {
        el.style = 'font-size: 15px'
    })
})


app.mount('#app')