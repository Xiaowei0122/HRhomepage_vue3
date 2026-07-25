"""
首页轮播图路由。
"""
from fastapi import APIRouter

from schemas.hero import HeroSlide

router = APIRouter(tags=["首页轮播"])

# TODO: 接入数据库
_MOCK_SLIDES = [
    HeroSlide(
        image="https://images.unsplash.com/photo-1497215728101-856f4ea42174",
        alt="办公设备解决方案",
        label="专业服务",
        title="办公设备一站式解决方案",
        sub="覆盖打印、复印、扫描全品类设备",
        cta1={"text": "了解产品", "href": "/products"},
        cta2={"text": "联系我们", "href": "/contact"},
    ),
    HeroSlide(
        image="https://images.unsplash.com/photo-1600880292203-757bb62b4baf",
        alt="耗材配件",
        label="正品保障",
        title="原装耗材 品质保证",
        sub="各大品牌原装耗材，质量可靠",
        cta1={"text": "查看耗材", "href": "/products?category=consumables"},
        cta2={"text": "立即咨询", "href": "/contact"},
    ),
]


@router.get("/hero-slides", response_model=list[HeroSlide])
def get_hero_slides():
    """获取首页轮播图列表"""
    return _MOCK_SLIDES
