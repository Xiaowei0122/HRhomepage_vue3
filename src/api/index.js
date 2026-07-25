/**
 * API 层 — 统一导出入口。
 *
 * 使用示例:
 *   import { getHeroSlides, getProducts, submitContact } from './api/index.js'
 *   const slides = await getHeroSlides()
 */

// 请求工具
export { request, get, post, put, del, setHook, ApiError } from './request.js'

// 首页轮播
export { getHeroSlides } from './modules/hero.js'

// 产品
export { getProducts, getProductDetail, getRelatedProducts } from './modules/products.js'

// 新闻动态
export { getNewsList, getFeaturedNews, getNewsDetail } from './modules/news.js'

// 服务
export { getServices, getServiceDetail } from './modules/services.js'

// 合作伙伴 & 案例
export { getPartners, getPartnerBrands, getCases } from './modules/partners.js'

// 关于我们
export { getAboutStats, getAboutCulture, getAboutDepartments, getAboutCertificates } from './modules/about.js'

// 公司相册
export { getGallery } from './modules/gallery.js'

// 联系我们
export { submitContact } from './modules/contact.js'
