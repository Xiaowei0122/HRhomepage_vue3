<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-white">
      <div class="container-max d-flex align-items-center justify-content-between w-100">
        
        <router-link class="navbar-brand m-0 p-0" to="/">
          <img :src="logoFull" alt="鸿瑞办公" class="logo-img" />
        </router-link>

        <div class="d-flex align-items-center">
          <button class="navbar-toggler border-0 shadow-none p-0" type="button" @click="toggleMenu">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" :class="{ 'show': isMenuShow }" id="mainNav">
            <ul class="navbar-nav align-items-lg-center">
              <li class="nav-item" v-for="item in navLinks" :key="item.path">
                <router-link :to="item.path" class="nav-link header-nav-link" active-class="active">
                  {{ item.name }}
                </router-link>
              </li>
              
              <li class="nav-item d-lg-none mt-4 px-2">
                <a href="javascript:void(0)" class="nav-cta-mobile" @click="handleMobileCta">售后服务</a>
              </li>
            </ul>
          </div>

          <div class="ms-3 d-none d-lg-block">
            <a href="javascript:void(0)" class="nav-cta" @click="isModalOpen = true">售后服务</a>
          </div>
        </div>
      </div>
    </nav>

    <div v-if="isModalOpen" class="after-sales-modal" @click.self="isModalOpen = false">
      <div class="modal-card text-center">
        <div class="close-btn" @click="isModalOpen = false">&times;</div>
        <div class="modal-body p-4">
          <div class="icon-circle mb-3">🛠️</div>
          <h4 class="fw-bold mb-3">功能升级中</h4>
          <p class="text-secondary small mb-4">为了提供更优质的线上体验，售后平台正在筹备中。</p>
          <div class="phone-box p-3 bg-light rounded-3 mb-4">
            <div class="fw-bold text-danger h5 mb-0">029-85550780</div>
          </div>
          <button class="btn btn-dark w-100 rounded-pill" @click="isModalOpen = false">我知道了</button>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const logoFull = 'assets/partners/logo-full.png'
const isModalOpen = ref(false)
const isMenuShow = ref(false)
const route = useRoute()

const navLinks = [
  { name: '首页', path: '/' },
  { name: '产品中心', path: '/products' },
  { name: '我们的服务', path: '/services' },
  { name: '关于鸿瑞办公', path: '/about' },
  { name: '合作伙伴 & 案例', path: '/partner-cases' },
  { name: '新闻公告', path: '/news' },
  { name: '联系我们', path: '/contact' }
]

const toggleMenu = () => { isMenuShow.value = !isMenuShow.value }
const handleMobileCta = () => { isMenuShow.value = false; isModalOpen.value = true }

// 路由改变自动关闭菜单
watch(() => route.path, () => { isMenuShow.value = false })
</script>

<style scoped>
header { background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 1100; }
.logo-img { height: 50px; transition: 0.3s; }

/* PC端：保留 Hover 动画 */
@media (min-width: 992px) {
  .header-nav-link { position: relative; padding: 10px 15px !important; transition: color 0.3s; }
  .header-nav-link::after {
    content: ''; position: absolute; width: 0; height: 2px;
    bottom: 0; left: 50%; background: #dc3545;
    transition: all 0.3s ease; transform: translateX(-50%);
  }
  .header-nav-link:hover::after, .header-nav-link.active::after { width: 70%; }
  .header-nav-link:hover, .header-nav-link.active { color: #dc3545 !important; }
}

/* 移动端调整：增加平滑渐显动画 */
@media (max-width: 991px) {
  .container-max { padding: 0 20px !important; }
  .logo-img { height: 36px; }

  /* 抽屉菜单：由 display 改为透明度控制以实现动画 */
  .navbar-collapse {
    position: absolute; 
    top: 100%; 
    left: 0; 
    right: 0;
    background: #fff; 
    padding: 10px 25px 30px;
    box-shadow: 0 15px 30px rgba(0,0,0,0.1); 
    border-top: 1px solid #f0f0f0;
    
    /* 核心动画设置 */
    display: block !important;       /* 必须始终为 block */
    opacity: 0;                      /* 初始透明度为 0 */
    visibility: hidden;              /* 隐藏时不可点击 */
    transform: translateY(-10px);    /* 初始向上偏移 10px */
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); /* 丝滑的贝塞尔曲线 */
    pointer-events: none;            /* 隐藏时穿透点击 */
  }

  /* 菜单展开后的激活状态 */
  .navbar-collapse.show { 
    opacity: 1;                      /* 变为不透明 */
    visibility: visible;             /* 变为可见 */
    transform: translateY(0);        /* 回归原位 */
    pointer-events: auto;            /* 恢复点击事件 */
  }

  /* 移动端菜单项样式 */
  .header-nav-link {
    padding: 15px 0 !important;
    border-bottom: 1px solid #f8f8f8;
    color: #333 !important;
    font-size: 16px;
    /* 让文字也有细微的浮现感 */
    transition: opacity 0.3s ease;
  }
  .header-nav-link::after { display: none !important; } 
  .header-nav-link.active { color: #dc3545 !important; font-weight: bold; }

  /* 移动端售后按钮 */
  .nav-cta-mobile {
    display: block; width: 100%; padding: 12px;
    border: 1px solid #dc3545; color: #dc3545;
    text-align: center; border-radius: 12px;
    font-weight: 600; text-decoration: none;
    transition: background 0.2s;
  }
  .nav-cta-mobile:active { background: rgba(220, 53, 69, 0.05); }
}

/* 弹窗样式 */
.after-sales-modal { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); backdrop-filter: blur(4px); display: flex; justify-content: center; align-items: center; z-index: 2000; }
.modal-card { background: white; width: 90%; max-width: 380px; border-radius: 16px; position: relative; box-shadow: 0 15px 35px rgba(0,0,0,0.2); }
.close-btn { position: absolute; top: 10px; right: 15px; font-size: 24px; color: #999; cursor: pointer; }
.phone-box { border: 1px dashed #dee2e6; }
</style>