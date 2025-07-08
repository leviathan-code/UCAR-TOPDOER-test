from dataclasses import dataclass


@dataclass
class ReviewCreateDTO:
    text: str


@dataclass
class ReviewResponseDTO:
    id: int
    text: str
    sentiment: str
    created_at: str
