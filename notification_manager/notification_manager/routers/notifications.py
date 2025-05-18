from fastapi import APIRouter
from fastapi.responses import JSONResponse
from notification_manager.schemas import SendEmailRequest
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

router = APIRouter(prefix="/notification")


@router.post("/send-email")
async def send_email(email_request: SendEmailRequest):
    logging.INFO(f"Sending email with details: {email_request}")
    return JSONResponse(content={"status": "Email sent"}, status_code=200)
