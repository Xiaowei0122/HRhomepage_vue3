/**
 * 服务 API。
 */
import { get } from '../request.js'

/**
 * 获取首页服务卡片列表（4 个分类）。
 * @returns {Promise<Array<{
 *   id: string,    // 服务标识
 *   icon: string,  // 图标类名
 *   title: string, // 标题
 *   desc: string   // 描述
 * }>>}
 */
export function getServices() {
  return get('/api/services')
}

/**
 * 获取服务详情页内容。
 * @returns {Promise<Array<{
 *   id: string,
 *   tag: string,      // 标签
 *   title: string,    // 标题
 *   image: string,    // 配图
 *   desc: string,     // 描述
 *   points: string[]  // 要点列表
 * }>>}
 */
export function getServiceDetail() {
  return get('/api/services/detail')
}
