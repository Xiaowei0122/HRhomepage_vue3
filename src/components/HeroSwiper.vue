<template>
  <section class="hero">
    <swiper
      class="banner-swiper"
      :modules="modules"
      :loop="true"
      :autoplay="{ delay: 3800, disableOnInteraction: false }"
      :pagination="{ clickable: true }"
      effect="fade"
    >
      <swiper-slide v-for="(slide, idx) in slides" :key="idx">
        <img :src="slide.image" :alt="slide.alt" />
        <div class="hero-content">
          <div class="slide-label">{{ slide.label }}</div>
          <div class="hero-title">{{ slide.title }}</div>
          <div class="hero-sub">{{ slide.sub }}</div>
          <div class="hero-actions">
            <a class="btn btn-primary" :href="slide.cta1.href">{{ slide.cta1.text }}</a>
            <a class="btn btn-outline" :href="slide.cta2.href">{{ slide.cta2.text }}</a>
          </div>
        </div>
      </swiper-slide>
    </swiper>
  </section>
</template>

<script setup>
import { ref } from 'vue'
// 1. 核心组件引入
import { Swiper, SwiperSlide } from 'swiper/vue'

// 2. 模块引入路径修正：Swiper 10+ 必须从 'swiper/modules' 引入
import { Autoplay, Pagination, EffectFade } from 'swiper/modules'

// 3. 必须引入 Swiper 的 CSS 样式，否则图片会堆叠在一起
import 'swiper/css'
import 'swiper/css/pagination'
import 'swiper/css/effect-fade'

// 4. 定义模块
const modules = [Autoplay, Pagination, EffectFade]

const slides = ref([
  {
    image: 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1600&q=70',
    alt: '办公设备',
    label: '办公设备',
    title: '办公设备',
    sub: '多品牌复印机 / 打印机 / 投影仪 / 扫描仪 等办公硬件提供与安装服务。',
    cta1: { text: '产品中心', href: '#services' },
    cta2: { text: '咨询采购', href: '#contact' }
  },
  {
    image: 'https://img0.baidu.com/it/u=1835320837,3154296533&fm=253&app=120&f=JPEG?w=1422&h=800',
    alt: '技术服务',
    label: '技术服务',
    title: '技术服务',
    sub: '提供设备维护、故障检修、驻场工程师与系统运维支持，保障业务连续运行。',
    cta1: { text: '申请维修', href: '#services' },
    cta2: { text: '立即联系', href: '#contact' }
  },
  {
    image: 'https://images.unsplash.com/photo-1518779578993-ec3579fee39f?auto=format&fit=crop&w=1600&q=70',
    alt: '数字化解决方案',
    label: '数字化解决方案',
    title: '数字化解决方案',
    sub: 'OA 自动化 / 云打印 / 打印管控与无纸化会议等一站式整合，提升协同效率。',
    cta1: { text: '了解方案', href: '#about' },
    cta2: { text: '申请演示', href: '#contact' }
  },
  {
    image: 'https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=1600&q=70',
    alt: '政府采购',
    label: '政府采购',
    title: '省市区级政府采购在册供应商',
    sub: '作为省市区各级机关事业单位在册的办公设备供应商，我们提供合规采购、稳定交付与长期维保服务。',
    cta1: { text: '合作资质', href: '#partners' },
    cta2: { text: '获取合同条款', href: '#contact' }
  },
  {
    image: 'https://images.unsplash.com/photo-1556742044-3c52d6e88c62?auto=format&fit=crop&w=1600&q=70',
    alt: '办公耗材',
    label: '办公耗材',
    title: '办公用品 · 办公耗材',
    sub: '文具 / 打印耗材 / 电脑配件 / 清洁用品 一站式配齐，企业客户享优先配送与库存管理。',
    cta1: { text: '耗材采购', href: '#services' },
    cta2: { text: '定制配送', href: '#contact' }
  }
])
</script>

<style scoped>
.hero {
  position: relative;
  overflow: hidden;
  background: #111;
}

.banner-swiper {
  width: 100%;
  height: 640px; /* 显式给 Swiper 容器高度，防止塌陷 */
}

.banner-swiper .swiper-slide {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}

.banner-swiper .swiper-slide img {
  width: 100%;
  height: 100%; /* 跟随 slide 高度 */
  object-fit: cover;
  display: block;
  filter: brightness(0.96) contrast(1.03);
}

.hero-content {
  position: absolute;
  left: 6%;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
  width: 44%;
  color: #fff;
  padding: 0 12px;
}

/* 简单的按钮样式占位，防止看着奇怪，你可以根据你自己的 bootstrap 样式调整 */
.hero-actions {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}
.btn {
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 4px;
  display: inline-block;
}
.btn-primary {
  background-color: #0d6efd;
  color: white;
}
.btn-outline {
  border: 1px solid white;
  color: white;
}
</style>