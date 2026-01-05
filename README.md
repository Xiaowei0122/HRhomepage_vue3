# 鸿瑞办公 - Vue3 Demo

这是将原始单页 HTML 拆分为一个可运行的 **Vue 3 (Vite)** 项目的示例。  
保持了原始样式、布局与交互（包括 Swiper 轮播），并把每个页面模块拆成独立组件，CSS 提取到 `src/styles/main.css`。

## 项目结构（关键文件）
```
hongrui-vue3-demo/
├─ package.json
├─ index.html
├─ src/
│  ├─ main.js
│  ├─ App.vue
│  ├─ router/
│  │  └─ index.js
│  ├─ pages/
│  │  └─ HomePage.vue
│  ├─ components/
│  │  ├─ HeaderBar.vue
│  │  ├─ FooterBar.vue
│  │  ├─ HeroSwiper.vue
│  │  ├─ Services.vue
│  │  ├─ About.vue
│  │  ├─ Partners.vue
│  │  ├─ News.vue
│  │  └─ ContactAnchor.vue
│  └─ styles/
│     └─ main.css
└─ public/
   └─ assets/...
```

## 使用方法
1. 安装依赖：`npm install`  
2. 运行开发服务器：`npm run dev`  
3. 打包：`npm run build`  
4. 预览打包内容：`npm run preview`

## 说明
- Swiper 使用 `swiper` 官方 Vue 组件进行初始化（已在 `HeroSwiper.vue` 中迁移）。
- Bootstrap 只用于响应式栅格与少量组件（通过 npm 安装）。
- 所有页面锚点（如 `#services`）在组件里保留以维持平滑滚动行为。
- `assets/partners/` 文件夹包含占位文件，替换为真实 Logo 即可自动替换。

## Ver0.1版本
- 更新所有项目文件及组件

## Ver0.2版本
- 新增《新闻资讯》子页面及其详情的三级页面
- 修改HeaderBar和FooterBar的样式，导航添加了一些动画效果。
- 在导航的关于我们板块添加了二级页面。
- 修改了对应的router路由逻辑。
- 在App.vue中添加了组件插入的平滑过度效果。

## Ver0.3版本
- 新增《产品中心》的产品详情三级子页面
- 新增《我们的服务》板块的子页面
- 新增《合作伙伴&案例》板块的子页面
- 新增《联系我们》板块的子页面
- 修改《售后服务》，产品详情中的《产品彩页获取》的弹窗逻辑，进行友好化处理
- nav主导航和底端快速导航所有的router-link正常链接各个组件。

