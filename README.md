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

如果你希望我把图片资产也换成本地占位图片，或把项目转换为带更多页面路由（如单独的 News 页面），我可以直接在此工程内继续完善并打包新的 zip。
