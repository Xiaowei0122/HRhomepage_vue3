<template>
  <footer id="contact">
    <div class="container-max">
      <div class="row gy-4 align-items-start">
        <div class="col-lg-4">
          <div class="logo-small mb-3">
            <img :src="logoIcon" alt="logo" />
          </div>
          <p class="muted">鸿瑞办公 — 专注办公设备与运维服务，提供设备采购、售后、耗材配送与智能办公整体解决方案。</p>
          <p class="muted small">© <span id="footer-year">{{ year }}</span> 鸿瑞办公有限公司</p>
        </div>

        <div class="col-lg-4">
          <h5 class="white">联系我们</h5>
          <p class="muted mb-1">服务热线： <strong class="brand">029-85550780</strong></p>
          <p class="muted mb-1">邮箱：service@example.com</p>
          <p class="muted mb-1">地址：陕西省西安市XXX工业园</p>
        </div>

        <div class="col-lg-4">
          <h5 class="white">快速导航</h5>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="#">首页</a>
            <a href="#services">我们的服务</a>
            <a href="#about">关于我们</a>
            <a href="#partners">合作伙伴</a>
            <a href="#news">新闻公告</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
const logoIcon = '/assets/logo-icon.png'
const year = new Date().getFullYear()
</script>
