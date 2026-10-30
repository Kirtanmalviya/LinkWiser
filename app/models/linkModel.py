from ..config.database import Base
from sqlalchemy import String, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Links(Base):
    __tablename__ = "links_table"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, nullable = False)
    original_url: Mapped[str] = mapped_column(String, unique = True, nullable = False)
    generated_url: Mapped[str] = mapped_column(String, unique = True, nullable = False)
    count: Mapped[int] = mapped_column(Integer, default = 0)
    created_at: Mapped[datetime] = mapped_column(server_default = func.now())