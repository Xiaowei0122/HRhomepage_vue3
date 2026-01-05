<template>
  <footer id="contact">
    <div class="container-max">
      <div class="row gy-4 align-items-start">
        
        <div class="col-lg-4">
          <div class="logo-small mb-3">
            <img :src="logoIcon" alt="logo" />
          </div>
          <p class="muted">鸿瑞办公 — 专注办公设备与运维服务，提供设备采购、售后、耗材配送、供应链与智能办公整体解决方案。</p>
          <p class="muted small">© <span id="footer-year">{{ year }}</span> 西安鸿瑞办公设备有限公司 . 保留所有权利</p>
        </div>

        <div class="col-lg-4">
          <h5 class="white">联系我们</h5>
          <p class="muted mb-1">服务热线： <strong class="brand">029-85550780</strong></p>
          <p class="muted mb-1">商务合作： <strong class="brand">134-8810-7706</strong></p>
          <p class="muted mb-1">鸿瑞商城：ds.xashrbg.com</p>
          <p class="muted mb-1">地址：陕西省西安市碑林区雁塔中路19号<br>鹏博大厦A座1001</p>
        </div>

        <div class="col-lg-4 text-lg-end">
          <div class="footer-links-column">
            <h5 class="footer-title">快速导航</h5>
            <ul class="footer-nav-list list-unstyled">
              <li class="nav-item"><router-link to="/" class="active">首页</router-link></li>
              <li class="nav-item"><router-link to="/products">产品中心</router-link></li>
              <li class="nav-item"><router-link to="/services">我们的服务</router-link></li>
              <li class="nav-item"><router-link to="/about">关于鸿瑞办公</router-link></li>
              <li class="nav-item"><router-link to="/partner-cases">合作伙伴 & 案例</router-link></li>
              <li class="nav-item"><router-link to="/news">新闻公告</router-link></li>
              <li class="nav-item"><router-link to="/contact">联系我们</router-link></li>
            </ul>
          </div>
        </div>

      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
const logoIcon = 'public/assets/partners/logo-icon.png'
const year = new Date().getFullYear()
</script>
