from abc import ABC, abstractmethod

from presentation.schemas import ReviewCreate, ReviewResponse


class IReviewService(ABC):
    @abstractmethod
    def create_review(self, review: ReviewCreate) -> ReviewResponse:
        raise NotImplementedError

    @abstractmethod
    def get_reviews(self, sentiment: str) -> list[ReviewResponse]:
        raise NotImplementedError
