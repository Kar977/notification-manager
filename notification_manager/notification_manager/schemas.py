from pydantic import BaseModel


class SendEmailRequest(BaseModel):
    title: str
    email_body: str
