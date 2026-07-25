"""
关于我们 Schema。
"""
from pydantic import BaseModel, Field


class Stat(BaseModel):
    """公司统计数据"""
    num: str = Field(..., description="数值")
    label: str = Field(..., description="标签")


class Culture(BaseModel):
    """企业文化/价值观"""
    title: str = Field(..., description="标题")
    desc: str = Field(..., description="描述")
    icon: str = Field(..., description="图标类名")


class Department(BaseModel):
    """部门"""
    name: str = Field(..., description="部门名称")
    duty: str = Field(..., description="部门职责")
