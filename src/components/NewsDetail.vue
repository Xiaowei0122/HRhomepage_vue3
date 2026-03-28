<template>
  <div class="article-detail container py-5">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <nav aria-label="breadcrumb" class="mb-4 custom-breadcrumb-nav">
          <ol class="breadcrumb mb-0 small text-nowrap">
            <li class="breadcrumb-item"><router-link to="/">首页</router-link></li>
            <li class="breadcrumb-item"><router-link to="/news">新闻中心</router-link></li>
            <li class="breadcrumb-item active text-truncate">{{ article.title }}</li>
          </ol>
        </nav>

        <div class="newshead mb-5">
          <h1 class="display-6 fw-bold mb-3 article-title">{{ article.title }}</h1>
          <div class="text-muted small header-meta">
            <span>发布时间：{{ article.date }}</span>
            <span class="mx-2">|</span>
            <span class="source-text">来源：鸿瑞办公</span>
          </div>
        </div>

        <div class="article-content" v-html="article.content"></div>

        <div class="border-top mt-5 pt-4 d-flex justify-content-between align-items-center bottom-bar">
          <button class="btn btn-light px-4" @click="$router.back()">返回列表</button>
          <div class="share-links text-muted small">
            分享至：<i class="bi bi-wechat ms-2"></i> <i class="bi bi-info-circle ms-2"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps(['id'])
const article = ref({
  title: '正在加载...',
  date: '',
  content: ''
})

onMounted(() => {
  // 实际开发中，这里会根据 props.id 调用 API
  // 下面是模拟数据
  setTimeout(() => {
    article.value = {
      title: '鸿瑞办公成功为某市政府打印设备指定供应商',
      date: '2025-09-18',
      content: '<p>这里是详细的文章内容...</p><p>鸿瑞办公深耕办公设备领域20年...</p><p>作为一家在办公设备领域深耕二十年的企业，我们始终坚持以客户需求为导向，致力于为各类企业提供高效、智能的办公解决方案。从最初的复印机、打印机到如今的全方位办公硬件设备，我们不断提升产品质量与技术创新，力求为客户提供更加优质的办公体验。</p>'
                +'<p>二十年的历程不仅是企业发展的见证，也是我们不断积累经验、提升服务的过程。通过与各大品牌的紧密合作，我们的产品涵盖了复印机、打印机、投影仪、扫描仪等多个领域，满足了不同行业客户的多样化需求。此外，我们还为客户提供专业的安装、维修及售后服务，确保设备始终高效运行，助力客户在日常办公中实现更高效、更节省的工作模式。</p>'
                +'<p>未来，我们将继续秉持“创新驱动，服务至上”的理念，不断突破技术边界，推动办公设备行业的发展，为客户创造更多价值。</p>'
    }
  }, 500)
})
</script>

<style scoped>
/* 1. PC端基础美化 */
.custom-breadcrumb-nav .breadcrumb-item + .breadcrumb-item::before {
  content: "»";
  color: #ccc;
  font-size: 1.1rem;
}

.custom-breadcrumb-nav .breadcrumb-item a {
  transition: all 0.3s;
  color: #555;
  text-decoration: none !important;
}

.custom-breadcrumb-nav .breadcrumb-item:first-child a {
  color: #dc3545;
  font-weight: bold;
}

.custom-breadcrumb-nav .breadcrumb-item a:hover {
  color: #dc3545;
}

.custom-breadcrumb-nav .breadcrumb-item.active {
  color: #999;
  max-width: 300px;
}

.article-content {
  font-size: 1.15rem;
  line-height: 1.8;
  color: #333;
}

:deep(.article-content p) {
  margin-bottom: 1.5rem !important;
  text-align: justify;
}

.share-links i {
  color: #777;
  cursor: pointer;
  transition: 0.3s;
}
.share-links i:hover { color: #dc3545; }

/* 2. 移动端专项适配 */
@media (max-width: 991px) {
  .container.py-5 {
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
  }

  .custom-breadcrumb-nav {
    overflow-x: auto;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
  }
  .custom-breadcrumb-nav::-webkit-scrollbar { display: none; }

  .breadcrumb-item { font-size: 13px; }
  .custom-breadcrumb-nav .breadcrumb-item.active { max-width: none !important; }

  .newshead.mb-5 { margin-bottom: 2rem !important; }
  .article-title {
    font-size: 1.6rem !important;
    line-height: 1.3;
  }
  
  .header-meta { font-size: 0.8rem; }
  .source-text { display: none; } /* 移动端隐藏来源，保持单行 */

  .article-content {
    font-size: 1rem !important;
    line-height: 1.7 !important;
  }
  
  .bottom-bar {
    flex-direction: column !important;
    gap: 15px;
  }
  
  .bottom-bar .btn {
    width: 100%;
    padding: 10px;
  }
}
</style>