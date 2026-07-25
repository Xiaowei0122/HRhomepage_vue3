/**
 * 公司相册 / 办公环境 API。
 */
import { get } from '../request.js'

/**
 * 获取公司相册列表，可按分类筛选。
 * @param {string} [category] - 分类筛选（如 'office', 'team', 'event'）
 * @returns {Promise<Array<{
 *   id: number,
 *   category: string,     // 分类标识
 *   categoryName: string, // 分类名称
 *   title: string,        // 照片标题
 *   image: string,        // 图片地址
 *   description: string   // 描述
 * }>>}
 */
export function getGallery(category) {
  return get('/api/gallery', category ? { category } : undefined)
}
