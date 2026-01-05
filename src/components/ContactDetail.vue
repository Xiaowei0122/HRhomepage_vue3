<template>
  <div class="contact-page-container">
    <section class="contact-hero text-center py-5 bg-dark text-white">
      <div class="container py-4">
        <h1 class="display-5 fw-bold mb-3">联系我们</h1>
        <p class="lead opacity-75">西安鸿瑞办公 · 24小时响应 · 全城上门服务</p>
        <p class="lead opacity-75">专业的办公方案，只需一个电话或一次到访</p>
        <div class="title-underline mx-auto"></div>
      </div>
    </section>

    <section class="service-flow py-5 bg-white">
      <div class="container">
        <div class="text-center mb-5">
          <h4 class="fw-bold">合作流程</h4>
          <p class="text-muted small">简单四步，开启高效办公体验</p>
        </div>
        <div class="row g-4 text-center">
          <div class="col-6 col-md-3" v-for="(step, index) in flowSteps" :key="index">
            <div class="flow-item">
              <div class="flow-icon-wrapper">
                <i :class="['bi', step.icon]"></i>
                <div class="step-number">{{ index + 1 }}</div>
              </div>
              <h6 class="mt-3 fw-bold">{{ step.title }}</h6>
              <p class="small text-muted d-none d-md-block">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="contact-main py-5 bg-light">
      <div class="container">
        <div class="row g-5">
          <div class="col-lg-5">
            <div class="info-card shadow-sm p-4 rounded-4 bg-white mb-4">
              <h5 class="section-title mb-4">业务咨询</h5>
              <div class="d-flex align-items-center mb-4">
                <div class="icon-box me-3"><i class="bi bi-headset"></i></div>
                <div>
                  <div class="text-muted small">服务热线</div>
                  <div class="fs-5 fw-bold text-danger">029-85550780 / 85550781</div>
                </div>
              </div>
              <div class="d-flex align-items-center mb-4">
                <div class="icon-box me-3"><i class="bi bi-headset"></i></div>
                <div>
                  <div class="text-muted small">业务合作</div>
                  <div class="fs-5 fw-bold text-danger">134-8810-7706</div>
                </div>
              </div>
              <div class="d-flex align-items-center mb-4">
                <div class="icon-box me-3"><i class="bi bi-geo-alt"></i></div>
                <div>
                  <div class="text-muted small">公司地址</div>
                  <div class="fw-bold">西安市碑林区雁塔中路19号鹏博大厦A座1001</div>
                </div>
              </div>
              <div class="p-3 bg-light rounded-3">
                <p class="small text-muted mb-0"><i class="bi bi-clock me-2"></i>周一至周五 08:30 - 18:00 (紧急维护全天候)</p>
              </div>
            </div>
            
            <div class="map-card shadow-sm rounded-4 overflow-hidden" style="height: 220px; background: #eee;">
              <div class="h-100 d-flex flex-column align-items-center justify-content-center text-muted">
                <i class="bi bi-map fs-2 mb-2"></i>
                <span class="small">高德地图 API 交互位</span>
                <button class="btn btn-sm btn-outline-danger mt-2 rounded-pill px-3" @click="openNavigation">导航去公司</button>
              </div>
            </div>
          </div>

          <div class="col-lg-7 position-relative">
            <div class="form-card shadow-sm p-4 p-md-5 rounded-4 bg-white h-100">
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
                    <option value="rent">设备租赁及销售咨询</option>
                    <option value="buy">耗材/办公用品采购咨询</option>
                    <option value="service">用户维护报修咨询</option>
                  </select>
                </div>
                <div class="col-12">
                  <textarea v-model="formData.message" class="form-control custom-input" rows="4" placeholder="请简要描述您的需求..." required></textarea>
                </div>
                <div class="col-12 text-end">
                  <button type="submit" class="btn btn-danger btn-lg px-5 rounded-pill shadow-sm" :disabled="isSubmitting">
                    {{ isSubmitting ? '提交中...' : '提交需求' }}
                  </button>
                </div>
              </form>
            </div>

            <transition name="toast">
              <div v-if="showStatus" class="status-toast shadow-lg rounded-4 p-4 text-center">
                <i class="bi bi-check-circle-fill text-success fs-1 mb-3"></i>
                <h5 class="fw-bold">提交成功</h5>
                <p class="text-muted small mb-0">感谢信任，我们将尽快为您安排经理回电。</p>
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

<style scoped>
/* 流程项样式 */
.flow-icon-wrapper {
  position: relative;
  width: 70px;
  height: 70px;
  background: #f8f9fa;
  border: 1px dashed #dc3545;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  font-size: 1.8rem;
  color: #dc3545;
  transition: all 0.3s;
}
.flow-item:hover .flow-icon-wrapper {
  background: #dc3545;
  color: #fff;
  border-style: solid;
}
.step-number {
  position: absolute;
  top: 0; right: 0;
  width: 22px; height: 22px;
  background: #dc3545;
  color: #fff;
  font-size: 0.7rem;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}

/* 核心 UI */
.section-title {
  border-left: 4px solid #dc3545;
  padding-left: 15px;
  font-weight: 700;
}
.icon-box {
  width: 45px; height: 45px;
  background: #fff5f5; color: #dc3545;
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem;
}
.custom-input {
  border: 1px solid #eee; padding: 12px; border-radius: 10px;
}
.custom-input:focus {
  border-color: #dc3545; box-shadow: none; background: #fff;
}

/* 状态弹窗动画 */
.status-toast {
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  background: white; z-index: 100;
  width: 300px; border: 1px solid #f0f0f0;
}
.toast-enter-active, .toast-leave-active {
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.toast-enter-from, .toast-leave-to {
  opacity: 0; transform: translate(-50%, -40%) scale(0.8);
}

.title-underline {
  width: 50px; height: 3px; background: #dc3545; margin-top: 12px;
}
</style>