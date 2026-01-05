<template>
  <header>
    <nav class="navbar navbar-expand-lg">
      <div class="container-max d-flex align-items-center justify-content-between">
        <a class="navbar-brand d-flex align-items-center" href="#">
          <img :src="logoFull" alt="鸿瑞办公" />
        </a>

        <div class="d-flex align-items-center">
          <button class="navbar-toggler me-2" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="mainNav">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 align-items-lg-center">
              <li class="nav-item"><router-link to="/" class="nav-link header-nav-link">首页</router-link></li>
              <li class="nav-item"><router-link to="/products" class="nav-link header-nav-link">产品中心</router-link></li>
              <li class="nav-item"><router-link to="/services" class="nav-link header-nav-link" >我们的服务</router-link></li>
              <li class="nav-item"><router-link to="/about" class="nav-link header-nav-link">关于鸿瑞办公</router-link></li>
              <li class="nav-item"><router-link to="/partner-cases" class="nav-link header-nav-link" >合作伙伴 & 案例</router-link></li>
              <li class="nav-item"><router-link to="/news" class="nav-link header-nav-link">新闻公告</router-link></li>
              <li class="nav-item"><router-link to="/contact" class="nav-link header-nav-link">联系我们</router-link></li>
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
          <p class="text-secondary small mb-4">为了提供更优质的线上体验，售后平台正在筹备中。<br>如需紧急报修，请直接联系我们。</p>
          <div class="phone-box p-3 bg-light rounded-3 mb-4">
            <div class="text-muted small mb-1">服务热线</div>
            <div class="fw-bold text-danger h5 mb-0">029-85550780</div> </div>
          <button class="btn btn-dark w-100 rounded-pill" @click="isModalOpen = false">我知道了</button>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
// 修改图片路径为推荐的绝对路径形式
const logoFull = 'assets/partners/logo-full.png'

// 控制弹窗显示状态
const isModalOpen = ref(false)
</script>

<style scoped>
/* 弹窗专用样式 - 保持简洁不影响全局 */
.after-sales-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
}

.modal-card {
  background: white;
  width: 90%;
  max-width: 380px;
  border-radius: 16px;
  position: relative;
  box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}

.icon-circle {
  font-size: 40px;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 24px;
  color: #999;
  cursor: pointer;
}

.phone-box {
  border: 1px dashed #dee2e6;
}
</style>