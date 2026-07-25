"""
合作伙伴 & 案例 Schema。
"""
from pydantic import BaseModel, Field


class Partner(BaseModel):
    """合作伙伴 Logo"""
    src: str = Field(..., description="Logo 图片路径")
    alt: str = Field(..., description="品牌名称（替代文本）")


class PartnerBrand(BaseModel):
    """品牌合作方"""
    name: str = Field(..., description="品牌名称")
    logo: str = Field(..., description="Logo 图片路径")
    role: str = Field(..., description="合作角色")


class CaseStudy(BaseModel):
    """客户案例"""
    tag: str = Field(..., description="标签（行业/类型）")
    title: str = Field(..., description="标题")
    desc: str = Field(..., description="描述")
    stat: str = Field(..., description="关键数据")
    img: str = Field(..., description="配图")
