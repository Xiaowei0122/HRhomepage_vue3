<template>
  <div class="about-page pb-5">
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
  { title: '企业愿景', desc: '成为行业领先的数字化办公集成商', icon: 'bi bi-eye' },
  { title: '企业使命', desc: '助力企业办公效率全面升级', icon: 'bi bi-lightning-charge' },
  { title: '核心价值观', desc: '诚信、专业、高效、共赢', icon: 'bi bi-heart' }
]

const depts = [
  { name: '直销大客户部', duty: '负责省市区级机关事业单位招标与项目交付。' },
  { name: '技术运维部', duty: '专业工程师，负责驻场运维与售后保障。' },
  { name: '分销与渠道拓展部', duty: '负责公司产品的渠道建设、战略合作伙伴关系的拓展与管理。' },
  { name: '仓储物流部', duty: '一站式耗材配送与设备库存实时管理。' },
  {name:'后勤保障部',duty:'日常运营中的商务支持、采购管理、物资保障及后勤服务'}
]
</script>

<style scoped>
/* 统一样式，保持与主页一致的 16px/24px 圆角 */
.sub-nav { top: 0; z-index: 1020; border-bottom: 1px solid #eee; }
.sub-nav .nav-link { color: #555; font-weight: 500; transition: 0.3s; }
.sub-nav .nav-link:hover { color: #dc3545; }

.culture-card, .dept-card, .cert-item {
  border-radius: 20px; /* 大圆角保持一致 */
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
</style>