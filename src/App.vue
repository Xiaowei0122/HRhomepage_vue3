<template>
  <div>
    <HeaderBar />
    <router-view />
    <FooterBar />
  </div>
</template>

<script setup>
import HeaderBar from './components/HeaderBar.vue'
import FooterBar from './components/FooterBar.vue'
</script>
