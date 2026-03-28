<template>
  <section id="services" class="section-wrap services">
    <div class="section-title">
      <h3>OUR SERVICES</h3>
      <h2>我们的服务</h2>
    </div>

    <div class="container-max">
      <div class="services-grid">
        <div class="service-card" v-for="(s, idx) in services" :key="idx">
          <div class="service-icon-box">
            <span class="icon-emoji">{{ s.icon }}</span>
          </div>
          <h5 class="service-card-title">{{ s.title }}</h5>
          <p class="service-card-desc">{{ s.desc }}</p>
          
          <router-link 
            :to="{ path: '/services', hash: '#' + s.id }" 
            class="service-link"
          >
            了解更多 →
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const services = [
  { id: 'sales', icon: '🖨️', title: '办公设备销售', desc: '提供打印机、复印机、投影等主流办公设备采购与配置。' },
  { id: 'repair', icon: '🛠️', title: '打印机/复印机维修', desc: '全国服务网络，快速到场、原厂配件与专业工程师保障。' },
  { id: 'supplies', icon: '📦', title: '耗材配送服务', desc: '稳定供货与库存管理，支持协议客户优先配送。' },
  { id: 'solutions', icon: '💡', title: '智能化办公方案', desc: 'OA集成、打印管控与设备运维一体化，提升管理效率。' }
]
</script>

<style scoped>
/* --- 基础布局 --- */
.services { background: #fff; }

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* PC端 4 列 */
  gap: 24px;
}

.service-card {
  background: #fff;
  padding: 30px 20px;
  border-radius: var(--card-radius, 12px);
  text-align: center;
  box-shadow: 0 10px 30px rgba(20,20,20,0.05);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
  border: 1px solid #f5f5f5;
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 48px rgba(20,20,20,0.12);
}

.service-icon-box {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, rgba(211,34,35,0.08), rgba(211,34,35,0.02));
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
}

.icon-emoji { font-size: 28px; }

.service-card-title {
  font-size: 18px;
  font-weight: 800;
  margin-bottom: 12px;
  color: #222;
}

.service-card-desc {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
  flex-grow: 1; /* 确保描述文字撑开高度，使按钮对齐 */
}

.service-link {
  color: var(--brand-red, #dc3545);
  font-weight: 700;
  text-decoration: none;
  font-size: 14px;
  transition: opacity 0.2s;
}

.service-link:hover { opacity: 0.8; }

/* --- 移动端适配 (核心修改) --- */
@media (max-width: 991px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr); /* 手机端两两排列，更精致 */
    gap: 15px; /* 减小间距 */
  }

  .service-card {
    padding: 20px 15px; /* 减小内边距，腾出空间 */
  }

  .service-icon-box {
    width: 50px;
    height: 50px;
    margin-bottom: 15px;
    border-radius: 12px;
  }

  .icon-emoji { font-size: 22px; }

  .service-card-title {
    font-size: 15px; /* 缩小标题 */
    margin-bottom: 8px;
  }

  .service-card-desc {
    font-size: 12px; /* 缩小描述文字 */
    line-height: 1.5;
    margin-bottom: 15px;
    /* 限制描述文字在手机端只显示两行，防止高度不一 */
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .service-link { font-size: 13px; }
}

/* 极小屏幕适配 (如 iPhone SE) */
@media (max-width: 375px) {
  .services-grid {
    grid-template-columns: 1fr; /* 如果屏幕太窄，退回到单列 */
  }
}
</style>