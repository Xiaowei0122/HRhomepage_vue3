"""
联系我们 Schema。
"""
from pydantic import BaseModel, Field


class ContactForm(BaseModel):
    """咨询/需求表单"""
    name: str = Field(..., min_length=1, description="联系人姓名")
    phone: str = Field(..., min_length=1, description="联系电话")
    type: str = Field(default="", description="咨询类型: rent(租赁)/buy(采购)/service(报修)/空(意向咨询)")
    message: str = Field(default="", description="留言内容")


class ContactResponse(BaseModel):
    """提交响应"""
    success: bool = Field(..., description="是否成功")
    message: str = Field(..., description="提示信息")
