<template>
  <div class="about-page">
    <nav class="sub-nav sticky-top shadow-sm bg-white">
      <div class="container d-flex justify-content-center">
        <a v-for="link in subNav" :key="link.id" :href="'#' + link.id" class="nav-link px-3 py-3">{{ link.name }}</a>
      </div>
    </nav>

    <section id="culture" class="container py-5">
      <div class="row g-4">
        <div class="col-md-4" v-for="item in culture" :key="item.title">
          <div class="culture-card p-4 text-center h-100">
            <div class="icon-circle mb-3 mx-auto text-danger"><i :class="item.icon"></i></div>
            <h4 class="fw-bold">{{ item.title }}</h4>
            <p class="text-muted mb-0">{{ item.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="structure" class="bg-light py-5">
      <div class="container">
        <h3 class="section-title text-center mb-5">组织架构 / 部门介绍</h3>
        <div class="row g-3">
          <div class="col-md-6 col-lg-3" v-for="dept in depts" :key="dept.name">
            <div class="dept-card p-4 bg-white shadow-sm border-0 h-100">
              <h5 class="text-danger border-bottom pb-2">{{ dept.name }}</h5>
              <p class="small text-muted mt-2 mb-0">{{ dept.duty }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="honor" class="container py-5">
      <h3 class="section-title text-center mb-5">资质荣誉 & 授权书</h3>
      <div class="row row-cols-2 row-cols-md-4 g-4">
        <div class="col" v-for="cert in 4" :key="cert">
          <div class="cert-item p-2 border rounded-4 text-center">
             <div class="aspect-ratio-box bg-light rounded-3 mb-2 d-flex align-items-center justify-content-center">
                <span class="text-muted small">授权证书 {{ cert }}</span>
             </div>
             <p class="small mb-0 fw-bold">代理证书 / 资质</p>
          </div>
        </div>
      </div>
    </section>

    <section id="gallery" class="bg-dark py-5 text-white">
      <div class="container">
        <h3 class="text-center mb-5">办公环境 / 公司相册</h3>
        <div class="row g-2">
          <div class="col-md-4" v-for="img in 6" :key="img">
            <div class="album-img-wrapper rounded-3 overflow-hidden">
               <img :src="`https://picsum.photos/600/400?random=${img}`" class="w-100 h-100 object-fit-cover" alt="Environment">
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const subNav = [
  { id: 'culture', name: '企业文化' },
  { id: 'structure', name: '组织架构' },
  { id: 'honor', name: '资质荣誉' },
  { id: 'gallery', name: '公司相册' }
]

const culture = [
  { title: '企业愿景', desc: '成为行业领先的数字化办公集成商', icon: 'bi bi-eye-fill' },
  { title: '企业使命', desc: '助力企业办公效率全面升级', icon: 'bi bi-lightning-charge-fill' },
  { title: '核心价值观', desc: '诚信、专业、高效、共赢', icon: 'bi bi-heart-fill' }
]

const depts = [
  { name: '直销大客户部', duty: '负责省市区级机关事业单位招标与项目交付。' },
  { name: '技术运维部', duty: '专业工程师，负责驻场运维与售后保障。' },
  { name: '分销与渠道拓展部', duty: '负责公司产品的渠道建设、战略合作伙伴关系的拓展与管理。' },
  { name: '仓储物流部', duty: '一站式耗材配送与设备库存实时管理。' },
  { name:'后勤保障部',duty:'日常运营中的商务支持、采购管理、物资保障及后勤服务'},
  { name:'财务与内控管理部',duty:'负责公司资金管理、预算编制、成本核算、税务筹划及财务风险管控，为业务运营提供专业财务支撑与决策依据。'},
]
</script>

<style scoped>
/* ============================================================
   1. 基础/PC端样式 (保持不变)
   ============================================================ */
.sub-nav { top: 0; z-index: 1020; border-bottom: 1px solid #eee; }
.sub-nav .nav-link { color: #555; font-weight: 500; transition: 0.3s; }
.sub-nav .nav-link:hover { color: #dc3545; }

.culture-card, .dept-card, .cert-item {
  border-radius: 20px;
  transition: transform 0.3s;
}

.culture-card:hover, .dept-card:hover {
  transform: translateY(-5px);
}

.icon-circle {
  width: 60px; height: 60px;
  background: #fff5f5;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem;
}

.section-title::after {
  content: "";
  display: block; width: 40px; height: 3px;
  background: #dc3545; margin: 10px auto;
}

.aspect-ratio-box { aspect-ratio: 3/4; border: 1px dashed #ddd; }
.album-img-wrapper { aspect-ratio: 16/9; cursor: pointer; }
.album-img-wrapper img { transition: 0.5s; }
.album-img-wrapper:hover img { transform: scale(1.1); }

/* ============================================================
   2. 移动端深度适配 (max-width: 991px) - 核心修改区域
   ============================================================ */
@media (max-width: 991px) {
  /* 2.0 通用间距调整 */
  .container.py-5, #culture.py-5, #honor.py-5 {
    padding-top: 2.5rem !important;
    padding-bottom: 2.5rem !important;
  }
  .section-title {
    font-size: 1.5rem !important;
    margin-bottom: 2rem !important;
  }

  /* 2.1 副导航：横向滑动 */
  .sub-nav .container {
    display: flex !important;
    overflow-x: auto;
    white-space: nowrap;
    justify-content: flex-start !important;
    padding: 0 10px;
    -webkit-overflow-scrolling: touch;
  }
  .sub-nav .container::-webkit-scrollbar { display: none; }
  .sub-nav .nav-link {
    padding: 12px 15px !important;
    font-size: 14px;
  }

 /* ==========================================================
     2.1 企业文化：打造“大气、精致”的左右图文布局
     ========================================================== */
  #culture {
    padding-top: 3rem !important; /* 增加顶部间距，更显稳重 */
    padding-bottom: 2rem !important;
  }
  
  #culture .row {
    display: flex !important;
    flex-direction: column !important; /* 恢复三行垂直排列 */
    gap: 20px !important; /* 增加卡片之间的间距 */
  }

  #culture .col-md-4 {
    width: 100% !important;
    padding: 0 !important;
  }

  .culture-card {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    text-align: left !important;
    /* 核心：增加Padding，让文字有呼吸感 */
    padding: 2rem 1.8rem !important; 
    border-radius: 16px; /* 加大圆角，更显圆润精致 */
    background: #fff;
    border: 1px solid #f2f2f2;
    box-shadow: 0 5px 15px rgba(0,0,0,0.03); /* 极淡的阴影区分 */
  }

  /* 图标区域微调 */
  .icon-circle {
    width: 50px !important; /* 适中的大小，不突兀 */
    height: 50px !important;
    min-width: 50px;
    font-size: 1.3rem !important;
    margin: 0 20px 0 0 !important; /* 增加图标与文字的间距 */
    color: #dc3545; /* 确保使用品牌红 */
  }

  /* 文字区域：让文字湊得不紧 */
  .culture-card h4 {
    font-size: 1.15rem !important; /* 稍微加大标题字号 */
    margin-bottom: 4px !important; /* 增加标题与描述的间距 */
    font-weight: 700;
    color: #333;
    padding-right: 1rem !important; /* 增加右侧内边距，防止文字贴边 */
  }

  .culture-card p {
    font-size: 13px !important; /* 描述文字大小 */
    line-height: 1.6 !important; /* 加大行高，防止文字拥挤 */
    margin-bottom: 0 !important;
    color: #666; /* 稍微加深文字颜色，增加可读性 */
  }

  /* ==========================================================
     2.2 组织架构 (保持 2x2 宫格，确保页面整体高度可控)
     ========================================================== */
  #structure {
    padding: 3rem 0 !important;
  }

  #structure .row {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 12px 0 !important;
    margin: 0 !important;
  }

  #structure .col-md-6, #structure .col-lg-3 {
    width: 50% !important;
    padding: 0 6px !important;
  }

  .dept-card {
    padding: 1.2rem !important;
    border-radius: 12px;
    height: 100%;
    text-align: center;
  }

  .dept-card h5 {
    font-size: 0.9rem !important;
    margin-bottom: 8px !important;
    padding-bottom: 8px !important;
  }

  .dept-card p {
    font-size: 11px !important;
    line-height: 1.4 !important;
    margin-bottom: 0;
  }

  #structure .row > .col:last-child {
    width: 100% !important;
    margin-top: 6px;
  }

  /* ==========================================================
     2.4 其他板块适配 (保持不变)
     ========================================================== */
  #honor .row-cols-2 > .col { width: 50%; }
  .cert-item { padding: 10px !important; border-radius: 12px !important; }
  .aspect-ratio-box { margin-bottom: 8px !important; }
  .cert-item p { font-size: 11px !important; line-height: 1.2; }
  .pb-5 { padding:0 !important;}

  #gallery .row.g-2 { --bs-gutter-x: 6px; --bs-gutter-y: 6px; }
  #gallery .col-md-4 { width: 33.3333%; float: left; }
  .album-img-wrapper { aspect-ratio: 1/1; border-radius: 4px !important; }
}
</style>