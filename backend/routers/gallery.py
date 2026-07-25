"""
公司相册路由。
"""
from fastapi import APIRouter, Query

from schemas.gallery import GalleryItem

router = APIRouter(tags=["公司相册"])

# TODO: 接入数据库
_MOCK_GALLERY: list[GalleryItem] = [
    GalleryItem(
        id=1, category="office", categoryName="办公环境",
        title="公司前台",
        image="https://images.unsplash.com/photo-1497366216548-37526070297c",
        description="宽敞明亮的公司前台接待区",
    ),
    GalleryItem(
        id=2, category="office", categoryName="办公环境",
        title="开放式办公区",
        image="https://images.unsplash.com/photo-1497366811353-6870744d04b2",
        description="现代化开放式办公区域",
    ),
    GalleryItem(
        id=3, category="office", categoryName="办公环境",
        title="产品展示厅",
        image="https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
        description="展示各品牌最新办公设备",
    ),
    GalleryItem(
        id=4, category="office", categoryName="办公环境",
        title="会议室",
        image="https://images.unsplash.com/photo-1577412647305-991150c7d5bb",
        description="配备多媒体设备的现代化会议室",
    ),
    GalleryItem(
        id=5, category="team", categoryName="团队活动",
        title="2026 年度团建",
        image="https://images.unsplash.com/photo-1522071820081-009f0129c71c",
        description="全体员工户外拓展活动",
    ),
    GalleryItem(
        id=6, category="team", categoryName="团队活动",
        title="技术培训",
        image="https://images.unsplash.com/photo-1552664730-d307ca884978",
        description="工程师定期参加厂商技术培训",
    ),
    GalleryItem(
        id=7, category="event", categoryName="公司大事记",
        title="签约理光授权经销商",
        image="https://images.unsplash.com/photo-1559136555-9303baea8ebd",
        description="2026 年正式签约成为理光授权经销商",
    ),
    GalleryItem(
        id=8, category="event", categoryName="公司大事记",
        title="公司乔迁新址",
        image="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab",
        description="2026 年 7 月迁入新办公楼",
    ),
]


@router.get("/gallery", response_model=list[GalleryItem])
def get_gallery(category: str | None = Query(None, description="分类筛选: office / team / event")):
    """获取公司相册列表，可按分类筛选"""
    if category:
        return [item for item in _MOCK_GALLERY if item.category == category]
    return _MOCK_GALLERY
