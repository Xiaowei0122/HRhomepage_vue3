/**
 * 公开接口模块 — 对应后端 /api/public/*（无需登录）
 */
import { get, post } from './request'

// 站点全局配置（含 banner/service/about/contact），模块内做一层缓存避免多次重复请求
let configCache = null
export const getPublicConfig = () => {
  if (configCache) return Promise.resolve(configCache)
  return get('/public/config').then((data) => {
    configCache = data || {}
    return configCache
  })
}

export const getBanners = () => get('/public/banners')
export const getNews = (params) => get('/public/news', params)
export const getNewsDetail = (id) => get(`/public/news/${id}`)
export const getProducts = (params) => get('/public/products', params)
export const getProductDetail = (id) => get(`/public/products/${id}`)
export const getBrands = () => get('/public/brands')
export const getCases = () => get('/public/cases')
export const getHonors = (params) => get('/public/honors', params)
export const submitLead = (body) => post('/public/leads', body)

export default {
  getPublicConfig,
  getBanners,
  getNews,
  getNewsDetail,
  getProducts,
  getProductDetail,
  getBrands,
  getCases,
  getHonors,
  submitLead,
}
