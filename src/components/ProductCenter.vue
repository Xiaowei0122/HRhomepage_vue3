<template>
  <div class="product-center container-fluid py-5 bg-light">
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-3">
          <div class="category-sidebar sticky-top shadow-sm">
            <h5 class="sidebar-title">产品中心</h5>
            <ul class="nav flex-column p-2">
              <li class="nav-item" v-for="cat in categories" :key="cat.id">
                <button 
                  class="nav-link w-100 text-start border-0 bg-transparent"
                  :class="{ 'active': currentCategory === cat.id }"
                  @click="currentCategory = cat.id"
                >
                  {{ cat.name }}
                  <span class="badge rounded-pill bg-light text-dark float-end">{{ getProductCount(cat.id) }}</span>
                </button>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-9">
          <div class="product-grid-header d-flex justify-content-between align-items-end mb-4">
            <div>
              <h3 class="fw-bold mb-1">{{ activeCategoryName }}</h3>
              <p class="text-muted small">为您精选优质高效的办公硬件设备</p>
            </div>
          </div>

          <div class="row g-3">
            <div class="col-6 col-md-4 col-xl-3" v-for="product in filteredProducts" :key="product.id">
              <div class="product-card">
                <div class="image-wrapper">
                  <img :src="product.image" :alt="product.name" class="product-img">
                  <div class="hover-mask">
                    <button class="btn btn-light btn-sm rounded-pill px-3">查看详情</button>
                  </div>
                </div>
                <div class="p-3 text-center">
                  <div class="product-category text-uppercase text-danger">{{ product.categoryName }}</div>
                  <h6 class="product-name text-truncate mb-0">{{ product.name }}</h6>
                </div>
              </div>
            </div>
          </div>
          
          <div v-if="filteredProducts.length === 0" class="text-center py-5">
            <p class="text-muted">该分类下暂无产品</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// 分类数据
const categories = ref([
  { id: 'all', name: '全部分类' },
  { id: 'copier', name: '复印机 / 多功能一体机' },
  { id: 'printer', name: '激光打印机' },
  { id: 'projector', name: '投影仪 / 演示设备' },
  { id: 'scanner', name: '高速扫描仪' },
  { id: 'consumables', name: '办公耗材 / 纸张' },
  { id: 'accessories', name: '配件 / 附件' },
  {id: 'others', name: '其他办公设备' },
  {id: 'laobao', name: '劳保用品' },
])

const currentCategory = ref('all')

// 模拟产品数据
const products = ref([
  { id: 1, catId: 'copier', categoryName: '复印机', name: '理光 IM C3500 彩机', image: 'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?auto=format&fit=crop&w=400&q=80' },
  { id: 2, catId: 'printer', categoryName: '打印机', name: '惠普 LaserJet Pro M404n', image: 'https://images.unsplash.com/photo-1588702547919-26089e690ecc?auto=format&fit=crop&w=400&q=80' },
  { id: 3, catId: 'copier', categoryName: '复印机', name: '柯尼卡美能达 C250i', image: 'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?auto=format&fit=crop&w=400&q=80' },
  { id: 4, catId: 'projector', categoryName: '投影仪', name: '爱普生 CB-X06E 商务机', image: 'https://images.unsplash.com/photo-1535016120720-40c646bebbfc?auto=format&fit=crop&w=400&q=80' },
  // ... 可以继续添加更多产品
])

const activeCategoryName = computed(() => {
  return categories.value.find(c => c.id === currentCategory.value)?.name || ''
})

const filteredProducts = computed(() => {
  if (currentCategory.value === 'all') return products.value
  return products.value.filter(p => p.catId === currentCategory.value)
})

const getProductCount = (catId) => {
  if (catId === 'all') return products.value.length
  return products.value.filter(p => p.catId === catId).length
}
</script>

<style scoped>
/* 侧边栏样式 */
.category-sidebar {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  top: 100px; /* 避开可能存在的导航栏高度 */
}

.sidebar-title {
  padding: 20px;
  background: #f8f9fa;
  margin-bottom: 0;
  font-weight: bold;
  border-bottom: 1px solid #eee;
}

.nav-link {
  padding: 12px 20px;
  color: #444; /* 默认未选中的文字颜色 */
  transition: all 0.3s;
  border-radius: 0;
  font-size: 0.95rem;
  display: flex;         /* 建议增加：方便对齐 */
  justify-content: space-between; /* 建议增加：文字和数字两头对齐 */
  align-items: center;
}

.nav-link:hover {
  background: #fff5f5;
  color: #dc3545;
}

.nav-link.active {
  background: #dc3545 !important; /* 选中后的背景红色 */
  color: #ffffff !important;    /* 强制文字为白色，解决“不见了”的问题 */
  font-weight: 600;
}

.nav-link.active .badge {
  background-color: rgba(255, 255, 255, 0.2) !important;
  color: #ffffff !important;
}

/* 产品卡片样式 */
.product-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid #f0f0f0;
  height: 100%;
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.08) !important;
}

.image-wrapper {
  position: relative;
  aspect-ratio: 1/1;
  overflow: hidden;
  background: #fafafa;
}

.product-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  padding: 15px;
  transition: transform 0.5s;
}

.product-card:hover .product-img {
  transform: scale(1.1);
}

.hover-mask {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: 0.3s;
}

.product-card:hover .hover-mask {
  opacity: 1;
}

.product-category {
  font-size: 0.7rem;
  font-weight: bold;
  letter-spacing: 1px;
  margin-bottom: 4px;
}

.product-name {
  font-size: 0.95rem;
  font-weight: 600;
}
</style>