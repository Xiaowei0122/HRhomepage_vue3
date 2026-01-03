<template>
  <div>
    <HeaderBar />
    
    <router-view v-slot="{ Component }">
      <transition name="fade-slide" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>

    <FooterBar />
  </div>
</template>

<script setup>
import HeaderBar from './components/HeaderBar.vue'
import FooterBar from './components/FooterBar.vue'
</script>

<style>
/* 动画过程控制：0.3秒左右是最符合用户心理预期的流畅速度 */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.35s ease;
}

/* 离开时的状态：透明度归零，并向上轻微移动 10px */
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* 进入前的起始状态：透明度为零，从下方 10px 处升起 */
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
</style>