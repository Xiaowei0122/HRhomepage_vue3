"""
新闻动态 Schema。
"""
from pydantic import BaseModel, Field


class NewsListItem(BaseModel):
    """新闻列表项"""
    id: int = Field(..., description="新闻 ID")
    type: str = Field(..., description="类型: company / industry")
    title: str = Field(..., description="标题")
    date: str = Field(..., description="日期")
    excerpt: str = Field(..., description="摘要")


class FeaturedNews(BaseModel):
    """首页推荐新闻"""
    title: str = Field(..., description="标题")
    date: str = Field(..., description="日期")
    tag: str = Field(..., description="标签")
    summary: str = Field(..., description="摘要")


class NewsDetail(BaseModel):
    """新闻详情"""
    title: str = Field(..., description="标题")
    date: str = Field(..., description="日期")
    content: str = Field(..., description="正文内容")
