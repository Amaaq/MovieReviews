import { createWebHistory, createRouter } from 'vue-router'
import MoviesList from '@/views/MoviesList.vue'
import MovieDetail from '@/views/MovieDetail.vue'
const routes = [
  { path: '/', component: MovieDetail},
  { path: '/:id', component: MoviesList},
]
const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router