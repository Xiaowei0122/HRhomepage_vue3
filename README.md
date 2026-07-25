# 西安鸿瑞办公 - 企业官网

基于 **Vue 3 + Vite** 构建的响应式企业官网，涵盖产品展示、新闻动态、服务介绍、合作伙伴案例、关于我们、在线联系等完整模块。

## 技术栈

| 类别 | 技术 |
|------|------|
| 框架 | Vue 3 (Composition API) |
| 构建工具 | Vite 5 |
| 路由 | Vue Router 4 (History 模式) |
| UI 库 | Bootstrap 5 (栅格 + 组件) |
| 图标 | Bootstrap Icons |
| 轮播 | Swiper 10 |
| HTTP 客户端 | 原生 fetch 封装（零依赖） |
| 地图 | 高德地图 API |

## 项目结构

```
HRhomepage_vue3/
├── index.html                       # 入口 HTML
├── vite.config.mjs                  # Vite 配置
├── package.json
├── public/
│   └── assets/
│       └── partners/                # Logo 及静态资源
└── src/
    ├── main.js                      # 应用入口
    ├── App.vue                      # 根组件（Header + RouterView + Footer）
    ├── router/
    │   └── index.js                 # 路由配置（含滚动行为优化）
    ├── pages/
    │   └── HomePage.vue             # 首页（组装各模块组件）
    ├── components/
    │   ├── HeaderBar.vue            # 全局导航栏（含移动端菜单）
    │   ├── FooterBar.vue            # 全局页脚（含快速导航）
    │   ├── HeroSwiper.vue           # Banner 轮播图
    │   ├── Services.vue             # 首页-我们的服务
    │   ├── ServiceView.vue          # 服务子页面
    │   ├── About.vue                # 首页-关于我们
    │   ├── AboutSecPage.vue         # 关于我们子页面
    │   ├── Partners.vue             # 首页-合作伙伴
    │   ├── PartnerCaseView.vue      # 合作伙伴&案例子页面
    │   ├── News.vue                 # 首页-新闻动态
    │   ├── NewsPage.vue             # 新闻列表页
    │   ├── NewsDetail.vue           # 新闻详情页（v-html 渲染）
    │   ├── ProductCenter.vue        # 产品中心列表页
    │   ├── ProductDetail.vue        # 产品详情页（含彩页弹窗）
    │   ├── ContactAnchor.vue        # 首页-联系我们锚点
    │   └── ContactDetail.vue        # 联系我们详情页（含地图）
    ├── api/
    │   ├── index.js                 # API 统一导出入口
    │   ├── request.js               # fetch 封装（拦截器 / ApiError / 快捷方法）
    │   └── modules/
    │       ├── hero.js              # 轮播图接口
    │       ├── products.js          # 产品接口
    │       ├── news.js              # 新闻接口
    │       ├── services.js          # 服务接口
    │       ├── partners.js          # 合作伙伴 & 案例接口
    │       ├── about.js             # 关于我们接口
    │       ├── contact.js           # 联系我们（表单提交）
    │       └── gallery.js           # 公司相册接口
    └── styles/
        └── main.css                 # 全局样式
```

## 路由一览

| 路径 | 名称 | 组件 | 说明 |
|------|------|------|------|
| `/` | Home | HomePage | 首页 |
| `/products` | Products | ProductCenter | 产品中心 |
| `/product/:id` | ProductDetail | ProductDetail | 产品详情（动态路由） |
| `/news` | News | NewsPage | 新闻列表 |
| `/news/:id` | NewsDetail | NewsDetail | 新闻详情（动态路由） |
| `/services` | Services | ServiceView | 我们的服务 |
| `/partner-cases` | PartnerCases | PartnerCaseView | 合作伙伴 & 案例 |
| `/about` | About | AboutSecPage | 关于我们 |
| `/contact` | Contact | ContactDetail | 联系我们 |

## 快速开始

```bash
# 1. 安装依赖
npm install

# 2. 启动开发服务器（默认 http://localhost:5173）
npm run dev

# 3. 生产构建
npm run build

# 4. 预览构建结果
npm run preview
```

> 开发服务器监听 `0.0.0.0:5173`，可在局域网内通过本机 IP 访问。

## API 层设计

API 层基于原生 `fetch` 封装，位于 `src/api/request.js`，具备以下特性：

- **零外部依赖**：不引入 axios 等第三方库
- **拦截器机制**：通过 `setHook()` 注册 `onRequest` / `onResponse` / `onError` 钩子
- **统一错误类**：`ApiError` 携带 `status` 和 `data`，便于上层统一处理
- **快捷方法**：`get()` / `post()` / `put()` / `del()` 开箱即用
- **后端地址**：默认指向 `http://localhost:8080`，按需修改 `BASE_URL`

```js
import { getProducts, submitContact } from './api/index.js'

// 获取产品列表
const products = await getProducts()

// 提交联系表单
await submitContact({ name: '张三', phone: '13800138000', message: '...' })
```

## 功能特性

- **响应式适配**：PC 端与移动端均已适配，导航、轮播、卡片、表单等组件在不同屏幕尺寸下均有对应 UI
- **页面过渡动画**：路由切换时 `fade-slide` 淡入上移效果，体验流畅
- **平滑滚动**：锚点跳转自动偏移 80px（避开固定导航栏），滚动行为可配置
- **新闻详情**：`v-html` 渲染富文本正文，面包屑在移动端支持横向滑动
- **产品彩页**：弹窗获取表单，交互友好
- **高德地图**：联系我们页面嵌入地图组件
- **一键拨号**：移动端联系页面支持点击号码直接拨号
- **备案信息**：预留 ICP 备案与网安备案展示位

## 版本历史
### v0.5.2


### v0.5.1
- 新增高德地图 API，联系我们页面地图组件正常展示
- 替换 demo 内容为实际公司内容
- 新增网安备案与 ICP 备案展示位
- 添加网页 Favicon

### v0.5
- 新闻详情页重构：面包屑移动端横向滑动、品牌配色统一、`v-html` 正文响应式排版
- 联系我们页面优化：PC 端等高对齐、移动端 2×2 合作流程布局、一键拨号
- 全局响应式适配更新（Banner / 服务 / 合作伙伴板块）
- 修复二级子页面 Logo 路径、移动端 z-index 遮挡、子页面样式冲突

### v0.4
- 新增主页移动端 UI 适配
- 更新 Header / Footer 公共组件移动端样式
- 修复若干 bug

### v0.3
- 新增产品详情、服务子页、合作伙伴案例、联系我们等子页面
- 产品彩页获取弹窗友好化处理
- 主导航与底部快速导航 router-link 全部联通

### v0.2
- 新增新闻资讯列表及详情页（三级路由）
- Header / Footer 样式更新，导航动画效果
- 关于我们二级页面、路由逻辑完善
- App.vue 组件插入平滑过渡

### v0.1
- 初始版本：单页 HTML 拆分为 Vue 3 组件化项目

## 浏览器支持

支持所有现代浏览器（Chrome / Firefox / Safari / Edge），IE 不在支持范围内。
