"""
产品路由。
"""
from fastapi import APIRouter, HTTPException, Query

from schemas.products import ProductListItem, ProductDetail

router = APIRouter(prefix="/products", tags=["产品"])

# TODO: 接入数据库
_MOCK_PRODUCTS: list[ProductListItem] = [
    ProductListItem(id=1, catId="printer", categoryName="打印机", name="HP LaserJet Pro M404dn", image="https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6"),
    ProductListItem(id=2, catId="copier", categoryName="复印机", name="理光 MP C3004exSP", image="https://images.unsplash.com/photo-1597852074816-d933c7d2b988"),
    ProductListItem(id=3, catId="projector", categoryName="投影仪", name="爱普生 CB-X51", image="https://images.unsplash.com/photo-1616587226960-4a03badbe8bf"),
    ProductListItem(id=4, catId="consumables", categoryName="耗材", name="HP 26A 原装硒鼓", image="https://images.unsplash.com/photo-1589939705384-5185137a7f0f"),
]

# TODO: 接入数据库
_MOCK_DETAIL: dict[int, ProductDetail] = {
    1: ProductDetail(
        id=1, catId="printer", categoryName="打印机",
        name="HP LaserJet Pro M404dn",
        image="https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6",
        images=[
            "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6",
            "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6",
        ],
        description="高效双面打印，适合企业办公。",
        highlights=["双面打印", "每分钟 38 页", "USB + 以太网"],
        specs={"品牌": "惠普 (HP)", "类型": "黑白激光", "打印速度": "38 ppm"},
    ),
}


@router.get("", response_model=list[ProductListItem])
def get_products(category: str | None = Query(None, description="分类筛选")):
    """获取产品列表，支持按分类筛选"""
    if category:
        return [p for p in _MOCK_PRODUCTS if p.catId == category]
    return _MOCK_PRODUCTS


@router.get("/{product_id}", response_model=ProductDetail)
def get_product_detail(product_id: int):
    """获取产品详情"""
    detail = _MOCK_DETAIL.get(product_id)
    if not detail:
        raise HTTPException(status_code=404, detail="产品不存在")
    return detail


@router.get("/{product_id}/related", response_model=list[ProductListItem])
def get_related_products(product_id: int):
    """获取相关产品（同分类推荐）"""
    product = _MOCK_DETAIL.get(product_id)
    if not product:
        return []
    return [p for p in _MOCK_PRODUCTS if p.catId == product.catId and p.id != product_id]
