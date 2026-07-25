"""
公司相册 Schema。
"""
from pydantic import BaseModel, Field


class GalleryItem(BaseModel):
    """相册照片"""
    id: int = Field(..., description="照片 ID")
    category: str = Field(..., description="分类标识: office(办公环境) / team(团队活动) / event(公司大事记)")
    categoryName: str = Field(..., description="分类名称")
    title: str = Field(..., description="照片标题")
    image: str = Field(..., description="图片地址")
    description: str = Field(default="", description="描述")
