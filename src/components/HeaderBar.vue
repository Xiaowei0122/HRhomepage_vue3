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
              <li class="nav-item"><router-link to="/" class="nav-link active">首页</router-link></li>
              <li class="nav-item"><router-link to="/products" class="nav-link">产品中心</router-link></li>
              <li class="nav-item"><a class="nav-link" href="#services">我们的服务</a></li>
              <li class="nav-item"><a class="nav-link" href="#about">关于鸿瑞办公</a></li>
              <li class="nav-item"><a class="nav-link" href="#partners">合作伙伴</a></li>
              <li class="nav-item"><a class="nav-link" href="#news">新闻公告</a></li>
              <li class="nav-item"><a class="nav-link" href="#contact">联系我们</a></li>
            </ul>
          </div>

          <div class="ms-3 d-none d-lg-block">
            <a href="#contact" class="nav-cta">售后服务</a>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue'
const logoFull = '/assets/logo-full.png'
</script>
