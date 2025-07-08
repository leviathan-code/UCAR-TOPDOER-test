from fastapi import Depends
from sqlalchemy.orm import Session

from infrastructure.database.review_repository import ReviewRepository
from interfaces.review_repository import IReviewRepository
from interfaces.reviews_services import IReviewService
from services.reviews_services import ReviewService
from settings.database import get_session


async def get_review_repository(
    session: Session = Depends(get_session),
) -> IReviewRepository:
    return ReviewRepository(session=session)


async def get_review_service(
    repository: IReviewRepository = Depends(get_review_repository),
) -> IReviewService:
    return ReviewService(repository=repository)
