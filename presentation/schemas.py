from pydantic import BaseModel


class ReviewCreate(BaseModel):
    text: str


class ReviewResponse(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str
