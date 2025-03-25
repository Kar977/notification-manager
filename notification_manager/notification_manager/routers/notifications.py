from fastapi import APIRouter
from fastapi.responses import JSONResponse
from notification_manager.schemas import SendEmailRequest

router = APIRouter(prefix="/notification")


@router.post("/send-email")
async def send_email(email_request: SendEmailRequest):
    print("Sending email with details:", email_request, flush=True)

    return JSONResponse(content={"status": "Email sent"}, status_code=200)
