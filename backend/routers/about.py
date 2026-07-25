"""
关于我们路由。
"""
from fastapi import APIRouter

from schemas.about import Stat, Culture, Department

router = APIRouter(prefix="/about", tags=["关于我们"])

# TODO: 接入数据库
_MOCK_STATS: list[Stat] = [
    Stat(num="15+", label="年行业经验"),
    Stat(num="500+", label="服务客户"),
    Stat(num="50+", label="合作品牌"),
    Stat(num="98%", label="客户满意度"),
]

# TODO: 接入数据库
_MOCK_CULTURE: list[Culture] = [
    Culture(title="诚信为本", desc="以诚信为立身之本，与客户建立长期信任关系。", icon="bi-shield-check"),
    Culture(title="品质为先", desc="只提供经过严格筛选的优质产品和耗材。", icon="bi-star"),
    Culture(title="服务至上", desc="快速响应，专业服务，让客户无后顾之忧。", icon="bi-heart"),
    Culture(title="创新驱动", desc="持续关注行业前沿技术，为客户提供智能化方案。", icon="bi-lightbulb"),
]

# TODO: 接入数据库
_MOCK_DEPARTMENTS: list[Department] = [
    Department(name="销售部", duty="负责设备租赁、销售及客户开发"),
    Department(name="技术部", duty="负责设备安装、维护及技术支持"),
    Department(name="采购部", duty="负责耗材配件采购及供应链管理"),
    Department(name="财务部", duty="负责公司财务核算及成本管控"),
]


@router.get("/stats", response_model=list[Stat])
def get_about_stats():
    """获取公司统计数据"""
    return _MOCK_STATS


@router.get("/culture", response_model=list[Culture])
def get_about_culture():
    """获取企业文化/价值观"""
    return _MOCK_CULTURE


@router.get("/departments", response_model=list[Department])
def get_about_departments():
    """获取部门架构"""
    return _MOCK_DEPARTMENTS


@router.get("/certificates", response_model=list[dict])
def get_about_certificates():
    """获取资质证书列表"""
    # TODO: 接入数据库
    return [
        {"name": "ISO 9001 质量管理体系认证", "year": "2025"},
        {"name": "政府采购供应商资格", "year": "2026"},
        {"name": "理光授权经销商证书", "year": "2026"},
    ]
