from pydantic import BaseModel
from datetime import datetime

class LinkSchema(BaseModel):
    original_url: str

class LinkSchemaResponse(BaseModel):
    generated_url: str

class LinkList(BaseModel):
    id: int
    original_url: str
    generated_url: str
    count: int
    created_at: datetime