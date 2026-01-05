import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import ProductsPage from '../components/ProductCenter.vue'
import NewsPage from '../components/NewsPage.vue'
import NewsDetail from '../components/NewsDetail.vue'
import AboutSecPage from '../components/AboutSecPage.vue'
import ContactDetail from '../components/ContactDetail.vue'
import ProductDetail from '../components/ProductDetail.vue'
import ServiceView from '../components/ServiceView.vue'
import PartnerCaseView from '../components/PartnerCaseView.vue'

const routes = [
  {path: '/', name: 'Home', component: HomePage },
  {path: '/products', name: 'Products', component: ProductsPage },
  {path:'/news',name:'News',component:NewsPage},
  {path:'/news/:id',name:NewsDetail,component:NewsDetail,props:true},
  {path:'/about',name: 'About', component: AboutSecPage},
  {path:'/contact',name:'Contact',component:ContactDetail},
  {path:'/product/:id',name:'ProductDetail',component:ProductDetail,props:true},
  {path:'/services',name:'Services',component:ServiceView},
  {path:'/partner-cases',name:'PartnerCases',component:PartnerCaseView}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: 'active', 
  linkExactActiveClass: 'active',
  // 优化后的滚动逻辑
  scrollBehavior(to, from, savedPosition) {
    // 1. 如果路径中带有锚点（如 #repair）
    if (to.hash) {
      return {
        el: to.hash,           // 滚动到对应的 ID 元素位置
        behavior: 'smooth',    // 平滑滚动效果
        top: 80                // 偏移量：如果导航栏遮挡，可以预留出 80px 的间距
      }
    }
    
    // 2. 如果是浏览器前进/后退，回到之前保存的位置
    if (savedPosition) {
      return savedPosition
    }

    // 3. 普通页面切换，默认回到顶部
    return { top: 0, behavior: 'smooth' }
  }
})

export default router