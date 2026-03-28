<template>
  <div class="partner-case-view bg-light">
    <section class="case-hero py-5 text-center">
      <div class="container py-4">
        <h6 class="text-danger fw-bold">PARTNERS & CASES</h6>
        <h1 class="display-5 fw-bold text-dark">合作伙伴与案例</h1>
        <div class="red-line mx-auto mt-3"></div>
      </div>
    </section>

    <section class="container mb-5">
      <div class="ui-card p-5 border-0">
        <h4 class="text-center fw-bold mb-5">官方授权品牌</h4>
        <div class="row g-4 align-items-center justify-content-center">
           <div class="col-6 col-md-3 text-center brand-wrapper" v-for="b in brands" :key="b.name">
             <div class="brand-box p-3 border rounded-3">
               <img :src="b.logo" :alt="b.name" class="img-fluid gray-to-color" style="max-height: 50px;">
               <div class="brand-info mt-2 small fw-bold text-muted">{{ b.role }}</div>
             </div>
           </div>
        </div>
      </div>
    </section>

    <section class="container py-5">
      <h3 class="fw-bold mb-5 text-center">行业成功案例</h3>
      <div class="row g-4">
        <div class="col-lg-6" v-for="(item, idx) in caseStories" :key="idx">
          <div class="ui-card case-item-card d-flex flex-column flex-md-row overflow-hidden h-100">
            <div class="case-img-side" :style="{ backgroundColor: '#f8f9fa', backgroundImage: `url(${item.img})` }"></div>
            <div class="case-content-side p-4 flex-grow-1">
              <span class="badge bg-danger mb-2">{{ item.tag }}</span>
              <h5 class="fw-bold mb-3">{{ item.title }}</h5>
              <p class="text-muted small">{{ item.desc }}</p>
              <div class="mt-3 pt-3 border-top text-danger fw-bold small">
                效率提升: {{ item.stat }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// 修正报错：定义模板所需的变量
const brands = [
  { name: 'deli', logo: 'assets/partners/deli.svg', role: '核心合作伙伴' },
  { name: 'Pantum', logo: 'assets/partners/pentum.png', role: '核心合作伙伴' },
  { name: 'Zhonguan', logo: 'assets/partners/zg_placeholder.png', role: '品牌耗材商' },
  { name: 'Lenovo', logo: 'assets/partners/lenovo.png', role: '授权经销商' },
  { name: 'HP', logo: 'assets/partners/hp.png', role: '金牌合作伙伴' },
  { name: 'Canon', logo: 'assets/partners/canon.png', role: '专业售后中心' },
  { name: 'Epson', logo: 'assets/partners/epson.png', role: '特约服务商' },
  { name: 'Huawei', logo: 'assets/partners/huawei.png', role: '生态合作伙伴' }
]

const caseStories = [
  { 
    tag: '教育行业', 
    title: '某高校自助打印系统部署', 
    desc: '通过云打印方案解决了学生排队打印难题，实现了24小时无人值守服务。', 
    stat: '50%', 
    img: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400' 
  },
  { 
    tag: '政府办公', 
    title: '某机关单位信创设备采购', 
    desc: '提供全套符合安全标准的国产化办公设备，并建立完善的定期维保体系。', 
    stat: '35%', 
    img: 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=400' 
  }
]
</script>

<style scoped>
/* 1. 通用卡片容器 (ui-card) - 继承自您的基础定义 */
.ui-card { 
  background: #fff; 
  border-radius: 12px; 
  box-shadow: 0 4px 12px rgba(0,0,0,0.03); 
  border: 1px solid #ebedf0;
  transition: all 0.3s ease;
}

/* 2. 品牌矩阵部分 - 解决框体不一致问题 */
.brand-box {
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 8px;
  padding: 20px 10px;
  height: 140px;            /* 统一所有品牌框的高度 */
  display: flex;
  flex-direction: column;
  justify-content: center;  /* 垂直居中 */
  align-items: center;      /* 水平居中 */
  transition: all 0.3s ease;
}

.brand-box:hover {
  border-color: #dc3545;    /* 悬停时边框变红 */
  box-shadow: 0 8px 20px rgba(0,0,0,0.06);
  transform: translateY(-5px);
}

/* 3. Logo 图片控制 - 解决图片撑大容器问题 */
.logo-container {
  width: 100%;
  height: 55px;             /* 限制 Logo 占据的高度区域 */
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 12px;
}

.brand-img {
  max-width: 85%;           /* 宽度不超出框体 */
  max-height: 100%;         /* 高度不超出 logo-container */
  object-fit: contain;      /* 保持比例，不拉伸 */
  filter: grayscale(100%);  /* 您的灰色特效 */
  opacity: 0.6;
  transition: 0.5s;
}

/* 悬停变色特效 */
.brand-wrapper:hover .brand-img {
  filter: grayscale(0%);
  opacity: 1;
}

/* 4. 品牌文字信息 */
.role-text {
  font-size: 13px;
  font-weight: 600;
  color: #888;
  white-space: nowrap;      /* 保证文字不换行 */
}

/* 5. 行业案例部分样式 */
.red-line { 
  width: 50px; 
  height: 4px; 
  background: #dc3545; 
  border-radius: 2px; 
}

.case-item-card {
  transition: 0.3s;
}

.case-item-card:hover {
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.case-img-side { 
  width: 40%; 
  min-height: 180px; 
  background-size: cover; 
  background-position: center; 
}

/* 6. 响应式适配 */
@media (max-width: 991px) {
  /* 1. 头部 Hero 区域：缩小字号，避免折行过多 */
  .case-hero {
    padding: 2.5rem 0 !important;
  }
  .case-hero h1 {
    font-size: 1.8rem !important;
    margin-top: 10px;
  }
  .case-hero h6 {
    font-size: 0.8rem !important;
    letter-spacing: 1px;
  }

  /* 2. 品牌矩阵部分：从 4 列改为 2 列，并优化间距 */
  .ui-card.p-5 {
    padding: 1.5rem !important; /* 缩小外部大卡片的内边距 */
  }

  .ui-card h4 {
    font-size: 1.1rem !important;
    margin-bottom: 1.5rem !important;
  }

  /* 调整品牌格子 */
  .brand-box {
    height: 110px !important; /* 进一步压缩高度，保持紧凑 */
    padding: 12px 8px !important;
    border-radius: 12px !important;
  }

  .brand-box img {
    max-height: 35px !important; /* 缩小 Logo 尺寸 */
    margin-bottom: 5px;
  }

  .brand-info {
    font-size: 10px !important; /* 缩小底部文字 */
    transform: scale(0.9); /* 针对极细文字微调 */
  }

  /* 3. 行业案例部分：改为垂直堆叠，并优化图文比例 */
  #cases-section {
    padding: 2rem 0 !important;
  }

  .case-item-card {
    flex-direction: column !important; /* 强制图文上下排列 */
    border-radius: 16px !important;
  }

  .case-img-side {
    width: 100% !important; /* 图片占满宽度 */
    height: 200px !important; /* 固定高度，防止长短不一 */
    min-height: 200px !important;
  }

  .case-content-side {
    padding: 1.25rem !important;
  }

  .case-content-side h5 {
    font-size: 1.1rem !important;
    margin-bottom: 10px !important;
  }

  .case-content-side p {
    font-size: 13px !important;
    line-height: 1.5 !important;
    margin-bottom: 15px !important;
  }

  /* 4. 统计信息：在移动端更醒目 */
  .case-content-side .border-top {
    margin-top: 10px !important;
    padding-top: 12px !important;
    font-size: 12px !important;
  }

  /* 调整布局行间距 */
  .row.g-4 {
    --bs-gutter-y: 1rem !important;
  }
}
</style>
