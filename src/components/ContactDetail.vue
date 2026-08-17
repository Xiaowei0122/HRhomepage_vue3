<template>
  <div class="contact-page-container">
    <section class="contact-hero text-center py-5 bg-dark text-white">
      <div class="container py-4">
        <h1 class="display-6 fw-bold mb-2">联系我们</h1>
        <p class="small opacity-75 mb-0">西安鸿瑞办公 · 24小时响应 · 全城上门服务</p>
        <p class="small opacity-75">专业的办公方案，只需一个电话或一次到访</p>
        <div class="title-underline mx-auto mt-3"></div>
      </div>
    </section>

    <section class="service-flow py-5 bg-white">
      <div class="container">
        <div class="text-center mb-4 mb-md-5">
          <h4 class="fw-bold section-title-center">合作流程</h4>
          <p class="text-muted x-small">简单四步，开启高效办公体验</p>
        </div>
        <div class="row g-3 g-md-4 text-center">
          <div class="col-6 col-md-3" v-for="(step, index) in flowSteps" :key="index">
            <div class="flow-item p-3">
              <div class="flow-icon-wrapper">
                <i :class="['bi', step.icon]"></i>
                <div class="step-number">{{ index + 1 }}</div>
              </div>
              <h6 class="mt-3 fw-bold small-title">{{ step.title }}</h6>
              <p class="small text-muted d-none d-md-block">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="contact-main py-4 py-md-5 bg-light">
      <div class="container">
        <div class="row g-4 g-lg-5">
          <div class="col-lg-5">
            <div class="info-card shadow-sm p-4 rounded-4 bg-white mb-4">
              <h5 class="section-title mb-4">业务咨询</h5>
              
              <a :href="'tel:' + servicePhone" class="d-flex align-items-center mb-4 text-decoration-none text-dark contact-link">
                <div class="icon-box me-3"><i class="bi bi-headset"></i></div>
                <div>
                  <div class="text-muted x-small">服务热线 (点击拨打)</div>
                  <div class="fw-bold text-danger">{{ servicePhone }}</div>
                </div>
              </a>

              <a :href="'tel:' + businessPhone" class="d-flex align-items-center mb-4 text-decoration-none text-dark contact-link">
                <div class="icon-box me-3"><i class="bi bi-phone"></i></div>
                <div>
                  <div class="text-muted x-small">业务合作</div>
                  <div class="fw-bold text-danger">{{ businessPhone }}</div>
                </div>
              </a>

              <div class="d-flex align-items-start mb-4">
                <div class="icon-box me-3"><i class="bi bi-geo-alt"></i></div>
                <div>
                  <div class="text-muted x-small">公司地址</div>
                  <div class="fw-bold small">{{ address }}</div>
                </div>
              </div>

              <div class="p-3 bg-light rounded-3">
                <p class="x-small text-muted mb-0"><i class="bi bi-clock me-2"></i>{{ workingHours }}</p>
              </div>
            </div>
            
            <div class="map-card shadow-sm rounded-4 overflow-hidden position-relative" style="height: 250px; background: #e9ecef;">
      <!-- 1. 真实的地图容器 -->
      <div id="amap-container" class="h-100 w-100"></div>

      <!-- 2. 悬浮在地图上的 UI 遮罩 (可选：如果你想让地图露出来，可以去掉 bg-white 或调高透明度) -->
      <div class="map-overlay-content position-absolute bottom-0 start-0 w-100 p-3" style="background: linear-gradient(transparent, rgba(0,0,0,0.6));">
        <div class="d-flex justify-content-between align-items-center">
          <div class="text-white">
            <div class="x-small fw-bold">西安鸿瑞办公设备有限公司</div>
            <div style="font-size: 10px; opacity: 0.8;">碑林区鹏博大厦A座1001</div>
          </div>
          <button class="btn btn-sm btn-danger rounded-pill px-3 shadow-sm" @click="openNavigation">
            <i class="bi bi-geo-alt-fill me-1"></i>开始导航
          </button>
        </div>
      </div>
