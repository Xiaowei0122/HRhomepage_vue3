<template>
  <div class="product-page bg-light-gray pb-5" v-if="product && product.id">
    
    <nav class="container py-3">
      <div class="breadcrumb-custom">
        <router-link to="/">首页</router-link> <span class="sep">/</span>
        <router-link to="/products">产品中心</router-link> <span class="sep">/</span>
        <span class="current">{{ product.name }}</span>
      </div>
    </nav>

    <div class="container">
      <div class="row g-4 mb-5 align-items-stretch">
        <div class="col-lg-7">
          <div class="ui-card p-3 h-100 d-flex gap-3 overflow-hidden">
            <div class="thumb-strip d-none d-md-flex flex-column gap-2">
              <div 
                v-for="(img, index) in product.images" :key="index"
                class="thumb-box" 
                :class="{ active: currentImgIndex === index }"
                @mouseenter="currentImgIndex = index"
              >
                <img :src="img" class="img-contain" />
              </div>
            </div>

            <div class="main-stage flex-grow-1 position-relative">
              <div class="zoom-box" @mousemove="handleMouseMove" @mouseleave="handleMouseLeave">
                <img :src="product.images[currentImgIndex]" class="main-img img-contain" />
                <div v-show="isZooming" class="zoom-lens" :style="lensStyle"></div>
                <div v-show="isZooming" class="zoom-panel" :style="resultStyle"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="ui-card info-panel h-100 p-4 d-flex flex-column">
            <div class="tag-red mb-2">{{ product.categoryName }}</div>
            <h2 class="fw-bold text-dark mb-3">{{ product.name }}</h2>
            <p class="text-secondary small mb-4 lh-lg">{{ product.description }}</p>
            
            <div class="highlights mb-4">
              <div v-for="h in product.highlights" :key="h" class="h-row">
                <i class="bi bi-check2-circle text-danger me-2"></i>
                <span>{{ h }}</span>
              </div>
            </div>

            <div class="action-zone mt-auto pt-4 border-top">
              <router-link 
                :to="{ path: '/contact', query: { product: product.name } }" 
                class="btn btn-red-filled w-100 mb-3 py-2 fw-bold text-decoration-none d-flex"
              >
                获取报价
              </router-link>
              <button class="btn btn-dark-outline w-100 py-2 fw-bold" @click="downloadPDF">
                <i class="bi bi-file-pdf"></i> 技术彩页下载
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="ui-card mb-5 overflow-hidden">
        <div class="tab-header d-flex border-bottom px-4">
           <button v-for="(tab, index) in productTabs" :key="index"
            class="tab-link" :class="{ active: activeTab === index }"
            @click="activeTab = index">
            {{ tab.label }}
          </button>
        </div>
        <div class="p-4">
           <div v-if="productTabs[activeTab]?.type === 'table'" class="spec-grid-container">
              <div v-for="(val, key) in productTabs[activeTab].content" :key="key" class="spec-item">
                <div class="spec-key">{{ key }}</div>
                <div class="spec-val">{{ val }}</div>
              </div>
           </div>
           <div v-else class="service-text text-muted p-3"> {{ productTabs[activeTab]?.content }} </div>
        </div>
      </div>

      <div class="recommend-section mb-5" v-if="relatedProducts.length > 0">
        <div class="d-flex align-items-center mb-4">
          <div class="red-line me-2"></div>
          <h5 class="fw-bold mb-0">相关产品推荐</h5>
        </div>
        <div class="row g-3">
          <div class="col-6 col-md-3" v-for="item in relatedProducts" :key="item.id">
            <router-link :to="'/product/' + item.id" class="text-decoration-none">
              <div class="recommend-card h-100">
                <div class="img-box p-3">
                  <img :src="item.image" class="img-contain" />
                </div>
                <div class="info-box p-3 border-top text-center">
                  <div class="small text-danger mb-1">{{ item.categoryName }}</div>
                  <div class="fw-bold text-dark text-truncate small-title">{{ item.name }}</div>
                  <div class="mt-2 extra-small text-danger">查看详情 →</div>
                </div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="modal-mask" @click.self="showModal = false">
      <div class="modal-content-custom">
        <div class="modal-body-custom text-center p-4">
          <div class="mb-3 fs-1">📂</div>
          <h5 class="fw-bold">技术彩页准备中</h5>
          <p class="text-muted small">为了确保参数实时准确，最新的产品彩页正在校对中。<br>如需获取详情，请拨打服务热线。</p>
          <div class="p-2 bg-light rounded mb-3">
             <span class="text-danger fw-bold">000-000-0000</span>
          </div>
          <button class="btn btn-dark w-100 rounded-pill" @click="showModal = false">我知道了</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const product = ref(null)
const currentImgIndex = ref(0)
const activeTab = ref(0)
const isZooming = ref(false)
const showModal = ref(false) // 新增控制变量
const productTabs = ref([])
const relatedProducts = ref([])
const lensStyle = reactive({ top: '0', left: '0' })
const resultStyle = reactive({ backgroundPosition: '0 0', backgroundImage: '' })

