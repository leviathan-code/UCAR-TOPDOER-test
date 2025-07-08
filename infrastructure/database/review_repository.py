from datetime import datetime

from sqlalchemy import (
    insert,
    select,
)
from sqlalchemy.orm import Session

from domain.constant import SENTIMENT_CONSTANTS
from domain.review import ReviewCreateDTO, ReviewResponseDTO
from infrastructure.database.models import ReviewTable
from interfaces.review_repository import IReviewRepository


class ReviewRepository(IReviewRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_review(self, review: ReviewCreateDTO) -> ReviewResponseDTO:
        stmt = (
            insert(ReviewTable)
            .values(
                text=review.text,
                sentiment=SENTIMENT_CONSTANTS.get(review.text, "neutral"),
                created_at=datetime.utcnow().isoformat(),
            )
            .returning(ReviewTable)
        )
        result = self.session.execute(stmt).scalar_one()
        self.session.commit()

        return ReviewResponseDTO(
            id=result.id,
            text=result.text,
            sentiment=result.sentiment,
            created_at=result.created_at,
        )

    def get_reviews(self, sentiment: str) -> list[ReviewResponseDTO]:
        stmt = select(ReviewTable).where(ReviewTable.sentiment == sentiment)
        results = self.session.execute(stmt).scalars().all()

        return [
            ReviewResponseDTO(
                id=result.id,
                text=result.text,
                sentiment=result.sentiment,
                created_at=result.created_at,
            )
            for result in results
        ]
