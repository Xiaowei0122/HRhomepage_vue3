"""
FastAPI 应用入口。
启动: uvicorn main:app --reload --port 8080
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import API_PREFIX, CORS_ORIGINS

# 导入所有路由
from routers import (
    hero,
    products,
    news,
    services,
    partners,
    about,
    contact,
    gallery,
)

app = FastAPI(
    title="西安鸿瑞办公 API",
    description="鸿瑞办公门户网站后端接口",
    version="0.1.0",
)

# CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(hero.router, prefix=API_PREFIX)
app.include_router(products.router, prefix=API_PREFIX)
app.include_router(news.router, prefix=API_PREFIX)
app.include_router(services.router, prefix=API_PREFIX)
app.include_router(partners.router, prefix=API_PREFIX)
app.include_router(about.router, prefix=API_PREFIX)
app.include_router(contact.router, prefix=API_PREFIX)
app.include_router(gallery.router, prefix=API_PREFIX)


@app.get("/")
def root():
    """健康检查"""
    return {"status": "ok", "service": "鸿瑞办公 API"}
