<template>
  <section id="partners" class="section-wrap partners-section">
    <div class="section-title">
      <h3>PARTNERS</h3>
      <h2>合作伙伴</h2>
    </div>

    <div class="container-max">
      <div class="partners-container">
        <div class="partners-grid">
          <div 
            class="partner-card" 
            v-for="(p, idx) in partners" 
            :key="idx" 
            tabindex="0"
          >
            <div class="partner-img-box">
              <img :src="p.src" :alt="p.alt" class="partner-logo" />
            </div>
          </div>
        </div>
        
        <div class="disclaimer">
          免责声明：此处仅展示授权我司的合作品牌以及我司长期销售的品牌产品，禁止用作其他使用。（详见关于鸿瑞-资质荣誉页）
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// 确保路径以 / 开头，对应 public 目录
const partners = [
  { src: '/assets/partners/deli.svg', alt: '得力' },
  { src: '/assets/partners/pentum.png', alt: '奔图' },
  { src: '/assets/partners/lenovo.png', alt: '联想' },
  { src: '/assets/partners/hp.png', alt: '惠普' },
  { src: '/assets/partners/canon.png', alt: '佳能' },
  { src: '/assets/partners/epson.png', alt: '爱普生' },
  { src: '/assets/partners/zg_placeholder.png', alt: '众冠硒鼓' },
  { src: '/assets/partners/huawei.png', alt: '华为' },
]
</script>

<style scoped>
.partners-section { background: #fff; padding: 60px 0; }

.partners-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.partner-card {
  aspect-ratio: 16 / 9;
  background: #fcfcfc;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 15px;
  transition: all 0.3s ease;
}

.partner-card:hover {
  border-color: #dc3545;
  box-shadow: 0 10px 20px rgba(0,0,0,0.05);
  transform: translateY(-3px);
}

.partner-img-box {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.partner-logo {
  max-width: 80%;
  max-height: 65%;
  object-fit: contain;
  /* 重点：不再使用 grayscale 滤镜，改用透明度，防止 Logo 消失 */
  opacity: 0.5; 
  transition: all 0.3s;
}

.partner-card:hover .partner-logo {
  opacity: 1; /* 鼠标悬浮恢复 100% 亮度 */
}

.disclaimer {
  text-align: center;
  margin-top: 30px;
  color: #999;
  font-size: 13px;
  padding: 0 20px;
}

/* --- 移动端适配 --- */
@media (max-width: 991px) {
  .partners-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
  }

  .partner-card {
    padding: 10px;
    border-radius: 8px;
  }

  .partner-logo {
    opacity: 0.9; /* 移动端直接显示，不再需要悬浮 */
    max-width: 85%;
  }

  .disclaimer {
    font-size: 11px;
    margin-top: 20px;
  }
}
</style>