// 模拟数据库（保持原始数据不变）
const allProducts = [
  { 
    id: 100152130120, 
    catId: 'printer', 
    categoryName: '黑白激光一体机', 
    name: '惠普 (HP) 116w 无线激光多功能一体机', 
    image: 'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=600',
    images: [
      'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=800',
      'https://images.unsplash.com/photo-1597733336794-12d05021d510?w=800'
    ],
    description: '集打印、复印、扫描于一体，支持WiFi无线连接，小巧高效。',
    highlights: ['20页/分钟高速打印', 'WiFi无线办公', '经典高品质'],
    specs: {
      "品牌": "惠普 (HP)",
      "商品编号": "100152130120",
      "货号": "A00F8A",
      "是否信创商品": "否",
      "认证型号": "116w",
      "国补备案型号": "116w",
      "CCC强制性认证": "是",
      "网络打印": "支持无线网络打印",
      "打印速度": "20页/分钟 (黑白)",
      "随机印量": "1000页",
      "接口/端口": "WiFi端口, USB",
      "纸张输入容量": "150页",
      "基础功能": "打印, 复印, 扫描",
      "双面打印": "非自动双面",
      "自动双面复印": "不支持",
      "输稿器": "不支持",
      "扫描功能": "平板式扫描",
      "最大支持幅面": "A4",
      "能效等级": "二级能效"
    }
  },
  { 
    id: 2, catId: 'printer', categoryName: '一体机', name: '理光 IM C2000', 
    image: 'https://images.unsplash.com/photo-1512428559087-560fa5ceab42?w=600',
    images: ['https://images.unsplash.com/photo-1512428559087-560fa5ceab42?w=800'],
    description: '商用彩色一体机。',
    highlights: ['智能操作', '色彩还原'],
    specs: { "速度": "20ppm", "类型": "彩色激光" }
  }
]

const loadData = (id) => {
  const current = allProducts.find(p => String(p.id) === String(id)) || allProducts[0]
  product.value = current
  currentImgIndex.value = 0
  productTabs.value = [
    { label: '详细规格', type: 'table', content: current.specs },
    { label: '售后保障', type: 'text', content: '厂家提供全国联保，本站提供24小时技术支持。' }
  ]
  relatedProducts.value = allProducts.filter(p => p.catId === current.catId && String(p.id) !== String(id))
}

watch(() => route.params.id, (newId) => {
  if (newId) { loadData(newId); window.scrollTo({ top: 0, behavior: 'smooth' }); }
})

onMounted(() => loadData(route.params.id))

const handleMouseMove = (e) => {
  isZooming.value = true
  const { left, top, width, height } = e.currentTarget.getBoundingClientRect()
  let x = e.pageX - left - window.scrollX
  let y = e.pageY - top - window.scrollY
  let lX = Math.max(0, Math.min(x - 50, width - 100))
  let lY = Math.max(0, Math.min(y - 50, height - 100))
  lensStyle.left = `${lX}px`; lensStyle.top = `${lY}px`
  resultStyle.backgroundImage = `url(${product.value.images[currentImgIndex.value]})`
  resultStyle.backgroundPosition = `-${lX * 2.5}px -${lY * 2.5}px`
  resultStyle.backgroundSize = `${width * 2.5}px ${height * 2.5}px`
}

const handleMouseLeave = () => isZooming.value = false

// 友好化修改：点击不弹alert，而是切换控制变量
const downloadPDF = () => {
  showModal.value = true
}
</script>

<style scoped>
/* 保持所有原始样式不动 */
.bg-light-gray { background-color: #f5f6f8; }
.ui-card { background: #fff; border-radius: 12px; border: 1px solid #ebedf0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); overflow: hidden; }
.zoom-box { height: 460px; display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative; }
.img-contain { width: 100%; height: 100%; object-fit: contain; }
.thumb-strip { width: 72px; }
.thumb-box { width: 64px; height: 64px; border-radius: 6px; border: 1.5px solid #f0f0f0; cursor: pointer; padding: 2px; overflow: hidden; margin-bottom: 8px; transition: 0.2s; }
.thumb-box.active { border-color: #dc3545; }
.spec-grid-container { display: grid; grid-template-columns: 1fr 1fr; border-top: 1px solid #eee; border-left: 1px solid #eee; }
.spec-item { display: flex; align-items: stretch; border-right: 1px solid #eee; border-bottom: 1px solid #eee; }
.spec-key { width: 130px; background-color: #f9fafb; color: #666; padding: 12px 15px; font-size: 0.85rem; font-weight: 500; display: flex; align-items: center; flex-shrink: 0; }
.spec-val { flex-grow: 1; padding: 12px 15px; color: #333; font-size: 0.85rem; display: flex; align-items: center; }
.btn-red-filled { background: #dc3545; color: #fff !important; border: none; border-radius: 50px; display: flex; align-items: center; justify-content: center; transition: 0.3s; }
.btn-dark-outline { border: 1.5px solid #333; color: #333; border-radius: 50px; background: none; transition: 0.3s; }
.tag-red { display: inline-block; background: #fff1f2; color: #e11d48; font-size: 0.75rem; padding: 4px 12px; font-weight: 600; border-radius: 4px; }
.tab-link { background: none; border: none; padding: 18px 25px; font-weight: 700; color: #888; position: relative; }
.tab-link.active { color: #dc3545; }
.tab-link.active::after { content: ""; position: absolute; bottom: 0; left: 25px; right: 25px; height: 3px; background: #dc3545; border-radius: 10px; }
.recommend-card { border: 1px solid #eee; transition: 0.3s; background: #fff; border-radius: 12px; overflow: hidden; }
.recommend-card .img-box { height: 140px; display: flex; align-items: center; justify-content: center; }
.red-line { width: 4px; height: 20px; background: #dc3545; border-radius: 10px; }
.breadcrumb-custom { font-size: 0.85rem; color: #aaa; }
.breadcrumb-custom a { text-decoration: none; color: #888; }
.breadcrumb-custom .current { color: #dc3545; font-weight: 600; }
.sep { margin: 0 8px; }

/* 仅新增弹窗样式，且使用独立命名空间避免干扰 */
.modal-mask {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0,0,0,0.5); backdrop-filter: blur(2px);
  display: flex; justify-content: center; align-items: center; z-index: 9999;
}
.modal-content-custom {
  background: #fff; width: 90%; max-width: 350px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
</style>