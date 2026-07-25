"""
首页轮播图 Schema。
"""
from pydantic import BaseModel, Field


class CtaButton(BaseModel):
    """按钮"""
    text: str = Field(..., description="按钮文字")
    href: str = Field(..., description="跳转链接")


class HeroSlide(BaseModel):
    """轮播图"""
    image: str = Field(..., description="图片地址")
    alt: str = Field(..., description="图片替代文本")
    label: str = Field(..., description="标签文字")
    title: str = Field(..., description="标题")
    sub: str = Field(..., description="副标题")
    cta1: CtaButton = Field(..., description="主按钮")
    cta2: CtaButton = Field(..., description="次按钮")
