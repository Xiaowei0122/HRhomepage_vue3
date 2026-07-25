"""
产品 Schema。
"""
from pydantic import BaseModel, Field


class ProductListItem(BaseModel):
    """产品列表项"""
    id: int = Field(..., description="产品 ID")
    catId: str = Field(..., description="分类标识")
    categoryName: str = Field(..., description="分类名称")
    name: str = Field(..., description="产品名称")
    image: str = Field(..., description="产品图片")


class ProductDetail(BaseModel):
    """产品详情"""
    id: int = Field(..., description="产品 ID")
    catId: str = Field(..., description="分类标识")
    categoryName: str = Field(..., description="分类名称")
    name: str = Field(..., description="产品名称")
    image: str = Field(..., description="主图")
    images: list[str] = Field(default_factory=list, description="图片列表")
    description: str = Field(default="", description="产品描述")
    highlights: list[str] = Field(default_factory=list, description="产品亮点")
    specs: dict[str, str] = Field(default_factory=dict, description="规格参数")
