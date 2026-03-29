from pydantic import BaseModel
from typing import Optional


class ExtractRequest(BaseModel):
    text: str


class ExtractResponse(BaseModel):
    name: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None