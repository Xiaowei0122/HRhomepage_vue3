<template>
  <section id="about" class="section-wrap about">
    <div class="section-title">
      <h3>ABOUT HONGRUI</h3>
      <h2>关于鸿瑞办公</h2>
    </div>

    <div class="container-max">
      <div class="about-card-custom">
        <div class="about-media-wrapper">
          <img src="https://images.unsplash.com/photo-1527689368864-3a821dbccc34?auto=format&fit=crop&w=1200&q=60" alt="关于我们图" class="about-img" />
          
          <div class="stats-grid-overlay">
            <div class="stat-item" v-for="(stat, i) in stats" :key="i">
              <div class="num">{{ stat.num }}</div>
              <div class="label">{{ stat.label }}</div>
            </div>
          </div>
        </div>

        <div class="about-content-text">
          <h4 class="sub-title-red">我们的实力</h4>
          <h3 class="main-title-dark">二十年办公设备与服务沉淀</h3>
          <p class="description-text">
            鸿瑞办公深耕办公设备与运维服务领域，覆盖企业、政府、教育等行业。我们不仅提供优选设备与耗材，
            更通过标准化运维体系与数字化平台，保障设备稳定运行，帮助客户持续降低成本与提升效率。
          </p>

          <ul class="features-list">
            <li><strong>•</strong> 原厂配件、专业工程师团队</li>
            <li><strong>•</strong> 灵活的耗材配送与库存管理</li>
            <li><strong>•</strong> 定制化智能办公与打印管控方案</li>
          </ul>

          <div class="about-actions">
            <a href="#contact" class="btn-about-primary">联系我们</a>
            <a href="#services" class="btn-about-outline">查看服务 →</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const stats = [
  { num: '全平台', label: '省市区级采购入驻' },
  { num: '50+', label: '专业业务团队' },
  { num: '500+', label: '企事业客户' },
  { num: '24/7', label: '售后响应' }
]
</script>

<style scoped>
/* --- 基础布局 --- */
.about-card-custom {
  display: flex;
  background: #fff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(0,0,0,0.06);
}

.about-media-wrapper {
  flex: 1;
  position: relative;
  min-height: 450px;
}

.about-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 统计数据层布局 - 改为网格 */
.stats-grid-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  background: rgba(220, 53, 69, 0.9); /* 品牌红透明背景 */
  backdrop-filter: blur(5px);
  padding: 20px;
}

.stat-item {
  padding: 10px;
  color: #fff;
  text-align: center;
}

.stat-item .num { font-size: 18px; font-weight: 800; margin-bottom: 2px; }
.stat-item .label { font-size: 12px; opacity: 0.9; }

.about-content-text {
  flex: 1;
  padding: 50px;
}

.sub-title-red { color: #dc3545; font-weight: 700; margin-bottom: 8px; font-size: 16px; }
.main-title-dark { font-weight: 800; margin-bottom: 20px; font-size: 28px; line-height: 1.3; }
.description-text { color: #666; line-height: 1.8; margin-bottom: 25px; }

.features-list { list-style: none; padding: 0; margin-bottom: 30px; }
.features-list li { margin-bottom: 12px; color: #444; font-size: 15px; }
.features-list strong { color: #dc3545; margin-right: 8px; }

.about-actions { display: flex; gap: 15px; }
.btn-about-primary { background: #dc3545; color: #fff; padding: 12px 24px; border-radius: 10px; font-weight: 700; text-decoration: none; transition: 0.3s; }
.btn-about-outline { border: 1px solid #dc3545; color: #dc3545; padding: 12px 24px; border-radius: 10px; font-weight: 700; text-decoration: none; transition: 0.3s; }

/* --- 移动端适配 --- */
@media (max-width: 991px) {
  .about-card-custom { flex-direction: column; border-radius: 15px; }

  .about-media-wrapper { min-height: 300px; }

  .stats-grid-overlay {
    position: relative; /* 移动端不再悬浮，跟随在图片下方 */
    grid-template-columns: repeat(2, 1fr);
    padding: 15px 5px;
  }

  .about-content-text { padding: 30px 20px; }

  .main-title-dark { font-size: 22px; }
  
  .about-actions {
    flex-direction: row; /* 保持横排，但平分宽度 */
  }

  .btn-about-primary, .btn-about-outline {
    flex: 1;
    text-align: center;
    padding: 12px 10px;
    font-size: 14px;
  }
}
</style>