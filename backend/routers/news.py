"""
新闻动态路由。
"""
from fastapi import APIRouter, HTTPException, Query

from schemas.news import NewsListItem, NewsDetail, FeaturedNews

router = APIRouter(prefix="/news", tags=["新闻动态"])

# TODO: 接入数据库
_MOCK_NEWS: list[NewsListItem] = [
    NewsListItem(id=1, type="company", title="鸿瑞办公乔迁新址通知", date="2026-07-20", excerpt="为了更好地服务广大客户..."),
    NewsListItem(id=2, type="industry", title="2026 年办公设备行业趋势报告", date="2026-07-15", excerpt="数字化转型加速推进..."),
    NewsListItem(id=3, type="company", title="鸿瑞签约成为理光授权经销商", date="2026-07-10", excerpt="进一步拓展产品线..."),
]

# TODO: 接入数据库
_MOCK_FEATURED = [
    FeaturedNews(title="鸿瑞办公乔迁新址通知", date="2026-07-20", tag="公司动态", summary="为了更好地服务广大客户，公司已迁至新办公地址。"),
    FeaturedNews(title="2026 年办公设备行业趋势报告", date="2026-07-15", tag="行业资讯", summary="数字化转型加速推进，智能办公设备需求持续增长。"),
]

# TODO: 接入数据库
_MOCK_DETAIL: dict[int, NewsDetail] = {
    1: NewsDetail(title="鸿瑞办公乔迁新址通知", date="2026-07-20", content="为适应业务发展需要，西安鸿瑞办公设备有限公司已于 2026 年 7 月正式迁入新办公地址..."),
    2: NewsDetail(title="2026 年办公设备行业趋势报告", date="2026-07-15", content="随着企业数字化转型的深入推进，办公设备行业正迎来新一轮变革..."),
}


@router.get("", response_model=list[NewsListItem])
def get_news_list(type: str | None = Query(None, description="新闻类型: company / industry")):
    """获取新闻列表，可按类型筛选"""
    if type:
        return [n for n in _MOCK_NEWS if n.type == type]
    return _MOCK_NEWS


@router.get("/featured", response_model=list[FeaturedNews])
def get_featured_news():
    """获取首页推荐新闻"""
    return _MOCK_FEATURED


@router.get("/{news_id}", response_model=NewsDetail)
def get_news_detail(news_id: int):
    """获取新闻详情"""
    detail = _MOCK_DETAIL.get(news_id)
    if not detail:
        raise HTTPException(status_code=404, detail="新闻不存在")
    return detail
