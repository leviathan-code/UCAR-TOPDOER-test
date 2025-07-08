from domain.review import ReviewCreateDTO
from infrastructure.database.review_repository import ReviewRepository
from interfaces.review_repository import IReviewRepository
from interfaces.reviews_services import IReviewService
from presentation.schemas import ReviewResponse


class ReviewService(IReviewService):
    def __init__(self, repository: IReviewRepository = ReviewRepository):
        self.repository = repository

    def create_review(self, review: ReviewCreateDTO) -> ReviewResponse:
        result = self.repository.create_review(review)
        return ReviewResponse(
            id=result.id,
            text=result.text,
            sentiment=result.sentiment,
            created_at=result.created_at,
        )

    def get_reviews(self, sentiment: str) -> list[ReviewResponse]:
        result = self.repository.get_reviews(sentiment)
        return [
            ReviewResponse(
                id=item.id,
                text=item.text,
                sentiment=item.sentiment,
                created_at=item.created_at,
            )
            for item in result
        ]
