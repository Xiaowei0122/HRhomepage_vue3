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
import { getNewsDetail } from '../api/public'

const props = defineProps(['id'])
const article = ref({
  title: '正在加载...',
  date: '',
  content: ''
})

onMounted(async () => {
  try {
    const data = await getNewsDetail(props.id)
    article.value = {
      title: data.title || '未命名文章',
      date: data.date || '',
      content: data.content || '<p>暂无内容</p>',
    }
  } catch (e) {
    article.value = {
      title: '文章不存在或已下架',
      date: '',
      content: '<p>' + (e.message || '请返回新闻列表') + '</p>',
    }
  }
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