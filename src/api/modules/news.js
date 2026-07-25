/**
 * 新闻动态 API。
 */
import { get } from '../request.js'

/**
 * 获取新闻列表，可按类型筛选。
 * @param {'company'|'industry'} [type] - 新闻类型（公司动态 / 行业资讯）
 * @returns {Promise<Array<{
 *   id: number,
 *   type: 'company' | 'industry',
 *   title: string,   // 标题
 *   date: string,    // 日期
 *   excerpt: string  // 摘要
 * }>>}
 */
export function getNewsList(type) {
  return get('/api/news', type ? { type } : undefined)
}

/**
 * 获取首页推荐的新闻。
 * @returns {Promise<Array<{
 *   title: string,
 *   date: string,
 *   tag: string,     // 标签
 *   summary: string  // 摘要
 * }>>}
 */
export function getFeaturedNews() {
  return get('/api/news/featured')
}

/**
 * 获取单篇新闻详情。
 * @param {number|string} id - 新闻 ID
 * @returns {Promise<{
 *   title: string,
 *   date: string,
 *   content: string  // 正文内容
 * }>}
 */
export function getNewsDetail(id) {
  return get(`/api/news/${id}`)
}
