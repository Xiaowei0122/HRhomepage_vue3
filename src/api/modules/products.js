/**
 * 产品 API。
 */
import { get } from '../request.js'

/**
 * 获取产品列表，可按分类筛选。
 * @param {string} [category] - 分类标识（如 'printer', 'copier', 'consumables'）
 * @returns {Promise<Array<{
 *   id: number,
 *   catId: string,        // 分类标识
 *   categoryName: string, // 分类名称
 *   name: string,         // 产品名称
 *   image: string         // 产品图片
 * }>>}
 */
export function getProducts(category) {
  return get('/api/products', category ? { category } : undefined)
}

/**
 * 获取单个产品的详细信息。
 * @param {number|string} id - 产品 ID
 * @returns {Promise<{
 *   id: number,
 *   catId: string,
 *   categoryName: string,
 *   name: string,
 *   image: string,        // 主图
 *   images: string[],     // 图片列表
 *   description: string,  // 描述
 *   highlights: string[], // 亮点
 *   specs: Record<string, string>  // 规格参数（键值对）
 * }>}
 */
export function getProductDetail(id) {
  return get(`/api/products/${id}`)
}

/**
 * 获取指定产品的相关产品（同分类推荐）。
 * @param {number|string} id - 产品 ID
 * @returns {Promise<Array<{
 *   id: number,
 *   catId: string,
 *   categoryName: string,
 *   name: string,
 *   image: string
 * }>>}
 */
export function getRelatedProducts(id) {
  return get(`/api/products/${id}/related`)
}
