/**
 * 合作伙伴 & 案例 API。
 */
import { get } from '../request.js'

/**
 * 获取合作伙伴 Logo 列表（首页展示）。
 * @returns {Promise<Array<{ src: string, alt: string }>>}
 */
export function getPartners() {
  return get('/api/partners')
}

/**
 * 获取品牌合作方列表（含角色描述）。
 * @returns {Promise<Array<{ name: string, logo: string, role: string }>>}
 */
export function getPartnerBrands() {
  return get('/api/partners/brands')
}

/**
 * 获取客户案例列表。
 * @returns {Promise<Array<{
 *   tag: string,   // 标签
 *   title: string, // 标题
 *   desc: string,  // 描述
 *   stat: string,  // 关键数据
 *   img: string    // 配图
 * }>>}
 */
export function getCases() {
  return get('/api/cases')
}
