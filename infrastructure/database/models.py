from datetime import datetime

from sqlalchemy import (
    Integer,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from settings.database import BaseSqlalchemyModel


class ReviewTable(BaseSqlalchemyModel):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[str] = mapped_column(
        Text, nullable=False, default=datetime.utcnow().isoformat()
    )
