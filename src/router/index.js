import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import ProductsPage from '../components/ProductCenter.vue'
import NewsPage from '../components/NewsPage.vue'
import NewsDetail from '../components/NewsDetail.vue'
import AboutSecPage from '../components/AboutSecPage.vue'
const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/products', name: 'Products', component: ProductsPage },
  {path:'/news',name:'News',component:NewsPage},
  {path:'/news/:id',name:NewsDetail,component:NewsDetail,Props:true},
  {path:'/about',name: 'About', component: AboutSecPage}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: 'active', 
  linkExactActiveClass: 'active',
  scrollBehavior() {
    return { top: 0,behavior: 'smooth' }
  }
})

export default router
