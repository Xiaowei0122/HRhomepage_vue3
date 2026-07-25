"""
服务路由。
"""
from fastapi import APIRouter

from schemas.services import ServiceCard, ServiceDetail

router = APIRouter(prefix="/services", tags=["服务"])

# TODO: 接入数据库
_MOCK_SERVICES: list[ServiceCard] = [
    ServiceCard(id="sales", icon="bi-display", title="设备租赁及销售", desc="提供复印机、打印机、投影仪等办公设备的租赁和销售服务。"),
    ServiceCard(id="repair", icon="bi-tools", title="用户维护报修", desc="专业技术团队，快速响应，保障您的设备稳定运行。"),
    ServiceCard(id="supplies", icon="bi-box-seam", title="耗材/办公用品采购", desc="原装正品耗材及各类办公用品一站式采购。"),
    ServiceCard(id="solutions", icon="bi-lightbulb", title="办公解决方案", desc="根据企业需求量身定制智能办公解决方案。"),
]

# TODO: 接入数据库
_MOCK_DETAIL: list[ServiceDetail] = [
    ServiceDetail(
        id="sales", tag="设备服务", title="设备租赁及销售",
        image="https://images.unsplash.com/photo-1497215728101-856f4ea42174",
        desc="提供主流品牌复印机、打印机、投影仪等设备的租赁与销售，灵活方案满足不同规模企业需求。",
        points=["品牌齐全，惠普、理光、爱普生等", "灵活的租赁方案，按月/按年", "免费上门安装调试", "设备以旧换新服务"],
    ),
    ServiceDetail(
        id="repair", tag="运维服务", title="用户维护报修",
        image="https://images.unsplash.com/photo-1581092160562-40aa08e78837",
        desc="专业工程师团队提供及时的设备维护与修理服务，最大限度减少设备停机时间。",
        points=["2 小时快速响应", "定期巡检保养", "原装配件更换", "远程技术支持"],
    ),
]


@router.get("", response_model=list[ServiceCard])
def get_services():
    """获取首页服务卡片列表"""
    return _MOCK_SERVICES


@router.get("/detail", response_model=list[ServiceDetail])
def get_service_detail():
    """获取服务详情页内容"""
    return _MOCK_DETAIL
