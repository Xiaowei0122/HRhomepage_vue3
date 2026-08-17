<template>
  <section id="contact" class="section-wrap contact-anchor">
    <div class="container-max">
      <div class="cta-card text-center">
        <h2 class="cta-title">需要专业办公设备与运维服务？</h2>
        <p class="cta-desc">拨打电话或在线提交需求，我们将第一时间为您提供针对性方案。</p>
        <div class="cta-actions">
          <a :href="'tel:' + phone" class="btn btn-primary-custom">{{ phone }}</a>
          <router-link to="/contact" class="btn btn-outline-custom">在线提交需求</router-link>
        </div>
        <p v-if="address" class="cta-address"><i class="bi bi-geo-alt me-1"></i>{{ address }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getPublicConfig } from '../api/public'

const phone = ref('029-85550780')
const address = ref('陕西省西安市碑林区雁塔中路19号鹏博大厦A座1001')

onMounted(async () => {
  try {
    const cfg = await getPublicConfig()
    const c = cfg.contact || {}
    if (c.businessPhone || c.phone) phone.value = c.businessPhone || c.phone
    if (c.address) address.value = c.address
  } catch { /* 后端不可用时保留默认联系方式 */ }
})
</script>

<style scoped>
.contact-anchor {
  background: linear-gradient(135deg, #dc3545 0%, #b02a37 100%);
  padding: 70px 0;
}
.cta-card { color: #fff; }
.cta-title { font-size: 30px; font-weight: 800; margin-bottom: 12px; }
.cta-desc { font-size: 15px; opacity: 0.9; margin-bottom: 28px; }
.cta-actions { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; }
.btn-primary-custom {
  background: #fff; color: #dc3545; padding: 12px 30px; border-radius: 50px;
  font-weight: 700; text-decoration: none; font-size: 16px; transition: 0.3s;
}
.btn-outline-custom {
  background: transparent; color: #fff; border: 2px solid rgba(255,255,255,0.7);
  padding: 12px 30px; border-radius: 50px; font-weight: 700; text-decoration: none; font-size: 16px; transition: 0.3s;
}
.btn-primary-custom:hover { transform: translateY(-2px); }
.btn-outline-custom:hover { background: #fff; color: #dc3545; }
.cta-address { margin-top: 22px; font-size: 13px; opacity: 0.85; }

@media (max-width: 991px) {
  .contact-anchor { padding: 50px 0; }
  .cta-title { font-size: 24px; }
  .cta-actions a { width: 100%; max-width: 320px; text-align: center; }
}
</style>
