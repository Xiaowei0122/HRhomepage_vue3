import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '192.168.20.5',   // 关键
    port: 5173,        // 可选，默认5173
    strictPort: true
  }    
})