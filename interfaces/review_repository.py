from abc import ABC, abstractmethod

from domain.review import ReviewCreateDTO, ReviewResponseDTO


class IReviewRepository(ABC):
    @abstractmethod
    def create_review(self, review: ReviewCreateDTO) -> ReviewResponseDTO:
        raise NotImplementedError

    @abstractmethod
    def get_reviews(self, sentiment: str) -> list[ReviewResponseDTO]:
        raise NotImplementedError
