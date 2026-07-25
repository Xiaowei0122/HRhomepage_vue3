"""
联系我们路由。
"""
import logging
from fastapi import APIRouter

from schemas.contact import ContactForm, ContactResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/contact", tags=["联系我们"])


@router.post("/submit", response_model=ContactResponse)
def submit_contact(form: ContactForm):
    """提交咨询/需求表单"""
    # TODO: 接入数据库，保存表单数据
    logger.info("收到咨询表单: name=%s, phone=%s, type=%s", form.name, form.phone, form.type)
    return ContactResponse(success=True, message="提交成功，我们会尽快与您联系！")
