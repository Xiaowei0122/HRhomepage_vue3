<template>
  <div class="services-page">
    <section class="service-hero d-flex align-items-center text-white">
      <div class="container text-center">
        <h1 class="display-3 fw-bold mb-3">我们的服务</h1>
        <p class="lead fs-4 opacity-75">全方位办公数字化解决方案，助力企业高效运营</p>
        <div class="mx-auto mt-4 hero-line"></div>
      </div>
    </section>

    <div class="container py-5">
      <section 
        v-for="(item, index) in serviceList" 
        :key="item.id"
        :id="item.id"
        class="row align-items-center py-5 my-5 service-row"
        :class="{ 'flex-row-reverse': index % 2 !== 0 }"
      >
        <div class="col-lg-6 mb-4 mb-lg-0 px-md-5">
          <div class="service-img-card shadow-lg rounded-4 overflow-hidden">
            <img :src="item.image" class="img-fluid hover-zoom" :alt="item.title">
          </div>
        </div>

        <div class="col-lg-6 px-md-5">
          <div class="service-badge mb-3">{{ item.tag }}</div>
          <h2 class="section-title fw-bold mb-4 text-dark">{{ item.title }}</h2>
          <p class="text-secondary lh-lg mb-4 fs-6">{{ item.desc }}</p>
          
          <div class="row g-3 mb-5">
            <div class="col-sm-6" v-for="point in item.points" :key="point">
              <div class="d-flex align-items-center">
                <div class="point-icon me-2">
                  <i class="bi bi-check-lg"></i>
                </div>
                <span class="fw-bold text-dark small">{{ point }}</span>
              </div>
            </div>
          </div>
          
          <router-link :to="{ path: '/contact', query: { service: item.title } }" class="btn btn-red-pill px-5 py-3 fw-bold">
            咨询详情 <i class="bi bi-arrow-right ms-2"></i>
          </router-link>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted, watch, nextTick } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// 专门处理“返回再进入”或“同页跳转”的增强函数
const forceScrollToAnchor = () => {
  if (route.hash) {
    // nextTick 确保数据已加载到 DOM
    nextTick(() => {
      // 稍微延迟，等浏览器完成页面渲染布局
      setTimeout(() => {
        const element = document.querySelector(route.hash)
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }
      }, 250) // 250ms 是经验值，能避开大部分加载冲突
    })
  }
}

// 解决：从首页点进来，或者“退回再点进来”的场景
onMounted(() => {
  forceScrollToAnchor()
})

// 解决：已经在 ServiceView 页面，点击导航栏或小卡片切换不同锚点的场景
watch(() => route.hash, () => {
  forceScrollToAnchor()
})

const serviceList = [
  {
    id: 'sales',
    tag: 'HARDWARE SALES',
    title: '办公设备销售',
    image: 'https://images.unsplash.com/photo-1557804506-669a67965ba0?w=800',
    desc: '提供惠普、理光、柯尼卡美能达等主流品牌打印机、复印机、投影仪等全线办公设备。我们不仅销售产品，更为您提供量身定制的采购方案，优化办公资产配置。',
    points: ['原厂正品保证', '多维度选型指导', '企业采购优惠', '样机试用支持']
  },
  {
    id: 'repair',
    tag: 'MAINTENANCE',
    title: '打印机/复印机维修',
    image: 'https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=800',
    desc: '专业的技术工程师团队，覆盖全市的服务网络。针对复印机卡纸、漏粉、不通电、色彩偏色等故障提供快速响应，确保您的办公节奏不被故障打断。',
    points: ['2小时快速响应', '原厂级维修配件', '资深工程师团队', '修复后质量跟踪']
  },
  {
    id: 'supplies',
    tag: 'SUPPLIES SERVICE',
    title: '耗材配送服务',
    image: 'https://images.unsplash.com/photo-1512428559087-560fa5ceab42?w=800',
    desc: '稳定供应各类原装/品牌碳粉、硒鼓、纸张等办公耗材。通过智能化的库存管理，为您提供定期补货与协议客户优先配送，彻底告别“缺粉停工”风险。',
    points: ['全型号覆盖', '正品环保耗材', '免费上门安装', '批量采购返利']
  },
  {
    id: 'solutions',
    tag: 'SMART SOLUTIONS',
    title: '智能化办公解决方案',
    image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800',
    desc: '通过OA集成、打印管控及设备运维一体化方案，帮助企业实现成本可视化管理。支持刷卡/人脸识别打印，保障文档安全，助力企业实现降本增效。',
    points: ['成本统计分析', '文档安全闭环', '云打印技术支持', '高效运维系统']
  }
]
</script>

<style scoped>
/* 报错修复：将 flex-column 改为正确的 flex-direction */
.service-row {
    scroll-margin-top: 100px;
    display: flex;
}

/* Hero Section */
.service-hero {
  height: 50vh;
  background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200');
  background-size: cover;
  background-position: center;
}

.hero-line {
  width: 60px;
  height: 4px;
  background: #dc3545;
  border-radius: 2px;
}

/* 服务卡片 */
.service-badge {
  color: #dc3545;
  font-weight: 800;
  letter-spacing: 2px;
  font-size: 0.8rem;
  text-transform: uppercase;
}

.section-title {
  font-size: 2.25rem;
  letter-spacing: -1px;
}

.service-img-card {
  transition: transform 0.4s ease;
}

.hover-zoom {
  transition: transform 1s ease;
}

.service-img-card:hover .hover-zoom {
  transform: scale(1.08);
}

/* 亮点样式 */
.point-icon {
  width: 24px;
  height: 24px;
  background: #fff1f2;
  color: #e11d48;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
}

/* 按钮样式 */
.btn-red-pill {
  background: #dc3545;
  color: #fff !important;
  border-radius: 100px;
  border: none;
  transition: 0.3s;
}

.btn-red-pill:hover {
  background: #c82333;
  transform: translateX(5px);
  box-shadow: 0 10px 20px rgba(220, 53, 69, 0.2);
}

/* 响应式：手机端取消反向排列，避免图片在下方 */
@media (max-width: 991px) {
  .flex-row-reverse {
    flex-direction: row !important;
  }
  .section-title {
    font-size: 1.75rem;
  }
}
</style>