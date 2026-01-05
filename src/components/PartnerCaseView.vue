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
    img: 'https://images.unsplash.com/photo-1523050853023-8c2d27443ef8?w=400' 
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
@media (max-width: 768px) {
  .brand-box {
    height: 120px;          /* 移动端稍微收窄高度 */
  }
  .case-img-side { 
    width: 100%;            /* 移动端案例图占满宽度 */
    height: 200px;
  }
}
</style>
