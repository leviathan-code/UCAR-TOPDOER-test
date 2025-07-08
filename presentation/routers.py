from typing import Annotated

from fastapi import APIRouter, Depends

from di.depends import get_review_service
from interfaces.reviews_services import IReviewService

from .schemas import ReviewCreate, ReviewResponse

app = APIRouter()


@app.post("/reviews", response_model=ReviewResponse)
async def create_item(
    service: Annotated[IReviewService, Depends(get_review_service)],
    review: ReviewCreate,
):
    return service.create_review(review)


@app.get("/reviews", response_model=list[ReviewResponse])
async def read_item(
    service: Annotated[IReviewService, Depends(get_review_service)],
    sentiment: str = "negative",
):
    return service.get_reviews(sentiment)
