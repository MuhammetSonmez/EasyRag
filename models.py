from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    response: str