</div>
          </div>

          <div class="col-lg-7">
            <div class="form-card shadow-sm p-4 p-md-5 rounded-4 bg-white">
              <h5 class="section-title mb-4">提交需求单</h5>
              <form @submit.prevent="handleSubmit" class="row g-3">
                <div class="col-md-6">
                  <input type="text" v-model="formData.name" class="form-control custom-input" placeholder="您的姓名" required>
                </div>
                <div class="col-md-6">
                  <input type="tel" v-model="formData.phone" class="form-control custom-input" placeholder="联系电话" required>
                </div>
                <div class="col-12">
                  <select v-model="formData.type" class="form-select custom-input">
                    <option value="">意向采购咨询</option>
                    <option value="rent">设备租赁及销售</option>
                    <option value="buy">耗材/办公用品采购</option>
                    <option value="service">用户维护报修</option>
                  </select>
                </div>
                <div class="col-12">
                  <textarea v-model="formData.message" class="form-control custom-input" rows="4" placeholder="请简要描述您的需求..." required></textarea>
                </div>
                <div class="col-12 text-md-end">
                  <button type="submit" class="btn btn-danger btn-lg w-100 w-md-auto px-5 rounded-pill shadow-sm" :disabled="isSubmitting">
                    {{ isSubmitting ? '正在提交...' : '立即提交需求' }}
                  </button>
                </div>
              </form>
            </div>

            <transition name="toast">
              <div v-if="showStatus" class="status-toast shadow-lg rounded-4 p-4 text-center">
                <i class="bi bi-check-circle-fill text-success fs-1 mb-3"></i>
                <h5 class="fw-bold">提交成功</h5>
                <p class="text-muted small mb-0">我们将尽快安排经理回电。</p>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { getPublicConfig, submitLead } from '../api/public'

const isSubmitting = ref(false)
const showStatus = ref(false)
const formData = reactive({ name: '', phone: '', type: '', message: '' })

// 联系方式（后端可配置，缺省用默认值）
const servicePhone = ref('029-85550780')
const businessPhone = ref('134-8810-7706')
const address = ref('西安市碑林区雁塔中路19号鹏博大厦A座1001')
const workingHours = ref('周一至周五 08:30 - 18:00')

onMounted(async () => {
  try {
    const cfg = await getPublicConfig()
    const c = cfg.contact || {}
    if (c.phone) servicePhone.value = c.phone
    if (c.businessPhone) businessPhone.value = c.businessPhone
    if (c.address) address.value = c.address
    if (c.workingHours) workingHours.value = c.workingHours
  } catch { /* 后端不可用时保留默认联系方式 */ }
})

// 服务流程配置数据
const flowSteps = [
  { icon: 'bi-chat-dots', title: '在线咨询', desc: '初步了解需求与预算' },
  { icon: 'bi-clipboard-check', title: '方案定制', desc: '提供针对性办公方案' },
  { icon: 'bi-truck', title: '上门安装', desc: '快速配送及调试使用' },
  { icon: 'bi-shield-check', title: '售后保障', desc: '定期维护与耗材配送' }
]

const handleSubmit = async () => {
  if (!formData.name.trim() || !formData.phone.trim()) return
  isSubmitting.value = true
  try {
    await submitLead({
      name: formData.name.trim(),
      phone: formData.phone.trim(),
      category: formData.type,
      content: formData.message,
    })
    showStatus.value = true
    setTimeout(() => { showStatus.value = false }, 3500)
    // 清空表单
    Object.assign(formData, { name: '', phone: '', type: '', message: '' })
  } catch (e) {
    alert(e.message || '提交失败，请稍后重试')
  } finally {
    isSubmitting.value = false
  }
}

let map = null

