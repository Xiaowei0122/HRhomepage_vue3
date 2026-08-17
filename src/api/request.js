/**
 * 官网请求层 — 基于 fetch（无 axios 依赖）
 * 后端统一响应：{ code: 200, data, message } 或 { code, data: null, message }
 * 此处统一解包为 data，非 200 抛出带 message 的错误
 */

const BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

async function request(url, options = {}) {
  const config = {
    method: options.method || 'GET',
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
  }
  if (options.body != null) config.body = JSON.stringify(options.body)

  let res
  try {
    res = await fetch(BASE_URL + url, config)
  } catch {
    throw new Error('网络异常，请检查后端服务是否启动')
  }

  let json
  try {
    json = await res.json()
  } catch {
    throw new Error('响应格式错误')
  }

  if (json && json.code === 200) return json.data
  throw new Error((json && json.message) || '请求失败')
}

/** GET，params 中空值会被忽略 */
export const get = (url, params) => {
  let qs = ''
  if (params) {
    const entries = Object.entries(params).filter(([, v]) => v !== '' && v != null && v !== undefined)
    if (entries.length) qs = '?' + new URLSearchParams(entries).toString()
  }
  return request(url + qs)
}

/** POST JSON */
export const post = (url, body) => request(url, { method: 'POST', body })

export default { get, post }
