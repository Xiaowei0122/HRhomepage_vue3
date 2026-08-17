<template>
  <footer id="contact">
    <div class="container-max">
      <div class="row gy-4 align-items-start footer-main">
        
        <div class="col-lg-4 col-md-12">
          <div class="logo-small mb-3">
            <img src="/assets/partners/logo-icon.png" alt="logo" />
          </div>
          <p class="muted">西安鸿瑞办公 — 专注办公设备与运维服务，提供设备采购、售后维保、耗材配送、供应链管理及智能办公整体解决方案。经营办公耗材、办公设备、办公文具、劳保日杂等全品类产品，一站式满足企业办公需求。</p>
        </div>

        <div class="col-lg-4 col-md-6">
          <h5 class="white">联系我们</h5>
          <div class="contact-info">
            <p class="muted mb-1">服务热线： <strong class="brand">{{ servicePhone }}</strong></p>
            <p class="muted mb-1">商务合作： <strong class="brand">{{ businessPhone }}</strong></p>
            <p class="muted mb-1">鸿瑞商城：ds.xashrbg.com</p>
            <p class="muted mb-1">地址：{{ address }}</p>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 text-lg-end">
          <h5 class="footer-title">快速导航</h5>
          <ul class="footer-nav-list list-unstyled">
            <li><router-link to="/">首页</router-link></li>
            <li><router-link to="/products">产品中心</router-link></li>
            <li><router-link to="/services">我们的服务</router-link></li>
            <li><router-link to="/about">关于鸿瑞办公</router-link></li>
            <li><router-link to="/partner-cases">合作伙伴 & 案例</router-link></li>
            <li><router-link to="/news">新闻公告</router-link></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="copyright-wrap">
          <div class="copyright-text">
            © {{ year }} 西安鸿瑞办公设备有限公司 . 保留所有权利
          </div>
          <div class="beian-links">
            <a v-if="icp" href="https://beian.miit.gov.cn/" target="_blank">{{ icp }}</a>
            <a v-if="gongan" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=61010302xxxxxx" target="_blank">
              <img src="/public/assets/partners/batb.png" alt="beian" style="height: 18px; vertical-align: middle; margin-right: 6px;" />
              {{ gongan }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getPublicConfig } from '../api/public'

const year = new Date().getFullYear()
const servicePhone = ref('029-85550780')
const businessPhone = ref('134-8810-7706')
const address = ref('陕西省西安市碑林区雁塔中路19号鹏博大厦A座1001')
const icp = ref('陕ICP备XXXXXXXX号-1')
const gongan = ref('陕公网安备61010302xxxxxx号')

onMounted(async () => {
  try {
    const cfg = await getPublicConfig()
    const c = cfg.contact || {}
    if (c.phone) servicePhone.value = c.phone
    if (c.businessPhone) businessPhone.value = c.businessPhone
    if (c.address) address.value = c.address
    if (cfg.icp) icp.value = cfg.icp
    if (cfg.gongan) gongan.value = cfg.gongan
  } catch { /* 后端不可用时保留默认值 */ }
})
</script>

<style scoped>
/* --- 基础背景与间距 --- */
footer {
  background: #1a1a1a; /* 统一整个页脚背景色 */
  padding: 80px 0 0;
  color: #fff;
}

/* --- 文字颜色与层级优化 --- */
.white { 
  color: #ffffff; /* 标题纯白，增加视觉冲击 */
  font-weight: 700; 
  margin-bottom: 25px; 
  font-size: 18px;
}

.brand { 
  color: #dc3545; 
  font-weight: 600; 
}

/* 正文颜色：统一调亮，确保在深色背景下不“闷” */
.muted { 
  color: #cccccc; 
  font-size: 14px; 
  line-height: 1.8; 
}

/* --- Logo 区域优化 --- */
.logo-small img {
  height: 45px;
  width: auto;
  display: block;
  /* 移除 filter 滤镜，确保 Logo 原始颜色正常显示 */
  /* 如果 Logo 本身是红色的，它在黑底上会非常醒目 */
}

/* --- 快速导航 PC 样式 --- */
.footer-nav-list {
  padding: 0;
  margin: 0;
  list-style: none;
}
.footer-nav-list li { margin-bottom: 12px; }
.footer-nav-list a { 
  color: #aaaaaa; 
  text-decoration: none; 
  transition: all 0.3s ease; 
  font-size: 14px; 
}

/* PC端悬浮：品牌红点亮 */
@media (min-width: 992px) {
  .footer-nav-list a:hover {
    color: #dc3545;
    padding-left: 6px; /* 增加灵动的位移感 */
  }
}

/* --- 版权区样式 (保持背景一致) --- */
.footer-bottom {
  margin-top: 60px;
  padding: 30px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.05); /* 仅留极淡的分隔线 */
  background: transparent; /* 移除黑色背景，保持整体一致 */
}

.copyright-wrap {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #666666; /* 降低版权信息视觉比重 */
  font-size: 13px;
}

.beian-links a {
  color: #666666;
  text-decoration: none;
  margin-left: 20px;
  transition: 0.3s;
}
.beian-links a:hover { color: #aaaaaa; }

/* ============================================================
   移动端 (完全保留之前的红色竖线与标签化布局)
   ============================================================ */
@media (max-width: 991px) {
  footer { padding-top: 50px; }
  
  .white, .footer-title {
    font-size: 16px;
    position: relative;
    padding-left: 15px;
    text-align: left !important;
  }
  .white::before, .footer-title::before {
    content: "";
    position: absolute;
    left: 0;
    top: 5px;
    bottom: 5px;
    width: 3px;
    background: #dc3545;
    border-radius: 2px;
  }

  .footer-nav-list {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 15px;
  }
  .footer-nav-list li { margin-bottom: 0; }
  .footer-nav-list a {
    background: rgba(255, 255, 255, 0.05);
    padding: 6px 15px;
    border-radius: 6px;
    color: #bbbbbb;
  }

  .copyright-wrap {
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }
  .beian-links a { margin: 0 5px; }
}
</style>