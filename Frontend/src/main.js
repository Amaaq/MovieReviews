
import { registerPlugins } from '@/plugins'

import App from './App.vue'

import { createApp } from 'vue'
import router from '@/router/index'
import store from '@/store/index'
const app = createApp(App)

registerPlugins(app)
app.use(router)
app.use(store)
app.mount('#app')
