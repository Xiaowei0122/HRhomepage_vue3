"""
合作伙伴 & 案例路由。
"""
from fastapi import APIRouter

from schemas.partners import Partner, PartnerBrand, CaseStudy

router = APIRouter(tags=["合作伙伴 & 案例"])

# TODO: 接入数据库
_MOCK_PARTNERS: list[Partner] = [
    Partner(src="/assets/partners/logo1.png", alt="惠普"),
    Partner(src="/assets/partners/logo2.png", alt="理光"),
    Partner(src="/assets/partners/logo3.png", alt="爱普生"),
]

# TODO: 接入数据库
_MOCK_BRANDS: list[PartnerBrand] = [
    PartnerBrand(name="惠普 (HP)", logo="/assets/partners/logo1.png", role="核心经销商"),
    PartnerBrand(name="理光 (Ricoh)", logo="/assets/partners/logo2.png", role="授权经销商"),
    PartnerBrand(name="爱普生 (Epson)", logo="/assets/partners/logo3.png", role="合作伙伴"),
]

# TODO: 接入数据库
_MOCK_CASES: list[CaseStudy] = [
    CaseStudy(
        tag="教育行业", title="某高校打印解决方案",
        desc="为某高校图书馆部署 50 台自助打印终端，实现无人化管理。",
        stat="日均服务 3000+ 人次", img="https://images.unsplash.com/photo-1541339907198-e08756dedf3f",
    ),
    CaseStudy(
        tag="政府单位", title="某区政府办公设备升级",
        desc="统一升级全区办公设备，实现集中管控与绿色节能。",
        stat="年节省耗材成本 40%", img="https://images.unsplash.com/photo-1497366216548-37526070297c",
    ),
]


@router.get("/partners", response_model=list[Partner])
def get_partners():
    """获取合作伙伴 Logo 列表"""
    return _MOCK_PARTNERS


@router.get("/partners/brands", response_model=list[PartnerBrand])
def get_partner_brands():
    """获取品牌合作方列表"""
    return _MOCK_BRANDS


@router.get("/cases", response_model=list[CaseStudy])
def get_cases():
    """获取客户案例列表"""
    return _MOCK_CASES
