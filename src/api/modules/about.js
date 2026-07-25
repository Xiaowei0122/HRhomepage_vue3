/**
 * 关于我们 API。
 */
import { get } from '../request.js'

/**
 * 获取公司统计数据（年限、客户数等）。
 * @returns {Promise<Array<{ num: string, label: string }>>}
 */
export function getAboutStats() {
  return get('/api/about/stats')
}

/**
 * 获取企业文化 / 价值观。
 * @returns {Promise<Array<{ title: string, desc: string, icon: string }>>}
 */
export function getAboutCulture() {
  return get('/api/about/culture')
}

/**
 * 获取部门架构。
 * @returns {Promise<Array<{ name: string, duty: string }>>}
 */
export function getAboutDepartments() {
  return get('/api/about/departments')
}

/**
 * 获取资质证书列表。
 * @returns {Promise<any[]>}
 */
export function getAboutCertificates() {
  return get('/api/about/certificates')
}
