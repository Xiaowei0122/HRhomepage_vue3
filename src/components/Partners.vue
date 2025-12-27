<template>
  <section id="partners" class="section-wrap" style="background:#fff;">
    <div class="section-title">
      <h3>PARTNERS</h3>
      <h2>合作伙伴</h2>
    </div>

    <div class="partners-wrap">
      <div class="partners-grid">
        <div class="partner-card" v-for="(p, idx) in partners" :key="idx" tabindex="0">
          <div class="imgbox"><img :src="p.src" :alt="p.alt" /></div>
        </div>
      </div>
      <!-- <div style="text-align:center; margin-top:18px; color:var(--muted); font-size:13px;">提示：将真实 Logo 放到 <code>assets/partners/</code> 下，并使用相同文件名即可自动替换</div> -->
    </div>
  </section>
</template>

<script setup>
const partners = [
  { src: '/assets/partners/deli.svg', alt: '得力' },
  { src: '/assets/partners/pentum.png', alt: '奔图' },
  { src: '/assets/partners/lenovo.png', alt: '联想' },
  { src: '/assets/partners/hp.png', alt: '惠普' },
  { src: '/assets/partners/canon.png', alt: '佳能' },
  { src: '/assets/partners/epson.png', alt: '爱普生' },
  { src: '/assets/partners/zg_placeholder.png', alt: '众冠硒鼓' },
  { src: '/assets/partners/huawei.png', alt: 'huawei' },
]
</script>
