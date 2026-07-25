"""
服务 Schema。
"""
from pydantic import BaseModel, Field


class ServiceCard(BaseModel):
    """首页服务卡片"""
    id: str = Field(..., description="服务标识")
    icon: str = Field(..., description="图标类名")
    title: str = Field(..., description="标题")
    desc: str = Field(..., description="描述")


class ServiceDetail(BaseModel):
    """服务详情"""
    id: str = Field(..., description="服务标识")
    tag: str = Field(..., description="标签")
    title: str = Field(..., description="标题")
    image: str = Field(..., description="配图")
    desc: str = Field(..., description="描述")
    points: list[str] = Field(default_factory=list, description="要点列表")
