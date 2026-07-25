/**
 * 基于原生 fetch 的 HTTP 请求封装。
 * 零外部依赖。
 */

// --- 配置 ---
const BASE_URL = 'http://localhost:8080'

// --- 拦截器钩子（预留，后续扩展用） ---
const hooks = {
  onRequest: null,   // (url, options) => { return { url, options } | Promise<{ url, options }> }
  onResponse: null,  // (response) => { return response | Promise<response> }
  onError: null,     // (error) => { return error | Promise<error> }
}

/**
 * 设置拦截器钩子函数。
 * @param {'onRequest'|'onResponse'|'onError'} name - 钩子名称
 * @param {Function} fn - 钩子函数
 *
 * @example
 * import { setHook } from './request.js'
 * setHook('onRequest', ({ url, options }) => {
 *   options.headers.Authorization = `Bearer ${getToken()}`
 *   return { url, options }
 * })
 */
export function setHook(name, fn) {
  hooks[name] = fn
}

/**
 * API 请求错误类。
 */
export class ApiError extends Error {
  constructor(status, message, data) {
    super(message)
    this.name = 'ApiError'
    this.status = status   // HTTP 状态码，网络错误为 0
    this.data = data       // 后端返回的错误数据
  }
}

/**
 * 核心请求函数。
 *
 * @param {string} url - 接口路径，例如 '/api/products'
 * @param {object} [options={}] - 请求配置
 * @param {string} [options.method='GET'] - 请求方法
 * @param {object} [options.params]  - URL 查询参数
 * @param {*}      [options.body]    - 请求体（自动序列化为 JSON）
 * @param {object} [options.headers] - 额外的请求头
 * @returns {Promise<any>} 解析后的 JSON 响应
 */
export async function request(url, options = {}) {
  const { method = 'GET', params, body, headers: extraHeaders } = options

  // 拼接完整 URL 和查询参数
  let fullUrl = `${BASE_URL}${url}`
  if (params) {
    const qs = new URLSearchParams(params).toString()
    if (qs) fullUrl += `?${qs}`
  }

  // 构建 fetch 配置
  const fetchOptions = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...extraHeaders,
    },
  }

  // GET/HEAD 请求不携带 body
  if (body && method !== 'GET' && method !== 'HEAD') {
    fetchOptions.body = JSON.stringify(body)
  }

  // --- 请求拦截 ---
  let req = { url: fullUrl, options: fetchOptions }
  if (hooks.onRequest) {
    req = await hooks.onRequest(req)
  }

  // --- 发起网络请求 ---
  let response
  try {
    response = await fetch(req.url, req.options)
  } catch (err) {
    if (hooks.onError) {
      hooks.onError(err)
    }
    throw new ApiError(0, `网络错误: ${err.message}`, null)
  }

  // --- 响应拦截 ---
  if (hooks.onResponse) {
    response = await hooks.onResponse(response)
  }

  // --- 处理非 OK 响应 ---
  if (!response.ok) {
    let data = null
    try { data = await response.json() } catch (_) { /* 忽略解析错误 */ }
    const err = new ApiError(response.status, data?.message || `请求失败 (${response.status})`, data)
    if (hooks.onError) {
      hooks.onError(err)
    }
    throw err
  }

  // --- 解析成功响应体 ---
  // 204 No Content
  if (response.status === 204) return null

  const contentType = response.headers.get('content-type') || ''
  if (contentType.includes('application/json')) {
    return response.json()
  }
  // 兜底：返回纯文本
  return response.text()
}

/**
 * 快捷方法。
 */
export const get  = (url, params) => request(url, { method: 'GET', params })
export const post = (url, body)   => request(url, { method: 'POST', body })
export const put  = (url, body)   => request(url, { method: 'PUT', body })
export const del  = (url)        => request(url, { method: 'DELETE' })

export default request
