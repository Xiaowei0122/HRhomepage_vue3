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
              
              <a href="tel:02985550780" class="d-flex align-items-center mb-4 text-decoration-none text-dark contact-link">
                <div class="icon-box me-3"><i class="bi bi-headset"></i></div>
                <div>
                  <div class="text-muted x-small">服务热线 (点击拨打)</div>
                  <div class="fw-bold text-danger">029-85550780</div>
                </div>
              </a>

              <a href="tel:13488107706" class="d-flex align-items-center mb-4 text-decoration-none text-dark contact-link">
                <div class="icon-box me-3"><i class="bi bi-phone"></i></div>
                <div>
                  <div class="text-muted x-small">业务合作</div>
                  <div class="fw-bold text-danger">134-8810-7706</div>
                </div>
              </a>

              <div class="d-flex align-items-start mb-4">
                <div class="icon-box me-3"><i class="bi bi-geo-alt"></i></div>
                <div>
                  <div class="text-muted x-small">公司地址</div>
                  <div class="fw-bold small">西安市碑林区雁塔中路19号鹏博大厦A座1001</div>
                </div>
              </div>

              <div class="p-3 bg-light rounded-3">
                <p class="x-small text-muted mb-0"><i class="bi bi-clock me-2"></i>周一至周五 08:30 - 18:00</p>
              </div>
            </div>
            
            <div class="map-card shadow-sm rounded-4 overflow-hidden position-relative" style="height: 200px; background: #e9ecef;">
               <div class="h-100 d-flex flex-column align-items-center justify-content-center text-muted">
                <i class="bi bi-geo-fill fs-2 text-danger mb-2"></i>
                <span class="x-small fw-bold">西安鸿瑞办公设备有限公司</span>
                <button class="btn btn-sm btn-danger mt-2 rounded-pill px-4 shadow-sm" @click="openNavigation">开始导航</button>
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
import { ref, reactive } from 'vue'

const isSubmitting = ref(false)
const showStatus = ref(false)
const formData = reactive({ name: '', phone: '', type: '', message: '' })

// 服务流程配置数据
const flowSteps = [
  { icon: 'bi-chat-dots', title: '在线咨询', desc: '初步了解需求与预算' },
  { icon: 'bi-clipboard-check', title: '方案定制', desc: '提供针对性办公方案' },
  { icon: 'bi-truck', title: '上门安装', desc: '快速配送及调试使用' },
  { icon: 'bi-shield-check', title: '售后保障', desc: '定期维护与耗材配送' }
]

const handleSubmit = () => {
  isSubmitting.value = true
  setTimeout(() => {
    isSubmitting.value = false
    showStatus.value = true
    setTimeout(() => { showStatus.value = false }, 3500)
    // 清空表单
    Object.assign(formData, { name: '', phone: '', type: '', message: '' })
  }, 1200)
}

const openNavigation = () => {
  window.open('https://uri.amap.com/marker?position=108.966,34.233&name=西安市鸿瑞办公设备有限公司', '_blank')
}
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