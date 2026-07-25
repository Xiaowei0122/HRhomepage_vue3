/**
 * 联系我们 API。
 */
import { post } from '../request.js'

/**
 * 提交咨询 / 需求表单。
 *
 * @param {object} payload - 表单数据
 * @param {string} payload.name    - 联系人姓名
 * @param {string} payload.phone   - 联系电话
 * @param {'rent'|'buy'|'service'} payload.type - 咨询类型
 *        'rent'    — 设备租赁及销售
 *        'buy'     — 耗材/办公用品采购
 *        'service' — 用户维护报修
 *        ''        — 意向采购咨询（默认）
 * @param {string} payload.message - 留言内容（可选）
 * @returns {Promise<any>} 提交成功响应
 */
export function submitContact(payload) {
  return post('/api/contact/submit', payload)
}
