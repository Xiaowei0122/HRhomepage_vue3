<template>
  <div class="news-page container py-5">
    <div class="text-center mb-5">
      <h2 class="fw-bold">新闻中心</h2>
      <p class="text-muted">了解鸿瑞办公最新动态与行业前沿资讯</p>
    </div>

    <ul class="nav nav-pills justify-content-center mb-5 news-tabs">
      <li class="nav-item">
        <button class="nav-link" :class="{ active: currentTab === 'company' }" @click="currentTab = 'company'">公司新闻</button>
      </li>
      <li class="nav-item">
        <button class="nav-link" :class="{ active: currentTab === 'industry' }" @click="currentTab = 'industry'">行业资讯</button>
      </li>
    </ul>

    <div class="news-list">
      <div v-for="item in filteredNews" :key="item.id" class="news-item shadow-sm p-4 mb-3" @click="goToDetail(item.id)">
        <div class="row align-items-center">
          <div class="col-md-2 text-center border-end">
            <div class="date-day h3 mb-0 fw-bold">{{ item.date.split('-')[2] }}</div>
            <div class="date-month text-muted">{{ item.date.split('-')[0] }}-{{ item.date.split('-')[1] }}</div>
          </div>
          <div class="col-md-8 ps-md-4">
            <h5 class="news-title mb-2">{{ item.title }}</h5>
            <p class="news-excerpt text-muted mb-0">{{ item.excerpt }}</p>
          </div>
          <div class="col-md-2 text-end">
            <span class="btn btn-outline-danger btn-sm rounded-pill">阅读更多 →</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const currentTab = ref('company')

const newsData = ref([
  { id: 1, type: 'company', title: '鸿瑞办公成功为省市区政府办公设备指定供应商', date: '2023-03-18', excerpt: '凭借稳定的供货与高质量的售后服务，公司中标并华为市内多家单位提供设备...' },
  { id: 2, type: 'company', title:'鸿瑞办公正式入驻京东慧采业务板块', date: '2026-01-10', excerpt: '2026年1月10日，鸿瑞办公京东慧采业务板块启动仪式正式开启.....'},
  { id: 5, type: 'industry', title:'擎启“鸿”图 智联未来 柯尼卡美能达旗下数码复合机完成与鸿蒙系统的深度适配', date: '2026-01-03', excerpt: '随着国家国产操作系统技术攻坚与生态建设顶层战略的加速落地，企业国产化....'},
  { id: 3, type: 'industry', title: '2025年办公设备行业数字化转型趋势分析', date: '2025-10-12', excerpt: '随着智能办公的普及，传统复印机正向云端集成终端设备转型...' },
  { id: 4, type: 'company', title:'热烈祝贺鸿瑞办公2024-2025年终总结大会圆满进行', date: '2025-01-25', excerpt: '在此次大会上，公司领导与各部门代表共同回顾了过去一年的工作成果与挑战，展望了未来发展的战略.....'},
])

const filteredNews = computed(() => {
  return newsData.value.filter(item => item.type === currentTab.ref || item.type === currentTab.value)
})

const goToDetail = (id) => {
  router.push(`/news/${id}`)
}
</script>

<style scoped>
.news-tabs .nav-link {
  color: #666;
  border-radius: 30px;
  padding: 10px 30px;
  margin: 0 10px;
}
.news-tabs .nav-link.active {
  background-color: #dc3545;
}
.news-item {
  background: #fff;
  border-radius: 16px;
  cursor: pointer;
  transition: 0.3s;
  border: 1px solid transparent;
}
.news-item:hover {
  transform: translateX(10px);
  border-color: #dc3545;
}
.news-title { font-weight: 600; }
</style>