onMounted(() => {
  // 【重要】设置安全密钥，否则 2.0 版本地图无法加载
  window._AMapSecurityConfig = {
    securityJsCode: '6427cae015cfd4935925e09d3cf43bb2', 
  }

  // 动态加载脚本
  const script = document.createElement('script')
  script.src = 'https://webapi.amap.com/maps?v=2.0&key=01b2f755499035d7fc9fcf0da9fc680f'
  script.async = true
  script.onload = () => {
    initAMap()
  }
  document.head.appendChild(script)
})

const initAMap = () => {
  if (!window.AMap) return
  
  map = new window.AMap.Map('amap-container', {
    viewMode: '2D',
    zoom: 16,
    center: [108.964398, 34.232499], // 鹏博大厦经纬度
    mapStyle: 'amap://styles/normal', // 可选：macaron, dark 等风格
  })

  // 添加公司位置标记
  const marker = new window.AMap.Marker({
    position: [108.964398, 34.232499],
    title: '西安市鸿瑞办公设备有限公司'
  })
  map.add(marker)
}

// 导航跳转逻辑 (保持你之前的即可)
const openNavigation = () => {
  window.open('https://uri.amap.com/marker?position=108.964398,34.232499&name=西安市鸿瑞办公设备有限公司', '_blank')
}

// 组件销毁时释放地图资源
onUnmounted(() => {
  if (map) {
    map.destroy()
    map = null
  }
})
</script>

<<style scoped>
/* 1. 流程样式优化 */
.flow-icon-wrapper {
  position: relative;
  width: 60px;
  height: 60px;
  background: #fff;
  border: 1px dashed #dc3545;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  font-size: 1.5rem;
  color: #dc3545;
  transition: all 0.4s ease;
}

.flow-item:hover .flow-icon-wrapper {
  background: #dc3545;
  color: #fff;
  border-style: solid;
  transform: rotate(360deg);
}

.step-number {
  position: absolute;
  top: -5px; right: -5px;
  width: 20px; height: 20px;
  background: #333; /* 改为深色，更有对比度 */
  color: #fff;
  font-size: 0.65rem;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}

/* 2. 核心 UI 组件 */
.section-title {
  border-left: 4px solid #dc3545;
  padding-left: 12px;
  font-weight: 700;
  font-size: 1.1rem;
}

.section-title-center::after {
  content: "";
  display: block;
  width: 30px;
  height: 3px;
  background: #dc3545;
  margin: 8px auto;
}

.icon-box {
  width: 42px; height: 42px;
  background: #fff5f5; color: #dc3545;
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.custom-input {
  border: 1px solid #eee; 
  padding: 12px 15px; 
  border-radius: 10px;
  font-size: 0.95rem;
  transition: 0.3s;
}

.custom-input:focus {
  border-color: #dc3545; 
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.1); 
  background: #fff;
}

/* 3. 辅助文字 */
.x-small { font-size: 0.75rem; }
.small-title { font-size: 0.9rem; }

/* 4. 交互反馈 */
.contact-link { transition: 0.3s; border-radius: 10px; }
.contact-link:hover { background: #f8f9fa; transform: translateX(5px); }

/* 5. 状态弹窗 */
.status-toast {
  position: fixed; /* 改为 fixed 确保在手机上居中 */
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  background: white; z-index: 2100;
  width: 280px; 
  border: 1px solid #f0f0f0;
}

/* 6. 移动端适配 */
@media (max-width: 991px) {
  .contact-hero { padding: 3rem 0 !important; }
  .display-6 { font-size: 1.8rem; }
  
  /* 流程在手机上 2x2 */
  .flow-item { padding: 10px !important; }
  .flow-icon-wrapper { width: 50px; height: 50px; font-size: 1.2rem; }
  
  .form-card { padding: 1.5rem !important; }
  .info-card { padding: 1.5rem !important; }
}

.title-underline {
  width: 40px; height: 3px; background: #dc3545;
}
</style>