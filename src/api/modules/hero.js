/**
 * 首页轮播图 API。
 */
import { get } from '../request.js'

/**
 * 获取首页轮播图列表。
 * @returns {Promise<Array<{
 *   image: string,   // 图片地址
 *   alt: string,     // 图片替代文本
 *   label: string,   // 标签文字
 *   title: string,   // 标题
 *   sub: string,     // 副标题
 *   cta1: { text: string, href: string },  // 主按钮
 *   cta2: { text: string, href: string }   // 次按钮
 * }>>}
 */
export function getHeroSlides() {
  return get('/api/hero-slides')
}
