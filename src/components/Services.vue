<template>
  <section id="services" class="section-wrap services" style="background:#fff;">
    <div class="section-title">
      <h3>OUR SERVICES</h3>
      <h2>我们的服务</h2>
    </div>

    <div class="container-max">
      <div class="row g-4">
        <div class="col-md-3" v-for="(s, idx) in services" :key="idx">
          <div class="card p-4 text-center h-100">
            <div class="service-icon">{{ s.icon }}</div>
            <h5 style="font-weight:800; margin-top:6px;">{{ s.title }}</h5>
            <p class="text-muted" style="font-size:14px;">{{ s.desc }}</p>
            <a href="#" style="color:var(--brand-red); font-weight:700;">了解更多 →</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const services = [
  { icon: '🖨️', title: '办公设备销售', desc: '提供打印机、复印机、投影等主流办公设备采购与配置。' },
  { icon: '🛠️', title: '打印机/复印机维修', desc: '全国服务网络，快速到场、原厂配件与专业工程师保障。' },
  { icon: '📦', title: '耗材配送服务', desc: '稳定供货与库存管理，支持定期补货与协议客户优先配送。' },
  { icon: '💡', title: '智能化办公解决方案', desc: 'OA集成、打印管控与设备运维一体化方案，提升管理效率。' }
]
</script>
