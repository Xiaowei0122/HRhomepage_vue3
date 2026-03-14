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
        <div class="hero-overlay"></div>
        
        <div class="hero-content">
          <div class="slide-label">{{ slide.label }}</div>
          <div class="hero-title">{{ slide.title }}</div>
          <div class="hero-sub">{{ slide.sub }}</div>
          <div class="hero-actions">
            <a class="btn btn-primary-custom" :href="slide.cta1.href">{{ slide.cta1.text }}</a>
            <a class="btn btn-outline-custom" :href="slide.cta2.href">{{ slide.cta2.text }}</a>
          </div>
        </div>
      </swiper-slide>
    </swiper>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, Pagination, EffectFade } from 'swiper/modules'

import 'swiper/css'
import 'swiper/css/pagination'
import 'swiper/css/effect-fade'

const modules = [Autoplay, Pagination, EffectFade]

// 数据保持不变
const slides = ref([
  // ... 您原有的 slides 数据
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
.hero { position: relative; overflow: hidden; background: #111; }

/* PC端高度 */
.banner-swiper { width: 100%; height: 640px; }
.banner-swiper .swiper-slide img { width: 100%; height: 100%; object-fit: cover; display: block; }

/* 文字容器基础样式 */
.hero-content {
  position: absolute; left: 8%; top: 50%; transform: translateY(-50%);
  z-index: 10; width: 40%; color: #fff;
}

.slide-label { font-size: 14px; color: #dc3545; font-weight: 700; margin-bottom: 12px; letter-spacing: 2px; }
.hero-title { font-size: 48px; font-weight: 800; line-height: 1.2; margin-bottom: 20px; }
.hero-sub { font-size: 18px; line-height: 1.6; opacity: 0.85; margin-bottom: 30px; }

/* 按钮样式优化 */
.hero-actions { display: flex; gap: 15px; }
.btn-primary-custom { background: #dc3545; color: #fff !important; padding: 12px 28px; border-radius: 50px; font-weight: 600; border: none; }
.btn-outline-custom { background: transparent; color: #fff !important; border: 2px solid rgba(255,255,255,0.3); padding: 12px 28px; border-radius: 50px; font-weight: 600; }
.btn-outline-custom:hover { background: #fff; color: #333 !important; }

/* 遮罩层防止白底图看不清字 */
.hero-overlay {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.2) 60%, transparent 100%);
  z-index: 1;
}

/* --- 移动端核心适配 --- */
/* --- 移动端深度优化：提升呼吸感与精致度 --- */
@media (max-width: 991px) {
  .banner-swiper { height: 520px; } /* 稍微增加高度，防止文案显得拥挤 */
  
  .hero-content {
    left: 0; 
    width: 100%; 
    padding: 0 25px; /* 增加左右留白 */
    text-align: center;
    top: 55%; /* 内容重心稍微下移，视觉更稳 */
  }
  
  /* 增强背景遮罩，确保文字在任何图片下都清晰 */
  .hero-overlay {
    background: linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.6) 100%);
  }

  /* 1. 顶部标签：缩小字号并拉开字间距，更有品牌感 */
  .slide-label { 
    font-size: 11px; 
    margin-bottom: 10px; 
    letter-spacing: 3px; 
    opacity: 0.9;
  }

  /* 2. 标题：减小字号，避免单行文字太长导致断行突兀 */
  .hero-title { 
    font-size: 26px; 
    margin-bottom: 15px; 
    font-weight: 700;
    line-height: 1.3;
  }

  /* 3. 副标题：调小字号并增加行高，提升易读性 */
  .hero-sub { 
    font-size: 14px; 
    margin-bottom: 30px; 
    line-height: 1.7; 
    opacity: 0.8;
    padding: 0 10px; 
  }
  
  /* 4. 按钮组：改回横排，减小体积，不再堵塞屏幕中心 */
  .hero-actions { 
    flex-direction: row !important; 
    justify-content: center;
    gap: 12px;
  }
  
  /* 主按钮：改为适配品牌的圆角，减小高度 */
  .btn-primary-custom {
    width: auto !important; 
    min-width: 120px;
    padding: 10px 20px !important;
    font-size: 14px;
    border-radius: 8px !important; /* 统一使用 8px 增加稳重感 */
    background: var(--brand-red) !important;
    box-shadow: 0 4px 12px rgba(220, 53, 69, 0.2);
  }
  
  /* 次按钮：使用半透明毛玻璃效果，增加通透感 */
  .btn-outline-custom {
    width: auto !important;
    min-width: 120px;
    padding: 10px 20px !important;
    font-size: 14px;
    border-radius: 8px !important;
    border: 1px solid rgba(255,255,255,0.4) !important;
    background: rgba(255,255,255,0.1); 
    backdrop-filter: blur(4px); /* 磨砂玻璃质感 */
  }
}
</style>