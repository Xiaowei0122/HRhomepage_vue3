<template>
  <section id="news" class="section-wrap news-section">
    <div class="section-title">
      <h3>NEWS</h3>
      <h2>新闻公告</h2>
    </div>

    <div class="container-max">
      <div class="news-content-grid">
        <div class="news-list-wrapper">
          <div class="news-card" v-for="(n, i) in news" :key="i">
            <div class="news-card-body">
              <div class="news-text">
                <div class="news-meta">
                  <span class="news-tag">{{ n.tag }}</span>
                  <span class="news-date">{{ n.date }}</span>
                </div>
                <h5 class="news-title">{{ n.title }}</h5>
                <p class="news-summary">{{ n.summary }}</p>
              </div>
              <div class="news-more-link">
                <router-link to="/news">阅读全文 →</router-link>
              </div>
            </div>
          </div>
        </div>

        <div class="news-sidebar">
          <div class="contact-card-modern">
            <h5 class="contact-title">联系我们</h5>
            <div class="contact-info-list">
              <div class="info-item">
                <span class="info-label">服务热线</span>
                <a href="tel:02985550780" class="info-value red">029-85550780</a>
              </div>
              <div class="info-item">
                <span class="info-label">商城地址</span>
                <span class="info-value">ds.xashrbg.com</span>
              </div>
              <div class="info-item">
                <span class="info-label">办公地址</span>
                <span class="info-value">西安市雁塔中路19号鹏博大厦A座1001</span>
              </div>
            </div>

            <div class="qr-box-wrapper">
              <div class="qr-code">
                <img src="https://picsum.photos/96" alt="QR" />
              </div>
              <div class="qr-text">
                <div class="qr-name">公众号：鸿瑞办公服务</div>
                <div class="qr-tips">扫码关注获取售后与优惠</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const news = [
  { title: '鸿瑞办公成为某市政府打印设备指定供应商', date: '2025-09-18', tag: '公司新闻', summary: '凭借稳定的供货与高质量的售后服务，公司中标并将为市内多家单位提供设备与维保服务。' },
  { title: '推出“耗材定投”服务，降低企业采购成本', date: '2025-08-02', tag: '产品服务', summary: '为中大型客户提供一体化耗材管理计划，实现库存自动补货与费用可视化。' }
]
</script>

<style scoped>
/* --- 基础布局 --- */
.news-section { background: #f9f9f9; }

.news-content-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr; /* PC端 左右布局 */
  gap: 30px;
}

.news-card {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 20px;
  transition: 0.3s;
  border: 1px solid #eee;
}

.news-card:hover { transform: translateX(5px); border-color: var(--brand-red); }

.news-meta { display: flex; gap: 12px; margin-bottom: 10px; align-items: center; }
.news-tag { background: rgba(220, 53, 69, 0.1); color: #dc3545; font-size: 12px; padding: 2px 8px; border-radius: 4px; font-weight: 600; }
.news-date { color: #999; font-size: 13px; }
.news-title { font-weight: 800; margin-bottom: 10px; line-height: 1.4; color: #222; }
.news-summary { color: #666; font-size: 14px; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }

.news-more-link { margin-top: 15px; text-align: right; }
.news-more-link a { color: #dc3545; text-decoration: none; font-weight: 700; font-size: 14px; }

/* 侧边栏卡片 */
.contact-card-modern {
  background: #fff;
  padding: 30px;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  position: sticky;
  top: 100px;
}

.contact-title { font-weight: 800; margin-bottom: 20px; border-left: 4px solid #dc3545; padding-left: 12px; }
.info-item { margin-bottom: 15px; }
.info-label { display: block; font-size: 12px; color: #999; margin-bottom: 2px; }
.info-value { font-size: 15px; color: #333; font-weight: 600; word-break: break-all; }
.info-value.red { color: #dc3545; font-size: 18px; }

.qr-box-wrapper {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-top: 25px;
  padding-top: 20px;
  border-top: 1px dashed #eee;
}
.qr-code img { width: 80px; height: 80px; border-radius: 8px; border: 1px solid #eee; padding: 4px; }
.qr-name { font-weight: 800; font-size: 14px; }
.qr-tips { font-size: 12px; color: #999; }

/* --- 移动端适配 --- */
@media (max-width: 991px) {
  .news-content-grid {
    grid-template-columns: 1fr; /* 纵向堆叠 */
  }

  .news-card {
    padding: 18px;
  }

  .news-title { font-size: 17px; }

  .news-sidebar {
    margin-top: 10px;
  }

  .contact-card-modern {
    padding: 20px;
  }

  /* 移动端二维码居中显示 */
  .qr-box-wrapper {
    justify-content: center;
    text-align: left;
  }
}
</style>