<template>
  <section id="news" class="section-wrap about">
    <div class="section-title">
      <h3>NEWS</h3>
      <h2>新闻公告</h2>
    </div>

    <div class="container-max">
      <div class="row g-4">
        <div class="col-lg-7">
          <div class="news-card" v-for="(n, i) in news" :key="i">
            <div class="d-flex justify-content-between align-items-start">
              <div>
                <h5 style="font-weight:800; margin-bottom:6px;">{{ n.title }}</h5>
                <small style="color:var(--muted);">{{ n.date }} · {{ n.tag }}</small>
                <p class="text-muted mt-2">{{ n.summary }}</p>
              </div>
              <div style="min-width:110px;">
                <a href="#" style="color:var(--brand-red); font-weight:700;">阅读更多 →</a>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="p-3" style="background:#fff; border-radius:12px; box-shadow:0 8px 20px rgba(0,0,0,0.04);">
            <h5 style="font-weight:800;">联系我们</h5>
            <p class="text-muted mb-1">服务热线： <strong style="color:var(--brand-red);">029-85550780</strong></p>
            <p class="text-muted mb-1">邮箱：service@example.com</p>
            <p class="text-muted mb-2">地址：陕西省西安市XXX工业园</p>

            <div class="d-flex align-items-center gap-3 mt-3">
              <div style="width:96px; height:96px; background:#fff; border-radius:8px; overflow:hidden; display:flex; align-items:center; justify-content:center;">
                <img src="https://picsum.photos/96" alt="QR" style="width:88px; height:88px; object-fit:cover; border-radius:6px;">
              </div>
              <div>
                <div style="font-weight:800;">公众号：鸿瑞办公服务</div>
                <div style="color:var(--muted); font-size:13px;">扫码关注获取售后与耗材优惠</div>
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
