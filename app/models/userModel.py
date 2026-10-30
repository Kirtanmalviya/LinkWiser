from ..config.database import Base
from sqlalchemy import String, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, nullable = False)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, nullable = False, unique = True)
    hashed_password: Mapped[str] = mapped_column(String, nullable = False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
